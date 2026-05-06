"""
American Express — Live Data Refresh Script
==========================================
Fetches the latest AXP stock data via yfinance and appends to datasets.
Run: python src/fetch_live_data.py
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os, json

# ── Try yfinance ──────────────────────────────────────────────
try:
    import yfinance as yf
    YF = True
except ImportError:
    YF = False
    print("⚠️  yfinance not installed. Run: pip install yfinance")

DATA_DIR = os.path.join(os.path.dirname(__file__), '..', 'data')

def fetch_stock_history(ticker='AXP', period='5y'):
    """Fetch historical stock price data."""
    if not YF:
        print("yfinance unavailable — using cached data.")
        return None
    print(f"📡 Fetching {ticker} stock data...")
    stock = yf.Ticker(ticker)
    hist  = stock.history(period=period)
    hist.index = pd.to_datetime(hist.index)
    hist['Return_Daily_pct'] = hist['Close'].pct_change() * 100
    hist['MA_50']  = hist['Close'].rolling(50).mean()
    hist['MA_200'] = hist['Close'].rolling(200).mean()
    hist['Volatility_30d'] = hist['Return_Daily_pct'].rolling(30).std()
    out = os.path.join(DATA_DIR, 'amex_stock_history.csv')
    hist.to_csv(out)
    print(f"✅ Stock data saved → {out}")
    print(f"   Records: {len(hist)} | Latest close: ${hist['Close'].iloc[-1]:.2f}")
    return hist

def fetch_stock_info(ticker='AXP'):
    """Fetch current fundamentals."""
    if not YF:
        return {}
    stock = yf.Ticker(ticker)
    info  = stock.info
    selected = {
        'Symbol':          info.get('symbol','AXP'),
        'Company':         info.get('longName','American Express'),
        'Sector':          info.get('sector','Financial Services'),
        'Market_Cap_B':    round(info.get('marketCap',0)/1e9, 2),
        'Current_Price':   info.get('currentPrice', info.get('regularMarketPrice', 0)),
        'PE_Ratio':        info.get('trailingPE', 0),
        'Forward_PE':      info.get('forwardPE', 0),
        'PB_Ratio':        info.get('priceToBook', 0),
        'EPS_TTM':         info.get('trailingEps', 0),
        'Dividend_Yield_pct': round((info.get('dividendYield',0) or 0)*100, 2),
        'Beta':            info.get('beta', 0),
        '52W_High':        info.get('fiftyTwoWeekHigh', 0),
        '52W_Low':         info.get('fiftyTwoWeekLow', 0),
        'Avg_Volume_M':    round(info.get('averageVolume',0)/1e6, 2),
        'Revenue_TTM_B':   round(info.get('totalRevenue',0)/1e9, 2),
        'Profit_Margin_pct': round((info.get('profitMargins',0) or 0)*100, 2),
        'ROE_pct':         round((info.get('returnOnEquity',0) or 0)*100, 2),
        'Fetched_At':      datetime.now().isoformat(),
    }
    out = os.path.join(DATA_DIR, 'amex_live_fundamentals.json')
    with open(out, 'w') as f:
        json.dump(selected, f, indent=2)
    print(f"✅ Live fundamentals saved → {out}")
    for k, v in selected.items():
        print(f"   {k:<28}: {v}")
    return selected

def compute_technical_signals(df):
    """Add technical indicators to stock dataframe."""
    if df is None:
        return None
    df = df.copy()
    # RSI
    delta = df['Close'].diff()
    gain  = delta.clip(lower=0).rolling(14).mean()
    loss  = (-delta.clip(upper=0)).rolling(14).mean()
    rs    = gain / loss
    df['RSI_14'] = 100 - (100 / (1 + rs))
    # MACD
    ema12 = df['Close'].ewm(span=12, adjust=False).mean()
    ema26 = df['Close'].ewm(span=26, adjust=False).mean()
    df['MACD']        = ema12 - ema26
    df['MACD_Signal'] = df['MACD'].ewm(span=9, adjust=False).mean()
    df['MACD_Hist']   = df['MACD'] - df['MACD_Signal']
    # Bollinger Bands
    df['BB_Mid']   = df['Close'].rolling(20).mean()
    df['BB_Std']   = df['Close'].rolling(20).std()
    df['BB_Upper'] = df['BB_Mid'] + 2 * df['BB_Std']
    df['BB_Lower'] = df['BB_Mid'] - 2 * df['BB_Std']
    # Signal
    last = df.iloc[-1]
    signals = []
    if last['RSI_14'] < 30:   signals.append("RSI Oversold 🟢")
    elif last['RSI_14'] > 70: signals.append("RSI Overbought 🔴")
    if last['MACD'] > last['MACD_Signal']:  signals.append("MACD Bullish 📈")
    else:                                    signals.append("MACD Bearish 📉")
    if last['Close'] > last['MA_200']:       signals.append("Above 200MA ✅")
    else:                                    signals.append("Below 200MA ⚠️")
    print(f"\n📊 Technical Signals for AXP:")
    for s in signals:
        print(f"   {s}")
    out = os.path.join(DATA_DIR, 'amex_stock_technical.csv')
    df.to_csv(out)
    print(f"\n✅ Technical indicators saved → {out}")
    return df

def generate_summary_report():
    """Generate a quick markdown summary of key stats."""
    ann = pd.read_csv(os.path.join(DATA_DIR, 'amex_annual_financials.csv'))
    latest = ann.iloc[-1]
    prev   = ann.iloc[-2]
    rev_chg = (latest.Total_Revenue_B - prev.Total_Revenue_B) / prev.Total_Revenue_B * 100
    ni_chg  = (latest.Net_Income_B - prev.Net_Income_B) / prev.Net_Income_B * 100

    report = f"""# AXP Quick Report — Generated {datetime.now().strftime('%Y-%m-%d %H:%M')}

## FY{int(latest.Year)} Highlights
| Metric | Value | YoY Change |
|--------|-------|------------|
| Total Revenue | ${latest.Total_Revenue_B:.1f}B | {rev_chg:+.1f}% |
| Net Income | ${latest.Net_Income_B:.2f}B | {ni_chg:+.1f}% |
| Diluted EPS | ${latest.EPS_Diluted:.2f} | — |
| Billed Business | ${latest.Billed_Business_T:.2f}T | — |
| Cards In Force | {latest.Cards_In_Force_M:.0f}M | — |
| Return on Equity | {latest.Return_on_Equity_pct:.1f}% | — |
| Net Margin | {latest.Net_Income_B/latest.Total_Revenue_B*100:.1f}% | — |

*Report auto-generated by fetch_live_data.py*
"""
    out = os.path.join(DATA_DIR, '..', 'reports', 'quick_summary.md')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, 'w') as f:
        f.write(report)
    print(f"\n✅ Summary report → reports/quick_summary.md")

if __name__ == '__main__':
    print("=" * 55)
    print("  🏦 American Express — Live Data Refresh")
    print("=" * 55)
    hist = fetch_stock_history()
    info = fetch_stock_info()
    if hist is not None:
        compute_technical_signals(hist)
    generate_summary_report()
    print("\n✅ All done!")
