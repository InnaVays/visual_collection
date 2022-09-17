import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
import squarify
from matplotlib_venn import venn2, venn3
from scipy.spatial import Voronoi, voronoi_plot_2d
import plotly.express as px

def column_stacked(data, categories, labels, xlabel='Category', ylabel='Value', title='Stacked Column Chart', bar_kwargs=None):
    """
    Creates a stacked column chart to show part-to-whole relationships.

    Best used for: Comparing multiple components within a category while maintaining total size.
    """
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
    """
    Creates a pie chart to visualize proportions within a whole.

    Best used for: Displaying simple part-to-whole relationships but may be hard to compare segment sizes.
    """
    if pie_kwargs is None:
        pie_kwargs = {}
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.pie(values, labels=labels, autopct='%1.1f%%', **pie_kwargs)
    ax.set_title(title)
    plt.show()


def doughnut_chart(values, labels, title='Doughnut Chart', pie_kwargs=None):
    """
    Creates a doughnut chart, similar to a pie chart but with a central hole.

    Best used for: Adding additional information in the center while still showing proportions.
    """
    if pie_kwargs is None:
        pie_kwargs = {}
    
    fig, ax = plt.subplots(figsize=(8, 6))
    wedges, _ = ax.pie(values, labels=labels, autopct='%1.1f%%', **pie_kwargs)
    plt.setp(wedges, width=0.4)
    ax.set_title(title)
    plt.show()


def treemap(values, labels, title='Treemap', treemap_kwargs=None):
    """
    Creates a treemap for hierarchical part-to-whole visualization.

    Best used for: Representing nested relationships with relative sizes but can be hard to interpret with many small segments.
    """
    if treemap_kwargs is None:
        treemap_kwargs = {}
    
    fig, ax = plt.subplots(figsize=(8, 6))
    squarify.plot(sizes=values, label=labels, ax=ax, **treemap_kwargs)
    ax.set_title(title)
    plt.axis('off')
    plt.show()


def venn_diagram(sets, labels, title='Venn Diagram'):
    """
    Creates a Venn diagram to show overlaps between sets.

    Best used for: Illustrating relationships between two or three sets.
    """
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
    """
    Creates a waterfall chart to display sequential changes in values, including positive and negative components.

    Best used for: Financial and budget analysis to show cumulative changes.
    """
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
    """
    Creates a Voronoi diagram to partition space based on proximity to given points.

    Best used for: Spatial analysis and nearest-neighbor relationships.
    """
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
    """
    fig = px.sunburst(data, path=path, values=values, title=title)
    fig.show()

def arc_chart(categories, values, title="Arc Chart", arc_kwargs=None):
    """
    Creates an arc chart (hemicycle) to visualize political or proportional results.

    Best used for: Displaying grouped proportional data in a half-circle format.
    """
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
    """
    Creates a gridplot for representing percentage-based information using whole numbers.

    Best used for: Visualizing proportions across multiple categories in a structured layout.
    """
    if grid_kwargs is None:
        grid_kwargs = {}

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.imshow(data, cmap="gray_r", **grid_kwargs)
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_title(title)
    plt.show()
