import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
from pandas.plotting import parallel_coordinates


def column_chart(categories, values, xlabel='Category', ylabel='Value', title='Column Chart', bar_kwargs=None):

    if bar_kwargs is None:
        bar_kwargs = {}
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(categories, values, **bar_kwargs)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    plt.show()


def bar_chart(categories, values, xlabel='Value', ylabel='Category', title='Bar Chart', bar_kwargs=None):

    if bar_kwargs is None:
        bar_kwargs = {}
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.barh(categories, values, **bar_kwargs)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    plt.show()


def column_grouped(data, categories, labels, xlabel='Category', ylabel='Value', title='Grouped Column Chart', bar_kwargs=None):

    if bar_kwargs is None:
        bar_kwargs = {}
    
    x = np.arange(len(categories))
    width = 0.3
    fig, ax = plt.subplots(figsize=(8, 6))
    for i, label in enumerate(labels):
        ax.bar(x + i * width, data[label], width=width, label=label, **bar_kwargs)
    
    ax.set_xticks(x + width / 2)
    ax.set_xticklabels(categories)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.legend()
    plt.show()


def bar_grouped(data, categories, labels, xlabel='Value', ylabel='Category', title='Grouped Bar Chart', bar_kwargs=None):

    if bar_kwargs is None:
        bar_kwargs = {}
    
    y = np.arange(len(categories))
    width = 0.3
    fig, ax = plt.subplots(figsize=(8, 6))
    for i, label in enumerate(labels):
        ax.barh(y + i * width, data[label], height=width, label=label, **bar_kwargs)
    
    ax.set_yticks(y + width / 2)
    ax.set_yticklabels(categories)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.legend()
    plt.show()


def symbol_proportional(categories, values, xlabel='Category', ylabel='Value', title='Proportional Symbol Chart', scatter_kwargs=None):

    if scatter_kwargs is None:
        scatter_kwargs = {}
    
    sizes = np.array(values) * 10  # Scale values for visualization
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(categories, values, s=sizes, **scatter_kwargs)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    plt.show()


def lollipop_chart(categories, values, xlabel='Category', ylabel='Value', title='Lollipop Chart', lollipop_kwargs=None):

    if lollipop_kwargs is None:
        lollipop_kwargs = {}
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.vlines(categories, 0, values, **lollipop_kwargs)
    ax.scatter(categories, values, color='red', zorder=3)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    plt.show()


def radar_chart(data, categories, title='Radar Chart', radar_kwargs=None):

    if radar_kwargs is None:
        radar_kwargs = {}
    
    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    values = data + data[:1]
    angles += angles[:1]
    
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw=dict(polar=True))
    ax.fill(angles, values, alpha=0.3, **radar_kwargs)
    ax.plot(angles, values, **radar_kwargs)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    ax.set_title(title)
    plt.show()

def bar_stacked_proportional(data, categories, labels, xlabel='Percentage', ylabel='Category', title='Stacked Proportional Bar Chart', bar_kwargs=None):

    if bar_kwargs is None:
        bar_kwargs = {}

    df = pd.DataFrame(data, index=categories, columns=labels)
    df = df.div(df.sum(axis=1), axis=0)  # Normalize to proportions

    fig, ax = plt.subplots(figsize=(8, 6))
    df.plot(kind='barh', stacked=True, ax=ax, **bar_kwargs)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.legend()
    plt.show()

def isotope_pictogram(values, labels, symbol='🔵', title='Isotope (Pictogram) Chart'):

    if any(v % 1 != 0 for v in values):
        raise ValueError("Isotope pictograms should only use whole numbers.")

    for label, value in zip(labels, values):
        print(f"{label}: {' '.join([symbol] * int(value))}")

    print(f"\n{title}")

def bullet_chart(value, target, xlabel='Value', title='Bullet Chart', bar_kwargs=None, target_kwargs=None):

    if bar_kwargs is None:
        bar_kwargs = {}
    if target_kwargs is None:
        target_kwargs = {'color': 'red', 'linewidth': 2}

    fig, ax = plt.subplots(figsize=(8, 2))
    ax.barh(0, value, height=0.4, **bar_kwargs)
    ax.axvline(target, **target_kwargs)
    ax.set_yticks([])
    ax.set_xlabel(xlabel)
    ax.set_title(title)
    plt.show()

def parallel_coordinates_chart(df, class_column, title='Parallel Coordinates Chart', line_kwargs=None):

    if line_kwargs is None:
        line_kwargs = {}

    fig, ax = plt.subplots(figsize=(10, 6))
    parallel_coordinates(df, class_column, ax=ax, **line_kwargs)
    ax.set_title(title)
    plt.show()


