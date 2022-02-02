import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

# Collection of all visualization functions
VISUAL_VOCABULARY = {}

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


def scatterplot(x, y, xlabel="X-axis", ylabel="Y-axis", title="Scatterplot", figsize=(8, 6), scatter_kwargs=None):
    """
    Creates a standard scatterplot to show relationships between two variables.
    
    Best used for: Correlation analysis between two numerical variables (e.g., income & life expectancy).
    """
    if scatter_kwargs is None:
        scatter_kwargs = {}
    
    fig, ax = plt.subplots(figsize=figsize)
    ax.scatter(x, y, **scatter_kwargs)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    plt.show()


def line_column(x, y_line, y_column, xlabel="X-axis", ylabel_line="Line Value", ylabel_column="Column Value", title="Line-Column Chart", figsize=(8, 6), line_kwargs=None, bar_kwargs=None):
    """
    Creates a combined line-column chart, showing relationships between an amount (column) and a rate (line).
    
    Best used for: Visualizing trends where a quantity and a rate interact (e.g., inflation vs. unemployment).
    """
    if line_kwargs is None:
        line_kwargs = {}
    if bar_kwargs is None:
        bar_kwargs = {}
    
    fig, ax1 = plt.subplots(figsize=figsize)
    ax2 = ax1.twinx()
    ax1.bar(x, y_column, alpha=0.6, **bar_kwargs)
    ax2.plot(x, y_line, color='red', marker='o', **line_kwargs)
    
    ax1.set_xlabel(xlabel)
    ax1.set_ylabel(ylabel_column, color='blue')
    ax2.set_ylabel(ylabel_line, color='red')
    ax1.set_title(title)
    plt.show()


def scatterplot_connected(x, y, xlabel="X-axis", ylabel="Y-axis", title="Connected Scatterplot", figsize=(8, 6), scatter_kwargs=None, line_kwargs=None):
    """
    Creates a connected scatterplot to show how relationships between two variables evolve over time.
    
    Best used for: Time-series analysis where correlation changes over time.
    """
    if scatter_kwargs is None:
        scatter_kwargs = {}
    if line_kwargs is None:
        line_kwargs = {}
    
    fig, ax = plt.subplots(figsize=figsize)
    ax.scatter(x, y, **scatter_kwargs)
    ax.plot(x, y, **line_kwargs)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    plt.show()


def bubble_chart(x, y, size, xlabel="X-axis", ylabel="Y-axis", title="Bubble Chart", figsize=(8, 6), scatter_kwargs=None):
    """
    Creates a bubble chart, similar to a scatterplot but with a third variable represented by bubble size.
    
    Best used for: Multivariate analysis where size represents importance (e.g., GDP, population, revenue).
    """
    if scatter_kwargs is None:
        scatter_kwargs = {}
    
    fig, ax = plt.subplots(figsize=figsize)
    ax.scatter(x, y, s=size, **scatter_kwargs)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    plt.show()


def xy_heatmap(data, x_labels, y_labels, title="XY Heatmap", figsize=(8, 6), heatmap_kwargs=None):
    """
    Creates an XY heatmap to visualize patterns between two categorical variables.
    
    Best used for: Showing interactions between two categorical datasets (e.g., industry vs. employment rate).
    """
    if heatmap_kwargs is None:
        heatmap_kwargs = {}
    
    fig, ax = plt.subplots(figsize=figsize)
    sns.heatmap(data, xticklabels=x_labels, yticklabels=y_labels, cmap="coolwarm", annot=True, **heatmap_kwargs)
    ax.set_title(title)
    plt.show()
