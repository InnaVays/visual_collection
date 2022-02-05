import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

def scatterplot(x, y, xlabel="X-axis", ylabel="Y-axis", title="Scatterplot", figsize=(8, 6), scatter_kwargs=None):

    if scatter_kwargs is None:
        scatter_kwargs = {}
    
    fig, ax = plt.subplots(figsize=figsize)
    ax.scatter(x, y, **scatter_kwargs)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    plt.show()


def line_column(x, y_line, y_column, xlabel="X-axis", ylabel_line="Line Value", ylabel_column="Column Value", title="Line-Column Chart", figsize=(8, 6), line_kwargs=None, bar_kwargs=None):

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

    if scatter_kwargs is None:
        scatter_kwargs = {}
    
    fig, ax = plt.subplots(figsize=figsize)
    ax.scatter(x, y, s=size, **scatter_kwargs)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    plt.show()


def xy_heatmap(data, x_labels, y_labels, title="XY Heatmap", figsize=(8, 6), heatmap_kwargs=None):

    if heatmap_kwargs is None:
        heatmap_kwargs = {}
    
    fig, ax = plt.subplots(figsize=figsize)
    sns.heatmap(data, xticklabels=x_labels, yticklabels=y_labels, cmap="coolwarm", annot=True, **heatmap_kwargs)
    ax.set_title(title)
    plt.show()
