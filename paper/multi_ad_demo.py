#!/usr/bin/env python

from promoplot import PromoPlot

from matplotlib import rc
import matplotlib.image as mpimg
rc('text', usetex=True)
import numpy as np
import pandas as pd
from scipy.stats import cauchy

#Dom Rowan 2025

#random data generated with the help of chatgpt

def paper_plots():

    size = 10000

    # 1. Fractal-like noise using Perlin noise approximation (self-similar structure)
    np.random.seed(42)
    fractal_noise = np.cumsum(np.random.randn(size))  # Random walk as an approximation

    # 2. Gaussian Mixture (structured bimodal distribution)
    gaussian_mixture = np.random.normal(-2, 1, size)
    mask = np.random.rand(size) < 0.5  # Select half the samples
    gaussian_mixture[mask] = np.random.normal(2, 1, size=np.sum(mask))

    # 3. Parabolic Relationship (dependent on fractal noise)
    parabolic_relation = 0.5 * fractal_noise**2 + np.random.normal(0, 10, size)

    # 4. Circular symmetry: Parameters forming a ring-like structure
    theta = np.random.uniform(0, 2 * np.pi, size)
    radius = np.abs(np.random.normal(2, 0.5, size))  # Gaussian-distributed radius
    circle_x = radius * np.cos(theta)
    circle_y = radius * np.sin(theta)

    # 5. Chaotic time series: Logistic map approximation (pseudo-random chaos)
    chaotic_series = np.zeros(size)
    chaotic_series[0] = 0.5  # Initial condition
    r = 3.8  # High-chaos parameter for logistic map
    for i in range(1, size):
        chaotic_series[i] = r * chaotic_series[i-1] * (1 - chaotic_series[i-1])

    # 6. Sigmoid transformation (sharp boundary effect)
    sigmoid_boundary = 1 / (1 + np.exp(-np.random.randn(size) * 5))

    # 7. Multiplicative noise (noise that scales with the value)
    multiplicative_noise = np.random.uniform(1, 2, size) * np.random.randn(size)

    # 8. Random walk (simulating fluctuating behavior like stock prices)
    random_walk = np.cumsum(np.random.normal(0, 1, size))

    # Greek letter column names
    columns = [r'$\alpha$', r'$\beta$', r'$\gamma$', r'$\delta$',
               r'$\epsilon$', r'$\zeta$', r'$\eta$', r'$\theta$']

    # Create DataFrame
    df = pd.DataFrame({
        columns[0]: fractal_noise,         # Random walk
        columns[1]: gaussian_mixture,      # Bimodal distribution
        columns[2]: parabolic_relation,    # Nonlinear structure
        columns[3]: circle_x,              # Ring structure (x)
        columns[4]: circle_y,              # Ring structure (y)
        columns[5]: chaotic_series,        # Logistic chaos
        columns[6]: sigmoid_boundary,      # Sharp transition
        columns[7]: random_walk            # Another random walk
    })

    kwargs = dict(
            hist_kwargs=dict(lw=3, color='black'),
            labels = df.columns,
            quantiles=[0.5],
            label_kwargs=dict(fontsize=22))

    fig = PromoPlot(df, coupon_code=False, ad_path='../promoplot/ad_images/equal_aspect/duolingo.png', **kwargs)

    ndim = df.shape[1]
    axes = np.array(fig.axes)
    axes = axes.reshape((ndim, ndim))

    axi = axes[0, 1].inset_axes(
        bounds=[0, 0, 2, 1], transform=axes[0, 1].transAxes)
    axi.imshow(mpimg.imread('../promoplot/ad_images/wide_aspect/amazon.png'))
    axi.axis('off')

    axi = axes[1, 2].inset_axes(
        bounds=[0, 0, 2, 1], transform=axes[1, 2].transAxes)
    axi.imshow(mpimg.imread('../promoplot/ad_images/wide_aspect/draftkings.png'))
    axi.axis('off')

    axi = axes[0, 3].inset_axes(
        bounds=[0, 0, 1, 1], transform=axes[0, 3].transAxes)
    axi.imshow(mpimg.imread('../promoplot/ad_images/equal_aspect/americanexpress.png'))
    axi.axis('off')

    axi = axes[2, 3].inset_axes(
        bounds=[0, 0, 1, 1], transform=axes[2, 3].transAxes)
    axi.imshow(mpimg.imread('../promoplot/ad_images/equal_aspect/dsc.png'))
    axi.axis('off')

    axi = axes[5, 6].inset_axes(
        bounds=[0, 0, 2, 2], transform=axes[5, 6].transAxes)
    axi.imshow(mpimg.imread('../promoplot/ad_images/equal_aspect/hello_fresh.png'))
    axi.axis('off')

    axi = axes[4, 5].inset_axes(
        bounds=[0, 0, 1, 1], transform=axes[4, 5].transAxes)
    axi.imshow(mpimg.imread('../promoplot/ad_images/equal_aspect/nordvpn.png'))
    axi.axis('off')

    axi = axes[6, 7].inset_axes(
        bounds=[0, 0, 1, 1], transform=axes[6, 7].transAxes)
    axi.imshow(mpimg.imread('../promoplot/ad_images/equal_aspect/betterhelp.png'))
    axi.axis('off')


    fig.savefig(f'example_multi_ad.pdf')

if __name__ == '__main__':

    paper_plots()
