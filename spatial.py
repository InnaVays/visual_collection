import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from mpl_toolkits.axes_grid1 import make_axes_locatable

def basic_choropleth(geo_data, data, column, cmap='Blues', title='Choropleth Map', map_kwargs=None):

    if map_kwargs is None:
        map_kwargs = {}
    
    fig, ax = plt.subplots(figsize=(10, 6))
    geo_data.plot(column=column, cmap=cmap, legend=True, ax=ax, **map_kwargs)
    ax.set_title(title)
    plt.show()


def proportional_symbol_map(geo_data, data, column, size_factor=100, title='Proportional Symbol Map', map_kwargs=None):

    if map_kwargs is None:
        map_kwargs = {}
    
    fig, ax = plt.subplots(figsize=(10, 6))
    geo_data.plot(ax=ax, color='lightgrey', edgecolor='black', **map_kwargs)
    ax.scatter(data['longitude'], data['latitude'], s=data[column] * size_factor, alpha=0.5, color='red')
    ax.set_title(title)
    plt.show()


def flow_map(geo_data, flows, title='Flow Map', map_kwargs=None):

    if map_kwargs is None:
        map_kwargs = {}
    
    fig, ax = plt.subplots(figsize=(10, 6))
    geo_data.plot(ax=ax, color='lightgrey', edgecolor='black', **map_kwargs)
    for _, row in flows.iterrows():
        ax.arrow(row['start_lon'], row['start_lat'], row['end_lon'] - row['start_lon'], row['end_lat'] - row['start_lat'],
                 head_width=0.2, alpha=0.6, color='blue', length_includes_head=True)
    ax.set_title(title)
    plt.show()


def contour_map(geo_data, data, column, cmap='coolwarm', title='Contour Map', map_kwargs=None):

    if map_kwargs is None:
        map_kwargs = {}
    
    fig, ax = plt.subplots(figsize=(10, 6))
    geo_data.plot(ax=ax, color='lightgrey', edgecolor='black', **map_kwargs)
    contour = ax.tricontourf(data['longitude'], data['latitude'], data[column], cmap=cmap)
    plt.colorbar(contour, ax=ax)
    ax.set_title(title)
    plt.show()


def heat_map(data, title='Heat Map', cmap='Reds', bins=50, heatmap_kwargs=None):

    if heatmap_kwargs is None:
        heatmap_kwargs = {}
    
    fig, ax = plt.subplots(figsize=(10, 6))
    counts, xedges, yedges = np.histogram2d(data['longitude'], data['latitude'], bins=bins)
    ax.imshow(counts.T, origin='lower', cmap=cmap, aspect='auto', **heatmap_kwargs)
    ax.set_title(title)
    plt.show()

