# Market Bias AI – Liquidity-Aware Algo Trading Engine

**Market Bias AI**, çoklu zaman dilimi OHLC verilerini analiz ederek piyasanın **yön eğilimini (bias)**, **olasılı likidite hedefini (DOL)** ve **güven skorunu (trust)** üreten, XGBoost tabanlı profesyonel bir algo-trading analiz motorudur.

> ⚠️ Önemli: Bu sistem **doğrudan al / sat sinyali üretmez**.  
> Kurumsal trader mantığıyla çalışır ve yalnızca piyasa eğilimlerini ve olası likidite noktalarını gösterir.

---

## ⚙️ Core Features

- 🧠 **XGBoost ML Model**
  - 50M+ candle ile eğitilmiş
  - Feature-based market behavior learning

- 💧 **Liquidity (DOL) Detection**
  - Olası stop-hunt / target bölgeleri
  - Smart money yönü

- 🧭 **Market Bias Classification**
  - `STRONG_LONG`
  - `WEAK_LONG`
  - `RANGE`
  - `WEAK_SHORT`
  - `STRONG_SHORT`
  - `NO_TRADE`

- 📊 **Trust / Confidence Score**
  - Market netliği ölçümü
  - Low trust = no trade zone

- ⏱️ **Multi-Timeframe Support**
  - 1m, 5m, 15m, 1h, 4h, Daily

- 🔌 **Modular Architecture**
  - Hook sistemi
  - API / bot / UI entegrasyonuna hazır

---

## 🧪 Example Output

```json
{
  "candles_used": 200,
  "bias": "WEAK_LONG",
  "trust_percent": 13.6,
  "DOL_target": 90105.08
}
