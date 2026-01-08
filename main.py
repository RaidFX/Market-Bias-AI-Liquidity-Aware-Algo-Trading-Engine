from colorama import Fore, Style, init
from tools.getchart import getchart
from model.market_bias_hook import MarketBiasEngine

init(autoreset=True)


def banner(symbol, tf):
    print(Fore.CYAN + "=" * 64)
    print(
        Fore.CYAN
        + Style.BRIGHT
        + f"   MARKET BIAS AI  |  {symbol.upper()}  [{tf}]"
    )
    print(Fore.CYAN + "=" * 64)


def render(result: dict):
    bias = result["bias"]
    trust = result["trust_percent"]
    dol = result["DOL"]
    candles = result["candles_used"]

    color = {
        "STRONG_LONG": Fore.GREEN,
        "WEAK_LONG": Fore.LIGHTGREEN_EX,
        "STRONG_SHORT": Fore.RED,
        "WEAK_SHORT": Fore.LIGHTRED_EX,
        "NO_TRADE": Fore.YELLOW,
    }.get(bias, Fore.WHITE)

    print(Fore.WHITE + f"\n Candles Used : {candles}")
    print(color + Style.BRIGHT + f" Bias         : {bias}")
    print(Fore.MAGENTA + f" Trust        : %{trust}")

    if dol:
        print(Fore.CYAN + f" DOL Target   : {dol}")
    else:
        print(Fore.YELLOW + " DOL Target   : None")

    print(Fore.CYAN + "-" * 64)


def main():
    symbol = input("Symbol (örn BTCUSDT): ").strip()
    exchange = input("Exchange (örn BINANCE): ").strip()
    tf = input("Timeframe (1,5,15,60,240,D): ").strip()

    print(Fore.YELLOW + "\nFetching OHLC data...\n")

    market = getchart(
        symbol=symbol,
        exchange=exchange,
        interval=tf,
        bars=200,
    )

    engine = MarketBiasEngine(
        model_path="model/xgb_full_market_model.pkl",
        min_trust=55,
        lookback_liquidity=20,
    )

    result = engine.evaluate(market["candles"])

    banner(market["symbol"], tf)
    render(result)


if __name__ == "__main__":
    main()
