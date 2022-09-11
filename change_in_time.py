import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

def line_chart(x, y, xlabel='Time', ylabel='Value', title='Line Chart', line_kwargs=None):
    """
    Creates a standard line chart to show changes over time.
    
    Best used for: Time series trends (e.g., stock prices, economic indicators).
    
    Parameters:
    - x: List or array of time values.
    - y: List or array of corresponding values.
    - xlabel: Label for the x-axis.
    - ylabel: Label for the y-axis.
    - title: Title of the chart.
    - line_kwargs: Dict for line customization (e.g., linestyle, color, marker).
    """

    if line_kwargs is None:
        line_kwargs = {}
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(x, y, **line_kwargs)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    plt.show()


def column_timeline(x, y, xlabel='Time', ylabel='Value', title='Column Timeline', bar_kwargs=None):

    if bar_kwargs is None:
        bar_kwargs = {}
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(x, y, **bar_kwargs)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    plt.show()


def slope_chart(categories, values, xlabel='Category', ylabel='Value', title='Slope Chart', line_kwargs=None):

    if line_kwargs is None:
        line_kwargs = {}
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(categories, values, marker='o', **line_kwargs)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    plt.show()


def area_chart(x, y, xlabel='Time', ylabel='Value', title='Area Chart', area_kwargs=None):

    if area_kwargs is None:
        area_kwargs = {}
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.fill_between(x, y, **area_kwargs)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    plt.show()

def stock_price_chart(dates, open_prices, close_prices, high_prices, low_prices, title='Stock Price Chart', candlestick_kwargs=None):

    if candlestick_kwargs is None:
        candlestick_kwargs = {}

    fig, ax = plt.subplots(figsize=(10, 6))
    for i in range(len(dates)):
        color = 'green' if close_prices[i] > open_prices[i] else 'red'
        ax.plot([dates[i], dates[i]], [low_prices[i], high_prices[i]], color=color, **candlestick_kwargs)
        ax.plot([dates[i], dates[i]], [open_prices[i], close_prices[i]], color=color, linewidth=3)
    
    ax.set_title(title)
    ax.set_xlabel('Time')
    ax.set_ylabel('Price')
    plt.show()

def fan_chart(x, y_mean, y_lower, y_upper, xlabel='Time', ylabel='Value', title='Fan Chart', line_kwargs=None, fill_kwargs=None):

    if line_kwargs is None:
        line_kwargs = {}
    if fill_kwargs is None:
        fill_kwargs = {}

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(x, y_mean, label='Projection', color='black', **line_kwargs)
    ax.fill_between(x, y_lower, y_upper, color='blue', alpha=0.3, **fill_kwargs)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.legend()
    plt.show()

def scatterplot_line_timeline(x, y, xlabel='Time', ylabel='Value', title='Connected Scatterplot Timeline', line_kwargs=None, scatter_kwargs=None):
 
    if line_kwargs is None:
        line_kwargs = {}
    if scatter_kwargs is None:
        scatter_kwargs = {}

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(x, y, linestyle='-', marker='o', **line_kwargs)
    ax.scatter(x, y, **scatter_kwargs)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    plt.show()

def calendar_heatmap(data, x_labels, y_labels, xlabel='Time', ylabel='Categories', title='Calendar Heatmap', heatmap_kwargs=None):

    if heatmap_kwargs is None:
        heatmap_kwargs = {}

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(data, xticklabels=x_labels, yticklabels=y_labels, **heatmap_kwargs)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    plt.show()

def priestley_timeline(events, durations, xlabel='Time', ylabel='Events', title='Priestley Timeline', bar_kwargs=None):

    if bar_kwargs is None:
        bar_kwargs = {}

    fig, ax = plt.subplots(figsize=(10, 6))
    for i, (start, end) in enumerate(durations):
        ax.barh(i, end - start, left=start, **bar_kwargs)
    
    ax.set_yticks(range(len(events)))
    ax.set_yticklabels(events)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    plt.show()

def circles_timeline(x, y, sizes, xlabel='Time', ylabel='Categories', title='Circles Timeline', scatter_kwargs=None):

    if scatter_kwargs is None:
        scatter_kwargs = {}

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(x, y, s=sizes, **scatter_kwargs)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    plt.show()

def seismogram(x, y, xlabel='Time', ylabel='Magnitude', title='Seismogram', line_kwargs=None):

    if line_kwargs is None:
        line_kwargs = {}

    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, y, **line_kwargs)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    plt.show()
