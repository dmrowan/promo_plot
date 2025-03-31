#!/usr/bin/env python

from promoplot import PromoPlot

from matplotlib import rc
rc('text', usetex=True)
import numpy as np
import pandas as pd

#Dom Rowan 2025

#random data generated with chatgpt

def paper_plots():

    size = 10000
    # Define correlated multivariate normal distribution
    mean = [0, 0, 0]
    cov = [[1, 0.9, 0.3],
           [0.9, 1, -0.7],
           [0.3, -0.7, 1]]

    data = np.random.multivariate_normal(mean, cov, size=size)

    # Generate a bimodal feature
    bimodal = np.random.normal(-2, 0.5, size=size)
    mask = np.random.rand(size) < 0.2  # Randomly select half the samples
    bimodal[mask] = np.random.normal(0.1, 0.5, size=np.sum(mask))

    # Introduce a nonlinear relationship
    nonlinear = 0.5 * data[:, 0]**2 + np.sin(data[:, 2]) + np.random.normal(0, 0.3, size=size)

    # Create DataFrame
    df = pd.DataFrame({r'$\alpha$': data[:, 0],
                       r'$\beta$': data[:, 1],
                       r'$\gamma$': bimodal,
                       r'$\delta$': data[:, 2],
                       r'$\epsilon$': nonlinear})

    kwargs = dict(
            hist_kwargs=dict(lw=3, color='black'),
            labels = df.columns,
            quantiles=[0.5],
            label_kwargs=dict(fontsize=22))

    fig = PromoPlot(df, code='Kozai-Lidov', **kwargs)
    fig.savefig(f'example_equal.pdf')

    size = 10000

    # Generate two correlated clusters
    cluster1 = np.random.multivariate_normal([2, 2], [[1, 0.9], [0.9, 1]], size=size//2)
    cluster2 = np.random.multivariate_normal([-2, -2], [[1, -0.8], [-0.8, 1]], size=size//2)
    x, y = np.vstack([cluster1, cluster2]).T  # Stack clusters together

    # Spiral relationship
    theta = np.linspace(0, 4 * np.pi, size)  # Angle
    r = np.linspace(0.5, 3, size)  # Radius
    spiral_x = r * np.cos(theta) + np.random.normal(0, 0.2, size)
    spiral_y = r * np.sin(theta) + np.random.normal(0, 0.2, size)

    # Exponential distribution
    exp_param = np.random.exponential(scale=2.0, size=size)

    # Categorical groupings with different distributions
    categories = np.random.choice(['A', 'B', 'C'], size=size)
    category_values = np.zeros(size)
    category_values[categories == 'A'] = np.random.normal(-3, 0.5, size=np.sum(categories == 'A'))
    category_values[categories == 'B'] = np.random.normal(3, 0.5, size=np.sum(categories == 'B'))
    category_values[categories == 'C'] = np.random.normal(0, 1, size=np.sum(categories == 'C'))

    # Cyclic behavior (sinusoidal variation)
    cyclic_var = np.sin(x * np.pi / 2) + np.random.normal(0, 0.2, size)

    r_dist = np.sqrt(x**2 + y**2) + np.random.normal(0, 0.2, size)

    # Create DataFrame
    df = pd.DataFrame({
        r'$\alpha$': x,
        r'$\beta$': y,
        r'$\gamma$': spiral_x,
        r'$\delta$': spiral_y,
        r'$\epsilon$': exp_param,
        r'$\zeta$': category_values,
        #r'$\eta$': cyclic_var,
    })

    kwargs['labels'] = df.columns

    fig = PromoPlot(df, code='Polycyclic Aromatic Hydrocarbons', **kwargs)
    fig.savefig(f'example_wide.pdf')

if __name__ == '__main__':

    paper_plots()
