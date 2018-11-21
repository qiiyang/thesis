NSE = 2.0 # Standard error multiplier

SQUID_COLUMNS = {0:"time",1:"T", 2:"H",3:"M",4:"err_M"}

import palette as pal

import numpy as np
from scipy.ndimage import filters

from matplotlib import rcParams, gridspec, ticker
rcParams['backend'] = 'PS'
rcParams['text.usetex'] = True
rcParams['text.latex.preamble'] = [r'\usepackage{bm}', r'\usepackage{amssymb}']
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

from elflab import datasets


tight = {"pad": 0.6, "h_pad": 0.0, "w_pad": 0.0}


def no_process(data):
    return data
    
def log_y(data):
    data["counts"] = np.log(data["counts"] + 1.)
    return data
    
def mean_filter(data):
    data = datasets.downsample(data, 9, method=np.nanmean)
    return data
    
def gaus_filter(data):
    data["counts"] = filters.gaussian_filter(data["counts"], 3)
    return data
    
def gaus_slope(data):
    mask = np.logical_and(data["2theta"] > 7, data["2theta"] < 80)
    data["counts"] = data["counts"][mask]
    data["2theta"] = data["2theta"][mask]
    data["counts"] = filters.gaussian_filter(data["counts"], 4)
    data["counts"] = data["counts"] * np.exp(0.049 * data["2theta"])
    return data


if __name__ == '__main__':
    
    # Figure configs
    lw = 1
    markersize=6
    plt.rc('font', family='Times New Roman')
    plt.rc('font', size=12)
    plt.rc('ps', usedistiller="xpdf")
    
    paperwidth = 8.5
    fig = plt.figure(dpi=1200)
    p = 0.7
    fig.set_size_inches([p * paperwidth, 0.17/0.4* p * paperwidth])
    
    # Sub figure layout
    gs1 = gridspec.GridSpec(1, 2)
    gs1.update(wspace=0.0, hspace=0.0)
    
    sub_b = fig.add_subplot(gs1[0, 0])
    sub_c = fig.add_subplot(gs1[0, 1])
    
    M_unit = 1.2e-5
    H_unit = 1.e4
    
    # Sub fig b
    sub_b.text(0.13, 0.18, "(a)", transform=sub_b.transAxes, ha="center", va="center", size="large")
    sub_b.text(16, 1.2, r"$T_C \approx 14.5$~K", ha="left", va="center", bbox=dict(facecolor="#ffffff", edgecolor='none', pad=0.2))
    
    sub_b.set_xlim([1.9, 39])
    #sub_b.set_xlim([2, 100])
    sub_b.set_ylim([0, 1.45])
    
    sub_b.tick_params('both', which="both", direction="in", pad=1, bottom=True, top=True, left=True, right=False)
    sub_b.set_xlabel(r"$T$ (K)", labelpad=0.1)
    sub_b.set_ylabel(r"$M_z$ (arb. unit)", labelpad=1.0)
    
    xminor_locator = AutoMinorLocator(5)
    sub_b.xaxis.set_minor_locator(xminor_locator)
    yminor_locator = AutoMinorLocator(5)
    sub_b.yaxis.set_minor_locator(yminor_locator)
    
    
    fn1 = r"squid\MvT.dat"
    data = datasets.load_csv(fn1, SQUID_COLUMNS)
    sub_b.errorbar(data["T"], data["M"] / M_unit, yerr=NSE * data["err_M"] / M_unit, color=pal.squid_T, marker="x", markersize=markersize, markerfacecolor="none", linestyle="None", linewidth=1, zorder=1)
    
    fn1 = r"squid\curie.dat"
    data = datasets.load_csv(fn1, {0:"x", 1:"y"})    
    sub_b.plot(data["x"], data["y"] / M_unit, color="black", marker=None, linestyle="-", linewidth=lw, zorder=2)
    #sub_b.axvline(x=14.5, color="k", linewidth=1, zorder=2)
    
    
    # Sub fig c
    # text and annotations
    sub_c.text(0.87, 0.18, "(b)", transform=sub_c.transAxes, ha="center", va="center", size="large")
    
    sub_c.arrow(-0.03, 5.0, -0.04, -6.5, width=0.001, head_length=1.5, head_width=0.01, ec=pal.squid_Ha, fc=pal.squid_Ha)
    sub_c.arrow(0.03, -5.0, 0.04, 6.5, width=0.001, head_length=1.5, head_width=0.01, ec=pal.squid_Hb, fc=pal.squid_Hb)
    
    sub_c.set_xlim([-0.15, 0.15])
    sub_c.set_ylim([-9, 9])
    sub_c.tick_params('both', which="both", direction="in", pad=1, bottom=True, top=True, left=False, right=True, labelleft=False, labelright=True)
        
    sub_c.set_xlabel(r"$H$ (T/$\mu_0$)", labelpad=0.1)
    sub_c.set_ylabel(r"$M_z$ (arb. unit)", labelpad=1.0)
    sub_c.yaxis.set_label_position("right")
    
    xminor_locator = AutoMinorLocator(5)
    sub_c.xaxis.set_minor_locator(xminor_locator)
    yminor_locator = AutoMinorLocator(5)
    sub_c.yaxis.set_minor_locator(yminor_locator)
    
    # origin aid lines
    sub_c.axvline(x=0, linestyle="--", color=pal.aid_lines, linewidth=1)
    sub_c.axhline(y=0, linestyle="--", color=pal.aid_lines, linewidth=1)
    
    # Plot
    fn1 = r"squid\MvHa.dat"
    data = datasets.load_csv(fn1, SQUID_COLUMNS)
    sub_c.errorbar(data["H"] / H_unit, data["M"] / M_unit, yerr=NSE * data["err_M"] / M_unit, color=pal.squid_Ha, marker="o", markersize=markersize, markerfacecolor="none", linestyle="None", linewidth=1)
    
    fn1 = r"squid\MvHb.dat"
    data = datasets.load_csv(fn1, SQUID_COLUMNS)
    sub_c.errorbar(data["H"] / H_unit, data["M"] / M_unit, yerr=NSE * data["err_M"] / M_unit, color=pal.squid_Hb, marker="x", markersize=markersize, markerfacecolor="none", linestyle="None", linewidth=1)
    
    #plt.legend()
    
    fig.set_tight_layout(tight)
    
    fig.savefig(r'squid.pdf', format='pdf')
    