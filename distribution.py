import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

def histogram(data, bins=10, xlabel='Value', ylabel='Frequency', title='Histogram', hist_kwargs=None):

    if hist_kwargs is None:
        hist_kwargs = {}
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.hist(data, bins=bins, **hist_kwargs)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    plt.show()

def boxplot(data, labels=None, xlabel='Category', ylabel='Value', title='Boxplot', box_kwargs=None):

    if box_kwargs is None:
        box_kwargs = {}
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.boxplot(data, labels=labels, **box_kwargs)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    plt.show()

def violin(data, labels=None, xlabel='Category', ylabel='Value', title='Violin Plot', violin_kwargs=None):

    if violin_kwargs is None:
        violin_kwargs = {}
    
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.violinplot(data=data, ax=ax, **violin_kwargs)
    ax.set_xticklabels(labels)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    plt.show()

def population_pyramid(male_values, female_values, age_groups, xlabel='Population', ylabel='Age Group', title='Population Pyramid', bar_kwargs=None):
    if bar_kwargs is None:
        bar_kwargs = {}
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.barh(age_groups, male_values, label='Male', **bar_kwargs)
    ax.barh(age_groups, [-val for val in female_values], label='Female', **bar_kwargs)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    ax.legend()
    plt.show()

def dot_plot_strip(data, xlabel='Value', ylabel='Category', title='Dot Strip Plot', strip_kwargs=None):

    if strip_kwargs is None:
        strip_kwargs = {}
    
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.stripplot(data=data, ax=ax, **strip_kwargs)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    plt.show()

def dot_plot(categories, values, xlabel='Category', ylabel='Value', title='Dot Plot', dot_kwargs=None):

    if dot_kwargs is None:
        dot_kwargs = {}
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(categories, values, **dot_kwargs)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    plt.show()

def barcode_plot(data, xlabel='Value', ylabel='Frequency', title='Barcode Plot', barcode_kwargs=None):

    if barcode_kwargs is None:
        barcode_kwargs = {}
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.vlines(data, ymin=0, ymax=1, **barcode_kwargs)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    plt.show()

def cumulative_curve(data, xlabel='Value', ylabel='Cumulative Frequency', title='Cumulative Curve', curve_kwargs=None):

    if curve_kwargs is None:
        curve_kwargs = {}
    
    sorted_data = np.sort(data)
    cumulative_freq = np.arange(1, len(data) + 1) / len(data)
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(sorted_data, cumulative_freq, **curve_kwargs)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)
    plt.show()