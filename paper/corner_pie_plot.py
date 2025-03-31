#!/usr/bin/env python

import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
rc('text', usetex=True)

#Jack Roberts & Dom Rowan 2025


def main():
    plots = 8
    fig,axs = plt.subplots(1,2,figsize=(16,8))
    fig.subplots_adjust(wspace=0.05)
    usedsum = 0
    unusedsum = plots*plots
    adsum = 0

    label_science = 'Science Space'
    label_waste = 'Wasted Space'

    x=0
    y=0
    box = [[x, x+plots, x+plots, x], [y, y, y+plots, y+plots]]
    axs[0].fill(box[0], box[1], color='gray', alpha=1.0, 
                fill=False, hatch='///', label=label_science)

    for x in np.arange(plots):
        usedsum += (x + 1)

        # Wasted Space using fill (replaces fill_between)
        axs[0].fill([plots - (x + 1), plots - x, plots - x, plots - (x + 1)],
                    [x + 1, x + 1, plots + 1, plots + 1],
                    color='white', alpha=1.0, edgecolor='none', label='_nolegend_')
        axs[0].fill([plots - (x + 1), plots - x, plots - x, plots - (x + 1)],
                    [x + 1, x + 1, plots + 1, plots + 1], 
                    color='xkcd:bluey purple', alpha=0.8, label=label_waste, edgecolor='none')
        label_waste = '_nolegend_'

    unusedsum-=usedsum
    if plots%2==0:
        fill = plots/2
        axs[0].fill_between([fill,plots],[fill,fill],[plots,plots],
                            color='xkcd:kelly green',label='Advertising Space',
                            edgecolor='black')
        adsum = fill*fill

        axs[0].text((fill+plots)/2, (fill+plots)/2, r'\textbf{\$\$\$}', 
                    ha='center', va='center', fontsize=40)
    elif plots%2==1:
        fill = (plots-1)/2
        axs[0].fill_between([fill+1,plots],[fill+1,fill+1],[plots,plots],
                            color='xkcd:kelly green',label='Advertising Space')
        adsum = fill*fill

        axs[0].text((fill+plots+1)/2, (fill+plots+1)/2, r'\textbf{\$\$\$}', 
                    ha='center', va='center', fontsize=40)

    unusedsum-=adsum
    axs[0].set_xlim(0,plots)
    axs[0].set_ylim(0,plots)
    axs[0].legend(loc='lower left', fontsize=18, edgecolor='black')

    wedges, _ = axs[1].pie([usedsum,unusedsum,adsum],
                           labels=['Science Space','Wasted Space','Advertising Space'],
                           colors=['xkcd:gray','xkcd:bluey purple','xkcd:kelly green'],
                           wedgeprops={"linewidth": 2, "edgecolor": "black", 'antialiased': True},
                           textprops={'fontsize': 18})

    wedges[0].set_hatch('//')
    wedges[0].set_alpha(0.2)
    wedges[1].set_alpha(0.8)

    axs[0].axis('off')
    for axis in ['top', 'bottom', 'left', 'right']:
            axs[0].spines[axis].set_linewidth(1.5)

    fig.savefig('saving_space.pdf')

if __name__ == '__main__':

    main()
