import json
from tvDatafeed import TvDatafeed, Interval


_tv = TvDatafeed()


_INTERVAL_MAP = {
    "1": Interval.in_1_minute,
    "5": Interval.in_5_minute,
    "15": Interval.in_15_minute,
    "60": Interval.in_1_hour,
    "240": Interval.in_4_hour,
    "D": Interval.in_daily
}


def getchart(symbol: str, exchange: str, interval: str, bars: int = 200) -> dict:
    tf = _INTERVAL_MAP.get(interval)
    if tf is None:
        raise ValueError("Invalid interval")

    df = _tv.get_hist(
        symbol=symbol,
        exchange=exchange,
        interval=tf,
        n_bars=bars
    )

    if df is None or df.empty:
        raise RuntimeError("No data received")

    df = df.reset_index()

    candles = [
        {
            "time": int(row["datetime"].timestamp()),
            "open": float(row["open"]),
            "high": float(row["high"]),
            "low": float(row["low"]),
            "close": float(row["close"]),
            "volume": float(row["volume"]),
        }
        for _, row in df.iterrows()
    ]

    return {
        "symbol": f"{exchange}:{symbol}",
        "interval": interval,
        "bars": len(candles),
        "candles": candles
    }


if __name__ == "__main__":
    data = getchart(
        symbol="BTCUSDT",
        exchange="BINANCE",
        interval="60",
        bars=200
    )
    print(json.dumps(data, indent=2))