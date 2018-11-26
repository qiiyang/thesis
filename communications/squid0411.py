NSE = 1.0 # Standard error multiplier

SQUID_COLUMNS = {0:"time",1:"T", 2:"H",3:"M",4:"err_M"}


import numpy as np
import scipy.optimize as opt

from matplotlib import rcParams, gridspec, ticker
rcParams['backend'] = 'PS'
rcParams['text.usetex'] = True
rcParams['text.latex.preamble'] = [r'\usepackage{bm}', r'\usepackage{amssymb}']
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

from elflab import datasets
import elflab.projects.mpms.analysis as mpms


tight = {"pad": 0.6, "h_pad": 0.0, "w_pad": 0.0}

def get_func(data):
    def func(params):
        C, Tc, M0 = params
        return data["M"] - C / (data["T"] - Tc) - M0
    return func



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
    fig.set_size_inches([p * paperwidth, 0.175/0.4* p * paperwidth])
    
    # Sub figure layout
    gs1 = gridspec.GridSpec(1, 2)
    gs1.update(wspace=0.0, hspace=0.0)
    sub_a = fig.add_subplot(gs1[0, 0])
    sub_b = fig.add_subplot(gs1[0, 1])
    
    # Sub fig a
    M_unit = 1.e-5
    H_unit = 1.e4
    sub_a.text(0.13, 0.8, "(a)", transform=sub_a.transAxes, ha="center", va="center", size="large")
    #sub_a.text(16, 1.2, r"$T_C \approx 14.5$~K", ha="left", va="center", bbox=dict(facecolor="#ffffff", edgecolor='none', pad=0.2))
    
    #sub_a.set_xlim([10, 23])
    sub_a.set_ylim([0, 7.5])
    #sub_a.set_ylim([0, 60])
    
    sub_a.tick_params('both', which="both", direction="in", bottom=True, top=True, left=True, right=False)
    sub_a.set_xlabel(r"$T$ (K)")
    sub_a.set_ylabel(r"$1 / M_z$ (arb. unit)")
    
    xminor_locator = AutoMinorLocator(5)
    sub_a.xaxis.set_minor_locator(xminor_locator)
    yminor_locator = AutoMinorLocator(5)
    sub_a.yaxis.set_minor_locator(yminor_locator)
    
    
    fn1 = r"130614_03_EuS11Sap_IS_MvT_warmup.rso.dat"
    data = mpms.loadfile_rso(fn1)
    data = data.mask(data["T"] < 22)
    data = data.mask(data["T"] > 10.0)
    sub_a.errorbar(data["T"], M_unit / (data["M"] + 4.096371e-006), yerr=NSE * data["err_M"] / (data["M"] + 4.096371e-006)**2 * M_unit, color="C0", marker="x", markersize=markersize, markerfacecolor="none", linestyle="None", linewidth=1, zorder=1)
    
    
    # Sub fig b
    M_unit = 2.e-5
    H_unit = 1.e4
    sub_b.text(0.13, 0.8, "(b)", transform=sub_b.transAxes, ha="center", va="center", size="large")
    #sub_b.text(16, 1.2, r"$T_C \approx 14.5$~K", ha="left", va="center", bbox=dict(facecolor="#ffffff", edgecolor='none', pad=0.2))
    
    #sub_b.set_xlim([10, 21])
    sub_b.set_ylim([0, 15])
    #sub_b.set_ylim([0, 7])
    
    sub_b.tick_params('both', which="both", direction="in", bottom=True, top=True, left=False, right=True, labelleft=False, labelright=True, labeltop=False, labelbottom=True)
    sub_b.set_xlabel(r"$T$ (K)", )
    sub_b.set_ylabel(r"$1 / M_z$ (arb. unit)")
    sub_b.yaxis.set_label_position("right")
    
    xminor_locator = AutoMinorLocator(5)
    sub_b.xaxis.set_minor_locator(xminor_locator)
    yminor_locator = AutoMinorLocator(5)
    sub_b.yaxis.set_minor_locator(yminor_locator)
    
    
    fn1 = r"20120825_03_EuS04_Al2O3_MvT_up.dat"
    data = mpms.loadfile_rso(fn1)
    
    data = data.mask(data["T"] < 22.5)
    data = data.mask(data["T"] > 10.0)
    sub_b.errorbar(data["T"], M_unit / (data["M"]+1.65e-6), yerr=NSE * data["err_M"] / (data["M"])**2 * M_unit, color="C0", marker="x", markersize=markersize, markerfacecolor="none", linestyle="None", linewidth=1, zorder=1)
    
    fig.set_tight_layout(tight)
    
    fig.savefig(r'squid.pdf', format='pdf')
    fig.savefig(r'squid.svg', format='svg')