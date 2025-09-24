"""Generate two analytical charts from sales_transaction.csv and save to analysis_charts.png.

Fixes applied compared to earlier version:
- set explicit x-ticks to avoid set_xticklabels warning
- use matplotlib barh with explicit color list to avoid seaborn palette deprecation
"""

import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


DATA_FILE = 'sales_transaction.csv'
OUT_FILE = 'analysis_charts.png'


def load_and_clean(path):
    df = pd.read_csv(path)
    df = df.drop_duplicates()
    df = df[~df['TransactionNo'].astype(str).str.startswith('C', na=False)]
    df = df[(df['Quantity'] > 0) & (df['Price'] > 0)]
    df['Revenue'] = df['Price'] * df['Quantity']
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df = df.dropna(subset=['Date'])
    df['YearMonth'] = df['Date'].dt.to_period('M').astype(str)
    return df


def plot_charts(df, out_path):
    # Monthly revenue
    monthly = (
        df.groupby('YearMonth', as_index=False)
          .agg(TotalRevenue=('Revenue', 'sum'), Orders=('TransactionNo', 'nunique'))
          .sort_values('YearMonth')
    )

    # Top-10 products by revenue
    top_products = (
        df.groupby('ProductName', as_index=False)
          .agg(TotalRevenue=('Revenue', 'sum'))
          .sort_values('TotalRevenue', ascending=False)
          .head(10)
    )

    sns.set(style='whitegrid')
    fig, axes = plt.subplots(1, 2, figsize=(16, 6), gridspec_kw={'width_ratios': [2, 1]})

    # Left: Monthly revenue trend (bars + line)
    ax = axes[0]
    ax2 = ax.twinx()
    sns.barplot(data=monthly, x='YearMonth', y='TotalRevenue', color='#4c72b0', ax=ax)
    sns.lineplot(data=monthly, x='YearMonth', y='Orders', marker='o', color='orange', ax=ax2)

    # Explicit ticks to avoid warnings and overlapping labels
    ticks = list(range(len(monthly)))
    ax.set_xticks(ticks)
    ax.set_xticklabels(monthly['YearMonth'], rotation=70)

    ax.set_title('Monthly Revenue (bars) and Orders (line)')
    ax.set_xlabel('Month')
    ax.set_ylabel('Revenue')
    ax2.set_ylabel('Orders')

    # Right: Top-10 products by revenue (use matplotlib barh with color list)
    ax_r = axes[1]
    colors = sns.color_palette('viridis', len(top_products))
    ax_r.barh(top_products['ProductName'], top_products['TotalRevenue'], color=colors)
    ax_r.invert_yaxis()
    ax_r.set_title('Top 10 Products by Revenue')
    ax_r.set_xlabel('Revenue')
    ax_r.set_ylabel('')

    plt.tight_layout()
    fig.savefig(out_path, dpi=150)
    plt.close(fig)


def main():
    cwd = os.path.dirname(__file__)
    data_path = os.path.join(cwd, DATA_FILE)
    out_path = os.path.join(cwd, OUT_FILE)

    if not os.path.exists(data_path):
        print(f"Data file not found: {data_path}")
        return

    df = load_and_clean(data_path)
    print('Loaded and cleaned data, rows=', len(df))
    plot_charts(df, out_path)
    print('Saved charts to', out_path)


if __name__ == '__main__':
    main()
