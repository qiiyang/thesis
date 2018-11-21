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
    lw = 2.0
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
    p = 0.62
    fig.set_size_inches([p * paperwidth, 0.35/0.4* p * paperwidth])
    
    # Sub figure layout
    gs1 = gridspec.GridSpec(2, 2)
    gs1.update(wspace=0.0, hspace=0.0)
    sub_a = fig.add_subplot(gs1[0, 0])
    sub_b = fig.add_subplot(gs1[0, 1])
    sub_c = fig.add_subplot(gs1[1, 0])
    sub_d = fig.add_subplot(gs1[1, 1])
    gs3 = gridspec.GridSpecFromSubplotSpec(30, 20, subplot_spec=gs1[0,1], wspace=0, hspace=0)
    sub_bi = fig.add_subplot(gs3[1:12, 6:14], fc='white')
    gs4 = gridspec.GridSpecFromSubplotSpec(30, 20, subplot_spec=gs1[1,1], wspace=0, hspace=0)
    sub_di = fig.add_subplot(gs4[1:12, 6:14], fc='white')
    
    xticks = range(-8, 9, 4)
    # Sub fig a
    sub = sub_a
    sub.text(0.85, 0.8, "(a)", transform=sub.transAxes, ha="center", va="center", size="large")
    
    # Annotations
    sub.text(-7, 15, "2K", color=pal.t2, size="small", ha="center", va="center")
    sub.text(0, -12, "4K", color=pal.t4, size="small", ha="center", va="center")
    sub.arrow(-1.3, -12, -0.5, 0, width=0.001, head_length=0.8, head_width=1.5, ec=pal.t4, fc=pal.t4)
    sub.text(-7, -6, "12K", color=pal.t12, size="small", ha="center", va="center")
    sub.text(-7, 22, "30K", color=pal.t30, size="small", ha="center", va="center")
    
    sub.tick_params(axis='both', which='both', direction="in", pad=1, bottom=True, top=True, left=True, right=False, labelleft=True, labelright=False, labeltop=True, labelbottom=False)
    sub.set_xlabel(r"$H$ (T $/\mu_0$)")
    sub.set_ylabel(r"$\Delta{}R(H) / R(0) (\%)$")
    sub.xaxis.set_label_position("top")
    sub.xaxis.set_label_coords(1, 1.15)
    sub.yaxis.set_label_position("left")
    sub.yaxis.set_label_coords(-0.17, 0.0)
    
    sub.set_xlim(xlim)
    sub.set_xticks(xticks)
    xminor_locator = AutoMinorLocator(4)
    sub.xaxis.set_minor_locator(xminor_locator)
    
    sub.set_ylim([-15, 29])
    sub.set_yticks(range(-10, 29, 10))
    yminor_locator = AutoMinorLocator(5)
    sub.yaxis.set_minor_locator(yminor_locator)
    
    fn1 = r"mr\s3_2K.csv"
    data = datasets.load_csv(fn1, mi_columns, has_header=True)
    sub.plot(data["H"] / H_unit, data["mr"] / mr_unit, color=pal.t2, marker=None, markersize=4.0, markerfacecolor="none", linestyle="-", linewidth=lw, zorder=1)
    
    fn1 = r"mr\s3_4K.csv"
    data = datasets.load_csv(fn1, mi_columns, has_header=True)
    sub.plot(data["H"] / H_unit, data["mr"] / mr_unit, color=pal.t4, marker=None, markersize=4.0, markerfacecolor="none", linestyle="--", linewidth=lw, zorder=1)
    
    fn1 = r"mr\s3_12K.csv"
    data = datasets.load_csv(fn1, mi_columns, has_header=True)
    sub.plot(data["H"] / H_unit, data["mr"] / mr_unit, color=pal.t12, marker=None, markersize=4.0, markerfacecolor="none", linestyle="-.", linewidth=lw, zorder=1)
    
    fn1 = r"mr\s3_30K.csv"
    data = datasets.load_csv(fn1, mi_columns, has_header=True)
    sub.plot(data["H"] / H_unit, data["mr"] / mr_unit, color=pal.t30, marker=None, markersize=4.0, markerfacecolor="none", linestyle="-", linewidth=lw, zorder=1)
    

    
    
    
    # Sub fig b
    sub = sub_b
    sub.text(0.1, 0.85, "(b)", transform=sub.transAxes, ha="center", va="center", size="large")
    
    # Annotations
    sub.text(-7.4, 8, "2K", color=pal.t2, size="small", ha="center", va="center")
    sub.text(-7.4, 5.5, "4K", color=pal.t4, size="small", ha="center", va="center")
    sub.text(-7.4, 3.2, "12K", color=pal.t12, size="small", ha="center", va="center")
    sub.text(-7.4, 1, "30K", color=pal.t30, size="small", ha="center", va="center")
    
    sub.tick_params(axis='both', which='both', direction="in", pad=1, bottom=True, top=True, left=False, right=True, labelleft=False, labelright=True, labeltop=True, labelbottom=False)
    
    sub.set_xlim(xlim)
    sub.set_xticks(xticks)
    xminor_locator = AutoMinorLocator(4)
    sub.xaxis.set_minor_locator(xminor_locator)
    
    sub.set_ylim([-0.5, 13.5])
    sub.set_yticks(range(0, 13, 5))
    yminor_locator = AutoMinorLocator(5)
    sub.yaxis.set_minor_locator(yminor_locator)
    
    fn1 = r"mr\s2_2K.csv"
    data = datasets.load_csv(fn1, mi_columns, has_header=True)
    sub.plot(data["H"] / H_unit, data["mr"] / mr_unit, color=pal.t2, marker=None, markersize=4.0, markerfacecolor="none", linestyle="-", linewidth=lw, zorder=1)
    
    fn1 = r"mr\s2_4K.csv"
    data = datasets.load_csv(fn1, mi_columns, has_header=True)
    sub.plot(data["H"] / H_unit, data["mr"] / mr_unit, color=pal.t4, marker=None, markersize=4.0, markerfacecolor="none", linestyle="--", linewidth=lw, zorder=1)
    
    fn1 = r"mr\s2_12K.csv"
    data = datasets.load_csv(fn1, mi_columns, has_header=True)
    sub.plot(data["H"] / H_unit, data["mr"] / mr_unit, color=pal.t12, marker=None, markersize=4.0, markerfacecolor="none", linestyle="-.", linewidth=lw, zorder=1)
    
    fn1 = r"mr\s2_30K.csv"
    data = datasets.load_csv(fn1, mi_columns, has_header=True)
    sub.plot(data["H"] / H_unit, data["mr"] / mr_unit, color=pal.t30, marker=None, markersize=4.0, markerfacecolor="none", linestyle="-", linewidth=lw, zorder=1)
    
    # b insert
    sub = sub_bi
    sub.tick_params(axis='both', which='both', direction="in", pad=1, bottom=True, top=True, left=True, right=True, labelleft=False, labelright=True, labeltop=False, labelbottom=True)
    
    sub.set_xlim([-0.2, 0.2])
    sub.set_ylim([-0.05, 0.18])
    
    xminor_locator = AutoMinorLocator(2)
    sub.xaxis.set_minor_locator(xminor_locator)
    
    """
    fn1 = r"mr\s2_2K.csv"
    data = datasets.load_csv(fn1, mi_columns, has_header=True)
    sub.errorbar(data["H"] / H_unit, data["mr"] / mr_unit, yerr=data["err"] / mr_unit * NSE, color=pal.t2, marker="x", markersize=2.0, markerfacecolor="none", linestyle="none", linewidth=lw, zorder=1)
    
    fn1 = r"mr\s2_4K.csv"
    data = datasets.load_csv(fn1, mi_columns, has_header=True)
    sub.errorbar(data["H"] / H_unit, data["mr"] / mr_unit, yerr=data["err"] / mr_unit * NSE, color=pal.t4, marker="o", markersize=2.0, markerfacecolor="none", linestyle="none", linewidth=lw, zorder=1)
    """
    fn1 = r"mr\s2_12K.csv"
    data = datasets.load_csv(fn1, mi_columns, has_header=True)
    sub.errorbar(data["H"] / H_unit, data["mr"] / mr_unit, yerr=data["err"] / mr_unit * NSE, color=pal.t12, marker="^", markersize=3.0, markerfacecolor="none", linestyle="none", linewidth=lw, zorder=1)
    
    fn1 = r"mr\s2_30K.csv"
    data = datasets.load_csv(fn1, mi_columns, has_header=True)
    sub.errorbar(data["H"] / H_unit, data["mr"] / mr_unit, yerr=data["err"] / mr_unit * NSE, color=pal.t30, marker="o", markersize=3.0, markerfacecolor="none", linestyle="none", linewidth=lw, zorder=1)
    

    
    # Sub fig c
    sub = sub_c
    sub.text(0.1, 0.15, "(c)", transform=sub.transAxes, ha="center", va="center", size="large")
    
    # Annotations
    sub.text(-4, 2.5, "2K", size="small", ha="center", va="center", color=pal.t2, bbox=dict(facecolor="#ffffff", edgecolor='none', pad=0))
    sub.text(-4, 2.1, "4K", size="small", ha="center", va="center", color=pal.t4, bbox=dict(facecolor="#ffffff", edgecolor='none', pad=0))
    sub.text(-4, 1.7, "8K", size="small", ha="center", va="center", color=pal.t8, bbox=dict(facecolor="#ffffff", edgecolor='none', pad=0))
    sub.text(-4, 1.15, "16K", size="small", ha="center", va="center", color=pal.t16, bbox=dict(facecolor="#ffffff", edgecolor='none', pad=0))
    sub.text(-4, 0.75, "30K", size="small", ha="center", va="center", color=pal.t30, bbox=dict(facecolor="#ffffff", edgecolor='none', pad=0))
    
    sub.tick_params(axis='both', which='both', direction="in", pad=1, bottom=True, top=True, left=True, right=False, labelleft=True, labelright=False, labeltop=False, labelbottom=True)
    
    sub.set_xlim(xlim)
    sub.set_xticks(xticks)
    xminor_locator = AutoMinorLocator(4)
    sub.xaxis.set_minor_locator(xminor_locator)
    
    #sub.set_yticks(range(-5, 9, 5))
    yminor_locator = AutoMinorLocator(2)
    sub.yaxis.set_minor_locator(yminor_locator)
    
    fn1 = r"mr\s1_2K.csv"
    data = datasets.load_csv(fn1, mi_columns, has_header=True)
    sub.plot(data["H"] / H_unit, data["mr"] / mr_unit, color=pal.t2, marker=None, markersize=4.0, markerfacecolor="none", linestyle="-", linewidth=lw, zorder=1)
    
    fn1 = r"mr\s1_4K.csv"
    data = datasets.load_csv(fn1, mi_columns, has_header=True)
    sub.plot(data["H"] / H_unit, data["mr"] / mr_unit, color=pal.t4, marker=None, markersize=4.0, markerfacecolor="none", linestyle="--", linewidth=lw, zorder=1)
    
    fn1 = r"mr\s1_8K.csv"
    data = datasets.load_csv(fn1, mi_columns, has_header=True)
    sub.plot(data["H"] / H_unit, data["mr"] / mr_unit, color=pal.t8, marker=None, markersize=4.0, markerfacecolor="none", linestyle="-.", linewidth=lw, zorder=1)
    
    fn1 = r"mr\s1_16K.csv"
    data = datasets.load_csv(fn1, mi_columns, has_header=True)
    sub.plot(data["H"] / H_unit, data["mr"] / mr_unit, color=pal.t16, marker=None, markersize=4.0, markerfacecolor="none", linestyle=":", linewidth=lw, zorder=1)
    
    fn1 = r"mr\s1_30K.csv"
    data = datasets.load_csv(fn1, mi_columns, has_header=True)
    sub.plot(data["H"] / H_unit, data["mr"] / mr_unit, color=pal.t30, marker=None, markersize=4.0, markerfacecolor="none", linestyle="-", linewidth=lw, zorder=1)
    
    
    # Sub fig d
    sub = sub_d
    sub.text(0.9, 0.15, "(d)", transform=sub.transAxes, ha="center", va="center", size="large")
    
    # Annotations
    sub.text(-6, 2.1, "2K", size="small", ha="center", va="center", color=pal.t2, bbox=dict(facecolor="#ffffff", edgecolor='none', pad=0))
    sub.text(-6, 0.4, "30K", size="small", ha="center", va="center", color=pal.t30, bbox=dict(facecolor="#ffffff", edgecolor='none', pad=0))
    sub.arrow(-6, 2.0, 0, -1.1, width=0.001, head_length=0.2, head_width=0.5, ec="#000000", fc="#000000")
    """
    sub.text(-4, 2.5, "2K", size="small", ha="center", va="center", color=pal.t2, bbox=dict(facecolor="#ffffff", edgecolor='none', pad=0))
    sub.text(-4, 2.1, "4K", size="small", ha="center", va="center", color=pal.t4, bbox=dict(facecolor="#ffffff", edgecolor='none', pad=0))
    sub.text(-4, 1.7, "8K", size="small", ha="center", va="center", color=pal.t8, bbox=dict(facecolor="#ffffff", edgecolor='none', pad=0))
    sub.text(-4, 1.15, "16K", size="small", ha="center", va="center", color=pal.t16, bbox=dict(facecolor="#ffffff", edgecolor='none', pad=0))
    sub.text(-4, 0.75, "30K", size="small", ha="center", va="center", color=pal.t30, bbox=dict(facecolor="#ffffff", edgecolor='none', pad=0))
    """
    
    sub.tick_params(axis='both', which='both', direction="in", pad=1, bottom=True, top=True, left=False, right=True, labelleft=False, labelright=True, labeltop=False, labelbottom=True)
    sub.set_xlabel(r"$H$ (T $/\mu_0$)")
    sub.set_ylabel(r"$\Delta{}R(H) / R(0) (\%)$")
    sub.xaxis.set_label_position("bottom")
    sub.xaxis.set_label_coords(0, -0.15)
    sub.yaxis.set_label_position("right")
    sub.yaxis.set_label_coords(1.14, 1.0)
    
    sub.set_xlim(xlim)
    sub.set_xticks(xticks)
    xminor_locator = AutoMinorLocator(4)
    sub.xaxis.set_minor_locator(xminor_locator)
    
    #sub.set_yticks(range(-5, 9, 5))
    yminor_locator = AutoMinorLocator(5)
    sub.yaxis.set_minor_locator(yminor_locator)
    
    fn1 = r"mr\s0_2K.csv"
    data = datasets.load_csv(fn1, mi_columns, has_header=True)
    sub.plot(data["H"] / H_unit, data["mr"] / mr_unit, color=pal.t2, marker=None, markersize=4.0, markerfacecolor="none", linestyle="-", linewidth=lw, zorder=1)
    
    fn1 = r"mr\s0_4K.csv"
    data = datasets.load_csv(fn1, mi_columns, has_header=True)
    sub.plot(data["H"] / H_unit, data["mr"] / mr_unit, color=pal.t4, marker=None, markersize=4.0, markerfacecolor="none", linestyle="--", linewidth=lw, zorder=1)
    
    fn1 = r"mr\s0_8K.csv"
    data = datasets.load_csv(fn1, mi_columns, has_header=True)
    sub.plot(data["H"] / H_unit, data["mr"] / mr_unit, color=pal.t8, marker=None, markersize=4.0, markerfacecolor="none", linestyle="-.", linewidth=lw, zorder=1)
    
    fn1 = r"mr\s0_16K.csv"
    data = datasets.load_csv(fn1, mi_columns, has_header=True)
    sub.plot(data["H"] / H_unit, data["mr"] / mr_unit, color=pal.t16, marker=None, markersize=4.0, markerfacecolor="none", linestyle=":", linewidth=lw, zorder=1)
    
    fn1 = r"mr\s0_30K.csv"
    data = datasets.load_csv(fn1, mi_columns, has_header=True)
    sub.plot(data["H"] / H_unit, data["mr"] / mr_unit, color=pal.t30, marker=None, markersize=4.0, markerfacecolor="none", linestyle="-", linewidth=lw, zorder=1)
    
    
    # d insert
    sub = sub_di
    sub.tick_params(axis='both', which='both', direction="in", pad=1, bottom=True, top=True, left=True, right=True, labelleft=False, labelright=True, labeltop=False, labelbottom=True)
    
    XLIM = 0.2
    sub.set_xlim([-XLIM, XLIM])
    sub.set_ylim([-0.05, 0.25])
    
    xminor_locator = AutoMinorLocator(2)
    sub.xaxis.set_minor_locator(xminor_locator)
    
    sub.set_yticks(np.arange(0.0, 0.4, 0.2))
    yminor_locator = AutoMinorLocator(2)
    sub.yaxis.set_minor_locator(yminor_locator)
    
    fn1 = r"mr\s0_2K.csv"
    data = datasets.load_csv(fn1, mi_columns, has_header=True)
    mask = np.logical_and(data["H"] / H_unit < XLIM, data["H"] / H_unit > -XLIM)
    data = data.mask(mask)
    sub.plot(data["H"] / H_unit, data["mr"] / mr_unit, color=pal.t2, marker=None, markersize=4.0, markerfacecolor="none", linestyle="-", linewidth=lw, zorder=1)
    
    fn1 = r"mr\s0_4K.csv"
    data = datasets.load_csv(fn1, mi_columns, has_header=True)
    mask = np.logical_and(data["H"] / H_unit < XLIM, data["H"] / H_unit > -XLIM)
    data = data.mask(mask)
    sub.plot(data["H"] / H_unit, data["mr"] / mr_unit, color=pal.t4, marker=None, markersize=4.0, markerfacecolor="none", linestyle="--", linewidth=lw, zorder=1)
    
    fn1 = r"mr\s0_8K.csv"
    data = datasets.load_csv(fn1, mi_columns, has_header=True)
    mask = np.logical_and(data["H"] / H_unit < XLIM, data["H"] / H_unit > -XLIM)
    data = data.mask(mask)
    sub.plot(data["H"] / H_unit, data["mr"] / mr_unit, color=pal.t8, marker=None, markersize=4.0, markerfacecolor="none", linestyle="-.", linewidth=lw, zorder=1)
    
    fn1 = r"mr\s0_16K.csv"
    data = datasets.load_csv(fn1, mi_columns, has_header=True)
    mask = np.logical_and(data["H"] / H_unit < XLIM, data["H"] / H_unit > -XLIM)
    data = data.mask(mask)
    sub.plot(data["H"] / H_unit, data["mr"] / mr_unit, color=pal.t16, marker=None, markersize=4.0, markerfacecolor="none", linestyle=":", linewidth=lw, zorder=1)
    
    fn1 = r"mr\s0_30K.csv"
    data = datasets.load_csv(fn1, mi_columns, has_header=True)
    mask = np.logical_and(data["H"] / H_unit < XLIM, data["H"] / H_unit > -XLIM)
    data = data.mask(mask)
    sub.plot(data["H"] / H_unit, data["mr"] / mr_unit, color=pal.t30, marker=None, markersize=4.0, markerfacecolor="none", linestyle="-", linewidth=lw, zorder=1)
    
    
    fig.set_tight_layout(tight)
    
    fig.savefig(r'mr.pdf', format='pdf')
    