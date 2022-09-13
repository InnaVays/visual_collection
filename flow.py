import matplotlib.pyplot as plt
import pandas as pd
import networkx as nx
import numpy as np
from matplotlib.sankey import Sankey
import seaborn as sns

def sankey_chart(flows, labels, title='Sankey Diagram'):
    """
    Creates a Sankey diagram to show flow between multiple conditions.
    
    Best used for: Visualizing transitions between states, such as financial flows or process changes.
    """
    fig, ax = plt.subplots(figsize=(8, 6))
    sankey = Sankey(ax=ax, unit=None)
    for flow, label in zip(flows, labels):
        sankey.add(flows=[flow], labels=[label])
    sankey.finish()
    ax.set_title(title)
    plt.show()

def waterfall_chart(categories, values, xlabel='Category', ylabel='Value', title='Waterfall Chart', bar_kwargs=None):
    """
    Creates a waterfall chart to show sequential changes in data, including positive and negative components.
    
    Best used for: Budget analysis, revenue breakdowns.
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

def chord_diagram(matrix, labels, title='Chord Diagram'):
    """
    Creates a chord diagram to visualize 2-way flows between multiple categories.
    
    Best used for: Displaying relationships in a matrix, such as trade flows or connectivity.
    """
    fig, ax = plt.subplots(figsize=(8, 8))
    G = nx.DiGraph()
    for i, label in enumerate(labels):
        for j, value in enumerate(matrix[i]):
            if value > 0:
                G.add_edge(labels[i], labels[j], weight=value)
    
    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', arrows=True)
    edge_labels = {(labels[i], labels[j]): matrix[i][j] for i in range(len(labels)) for j in range(len(labels)) if matrix[i][j] > 0}
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
    ax.set_title(title)
    plt.show()


def network_graph(edges, title='Network Graph'):
    """
    Creates a network graph to show interconnected relationships.
    
    Best used for: Visualizing relationships, such as trade partners, citations, or social networks.
    """
    fig, ax = plt.subplots(figsize=(8, 8))
    G = nx.Graph()
    G.add_edges_from(edges)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_color='lightblue', edge_color='gray', ax=ax)
    ax.set_title(title)
    plt.show()

