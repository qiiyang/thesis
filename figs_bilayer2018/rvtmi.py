NSE = 2.0 # Standard error multiplier

import palette as pal

import numpy as np
from scipy.ndimage import filters

from matplotlib import rcParams, gridspec, ticker, patches
rcParams['backend'] = 'PS'
rcParams['text.usetex'] = True
rcParams['text.latex.preamble'] = r'\usepackage{amssymb}'

rcParams['legend.frameon'] = False  # no frame for legends
rcParams['legend.shadow'] = False
rcParams['legend.handletextpad'] = 1.0

import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

from elflab import datasets

tight = {"pad": 0.2, "h_pad": 0.0, "w_pad": 0.0}

mi_columns = {0:"T", 1:"X", 2:"Y", 4:"err_X", 5:"err_Y"}
rvt_columns = {0:"T", 1:"R", 2:"err_R"}
hall_columns = {0:"H", 1:"R", 3:"err_R"}

if __name__ == '__main__':
    # Common parameters
    lw = 1.0
    unit_re = 2.5e-7
    offset_re = 0.0
    offset_im = 10.0
    #xminorLocator = MultipleLocator(5)
    
    # Figure configs
    markersize = 6.0
    plt.rc('font', family='Times New Roman')
    plt.rc('font', size=12)
    plt.rc('ps', usedistiller="xpdf")
    
    paperwidth = 8.5
    fig = plt.figure(dpi=1200)
    p = 0.62
    fig.set_size_inches([p * paperwidth, 0.3/0.4* p * paperwidth])
    
    # Sub figure layout
    gs0 = gridspec.GridSpec(2, 1, wspace=0, hspace=0)
    
    sub_mi = fig.add_subplot(gs0[1, 0])
    
    sub_rvt = fig.add_subplot(gs0[0, 0])
    
    
    # Sub fig MI
    xlim = [2, 100]
    xticks = range(10, 99, 20)
    sub = sub_mi
    sub.text(0.9, 0.2, "(b)", transform=sub.transAxes, ha="center", va="center", size="large")
    
    sub.tick_params(axis='both', which='both', direction="in", pad=1, bottom=True, top=True, left=True, right=True, labelleft=True, labelright=False, labeltop=False, labelbottom=True)
    sub.set_xlabel(r"$T$ (K)")
    sub.set_ylabel(r"$\chi$ (arb. unit) + offset")
    sub.yaxis.set_label_coords(-0.08, 0.37)
    sub.xaxis.set_label_position("bottom")
    sub.yaxis.set_label_position("left")
    
    sub.set_xlim(xlim)
    sub.set_xticks(xticks)
    xminor_locator = AutoMinorLocator(2)
    sub.xaxis.set_minor_locator(xminor_locator)
    
    #sub.set_ylim([-1.6, 1.9])
    yminor_locator = AutoMinorLocator(5)
    sub.yaxis.set_minor_locator(yminor_locator)
    
    fn1 = r"mi\0degree\0T_warm.csv"
    data = datasets.load_csv(fn1, mi_columns, has_header=True)
    
    mask = np.logical_and(data["T"] > xlim[0], data["T"] < xlim[1])
    
    sub.errorbar(data["T"][mask], data["Y"][mask] / unit_re - offset_re, yerr=data["err_Y"][mask] * NSE / unit_re, label="$\chi'$", color=pal.mi_re, marker="x", markersize=markersize, markerfacecolor="none", linestyle="None", linewidth=lw, zorder=1)
    sub.errorbar(data["T"][mask], data["X"][mask] / unit_re - offset_im, yerr=data["err_X"][mask] * NSE / unit_re, label="$\chi''$", color=pal.mi_im, marker="o", markersize=markersize, markerfacecolor="none", linestyle="None", linewidth=lw, zorder=1)
    
    sub.axvline(x=14.5, linestyle="--", color=pal.aid_lines, linewidth=lw, zorder=2)
    sub.axvline(x=31, linestyle="--", color=pal.aid_lines, linewidth=lw, zorder=2)
    sub.axvline(x=59, linestyle="--", color=pal.aid_lines, linewidth=lw, zorder=2)
    
    legend = sub.legend(handlelength=0.0, handletextpad=0.5, loc='center right', bbox_to_anchor=(0.85, 0.25))
    #legend = sub.legend(handlelength=0.0, bbox_to_anchor=(0.5, 0.5), bbox_transform=sub.transAxes)
    
    
    # Sub fig rvt
    xlim = [2, 100]
    xticks = range(10, 99, 20)
    sub = sub_rvt
    sub.text(0.9, 0.85, "(a)", transform=sub.transAxes, ha="center", va="center", size="large")
    #sub.text(80, 2e-2, "S1", ha="center", va="center", color=pal.s1)
    
    sub.tick_params(axis='both', which='both', direction="in", pad=1, bottom=True, top=True, left=True, right=True, labelleft=True, labelright=False, labeltop=False, labelbottom=False)
    #sub.set_xlabel(r"$T$ (K)")
    sub.set_ylabel(r"$R_\Box (h/e^2)$")
    #sub.xaxis.set_label_position("none")
    #sub.yaxis.set_label_position("left")
    #sub.yaxis.set_label_coords(-0.25, -0.1)
    
    sub.set_xlim(xlim)
    sub.set_xticks(xticks)
    xminor_locator = AutoMinorLocator(2)
    sub.xaxis.set_minor_locator(xminor_locator)
    
    sub.set_yscale("log")
    sub.set_yticks([0.01, 0.1, 1])
    #yminor_locator = AutoMinorLocator(2)
    #sub.yaxis.set_minor_locator(yminor_locator)
    
    #sub.set_xticks(xticks)
    #sub.xaxis.set_minor_locator(xminor_locator)
    
    fn1 = r"rvt\s1.dat"
    data = datasets.load_csv(fn1, rvt_columns, has_header=True)
    
    mask = np.logical_and(data["T"] > xlim[0], data["T"] < xlim[1])
    
    sub.plot(data["T"][mask], data["R"][mask], color=pal.rvt1, marker="x", markersize=markersize, markerfacecolor="none", linestyle="None", linewidth=lw, zorder=1)
    
    sub.axvline(x=14.5, linestyle="--", color=pal.aid_lines, linewidth=lw, zorder=2)
    sub.axvline(x=31, linestyle="--", color=pal.aid_lines, linewidth=lw, zorder=2)
    sub.axvline(x=59, linestyle="--", color=pal.aid_lines, linewidth=lw, zorder=2)
    
    
    fig.set_tight_layout(tight)
    
    fig.savefig(r'rvtmi.pdf', format='pdf')
    