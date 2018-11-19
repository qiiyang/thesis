NSE = 1.0 # Standard error multiplier

import palette as pal

import numpy as np

from matplotlib import rcParams, gridspec, ticker

rcParams['backend'] = 'ps'
rcParams['text.usetex'] = True
rcParams['text.latex.preamble'] = r'\usepackage{amssymb}'

rcParams['legend.frameon'] = False  # no frame for legends
rcParams['legend.shadow'] = False
rcParams['legend.handletextpad'] = 1.0

import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

from elflab import datasets, constants
from elflab.analysis import errors
import elflab.projects.ppms.analysis as ppmsana

vdp = constants.pi / constants.ln2  # van der Pauw prefix
quantum_resistance = constants.h / constants.e / constants.e # h/e^2

tight = {"pad": 0.3, "h_pad": 0.0, "w_pad": 0.0}

if __name__ == '__main__':    
    # Figure configs
    plt.rc('font', family='Times New Roman')
    plt.rc('font', size=12)
    plt.rc('ps', usedistiller="xpdf")
    
    paperwidth = 8.5
    fig = plt.figure(dpi=1200)
    fig.set_size_inches([0.45 * paperwidth, 0.25/0.4*0.45 * paperwidth])
    #fig.set_size_inches([3.375, 2.1])
    
    marker_size = 6
    mew = 0.5
    
    # Sub figure layout
    gs1 = gridspec.GridSpec(1, 1)
    gs1.update(wspace=0.0, hspace=0.0)
    sub_a = fig.add_subplot(gs1[0, 0])
    
    
    # Sub fig a
    sub = sub_a
    #sub.text(0.1, 0.8, "(c) M-VRH", transform=sub.transAxes, ha="left", va="center")
   
    x_trans = lambda x: x
    y_trans = lambda y: y
    xlim = [2.0, 300.0]
    
    sub.tick_params(axis='both', which='both', direction="in", bottom=True, top=True, left=True, right=True, labelleft=True, labelright=False, labeltop=False, labelbottom=True)
    sub.set_xlabel(r"$T (\mathrm{K})$")
    sub.set_ylabel(r"$R_\Box (e^2/h)$")
    sub.xaxis.set_label_position("bottom")
    #sub.xaxis.set_label_coords(1, 1.15)
    sub.yaxis.set_label_position("left")
    #sub.yaxis.set_label_coords(-0.17, 0.0)
    
    sub.set_xlim(xlim)
    #sub.set_ylim([0.2, 1.8])
    sub.set_xscale("log")
    sub.set_yscale("log")
    
    #xminor_locator = AutoMinorLocator(5)
    #sub.xaxis.set_minor_locator(xminor_locator)
    
    #yminor_locator = AutoMinorLocator(5)
    #sub.yaxis.set_minor_locator(yminor_locator)
    
    
    fn1 = r"rvt/20120729_01_RvT_down_Ch1EuS2SiBSxx_Ch2EuS3SapBSxx_Ch3EuS2SiBSxy.dat"
    data = ppmsana.import_dc(fn1)[1]
    sub.plot(x_trans(data["T"]), y_trans(data["R"] * vdp / quantum_resistance), color=pal.bl1, marker="d", markerfacecolor="none", markersize=marker_size, linestyle="none", label="BL1", mew=mew, zorder=1)
    fn1 = r"rvt/20121020_01_RvT_down_Ch1.10P.Al2O3.InterXX_Ch2.10Pa.EuS10.Al2O3.InterXX_Ch3.10Pb.EuS10.Al2O3.InterXX.dat"
    data = ppmsana.import_dc(fn1)[2]
    sub.plot(x_trans(data["T"]), y_trans(data["R"] * vdp / quantum_resistance), color=pal.bl2, marker="o", markerfacecolor="none", markersize=marker_size, linestyle="none", label="BL2", mew=mew, zorder=2)
    data = ppmsana.import_dc(fn1)[1]
    sub.plot(x_trans(data["T"]), y_trans(data["R"] * vdp / quantum_resistance), color=pal.bl3, marker="^", markerfacecolor="none", markersize=marker_size, linestyle="none", label="BL3", mew=mew, zorder=3)
    fn1 = r"rvt/20130518_16_RvT_up_180D_Ch1.temp_Ch2.11P.EuS11.Al2O3.xx_Ch3.off.dat"
    data = ppmsana.import_dc(fn1)[1]
    sub.plot(x_trans(data["T"]), y_trans(data["R"] * vdp / quantum_resistance), color=pal.bl4, marker="v", markerfacecolor="none", markersize=marker_size, linestyle="none", label="BL4", mew=mew, zorder=4)
    fn1 = r"rvt/20121020_01_RvT_down_Ch1.10P.Al2O3.InterXX_Ch2.10Pa.EuS10.Al2O3.InterXX_Ch3.10Pb.EuS10.Al2O3.InterXX.dat"
    data = ppmsana.import_dc(fn1)[0]
    sub.plot(x_trans(data["T"]), y_trans(data["R"] * vdp / quantum_resistance), color=pal.bl0, marker="^", markerfacecolor="none", markersize=marker_size, linestyle="none", label="TI3", mew=mew, zorder=5)
    
    legend = sub_a.legend(handlelength=1.0, handletextpad=0.5, ncol=1, loc='upper left', bbox_to_anchor=(1.00, 1.0))
    fig.set_tight_layout(tight)
    fig.savefig(r'rvt.pdf', format='pdf')