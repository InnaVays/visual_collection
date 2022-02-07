import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
import squarify
from matplotlib_venn import venn2, venn3
from scipy.spatial import Voronoi, voronoi_plot_2d
import plotly.express as px

def column_stacked(data, categories, labels, xlabel='Category', ylabel='Value', title='Stacked Column Chart', bar_kwargs=None):

    if bar_kwargs is None:
        bar_kwargs = {}
    
    df = pd.DataFrame(data, index=categories, columns=labels)
    df.plot(kind='bar', stacked=True, figsize=(8, 6), **bar_kwargs)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.legend()
    plt.show()

def pie_chart(values, labels, title='Pie Chart', pie_kwargs=None):

    if pie_kwargs is None:
        pie_kwargs = {}
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.pie(values, labels=labels, autopct='%1.1f%%', **pie_kwargs)
    ax.set_title(title)
    plt.show()


def doughnut_chart(values, labels, title='Doughnut Chart', pie_kwargs=None):

    if pie_kwargs is None:
        pie_kwargs = {}
    
    fig, ax = plt.subplots(figsize=(8, 6))
    wedges, _ = ax.pie(values, labels=labels, autopct='%1.1f%%', **pie_kwargs)
    plt.setp(wedges, width=0.4)
    ax.set_title(title)
    plt.show()


def treemap(values, labels, title='Treemap', treemap_kwargs=None):

    if treemap_kwargs is None:
        treemap_kwargs = {}
    
    fig, ax = plt.subplots(figsize=(8, 6))
    squarify.plot(sizes=values, label=labels, ax=ax, **treemap_kwargs)
    ax.set_title(title)
    plt.axis('off')
    plt.show()


def venn_diagram(sets, labels, title='Venn Diagram'):

    fig, ax = plt.subplots(figsize=(8, 6))
    if len(sets) == 2:
        venn2(sets, set_labels=labels, ax=ax)
    elif len(sets) == 3:
        venn3(sets, set_labels=labels, ax=ax)
    else:
        raise ValueError("Venn diagrams only support 2 or 3 sets.")
    
    ax.set_title(title)
    plt.show()


def waterfall_chart(categories, values, xlabel='Category', ylabel='Value', title='Waterfall Chart', bar_kwargs=None):

    if bar_kwargs is None:
        bar_kwargs = {}
    
    running_total = np.cumsum([0] + values[:-1])
    fig, ax = plt.subplots(figsize=(8, 6))
    colors = ['green' if v >= 0 else 'red' for v in values]
    ax.bar(categories, values, bottom=running_total, color=colors, **bar_kwargs)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    plt.show()

def voronoi_diagram(points, title="Voronoi Diagram", voronoi_kwargs=None):

    if voronoi_kwargs is None:
        voronoi_kwargs = {}

    vor = Voronoi(points)
    fig, ax = plt.subplots(figsize=(8, 6))
    voronoi_plot_2d(vor, ax=ax, **voronoi_kwargs)
    ax.set_title(title)
    plt.show()


def sunburst_chart(data, path, values, title="Sunburst Chart"):
    """
    Creates a sunburst chart for hierarchical part-to-whole relationships.

    Best used for: Hierarchical structures, organizational breakdowns.

    Parameters:
    - data: DataFrame containing hierarchical data.
    - path: List of column names defining hierarchy.
    - values: Column name containing numerical values.
    - title: Title of the chart.
    """
    fig = px.sunburst(data, path=path, values=values, title=title)
    fig.show()

def arc_chart(categories, values, title="Arc Chart", arc_kwargs=None):

    if arc_kwargs is None:
        arc_kwargs = {}

    fig, ax = plt.subplots(figsize=(8, 4), subplot_kw={'projection': 'polar'})
    theta = np.linspace(0, np.pi, len(values))
    ax.bar(theta, values, width=np.pi / len(values), **arc_kwargs)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(title)
    plt.show()

def gridplot(data, rows, cols, title="Gridplot", grid_kwargs=None):

    if grid_kwargs is None:
        grid_kwargs = {}

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.imshow(data, cmap="gray_r", **grid_kwargs)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(title)
    plt.show()
