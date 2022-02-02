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
    """
    Creates a column chart to show changes over time.
    
    Best used for: Displaying a single series of change over time (e.g., revenue, population growth).
    
    Parameters:
    - x: List or array of time values.
    - y: List or array of corresponding values.
    - xlabel: Label for the x-axis.
    - ylabel: Label for the y-axis.
    - title: Title of the chart.
    - bar_kwargs: Dict for bar customization (e.g., color, width).
    """
    if bar_kwargs is None:
        bar_kwargs = {}
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(x, y, **bar_kwargs)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    plt.show()


def slope_chart(categories, values, xlabel='Category', ylabel='Value', title='Slope Chart', line_kwargs=None):
    """
    Creates a slope chart to show changes between 2-3 key points.
    
    Best used for: Showing simple changes between categories without missing key details.
    
    Parameters:
    - categories: List of category labels.
    - values: List of corresponding values.
    - xlabel: Label for the x-axis.
    - ylabel: Label for the y-axis.
    - title: Title of the chart.
    - line_kwargs: Dict for line customization (e.g., linestyle, marker).
    """
    if line_kwargs is None:
        line_kwargs = {}
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(categories, values, marker='o', **line_kwargs)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    plt.show()


def area_chart(x, y, xlabel='Time', ylabel='Value', title='Area Chart', area_kwargs=None):
    """
    Creates an area chart to show changes in total values over time.
    
    Best used for: Highlighting cumulative change but not ideal for seeing individual component changes.
    
    Parameters:
    - x: List or array of time values.
    - y: List or array of corresponding values.
    - xlabel: Label for the x-axis.
    - ylabel: Label for the y-axis.
    - title: Title of the chart.
    - area_kwargs: Dict for fill customization (e.g., color, alpha).
    """
    if area_kwargs is None:
        area_kwargs = {}
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.fill_between(x, y, **area_kwargs)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    plt.show()
