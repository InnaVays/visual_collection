import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

def bar_ordered(categories, values, xlabel='Value', ylabel='Category', title='Ordered Bar Chart', bar_kwargs=None):
    """
    Creates an ordered bar chart to emphasize ranking.
    
    Best used for: Comparing ranked values, league tables, constituency election results.
    """
    if bar_kwargs is None:
        bar_kwargs = {}
    
    sorted_indices = np.argsort(values)[::-1]
    sorted_categories = np.array(categories)[sorted_indices]
    sorted_values = np.array(values)[sorted_indices]
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.barh(sorted_categories, sorted_values, **bar_kwargs)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    plt.show()

def column_ordered(categories, values, xlabel='Category', ylabel='Value', title='Ordered Column Chart', bar_kwargs=None):
    """
    Creates an ordered column chart to emphasize ranking.
    
    Best used for: Highlighting rankings when absolute values matter less.
    """
    if bar_kwargs is None:
        bar_kwargs = {}
    
    sorted_indices = np.argsort(values)[::-1]
    sorted_categories = np.array(categories)[sorted_indices]
    sorted_values = np.array(values)[sorted_indices]
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(sorted_categories, sorted_values, **bar_kwargs)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    plt.show()

def slope_chart(categories, values1, values2, xlabel='Category', ylabel='Value', title='Slope Chart', line_kwargs=None):
    """
    Creates a slope chart to show ranking changes between two time points.
    
    Best used for: Showing how rankings have changed over time or between categories.
    """
    if line_kwargs is None:
        line_kwargs = {}
    
    fig, ax = plt.subplots(figsize=(8, 6))
    for i in range(len(categories)):
        ax.plot([0, 1], [values1[i], values2[i]], marker='o', label=categories[i], **line_kwargs)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(['Start', 'End'])
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.legend()
    plt.show()

def lollipop_h(categories, values, xlabel='Value', ylabel='Category', title='Horizontal Lollipop Chart', lollipop_kwargs=None):
    """
    Creates a horizontal lollipop chart for ranking visualization.
    
    Best used for: Emphasizing specific values in a ranked dataset while maintaining order.
    """
    if lollipop_kwargs is None:
        lollipop_kwargs = {}
    
    sorted_indices = np.argsort(values)[::-1]
    sorted_categories = np.array(categories)[sorted_indices]
    sorted_values = np.array(values)[sorted_indices]
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.hlines(sorted_categories, 0, sorted_values, **lollipop_kwargs)
    ax.scatter(sorted_values, sorted_categories, color='red', zorder=3)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    plt.show()

def lollipop_v(categories, values, xlabel='Category', ylabel='Value', title='Vertical Lollipop Chart', lollipop_kwargs=None):
    """
    Creates a vertical lollipop chart for ranking visualization.
    
    Best used for: Highlighting specific values while maintaining an ordered ranking.
    """
    if lollipop_kwargs is None:
        lollipop_kwargs = {}
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.vlines(categories, 0, values, **lollipop_kwargs)
    ax.scatter(categories, values, color='red', zorder=3)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    plt.show()

def symbol_proportional_ordered(categories, values, xlabel='Category', ylabel='Value', title='Proportional Symbol Chart', scatter_kwargs=None):

    if scatter_kwargs is None:
        scatter_kwargs = {}

    sizes = np.array(values) * 10  # Scale values for visualization
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(categories, values, s=sizes, **scatter_kwargs)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    plt.show()

def dot_plot_strip(categories, values, xlabel='Category', ylabel='Value', title='Dot Strip Plot', strip_kwargs=None):

    if strip_kwargs is None:
        strip_kwargs = {}

    fig, ax = plt.subplots(figsize=(8, 6))
    sns.stripplot(x=categories, y=values, ax=ax, **strip_kwargs)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    plt.show()