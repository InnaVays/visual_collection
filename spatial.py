import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from mpl_toolkits.axes_grid1 import make_axes_locatable

def basic_choropleth(geo_data, data, column, cmap='Blues', title='Choropleth Map', map_kwargs=None):
    """
    Creates a choropleth map to represent spatial data using a color scale.
    
    Best used for: Representing rates rather than totals, with sensible base geography.
    """
    if map_kwargs is None:
        map_kwargs = {}
    
    fig, ax = plt.subplots(figsize=(10, 6))
    geo_data.plot(column=column, cmap=cmap, legend=True, ax=ax, **map_kwargs)
    ax.set_title(title)
    plt.show()


def proportional_symbol_map(geo_data, data, column, size_factor=100, title='Proportional Symbol Map', map_kwargs=None):
    """
    Creates a proportional symbol map where symbol size represents total values.
    
    Best used for: Displaying total values rather than rates.
    """
    if map_kwargs is None:
        map_kwargs = {}
    
    fig, ax = plt.subplots(figsize=(10, 6))
    geo_data.plot(ax=ax, color='lightgrey', edgecolor='black', **map_kwargs)
    ax.scatter(data['longitude'], data['latitude'], s=data[column] * size_factor, alpha=0.5, color='red')
    ax.set_title(title)
    plt.show()


def flow_map(geo_data, flows, title='Flow Map', map_kwargs=None):
    """
    Creates a flow map showing movement between locations.
    
    Best used for: Visualizing migration, trade, or movement between regions.
    """
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
    """
    Creates a contour map to represent areas of equal value.
    
    Best used for: Visualizing temperature, elevation, or other continuous spatial values.
    """
    if map_kwargs is None:
        map_kwargs = {}
    
    fig, ax = plt.subplots(figsize=(10, 6))
    geo_data.plot(ax=ax, color='lightgrey', edgecolor='black', **map_kwargs)
    contour = ax.tricontourf(data['longitude'], data['latitude'], data[column], cmap=cmap)
    plt.colorbar(contour, ax=ax)
    ax.set_title(title)
    plt.show()


def heat_map(data, title='Heat Map', cmap='Reds', bins=50, heatmap_kwargs=None):
    """
    Creates a heat map to visualize density patterns.
    
    Best used for: Highlighting areas of high and low concentration.
    """
    if heatmap_kwargs is None:
        heatmap_kwargs = {}
    
    fig, ax = plt.subplots(figsize=(10, 6))
    counts, xedges, yedges = np.histogram2d(data['longitude'], data['latitude'], bins=bins)
    ax.imshow(counts.T, origin='lower', cmap=cmap, aspect='auto', **heatmap_kwargs)
    ax.set_title(title)
    plt.show()

def equalised_cartogram(geo_data, title='Equalised Cartogram', cartogram_kwargs=None):
    """
    Creates an equalised cartogram where map units are converted to equally-sized shapes.
    
    Best used for: Representing voting regions with equal share.
    """
    if cartogram_kwargs is None:
        cartogram_kwargs = {}
    
    fig, ax = plt.subplots(figsize=(10, 6))
    geo_data.plot(ax=ax, **cartogram_kwargs)
    ax.set_title(title)
    plt.show()


def scaled_cartogram(geo_data, column, title='Scaled Cartogram', cartogram_kwargs=None):
    """
    Creates a scaled cartogram by resizing regions according to a specific value.
    
    Best used for: Showing how areas change based on data values.
    """
    if cartogram_kwargs is None:
        cartogram_kwargs = {}
    
    geo_data['scaled_area'] = np.sqrt(geo_data[column])  # Scale by square root for better proportions
    fig, ax = plt.subplots(figsize=(10, 6))
    geo_data.plot(ax=ax, **cartogram_kwargs)
    ax.set_title(title)
    plt.show()


def dot_density(data, title='Dot Density Map', dot_kwargs=None):
    """
    Creates a dot density map to show the location of individual events.
    
    Best used for: Displaying high-density event locations with annotations.
    """
    if dot_kwargs is None:
        dot_kwargs = {}
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(data['longitude'], data['latitude'], alpha=0.5, **dot_kwargs)
    ax.set_title(title)
    plt.show()