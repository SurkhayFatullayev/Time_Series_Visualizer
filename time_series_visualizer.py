import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_and_clean_data():
    df = pd.read_csv("fcc-forum-pageviews.csv", index_col="date", parse_dates=True)
    
    df = df[(df['value'] >= df['value'].quantile(0.025)) & (df['value'] <= df['value'].quantile(0.975))]
    
    return df

def draw_line_plot(df):
    fig, ax = plt.subplots(figsize=(12, 5))
    ax.plot(df.index, df['value'], color='red', linewidth=1)
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    
    return fig

def draw_bar_plot(df):
    df_bar = df.copy()
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month
    df_grouped = df_bar.groupby(['year', 'month'])['value'].mean().unstack()
    
    fig = df_grouped.plot(kind='bar', figsize=(12, 6)).figure
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months", labels=["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    
    return fig

def draw_box_plot(df):
    df_box = df.copy()
    df_box['year'] = df_box.index.year
    df_box['month'] = df_box.index.strftime('%b')
    
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))
    sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")
    
    order = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    sns.boxplot(x='month', y='value', data=df_box, ax=axes[1], order=order)
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")
    
    return fig

df = load_and_clean_data()

line_plot_fig = draw_line_plot(df)
bar_plot_fig = draw_bar_plot(df)
box_plot_fig = draw_box_plot(df)

# Show plots
plt.show()
