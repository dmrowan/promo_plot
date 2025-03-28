#!/usr/bin/env python

from promo_plot import promo_plot

import numpy as np
import pandas as pd


def test():

    columns = list('abcdefghijklmnop')[:8]

    kwargs = dict(
            labels=columns,
            hist_kwargs=dict(lw=3, color='black'),
            quantiles=[0.5],
            label_kwargs=dict(fontsize=22))

    df = pd.DataFrame({c: np.random.normal(0, 1, size=10000) for c in columns})

    fig = promo_plot(df, **kwargs)

    fig.savefig('test.pdf')

if __name__ == '__main__':
    test()
