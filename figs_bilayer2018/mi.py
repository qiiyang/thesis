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
#from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import AutoMinorLocator
from matplotlib.ticker import FormatStrFormatter

from elflab import datasets


tight = {"pad": 0.2, "h_pad": 0.0, "w_pad": 0.0}


if __name__ == '__main__':
    
    
    # Common parameters
    lw = 1.0
    unit_re = 2.5e-7
    xlim = [2, 42]
    xticks = range(10, 42, 10)
    #xminorLocator = MultipleLocator(5)
    xminor_locator = AutoMinorLocator(2)
    
    mi_columns = {0:"T", 1:"X", 2:"Y", 4:"err_X", 5:"err_Y"}
    
    # Figure configs
    markersize = 6.0
    plt.rc('font', family='Times New Roman')
    plt.rc('font', size=12)
    plt.rc('ps', usedistiller="xpdf")
    
    paperwidth = 8.5
    fig = plt.figure(dpi=1200)
    p = 0.65
    fig.set_size_inches([p * paperwidth, 0.3/0.4* p * paperwidth])
    
    # Sub figure layout
    gs1 = gridspec.GridSpec(3, 2)
    gs1.update(wspace=0.0, hspace=0.0)
    sub_a = fig.add_subplot(gs1[0, 0])
    sub_b = fig.add_subplot(gs1[0, 1])
    sub_c = fig.add_subplot(gs1[1, 0])
    sub_d = fig.add_subplot(gs1[1, 1])
    sub_e = fig.add_subplot(gs1[2, 0])
    sub_f = fig.add_subplot(gs1[2, 1])
    
    # Sub fig a, 0T ph=0
    sub = sub_a
    sub.tick_params(axis='both', which='both', direction="in", pad=1, bottom=True, top=True, left=True, right=False, labelleft=True, labelright=False, labeltop=True, labelbottom=False)
    sub.set_xlabel(r"$T$ (K)")
    sub.xaxis.set_label_position("top")
    sub.xaxis.set_label_coords(1, 1.18)
    
    offset_re = 0.9
    offset_im = 8.9
    
    sub.text(0.13, 0.82, "(a)", transform=sub.transAxes, ha="center", va="center", size="large")
    #sub.text(0.05, 0.6, r"$20 \mathrm{mT}$", transform=sub.transAxes, ha="left", va="center")
    
    sub.set_xlim(xlim)
    sub.set_xticks(xticks)
    sub.xaxis.set_minor_locator(xminor_locator)
    
    sub.set_yticks(np.arange(-0.5, 1, 0.5))
    yminor_locator = AutoMinorLocator(5)
    sub.yaxis.set_minor_locator(yminor_locator)
    
    fn1 = r"mi\0degree\0T_warm.csv"
    data = datasets.load_csv(fn1, mi_columns, has_header=True)
    data = data.mask(data["T"] < 42)
    sub.errorbar(data["T"], data["Y"] / unit_re - offset_re, yerr=data["err_Y"] * NSE / unit_re, label="$\chi'$", color=pal.mi_re, marker="x", markersize=markersize, markerfacecolor="none", linestyle="None", linewidth=lw, zorder=1)
    sub.errorbar(data["T"], data["X"] / unit_re - offset_im, yerr=data["err_X"] * NSE / unit_re, label="$\chi''$", color=pal.mi_im, marker="o", markersize=markersize, markerfacecolor="none", linestyle="None", linewidth=lw, zorder=1)
    
    
    sub.axvline(x=14.5, linestyle="--", color=pal.aid_lines, linewidth=lw, zorder=2)
    
    
    # Sub fig b, 0T ph=40
    sub = sub_b
    
    sub.tick_params(axis='both', which='both', direction="in", pad=1, bottom=True, top=True, left=False, right=True, labelleft=False, labelright=True, labeltop=True, labelbottom=False)
    
    offset_re = -5.4
    offset_im = 7.55
    
    sub.text(0.85, 0.82, "(b)", transform=sub.transAxes, ha="center", va="center", size="large")
    sub.text(0.0, 0.65, r"$\mu_0H = 0$", transform=sub.transAxes, ha="center", va="center", bbox=dict(facecolor="#ffffff", edgecolor='none', pad=2), zorder=256)
    #sub.text(0.95, 0.1, r"$\mu_0H = 20 \mathrm{mT}$", size="small", transform=sub.transAxes, ha="right", va="center")
    #sub.text(0.05, 0.6, r"$20 \mathrm{mT}$", transform=sub.transAxes, ha="left", va="center")
    
    sub.set_xlim(xlim)
    sub.set_xticks(xticks)
    sub.xaxis.set_minor_locator(xminor_locator)
    
    sub.set_yticks(np.arange(-0.5, 1.5, 0.5))
    yminor_locator = AutoMinorLocator(5)
    sub.yaxis.set_minor_locator(yminor_locator)
    
    fn1 = r"mi\220degree\0T_warm.csv"
    data = datasets.load_csv(fn1, mi_columns, has_header=True)
    data = data.mask(data["T"] < 42)
    sub.errorbar(data["T"], data["Y"] / unit_re - offset_re, yerr=data["err_Y"] * NSE / unit_re, label="$\chi'$", color=pal.mi_re, marker="x", markersize=markersize, markerfacecolor="none", linestyle="None", linewidth=lw, zorder=1)
    sub.errorbar(data["T"], data["X"] / unit_re - offset_im, yerr=data["err_X"] * NSE / unit_re, label="$\chi''$", color=pal.mi_im, marker="o", markersize=markersize, markerfacecolor="none", linestyle="None", linewidth=lw, zorder=1)
    
    
    sub.axvline(x=14.5, linestyle="--", color=pal.aid_lines, linewidth=lw, zorder=2)
    
    
    # Sub fig c, 0T ph=0
    sub = sub_c
    sub.text(0.13, 0.82, "(c)", transform=sub.transAxes, ha="center", va="center", size="large")
    
    sub.set_ylabel(r"$\chi$ (arb. unit) + offset", labelpad = 0.2)
    sub.yaxis.set_label_position("left")
    sub.yaxis.set_label_coords(-0.2, 0.5)
    
    sub.tick_params(axis='both', which='both', direction="in", pad=1, bottom=True, top=True, left=True, right=False, labelleft=True, labelright=False, labeltop=False, labelbottom=False)
    
    offset_re = 0.9
    offset_im = 8.9
    
    sub.set_xlim(xlim)
    sub.set_xticks(xticks)
    sub.xaxis.set_minor_locator(xminor_locator)
    
    sub.set_yticks(np.arange(-0.5, 1, 0.5))
    yminor_locator = AutoMinorLocator(5)
    sub.yaxis.set_minor_locator(yminor_locator)
    
    fn1 = r"mi\0degree\0.02T_cool.csv"
    data = datasets.load_csv(fn1, mi_columns, has_header=True)
    sub.errorbar(data["T"], data["Y"] / unit_re - offset_re, yerr=data["err_Y"] * NSE / unit_re, label="$\chi'$", color=pal.mi_re, marker="x", markersize=markersize, markerfacecolor="none", linestyle="None", linewidth=lw, zorder=1)
    sub.errorbar(data["T"], data["X"] / unit_re - offset_im, yerr=data["err_X"] * NSE / unit_re, label="$\chi''$", color=pal.mi_im, marker="o", markersize=markersize, markerfacecolor="none", linestyle="None", linewidth=lw, zorder=1)
    
    
    sub.axvline(x=14.5, linestyle="--", color=pal.aid_lines, linewidth=lw, zorder=2)
    
    
    # Sub fig d, 0.02T ph=40
    sub = sub_d
    sub.text(0.85, 0.82, "(d)", transform=sub.transAxes, ha="center", va="center", size="large")
    sub.text(0.0, 0.5, r"$\mu_0H = 20~\mathrm{mT}$", transform=sub.transAxes, ha="center", va="center", bbox=dict(facecolor="#ffffff", edgecolor='none', pad=2), zorder=256)
    
    sub.set_ylabel(r"$\chi$ (arb. unit) + offset", labelpad = 0.2)
    sub.yaxis.set_label_position("right")
    sub.yaxis.set_label_coords(1.18, 0.5)
    
    sub.tick_params(axis='both', which='both', direction="in", pad=1, bottom=True, top=True, left=False, right=True, labelleft=False, labelright=True, labeltop=False, labelbottom=False)
    
    offset_re = -5.5
    offset_im = 7.6
    
    sub.set_xlim(xlim)
    sub.set_xticks(xticks)
    sub.xaxis.set_minor_locator(xminor_locator)
    
    sub.set_yticks(np.arange(-0.5, 1.5, 0.5))
    yminor_locator = AutoMinorLocator(5)
    sub.yaxis.set_minor_locator(yminor_locator)
    
    fn1 = r"mi\220degree\0.02T_cool.csv"
    data = datasets.load_csv(fn1, mi_columns, has_header=True)
    sub.errorbar(data["T"], data["Y"] / unit_re - offset_re, yerr=data["err_Y"] * NSE / unit_re, label="$\chi'$", color=pal.mi_re, marker="x", markersize=markersize, markerfacecolor="none", linestyle="None", linewidth=lw, zorder=1)
    sub.errorbar(data["T"], data["X"] / unit_re - offset_im, yerr=data["err_X"] * NSE / unit_re, label="$\chi''$", color=pal.mi_im, marker="o", markersize=markersize, markerfacecolor="none", linestyle="None", linewidth=lw, zorder=1)
    
    
    sub.axvline(x=14.5, linestyle="--", color=pal.aid_lines, linewidth=lw, zorder=2)
    
    
    # Sub fig e, 2T ph=0
    sub = sub_e
    sub.text(0.13, 0.82, "(e)", transform=sub.transAxes, ha="center", va="center", size="large")
    
    sub.tick_params(axis='both', which='both', direction="in", pad=1, bottom=True, top=True, left=True, right=False, labelleft=True, labelright=False, labeltop=False, labelbottom=True)
    
    
    offset_re = 0.0
    offset_im = 6.0
    
    #sub.text(0.13, 0.82, "(a)", transform=sub.transAxes, ha="center", va="center", size="large")
    #sub.text(0.80, 0.82, r"$\mu_0H = 2 \mathrm{T}$", size="small", transform=sub.transAxes, ha="right", va="center")
    #sub.text(0.6, 0.82, r"$2 \mathrm{T}$", transform=sub.transAxes, ha="right", va="center")
    sub.set_xlabel(r"$T$ (K)")
    sub.xaxis.set_label_coords(1, -0.15)
    sub.xaxis.set_label_position("bottom")
    
    sub.set_xlim(xlim)
    sub.set_xticks(xticks)
    sub.xaxis.set_minor_locator(xminor_locator)
    
    sub.set_yticks(range(0, 11, 5))
    sub.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
    yminor_locator = AutoMinorLocator(5)
    sub.yaxis.set_minor_locator(yminor_locator)
    
    fn1 = r"mi\0degree\2T_cool.csv"
    data = datasets.load_csv(fn1, mi_columns, has_header=True)
    sub.errorbar(data["T"], data["Y"] / unit_re - offset_re, yerr=data["err_Y"] * NSE / unit_re, label="$\chi'$", color=pal.mi_re, marker="x", markersize=markersize, markerfacecolor="none", linestyle="None", linewidth=lw, zorder=1)
    sub.errorbar(data["T"], data["X"] / unit_re - offset_im, yerr=data["err_X"] * NSE / unit_re, label="$\chi''$", color=pal.mi_im, marker="o", markersize=markersize, markerfacecolor="none", linestyle="None", linewidth=lw, zorder=1)
    
    
    sub.axvline(x=14.5, linestyle="--", color=pal.aid_lines, linewidth=lw, zorder=2)
    
    
    # Sub fig f, 2T ph=40
    sub = sub_f
    sub.text(0.85, 0.82, "(f)", transform=sub.transAxes, ha="center", va="center", size="large")
    sub.text(0.0, 0.8, r"$\mu_0H = 2~\mathrm{T}$", transform=sub.transAxes, ha="center", va="center", bbox=dict(facecolor="#ffffff", edgecolor='none', pad=2), zorder=256)
    
    sub.tick_params(axis='both', which='both', direction="in", pad=1, bottom=True, top=True, left=False, right=True, labelleft=False, labelright=True, labeltop=False, labelbottom=True)
    offset_re = -1.6e-6
    offset_im = +1.7e-6
    
    #sub.text(0.87, 0.82, "(b)", transform=sub.transAxes, ha="center", va="center", size="large")
    #sub.text(0.02, 0.2, r"$\mu_0H = 2T$", size="small", transform=sub.transAxes, ha="left", va="center")
    #sub.text(0.8, 0.65, r"$2 \mathrm{T}$", transform=sub.transAxes, ha="left", va="center")
    
    sub.set_xlim(xlim)
    sub.set_xticks(xticks)
    sub.xaxis.set_minor_locator(xminor_locator)
    
    sub.set_yticks(range(0, 9, 5))
    sub.yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
    yminor_locator = AutoMinorLocator(5)
    sub.yaxis.set_minor_locator(yminor_locator)
    
    fn1 = r"mi\220degree\2T_cool.csv"
    data = datasets.load_csv(fn1, mi_columns, has_header=True)
    sub.errorbar(data["T"], (data["Y"] - offset_re) / unit_re, yerr=data["err_Y"] * NSE / unit_re, label="$\chi'$", color=pal.mi_re, marker="x", markersize=markersize, markerfacecolor="none", linestyle="None", linewidth=lw, zorder=1)
    sub.errorbar(data["T"], (data["X"] - offset_im) / unit_re, yerr=data["err_X"] * NSE / unit_re, label="$\chi''$", color=pal.mi_im, marker="o", markersize=markersize, markerfacecolor="none", linestyle="None", linewidth=lw, zorder=1)
    
    sub.axvline(x=14.5, linestyle="--", color=pal.aid_lines, linewidth=lw, zorder=2)
    
    
    legend = sub_b.legend(handlelength=1.0, handletextpad=0.5, ncol=1, loc='upper left', bbox_to_anchor=(1.05, 1.15))
    
    fig.set_tight_layout(tight)
    
    fig.savefig(r'mi.pdf', format='pdf')