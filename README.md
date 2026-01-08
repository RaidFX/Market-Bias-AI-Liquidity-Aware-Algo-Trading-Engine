# Market Bias AI – Liquidity-Aware Algo Trading Engine

**Market Bias AI** is a professional XGBoost-based algo-trading analysis engine that examines multi-timeframe OHLC data to determine the market's **directional bias**, **potential liquidity target (DOL)**, and **confidence score (trust)**.

> ⚠️ Important: This system **does not generate direct buy/sell signals**.  
> It operates with institutional trading logic and only provides market tendencies and potential liquidity zones.

---

## ⚙️ Core Features

- 🧠 **XGBoost ML Model**
  - Trained on 50M+ candles
  - Feature-based market behavior learning

- 💧 **Liquidity (DOL) Detection**
  - Identifies potential stop-hunt / target zones
  - Follows smart money flow

- 🧭 **Market Bias Classification**
  - `STRONG_LONG`
  - `WEAK_LONG`
  - `RANGE`
  - `WEAK_SHORT`
  - `STRONG_SHORT`
  - `NO_TRADE`

- 📊 **Trust / Confidence Score**
  - Measures market clarity
  - Low trust = no trade zone

- ⏱️ **Multi-Timeframe Support**
  - 1m, 5m, 15m, 1h, 4h, Daily

- 🔌 **Modular Architecture**
  - Hook system
  - Ready for API / bot / UI integration

---

## 🧪 Example Output

```json
{
  "candles_used": 200,
  "bias": "WEAK_LONG",
  "trust_percent": 13.6,
  "DOL_target": 90105.08
}
```

## ⚠️ Disclaimer / Responsibility

- This project **does not constitute financial advice** and should **not be used for live trading without proper risk management**.
- The author is **not responsible for any losses or damages** resulting from the use of this software.
- Users are fully responsible for their own trading decisions.
