#!/usr/bin/env python

import corner
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import os
import pandas as pd
import pkg_resources
from scipy.stats import skewnorm

#Dom Rowan 2025

def get_ad_file(filename):
    return pkg_resources.resource_filename(__name__, '../ad_images/' + filename)

coupon_codes = [
        'Magnetohydrodynamics',
        'Kozai-Lidov',
        'Isotopologues',
        'Polycyclic Aromatic Hydrocarbons',
        'Regulus',
        'Superluminous Supernovae',
        'Circumgalactic Medium',
        'Lithium Depletion']

def plotparams(ax, labelsize=15):
    '''
    Basic plot params

    :param ax: axes to modify

    :type ax: matplotlib axes object

    :returns: modified matplotlib axes object
    '''

    if isinstance(ax, np.ndarray):
        for a in ax.reshape(-1):
            plotparams(a)
        return

    ax.minorticks_on()
    ax.yaxis.set_ticks_position('both')
    ax.xaxis.set_ticks_position('both')
    ax.tick_params(direction='in', which='both', labelsize=labelsize)
    ax.tick_params('both', length=8, width=1.8, which='major')
    ax.tick_params('both', length=4, width=1, which='minor')
    for axis in ['top', 'bottom', 'left', 'right']:
        ax.spines[axis].set_linewidth(1.5)
    return ax

def get_optimal_fontsize(fig, ax, text, fraction=0.8):
    bbox = ax.get_window_extent().transformed(fig.dpi_scale_trans.inverted())
    width_inches = bbox.width
    return 0.8 * width_inches * 144 / len(text)  # 72 points per inch

def select_ad(equal):
    
    if equal:
        dir_path = get_ad_file('equal_aspect')
    else:
        dir_path = get_ad_file('wide_aspect')

    fnames = os.listdir(dir_path)
    return os.path.join(dir_path, np.random.choice(fnames))

def promo_plot(samples, **kwargs):

    figure = corner.corner(samples, **kwargs)

    ndim = samples.shape[1]

    axes = np.array(figure.axes)
    for ax in axes:
        ax = plotparams(ax)

    axes = axes.reshape((ndim, ndim))

    n = ndim // 2

    equal = np.random.choice([True, False])

    if equal:
        axi = axes[0, axes.shape[1]-1].inset_axes(
            bounds=[-n+1, -n+1, n, n], transform=axes[0, axes.shape[1]-1].transAxes)
    else:
        axi = axes[0, axes.shape[1]-1].inset_axes(
            bounds=[-n, -n+2, n+1, n-1], transform=axes[0, axes.shape[1]-1].transAxes)


    axi.imshow(mpimg.imread(select_ad(equal)))
    axi.axis('off')
    deal = int(skewnorm.rvs(15, loc=10, scale=3, size=1)[0])
    text = f'Use code "{np.random.choice(coupon_codes)}" for {deal}% off' + r'$^*$'
    fontsize = get_optimal_fontsize(figure, axi, text)
    axi.text(.5, -0.05, text,
             fontsize=fontsize,
             ha='center', va='bottom', transform=axi.transAxes)

    return figure

