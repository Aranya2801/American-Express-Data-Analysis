"""
amex_utils.py — Shared utilities for the AXP analysis project
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from matplotlib.patches import FancyBboxPatch
import os

# ── Brand palette ─────────────────────────────────────────────
AMEX_BLUE   = '#016FD0'
AMEX_GOLD   = '#C6A84C'
AMEX_DARK   = '#0F1B2D'
AMEX_CARD   = '#162032'
AMEX_BORDER = '#1E3A5F'
AMEX_GREEN  = '#00A878'
AMEX_RED    = '#E05C5C'
AMEX_SILVER = '#A8B2C1'

PALETTE = [AMEX_BLUE, AMEX_GOLD, AMEX_GREEN, AMEX_RED, AMEX_SILVER,
           '#FF9F43', '#7B5EA7', '#F4845F']

def apply_amex_style():
    """Apply the AXP dark brand style to all matplotlib plots."""
    plt.rcParams.update({
        'figure.facecolor':   AMEX_DARK,
        'axes.facecolor':     AMEX_CARD,
        'axes.edgecolor':     AMEX_BORDER,
        'axes.labelcolor':    '#FFFFFF',
        'text.color':         '#FFFFFF',
        'xtick.color':        AMEX_SILVER,
        'ytick.color':        AMEX_SILVER,
        'grid.color':         AMEX_BORDER,
        'grid.linestyle':     '--',
        'grid.alpha':         0.4,
        'font.family':        'DejaVu Sans',
        'axes.spines.top':    False,
        'axes.spines.right':  False,
        'axes.spines.left':   False,
        'axes.spines.bottom': False,
        'legend.facecolor':   AMEX_CARD,
        'legend.edgecolor':   AMEX_BORDER,
        'legend.labelcolor':  AMEX_SILVER,
    })

def fmt_billions(val, _):
    return f'${val:.0f}B'

def fmt_pct(val, _):
    return f'{val:.1f}%'

def add_value_labels(ax, bars, fmt='${:.1f}B', color=None, offset=0.3, fontsize=9):
    """Add value labels on top of bar charts."""
    for bar in bars:
        height = bar.get_height()
        label  = fmt.format(height)
        c = color or AMEX_GOLD
        ax.text(bar.get_x() + bar.get_width()/2., height + offset,
                label, ha='center', va='bottom', fontsize=fontsize,
                color=c, fontweight='bold')

def yoy_growth(series):
    """Return YoY percentage growth series."""
    return series.pct_change() * 100

def cagr(start_val, end_val, periods):
    """Compound Annual Growth Rate."""
    return ((end_val / start_val) ** (1 / periods) - 1) * 100

def describe_financials(df):
    """Print a rich financial summary table."""
    print("=" * 68)
    print(f"  {'AMERICAN EXPRESS — KEY FINANCIALS':^64}")
    print("=" * 68)
    print(f"  {'Year':<6} {'Revenue':>10} {'Net Inc':>9} {'EPS':>7} {'Margin':>8} {'ROE':>7} {'YoY Rev':>9}")
    print("  " + "-" * 60)
    for _, row in df.iterrows():
        margin = row.Net_Income_B / row.Total_Revenue_B * 100
        yoy    = row.get('Revenue_YoY_pct', float('nan'))
        yoy_s  = f"{yoy:+.1f}%" if not pd.isna(yoy) else "  —  "
        print(f"  {int(row.Year):<6} "
              f"${row.Total_Revenue_B:>8.2f}B "
              f"${row.Net_Income_B:>7.2f}B "
              f"${row.EPS_Diluted:>5.2f} "
              f"{margin:>7.1f}% "
              f"{row.Return_on_Equity_pct:>6.1f}% "
              f"{yoy_s:>9}")
    print("=" * 68)
    rev_cagr = cagr(df.iloc[0].Total_Revenue_B, df.iloc[-1].Total_Revenue_B, len(df)-1)
    ni_cagr  = cagr(df.iloc[0].Net_Income_B,    df.iloc[-1].Net_Income_B,    len(df)-1)
    print(f"  Revenue CAGR ({int(df.Year.min())}–{int(df.Year.max())}): {rev_cagr:.2f}%")
    print(f"  Net Income CAGR:  {ni_cagr:.2f}%")
    print("=" * 68)

def waterfall_chart(ax, labels, values, title='', color_pos=AMEX_GREEN, color_neg=AMEX_RED):
    """Render a waterfall chart on the given axes."""
    running = 0
    bottoms, tops, colors = [], [], []
    for v in values:
        bottoms.append(running if v > 0 else running + v)
        tops.append(abs(v))
        colors.append(color_pos if v >= 0 else color_neg)
        running += v
    bars = ax.bar(labels, tops, bottom=bottoms, color=colors, alpha=0.88, width=0.55)
    for bar, v in zip(bars, values):
        ax.text(bar.get_x() + bar.get_width()/2,
                bar.get_height() + bar.get_y() + 0.2,
                f'{v:+.1f}', ha='center', fontsize=9,
                color=color_pos if v >= 0 else color_neg, fontweight='bold')
    ax.set_title(title, fontsize=12, color='white', fontweight='bold')
    ax.yaxis.set_major_formatter(mticker.FuncFormatter(fmt_billions))
    ax.grid(axis='y', alpha=0.3)

def rolling_correlation(s1, s2, window=3):
    """Rolling correlation between two series."""
    return s1.rolling(window).corr(s2)

def load_all_data(data_dir='../data'):
    """Load all project CSVs into a dict of DataFrames."""
    files = {
        'annual':    'amex_annual_financials.csv',
        'quarterly': 'amex_quarterly_data.csv',
        'segments':  'amex_segments.csv',
        'customer':  'amex_customer_metrics.csv',
        'comp':      'competitor_analysis.csv',
    }
    dfs = {}
    for key, fname in files.items():
        path = os.path.join(data_dir, fname)
        if os.path.exists(path):
            dfs[key] = pd.read_csv(path)
            print(f"✅ Loaded {key:12s}: {dfs[key].shape}")
        else:
            print(f"⚠️  Missing: {path}")
    return dfs

def compute_annual_metrics(df):
    """Add derived columns to annual DataFrame in-place."""
    df['Revenue_YoY_pct']   = df['Total_Revenue_B'].pct_change() * 100
    df['NetIncome_YoY_pct'] = df['Net_Income_B'].pct_change() * 100
    df['Net_Margin_pct']    = df['Net_Income_B'] / df['Total_Revenue_B'] * 100
    df['Revenue_Per_Card']  = (df['Total_Revenue_B'] * 1e9) / (df['Cards_In_Force_M'] * 1e6)
    df['Card_Fee_pct_Rev']  = df['Net_Card_Fee_Revenue_B'] / df['Total_Revenue_B'] * 100
    df['P_E_Ratio']         = df['Stock_Price_EOY'] / df['EPS_Diluted']
    df['NII_as_pct_Rev']    = df['Net_Interest_Income_B'] / df['Total_Revenue_B'] * 100
    return df

if __name__ == '__main__':
    apply_amex_style()
    dfs = load_all_data(data_dir=os.path.join(os.path.dirname(__file__), '..', 'data'))
    if 'annual' in dfs:
        df = compute_annual_metrics(dfs['annual'])
        describe_financials(df)
        rev_cagr = cagr(df.iloc[0].Total_Revenue_B, df.iloc[-1].Total_Revenue_B, len(df)-1)
        print(f"\n  Card Fee CAGR: {cagr(df.iloc[0].Net_Card_Fee_Revenue_B, df.iloc[-1].Net_Card_Fee_Revenue_B, len(df)-1):.2f}%")
        print(f"  Billed Bus CAGR: {cagr(df.iloc[0].Billed_Business_T, df.iloc[-1].Billed_Business_T, len(df)-1):.2f}%")
