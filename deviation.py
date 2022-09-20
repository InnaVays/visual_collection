import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

def bar_diverging(data, labels, colors=('red', 'green'), figsize=(10, 6), bar_kwargs=None, vline_kwargs=None):
    """
    Creates a diverging bar chart with separate customization options for bars and vertical reference line.
    
    Best used for: Trade surplus/deficit, climate change, financial gains/losses.
    """
    if bar_kwargs is None:
        bar_kwargs = {}
    if vline_kwargs is None:
        vline_kwargs = {}

    bar_colors = [colors[0] if val < 0 else colors[1] for val in data]
    
    fig, ax = plt.subplots(figsize=figsize)
    ax.barh(labels, data, color=bar_colors, **bar_kwargs)
    ax.axvline(0, **vline_kwargs)
    plt.show()

def bar_diverging_stacked(data, categories, labels, xlabel='Percentage', title='Diverging Stacked Bar Chart', bar_kwargs=None):
    """
    Creates a diverging stacked bar chart for sentiment-based survey results.
    
    Best used for: Presenting sentiment (Agree/Neutral/Disagree), opinion polls.
    """
    if bar_kwargs is None:
        bar_kwargs = {}
    
    df = pd.DataFrame(data, index=categories, columns=labels)
    df.plot(kind='barh', stacked=True, figsize=(8, 6), **bar_kwargs)
    plt.axvline(0, color='black', linewidth=1)
    plt.xlabel(xlabel)
    plt.title(title)
    plt.show()


def spine_chart(categories, values1, values2, xlabel='Percentage', ylabel='Category', title='Spine Chart', bar_kwargs=None):
    """
    Creates a spine chart to compare two contrasting components (e.g., Male/Female).
    
    Best used for: Gender distribution, urban/rural population splits.
    """
    if bar_kwargs is None:
        bar_kwargs = {}
    
    y = np.arange(len(categories))
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.barh(y, values1, color='blue', label='Group 1', **bar_kwargs)
    ax.barh(y, -np.array(values2), color='orange', label='Group 2', **bar_kwargs)
    ax.axvline(0, color='black', linewidth=1)
    ax.set_yticks(y)
    ax.set_yticklabels(categories)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.legend()
    plt.show()


def line_surplus_deficit_filled(x, y1, y2, xlabel='Time', ylabel='Value', title='Surplus/Deficit Filled Line Chart', fill_kwargs=None, line_kwargs=None):
    """
    Creates a line chart with shaded areas to visualize surplus/deficit balance.
    
    Best used for: Budget balance, stock price fluctuations, economic indicators.
    """
    if line_kwargs is None:
        line_kwargs = {}
    if fill_kwargs is None:
        fill_kwargs = {}
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(x, y1, label='Series 1', color='blue', **line_kwargs)
    ax.plot(x, y2, label='Series 2', color='red', **line_kwargs)
    ax.fill_between(x, y1, y2, where=(y1 >= y2), interpolate=True, color='blue', alpha=0.3, **fill_kwargs)
    ax.fill_between(x, y1, y2, where=(y1 < y2), interpolate=True, color='red', alpha=0.3, **fill_kwargs)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.legend()
    plt.show()
