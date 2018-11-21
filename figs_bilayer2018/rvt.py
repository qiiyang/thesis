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

tight = {"pad": 0.3, "h_pad": 0.0, "w_pad": 0.0}

mi_columns = {0:"T", 1:"X", 2:"Y", 4:"err_X", 5:"err_Y"}
rvt_columns = {0:"T", 1:"R", 2:"err_R"}
hall_columns = {0:"H", 1:"R", 3:"err_R"}

if __name__ == '__main__':
    # Common parameters
    lw = 1.0
    #xminorLocator = MultipleLocator(5)
    
    
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
    gs0 = gridspec.GridSpec(4, 2, wspace=0, hspace=0)
    
    sub_rvt1 = fig.add_subplot(gs0[0, 0])
    sub_rvt2 = fig.add_subplot(gs0[1, 0])
    
    sub_rvt3 = fig.add_subplot(gs0[2, 0])
    sub_rvt4 = fig.add_subplot(gs0[3, 0])
    
    sub_halln = fig.add_subplot(gs0[2:4, 1])
    sub_hallp = fig.add_subplot(gs0[0:2, 1])
    
        
    # Sub fig rvt1
    xlim = [2, 100]
    xticks = range(10, 99, 20)
    sub = sub_rvt1
    sub.text(0.87, 0.8, "(a)", transform=sub.transAxes, ha="center", va="center", size="large")
    sub.text(80, 2e-2, "S1", ha="center", va="center", color=pal.s1)
    
    sub.tick_params(axis='both', which='both', direction="in", pad=1, bottom=True, top=True, left=True, right=False, labelleft=True, labelright=False, labeltop=False, labelbottom=False)
    #sub.set_xlabel(r"$T$ (K)")
    sub.set_ylabel(r"$R_\Box (h/e^2)$")
    #sub.xaxis.set_label_position("none")
    sub.yaxis.set_label_position("left")
    sub.yaxis.set_label_coords(-0.15, 0.0)
    
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
    
    #legend = sub.legend(handlelength=0.0)
    
    
    # Sub fig rvt2
    sub = sub_rvt2
    sub.text(0.87, 0.8, "(b)", transform=sub.transAxes, ha="center", va="center", size="large")
    sub.text(80, 0.8, "S2", ha="center", va="center", color=pal.s2)
    
    sub.tick_params(axis='both', which='both', direction="in", pad=1, bottom=True, top=True, left=True, right=False, labelleft=True, labelright=False, labeltop=False, labelbottom=False)
    #sub.set_xlabel(r"$T$ (K)")
    #sub.set_ylabel(r"$R_\Box (h/e^2)$")
    sub.xaxis.set_label_position("bottom")
    sub.yaxis.set_label_position("left")
    
    sub.set_xlim(xlim)
    sub.set_xticks(xticks)
    xminor_locator = AutoMinorLocator(2)
    sub.xaxis.set_minor_locator(xminor_locator)
    
    
    sub.set_ylim([0.6, 1.1])
    sub.set_yticks(np.arange(0.6, 1.1, 0.2))
    yminor_locator = AutoMinorLocator(2)
    sub.yaxis.set_minor_locator(yminor_locator)
    
    fn1 = r"rvt\s2.dat"
    data = datasets.load_csv(fn1, rvt_columns, has_header=True)
    
    mask = np.logical_and(data["T"] > xlim[0], data["T"] < xlim[1])
    
    sub.plot(data["T"][mask], data["R"][mask], color=pal.rvt2, marker="x", markersize=markersize, markerfacecolor="none", linestyle="None", linewidth=lw, zorder=1)
    
    sub.axvline(x=14.5, linestyle="--", color=pal.aid_lines, linewidth=lw, zorder=2)
    sub.axvline(x=31, linestyle="--", color=pal.aid_lines, linewidth=lw, zorder=2)
    sub.axvline(x=59, linestyle="--", color=pal.aid_lines, linewidth=lw, zorder=2)
    
    #legend = sub.legend(handlelength=0.0)
    
    R_unit2 = 1.e-3
    # Sub fig rvt3
    sub = sub_rvt3
    sub.text(0.25, 0.8, "(c)", transform=sub.transAxes, ha="center", va="center", size="large")
    sub.text(80, 17.5, "S3", ha="center", va="center", color=pal.s3)
    
    sub.tick_params(axis='both', which='both', direction="in", pad=1, bottom=True, top=True, left=True, right=False, labelleft=True, labelright=False, labeltop=False, labelbottom=False)
    #sub.set_xlabel(r"$T$ (K)")
    sub.set_ylabel(r"$R_\Box (10^{-3}h/e^2)$")
    #sub.xaxis.set_label_position("top")
    sub.yaxis.set_label_position("left")
    sub.yaxis.set_label_coords(-0.15, 0)
    
    sub.set_xlim(xlim)
    sub.set_xticks(xticks)
    xminor_locator = AutoMinorLocator(2)
    sub.xaxis.set_minor_locator(xminor_locator)
    
    sub.set_ylim([16.9, 18.4])
    sub.set_yticks(np.arange(17, 18.5, 0.5))
    yminor_locator = AutoMinorLocator(2)
    sub.yaxis.set_minor_locator(yminor_locator)
    
    fn1 = r"rvt\s3.dat"
    data = datasets.load_csv(fn1, rvt_columns, has_header=True)
    
    mask = np.logical_and(data["T"] > xlim[0], data["T"] < xlim[1])
    
    sub.plot(data["T"][mask], data["R"][mask] / R_unit2, color=pal.rvt3, marker="x", markersize=markersize, markerfacecolor="none", linestyle="None", linewidth=lw, zorder=1)
    
    sub.axvline(x=14.5, linestyle="--", color=pal.aid_lines, linewidth=lw, zorder=2)
    
    #legend = sub.legend(handlelength=0.0)
    
    
    # Sub fig rvt4
    sub = sub_rvt4
    sub.text(0.25, 0.8, "(d)", transform=sub.transAxes, ha="center", va="center", size="large")
    sub.text(80, 2.8, "S4", ha="center", va="center", color=pal.s4)
    
    sub.tick_params(axis='both', which='both', direction="in", pad=1, bottom=True, top=True, left=True, right=False, labelleft=True, labelright=False, labeltop=False, labelbottom=True)
    sub.set_xlabel(r"$T$ (K)")
    #sub.set_ylabel(r"$R_\Box (10^{-3}h/e^2)$")
    sub.xaxis.set_label_position("bottom")
    sub.yaxis.set_label_position("right")
    
    sub.set_xlim(xlim)
    sub.set_xticks(xticks)
    xminor_locator = AutoMinorLocator(2)
    sub.xaxis.set_minor_locator(xminor_locator)
    
    sub.set_yticks(np.arange(2.6, 3.1, 0.2))
    yminor_locator = AutoMinorLocator(2)
    sub.yaxis.set_minor_locator(yminor_locator)
    
    fn1 = r"rvt\s4.dat"
    data = datasets.load_csv(fn1, rvt_columns, has_header=True)
    
    mask = np.logical_and(data["T"] > xlim[0], data["T"] < xlim[1])
    
    sub.plot(data["T"][mask], data["R"][mask] / R_unit2, color=pal.rvt4, marker="x", markersize=markersize, markerfacecolor="none", linestyle="None", linewidth=lw, zorder=1)
    
    sub.axvline(x=14.5, linestyle="--", color=pal.aid_lines, linewidth=lw, zorder=2)
    
    
    xlim = (-0.1, 9.0)
    xticks = range(0, 9, 2)
    
    
    # Sub fig Hall p
    H_unit = 1.0e4
    sub = sub_hallp
    sub.text(0.13, 0.8, "(e)", transform=sub.transAxes, ha="center", va="center", size="large")
    
    sub.text(7, -1.8, "S4", ha="center", va="center", color=pal.s4, bbox=dict(facecolor="#ffffff", edgecolor='none', pad=0))
    sub.text(7, 7, "S3", ha="center", va="center", color=pal.s3)
    sub.text(7, 18, "S2", ha="center", va="center", color=pal.s2)    
    
    sub.tick_params(axis='both', which='both', direction="in", pad=1, bottom=True, top=True, left=False, right=True, labelleft=False, labelright=True, labeltop=False, labelbottom=False)
    #sub.set_xlabel(r"$H$ (T~$/\mu_0$)")
    sub.set_ylabel(r"$R_{xy} / \Omega$")
    sub.xaxis.set_label_position("top")
    sub.yaxis.set_label_position("right")
    sub.yaxis.set_label_coords(1.15, 0)
    
    
    sub.set_xlim(xlim)
    sub.set_xticks(xticks)
    xminor_locator = AutoMinorLocator(2)
    sub.xaxis.set_minor_locator(xminor_locator)
    
    sub.set_yticks(range(0, 25, 10))
    yminor_locator = AutoMinorLocator(2)
    sub.yaxis.set_minor_locator(yminor_locator)
    
    fn1 = r"hall\s4.dat"
    data = datasets.load_csv(fn1, hall_columns, has_header=True)
    
    sub.errorbar(data["H"] / H_unit, -data["R"], yerr=data["err_R"] * NSE, color=pal.hall4, marker="^", markersize=markersize, markerfacecolor="none", linestyle="None", linewidth=lw, zorder=1)
    
    fn1 = r"hall\s3.dat"
    data = datasets.load_csv(fn1, hall_columns, has_header=True)
    
    sub.errorbar(data["H"] / H_unit, -data["R"], yerr=data["err_R"] * NSE, color=pal.hall3, marker="o", markersize=markersize, markerfacecolor="none", linestyle="None", linewidth=lw, zorder=1)
    
    fn1 = r"hall\s2.dat"
    data = datasets.load_csv(fn1, hall_columns, has_header=True)
    
    sub.errorbar(data["H"] / H_unit, -data["R"], yerr=data["err_R"] * NSE, color=pal.hall2, marker="x", markersize=markersize, markerfacecolor="none", linestyle="None", linewidth=lw, zorder=1)
    
    
    # Sub fig Hall n
    sub = sub_halln
    sub.text(0.13, 0.2, "(f)", transform=sub.transAxes, ha="center", va="center", size="large")
    
    sub.text(7, -355, "S1", ha="center", va="center", color=pal.s1)
    
    H_unit = 1.0e4
    sub.tick_params(axis='both', which='both', direction="in", pad=1, bottom=True, top=True, left=False, right=True, labelleft=False, labelright=True, labeltop=False, labelbottom=True)
    sub.set_xlabel(r"$H$ (T~$/\mu_0$)")
    #sub.set_ylabel(r"$R_{xy} / \Omega$")
    #sub.xaxis.set_label_position("bottom")
    #sub.yaxis.set_label_position("right")
    
    sub.set_xlim(xlim)
    sub.set_xticks(xticks)
    xminor_locator = AutoMinorLocator(2)
    sub.xaxis.set_minor_locator(xminor_locator)
    
    sub.set_yticks(range(-500, 100, 500))
    yminor_locator = AutoMinorLocator(5)
    sub.yaxis.set_minor_locator(yminor_locator)
    
    fn1 = r"hall\s1.dat"
    data = datasets.load_csv(fn1, hall_columns, has_header=True)
    
    sub.errorbar(data["H"] / H_unit, -data["R"], yerr=data["err_R"] * NSE, color=pal.hall1, marker="x", markersize=markersize, markerfacecolor="none", linestyle="None", linewidth=lw, zorder=1)
    
    #plt.legend()
    
    fig.set_tight_layout(tight)
    
    fig.savefig(r'rvt.pdf', format='pdf')
    
    