NSE = 2.0 # Standard error multiplier

import palette as pal

import numpy as np
from scipy.ndimage import filters

from matplotlib import rcParams, gridspec, ticker

rcParams['backend'] = 'PS'
rcParams['text.usetex'] = True
rcParams['text.latex.preamble'] = r'\usepackage{amssymb}'

rcParams['legend.frameon'] = False  # no frame for legends
rcParams['legend.shadow'] = False
rcParams['legend.handletextpad'] = 1.0

import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

from elflab import datasets


tight = {"pad": 0.3, "h_pad": 0.0, "w_pad": 0.0}


if __name__ == '__main__':
    # Common parameters
    lw = 1.0
    xlim = [-9, 9]
    H_unit = 1.e4
    mr_unit = 0.01
    #xticks = range(10, 42, 10)
    #xminorLocator = MultipleLocator(5)
    #xminor_locator = AutoMinorLocator(2)
    
    mi_columns = {0:"H", 1:"mr", 3:"err"}
    
    # Figure configs
    markersize = 6.0
    plt.rc('font', family='Times New Roman')
    plt.rc('font', size=12)
    plt.rc('ps', usedistiller="xpdf")
    
    paperwidth = 8.5
    fig = plt.figure(dpi=1200)
    p = 0.5
    fig.set_size_inches([p * paperwidth, 0.3/0.4* p * paperwidth])
    
    # Sub figure layout
    gs1 = gridspec.GridSpec(1, 1)
    gs1.update(wspace=0.0, hspace=0.0)
    sub_d = fig.add_subplot(gs1[0, 0])
    
    
    
    # Sub fig d
    sub = sub_d
    #sub.text(0.85, 0.8, "(d)", transform=sub.transAxes, ha="center", va="center", size="large")
    
    sub.tick_params(axis='both', which='both', direction="in", bottom=True, top=True, left=True, right=True, labelleft=True, labelright=False, labeltop=False, labelbottom=True)
    sub.set_xlabel(r"sources", labelpad=0.1)
    sub.set_ylabel(r"$R_{\Box{}max} (h/e^2)$")
    sub.xaxis.set_label_position("bottom")
    sub.yaxis.set_label_position("left")
    
    xticks = range(8)
    #xlabels = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII"]
    xlabels = ["A", "B", "C", "D", "E", "F", "G", "H"]
    
    #sub.set_xlim(xlim)
    sub.set_xticks(xticks)
    sub.set_xticklabels(xlabels)
    #sub.xaxis.set_minor_locator(xminor_locator)
    
    sub.set_yscale("log")
    sub.set_ylim([10**-3.5, 10**2.4])
    #sub.set_yticks([1.e-2, 1.e-1, 1, 1.e1])
    
    trend_columns = {1: "source", 2: "WL", 3: "R"}
    fn1 = r"WL_trend\trend.csv"
    data = datasets.load_csv(fn1, trend_columns, has_header=True)
    
    mask = data["WL"] == 1
    d = data.mask(mask)
    sub.plot(d["source"], d["R"], label="negative magnetoresistance", color=pal.wl_yes, marker="o", markersize=6.0, markerfacecolor="none", linestyle="None", linewidth=lw, zorder=3)
    
    mask = data["WL"] == -1
    d = data.mask(mask)
    sub.plot(d["source"], d["R"], label="no negative magnetoresistance", color=pal.wl_no, marker="x", markersize=6.0, markerfacecolor="none", linestyle="None", linewidth=lw, zorder=1)
    
    mask = data["WL"] == 0
    d = data.mask(mask)
    sub.plot(d["source"], d["R"], label="", color=pal.wl_yes, marker="o", markersize=6.0, markerfacecolor="none", linestyle="None", linewidth=lw, zorder=2)
    
    
    sub.axhline(y=1, color=pal.aid_lines, linestyle="--")

    legend = sub.legend(handlelength=1.0, handletextpad=0.5, ncol=1, loc='upper left', bbox_to_anchor=(0.0, -0.16))
    
    fig.set_tight_layout(tight)
    
    fig.savefig(r'meta.pdf', format='pdf')
    