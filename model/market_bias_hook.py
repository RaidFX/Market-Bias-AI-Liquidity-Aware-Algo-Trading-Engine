import joblib
import numpy as np
from typing import List, Dict


class MarketBiasEngine:
    def __init__(
        self,
        model_path: str,
        min_candles: int = 50,
        max_candles: int = 300,
        min_trust: float = 15.0,
        lookback_liquidity: int = 20
    ):
        self.model = joblib.load(model_path)
        self.min_candles = min_candles
        self.max_candles = max_candles
        self.min_trust = min_trust
        self.lookback_liquidity = lookback_liquidity

    def _features(self, c):
        body = abs(c["close"] - c["open"])
        rng = c["high"] - c["low"]
        ret = (c["close"] - c["open"]) / c["open"] if c["open"] else 0
        hl_ratio = rng / c["open"] if c["open"] else 0
        return [body, rng, ret, hl_ratio]

    def _direction_from_prob(self, p_long: float):
        if p_long > 0.52:
            return "LONG"
        elif p_long < 0.48:
            return "SHORT"
        return "RANGE"

    def _bias_strength(self, p_long: float):
        if p_long > 0.6:
            return "STRONG_LONG"
        if p_long > 0.53:
            return "WEAK_LONG"
        if p_long < 0.4:
            return "STRONG_SHORT"
        if p_long < 0.47:
            return "WEAK_SHORT"
        return "RANGE"

    def _compute_dol(self, candles, direction):
        lookback = candles[-self.lookback_liquidity:]
        highs = [c["high"] for c in lookback]
        lows = [c["low"] for c in lookback]

        if direction == "LONG":
            return max(highs)
        if direction == "SHORT":
            return min(lows)
        return None

    def evaluate(self, candles: List[Dict]) -> Dict:
        if len(candles) < self.min_candles:
            return {"error": "NOT_ENOUGH_DATA"}

        candles = candles[-self.max_candles:]
        X = np.array([self._features(c) for c in candles])

        probs = self.model.predict_proba(X)
        avg_prob_long = float(np.mean(probs[:, 1]))
        trust = abs(avg_prob_long - 0.5) * 200

        direction = self._direction_from_prob(avg_prob_long)
        bias = self._bias_strength(avg_prob_long)
        dol = self._compute_dol(candles, direction)

        trade_allowed = trust >= self.min_trust and direction != "RANGE"

        return {
            "candles_used": len(candles),
            "direction": direction,
            "bias": bias,
            "trade_allowed": trade_allowed,
            "trust_percent": round(trust, 2),
            "avg_prob_long": round(avg_prob_long, 4),
            "DOL": round(dol, 5) if dol else None
        }
