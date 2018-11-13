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

from elflab import constants, datasets
import elflab.projects.ppms.analysis as ppmsana

vdp = constants.pi / constants.ln2  # van der Pauw prefix
quantum_resistance = constants.h / constants.e / constants.e # h/e^2

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
    plt.rc('font', family='serif')
    plt.rc('font', size=12)
    plt.rc('ps', usedistiller="xpdf")
    
    paperwidth = 8.5
    fig = plt.figure(dpi=1200)
    fig.set_size_inches([0.65 * paperwidth, 0.3/0.4*0.6 * paperwidth])
    #fig.set_size_inches([3.375, 2.1])
    
    marker_size = 6
    
    # Sub figure layout
    gs1 = gridspec.GridSpec(2, 2)
    gs1.update(wspace=0.0, hspace=0.0)
    sub_a = fig.add_subplot(gs1[0, 0])
    sub_b = fig.add_subplot(gs1[0, 1])
    sub_c = fig.add_subplot(gs1[1, 0])
    sub_d = fig.add_subplot(gs1[1, 1])
    
    
    # Sub fig a
    sub = sub_a
    sub.text(0.1, 0.8, "(a) EE", transform=sub.transAxes, ha="left", va="center")
   
    x_trans = lambda x: np.log10(x)
    y_trans = lambda y: 1.0 / y
    xlim = [x_trans(2.0), x_trans(300.0)]
    
    sub.tick_params(axis='both', which='both', direction="in", pad=1, bottom=False, top=True, left=True, right=False, labelleft=True, labelright=False, labeltop=True, labelbottom=False)
    sub.set_xlabel(r"$\log_{10}(T / \textrm{K})$")
    sub.set_ylabel(r"$\sigma_\Box (e^2/h)$")
    sub.xaxis.set_label_position("top")
    #sub.xaxis.set_label_coords(1, 1.15)
    sub.yaxis.set_label_position("left")
    #sub.yaxis.set_label_coords(-0.17, 0.0)
    
    sub.set_xlim(xlim)
    #sub.set_xticks(xticks)
    xminor_locator = AutoMinorLocator(5)
    sub.xaxis.set_minor_locator(xminor_locator)
    
    #sub.set_ylim([-15, 29])
    #sub.set_yticks(range(-10, 29, 10))
    yminor_locator = AutoMinorLocator(5)
    sub.yaxis.set_minor_locator(yminor_locator)
    
    fn1 = r"data/20120815_01_RvT_down_Ch1.03P.EuS2.Sap.InterXX_Ch2.03P.EuS3.Sap.InterXX_Ch303P.Sap.InterXX.dat"
    data = ppmsana.import_dc(fn1)[0]
    sub.plot(x_trans(data["T"]), y_trans(data["R"] * vdp / quantum_resistance), color=pal.bl0, marker="x", markerfacecolor="none", markersize=marker_size, linestyle="none", label="BL0")
    
    
    # Sub fig b
    sub = sub_b
    sub.text(0.1, 0.8, "(b) TA", transform=sub.transAxes, ha="left", va="center")
   
    x_trans = lambda x: 1.0 / x
    y_trans = lambda y: np.log10(y)
    xlim = [x_trans(300.0), x_trans(2.0)]
    #xlim = [x_trans(300.0), 0.025]
    
    sub.tick_params(axis='both', which='both', direction="in", pad=1, bottom=False, top=True, left=False, right=True, labelleft=False, labelright=True, labeltop=True, labelbottom=False)
    sub.set_xlabel(r"$T^{-1} (\mathrm{K}^{-1})$")
    sub.set_ylabel(r"$\log_{10}(R_\Box \cdot e^2/h)$")
    sub.xaxis.set_label_position("top")
    #sub.xaxis.set_label_coords(1, 1.15)
    sub.yaxis.set_label_position("right")
    #sub.yaxis.set_label_coords(-0.17, 0.0)
    
    sub.set_xlim(xlim)
    sub.set_ylim([-0.15, 0.42])
    #sub.set_ylim([-0.15, 0.1])
    
    #sub.set_xticks(xticks)
    xminor_locator = AutoMinorLocator(5)
    sub.xaxis.set_minor_locator(xminor_locator)
    
    #sub.set_ylim([-15, 29])
    #sub.set_yticks(range(-10, 29, 10))
    yminor_locator = AutoMinorLocator(5)
    sub.yaxis.set_minor_locator(yminor_locator)
    
    fn1 = r"data/20120815_01_RvT_down_Ch1.03P.EuS2.Sap.InterXX_Ch2.03P.EuS3.Sap.InterXX_Ch303P.Sap.InterXX.dat"
    data = ppmsana.import_dc(fn1)[0]
    sub.plot(x_trans(data["T"]), y_trans(data["R"] * vdp / quantum_resistance), color=pal.bl0, marker="x", markerfacecolor="none", markersize=marker_size, linestyle="none", label="BL0")
    
    
    # Sub fig c
    sub = sub_c
    sub.text(0.1, 0.8, "(c) M-VRH", transform=sub.transAxes, ha="left", va="center")
   
    x_trans = lambda x: np.power(x, -1.0/3.0)
    y_trans = lambda y: np.log10(y)
    xlim = [x_trans(300.0), x_trans(2.0)]
    
    sub.tick_params(axis='both', which='both', direction="in", pad=1, bottom=True, top=False, left=True, right=False, labelleft=True, labelright=False, labeltop=False, labelbottom=True)
    sub.set_xlabel(r"$T^{-1/3} (\mathrm{K}^{-1/3})$")
    sub.set_ylabel(r"$\log_{10}(R_\Box \cdot e^2/h)$")
    sub.xaxis.set_label_position("bottom")
    #sub.xaxis.set_label_coords(1, 1.15)
    sub.yaxis.set_label_position("left")
    #sub.yaxis.set_label_coords(-0.17, 0.0)
    
    sub.set_xlim(xlim)
    sub.set_ylim([-0.15, 0.42])
    
    #sub.set_xticks(xticks)
    xminor_locator = AutoMinorLocator(5)
    sub.xaxis.set_minor_locator(xminor_locator)
    
    #sub.set_ylim([-15, 29])
    #sub.set_yticks(range(-10, 29, 10))
    yminor_locator = AutoMinorLocator(5)
    sub.yaxis.set_minor_locator(yminor_locator)
    
    fn1 = r"data/20120815_01_RvT_down_Ch1.03P.EuS2.Sap.InterXX_Ch2.03P.EuS3.Sap.InterXX_Ch303P.Sap.InterXX.dat"
    data = ppmsana.import_dc(fn1)[0]
    sub.plot(x_trans(data["T"]), y_trans(data["R"] * vdp / quantum_resistance), color=pal.bl0, marker="x", markerfacecolor="none", markersize=marker_size, linestyle="none", label="BL0")
    
    
    # Sub fig d
    sub = sub_d
    sub.text(0.1, 0.8, "(d) ES-VRH", transform=sub.transAxes, ha="left", va="center")
   
    x_trans = lambda x: np.power(x, -1.0/2.0)
    y_trans = lambda y: np.log10(y)
    xlim = [x_trans(300.0), x_trans(2.0)]
    
    sub.tick_params(axis='both', which='both', direction="in", pad=1, bottom=True, top=False, left=False, right=True, labelleft=False, labelright=True, labeltop=False, labelbottom=True)
    sub.set_xlabel(r"$T^{-1/2} (\mathrm{K}^{-1/2})$")
    sub.set_ylabel(r"$\log_{10}(R_\Box \cdot e^2/h)$")
    sub.xaxis.set_label_position("bottom")
    #sub.xaxis.set_label_coords(1, 1.15)
    sub.yaxis.set_label_position("right")
    #sub.yaxis.set_label_coords(-0.17, 0.0)
    
    sub.set_xlim(xlim)
    sub.set_ylim([-0.15, 0.42])
    
    #sub.set_xticks(xticks)
    xminor_locator = AutoMinorLocator(5)
    sub.xaxis.set_minor_locator(xminor_locator)
    
    #sub.set_ylim([-15, 29])
    #sub.set_yticks(range(-10, 29, 10))
    yminor_locator = AutoMinorLocator(5)
    sub.yaxis.set_minor_locator(yminor_locator)
    
    fn1 = r"data/20120815_01_RvT_down_Ch1.03P.EuS2.Sap.InterXX_Ch2.03P.EuS3.Sap.InterXX_Ch303P.Sap.InterXX.dat"
    data = ppmsana.import_dc(fn1)[0]
    sub.plot(x_trans(data["T"]), y_trans(data["R"] * vdp / quantum_resistance), color=pal.bl0, marker="x", markerfacecolor="none", markersize=marker_size, linestyle="none", label="BL0")
    
    legend = sub_b.legend(handlelength=1.0, handletextpad=0.5, ncol=1, loc='upper left', bbox_to_anchor=(1.15, 1.15))
    fig.set_tight_layout(tight)
    
    #fig.savefig(r'bls_out.pdf', format='pdf')
    #fig.savefig(r'bls_out.svg', format='svg')
    fig.savefig(r'bl0.pdf', format='pdf')