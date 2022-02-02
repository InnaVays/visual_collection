import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

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

