NSE = 1.0 # Standard error multiplier

SQUID_COLUMNS = {0:"time",1:"T", 2:"H",3:"M",4:"err_M"}


import numpy as np

from matplotlib import rcParams, gridspec, ticker
rcParams['backend'] = 'PS'
rcParams['text.usetex'] = True
rcParams['text.latex.preamble'] = [r'\usepackage{bm}', r'\usepackage{amssymb}']
import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

from elflab import datasets
import elflab.projects.mpms.analysis as mpms


tight = {"pad": 0.6, "h_pad": 0.0, "w_pad": 0.0}


if __name__ == '__main__':
    
    # Figure configs
    lw = 1
    markersize=6
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
    
    sub_a = fig.add_subplot(gs1[0, 0])
    
    M_unit = 1.e-5
    H_unit = 1.e4
    
    # Sub fig b
    #sub_a.text(0.13, 0.18, "(a)", transform=sub_a.transAxes, ha="center", va="center", size="large")
    #sub_a.text(16, 1.2, r"$T_C \approx 14.5$~K", ha="left", va="center", bbox=dict(facecolor="#ffffff", edgecolor='none', pad=0.2))
    
    sub_a.set_xlim([10, 25])
    #sub_a.set_ylim([0, 30])
    #sub_a.set_ylim([0, 60])
    
    sub_a.tick_params('both', which="both", direction="in", pad=1, bottom=True, top=True, left=True, right=False)
    sub_a.set_xlabel(r"$T$ (K)", labelpad=0.1)
    sub_a.set_ylabel(r"$1 / M_z$ (arb. unit)", labelpad=1.0)
    
    xminor_locator = AutoMinorLocator(10)
    sub_a.xaxis.set_minor_locator(xminor_locator)
    yminor_locator = AutoMinorLocator(5)
    sub_a.yaxis.set_minor_locator(yminor_locator)
    
    
    fn1 = r"130614_03_EuS11Sap_IS_MvT_warmup.rso.dat"
    data = mpms.loadfile_rso(fn1)
    data = data.mask(data["T"] < 25)
    sub_a.errorbar(data["T"], M_unit / (data["M"] + 4.096371e-006), yerr=NSE * data["err_M"] / (data["M"] + 4.096371e-006)**2 * M_unit, color="C0", marker="x", markersize=markersize, markerfacecolor="none", linestyle="None", linewidth=1, zorder=1)
    #sub_a.errorbar(data["T"], (data["M"] + 4.096371e-006) / M_unit, yerr=NSE * data["err_M"] / M_unit, color="C0", marker="x", markersize=markersize, markerfacecolor="none", linestyle="None", linewidth=1, zorder=1)
    
    #xs = np.arange(12, 40, 0.1)
    #ys = (xs - 15.6823) / 1.40649
    #sub_a.plot(xs, ys, color="k", marker=None)
    
    #plt.legend()
    
    fig.set_tight_layout(tight)
    
    fig.savefig(r'squid.pdf', format='pdf')
    #fig.savefig(r'squid.svg', format='svg')