NSE = 1.0 # Standard error multiplier


import numpy as np

from matplotlib import rcParams, gridspec, ticker

rcParams['backend'] = 'Cairo'
rcParams['text.usetex'] = True
rcParams['text.latex.preamble'] = r'\usepackage{amssymb}'

import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

from elflab import datasets
from elflab.analysis import errors
import elflab.projects.ppms.analysis as ppmsana
import elflab.analysis.transport as transport
import elflab.analysis.temporal_drift as tdrift

columns = {0:"T", 1:"a", 2:"err", 3:"H"}

H0 = 5.e2
H1 = 5.e3
dH = 10.0

zero_H = 120.0
H_unit = 1.e4

tight = {"pad": 0.3, "h_pad": 0.0, "w_pad": 0.0}

if __name__ == '__main__':    
    # Figure configs
    plt.rc('font', family='Times New Roman')
    plt.rc('font', size=12)
    plt.rc('ps', usedistiller="xpdf")
    
    paperwidth = 8.5
    fig = plt.figure(dpi=1200)
    fig.set_size_inches([0.7 * paperwidth, 0.3/0.4*0.7 * paperwidth])
    #fig.set_size_inches([3.375, 2.1])
    
    marker_size = 6
    
    # Sub figure layout
    gs1 = gridspec.GridSpec(2, 2)
    gs1.update(wspace=0.0, hspace=0.0)
    sub_a = fig.add_subplot(gs1[0, 0])
    sub_b = fig.add_subplot(gs1[0, 1])
    sub_c = fig.add_subplot(gs1[1, 0])
    sub_d = fig.add_subplot(gs1[1, 1])
        
    fn1 = r"data/quadraticVar.dat"
    q = datasets.load_csv(fn1, columns, has_header=False)
    
    xlim = [-0.6, 0.6]
    # Sub fig a
    sub = sub_a
    sub.text(0.2, 0.8, "(a)", transform=sub.transAxes, ha="right", va="center", size="large")
    
    sub.tick_params(axis='both', which='both', direction="in", pad=1, bottom=False, top=True, left=True, right=False, labelleft=True, labelright=False, labeltop=True, labelbottom=False)
    sub.set_xlabel(r"$H$ (T $/\mu_0$)")
    sub.set_ylabel(r"$\Delta{}R(H) / R(0) / 10^{-2}$")
    sub.xaxis.set_label_position("top")
    sub.yaxis.set_label_position("left")
    sub.set_xlim(xlim)
    yunit = 0.01
    
    xminor_locator = AutoMinorLocator(5)
    sub.xaxis.set_minor_locator(xminor_locator)
    yminor_locator = AutoMinorLocator(5)
    sub.yaxis.set_minor_locator(yminor_locator)
        
    fn = r"data/20121020_02_RvH_2K_Ch1.10P.Al2O3.InterXX_Ch2.10Pa.EuS10.Al2O3.InterXX_Ch3.10Pb.EuS10.Al2O3.InterXX.dat"
    ch = 1
    data = ppmsana.import_dc(fn)[ch]
    
    corrected = tdrift.linear(data, "R", data["time"][0], data["R"][0], data["time"][-1], data["R"][-1])
    down, up = transport.split_MR_down_up(corrected)
  
    upsym = transport.symmetrize_MR(up, down)
    downsym = transport.symmetrize_MR(down, up)
    
    d = datasets.merge(upsym, downsym)
    
    # calculate R(0)
    d = d.sort("H")
    d0 = d.mask(np.abs(d["H"]) < zero_H)
    R0 = np.mean(d0["R"])
    n = d0["R"].shape[0]
    err2  = np.std(d0["R"]) / np.sqrt(n-1)
    
    d = d.mask(np.abs(d["H"]) <= H1)    
    d["mr"] = d["R"] / R0 - 1.0
    #d.errors["mr"] = np.sqrt(np.square(d.errors["R"] / R0) + np.square(d["R"])*err2 / R0**4)
    d.errors["mr"] = (d.errors["R"] + err2) / R0
    
    sub.errorbar(d["H"]/ H_unit, d["mr"] / yunit, yerr= d.errors["mr"] / yunit, marker="x", color="#6b1799", linestyle="none", zorder=1)
    
    H = q["H"][q["T"] == 2.0][0]
    a = q["a"][q["T"] == 2.0][0]
    xs = np.arange(-H, H, dH)
    sub.plot(xs / H_unit, xs*xs*a / yunit, marker=None, color="#fae16e", linestyle="-", zorder=2)
    
    # Sub fig b
    sub = sub_b
    sub.text(0.9, 0.2, "(b)", transform=sub.transAxes, ha="right", va="center", size="large")
    
    sub.tick_params(axis='both', which='both', direction="in", pad=1, bottom=False, top=True, left=False, right=True, labelleft=False, labelright=True, labeltop=True, labelbottom=False)
    sub.set_xlabel(r"$H$ (T $/\mu_0$)")
    sub.set_ylabel(r"$\Delta{}R(H) / R(0) / 10^{-2}$")
    sub.xaxis.set_label_position("top")
    sub.yaxis.set_label_position("right")
    sub.set_xlim(xlim)
    yunit = 0.01
    
    xminor_locator = AutoMinorLocator(5)
    sub.xaxis.set_minor_locator(xminor_locator)
    yminor_locator = AutoMinorLocator(5)
    sub.yaxis.set_minor_locator(yminor_locator)
        
    fn = r"data/20121022_08_RvH_30K_Ch1.10P.Al2O3.InterXX_Ch2.10Pa.EuS10.Al2O3.InterXX_Ch3.10Pb.EuS10.Al2O3.InterXX.dat"
    ch = 1
    data = ppmsana.import_dc(fn)[ch]
    
    corrected = tdrift.linear(data, "R", data["time"][0], data["R"][0], data["time"][-1], data["R"][-1])
    down, up = transport.split_MR_down_up(corrected)
  
    upsym = transport.symmetrize_MR(up, down)
    downsym = transport.symmetrize_MR(down, up)
    
    d = datasets.merge(upsym, downsym)
    
    # calculate R(0)
    d = d.sort("H")
    d0 = d.mask(np.abs(d["H"]) < zero_H)
    R0 = np.mean(d0["R"])
    n = d0["R"].shape[0]
    err2  = np.std(d0["R"]) / np.sqrt(n-1)
    
    d = d.mask(np.abs(d["H"]) <= H1)    
    d["mr"] = d["R"] / R0 - 1.0
    #d.errors["mr"] = np.sqrt(np.square(d.errors["R"] / R0) + np.square(d["R"])*err2 / R0**4)
    d.errors["mr"] = (d.errors["R"] + err2) / R0
    
    sub.errorbar(d["H"]/ H_unit, d["mr"] / yunit, yerr= d.errors["mr"] / yunit, marker="x", color="#e61717", linestyle="none", zorder=1)
    
    H = q["H"][q["T"] == 30.0][0]
    a = q["a"][q["T"] == 30.0][0]
    xs = np.arange(-H, H, dH)
    sub.plot(xs / H_unit, xs*xs*a / yunit, marker=None, color="k", linestyle="-", zorder=2)
    
    # Sub fig c
    sub = sub_c
    sub.text(0.9, 0.8, "(c)", transform=sub.transAxes, ha="right", va="center", size="large")
    
    sub.tick_params(axis='both', which='both', direction="in", pad=1, bottom=True, top=False, left=True, right=False, labelleft=True, labelright=False, labeltop=False, labelbottom=True)
    sub.set_xlabel("$T / \mathrm{K}$")
    sub.set_ylabel("$a / (\mu_0 / \mathrm{T})^{2}$")
    sub.xaxis.set_label_position("bottom")
    sub.yaxis.set_label_position("left")
    
    xminor_locator = AutoMinorLocator(5)
    sub.xaxis.set_minor_locator(xminor_locator)
    yminor_locator = AutoMinorLocator(5)
    sub.yaxis.set_minor_locator(yminor_locator)
        
    fn1 = r"data/quadraticVar.dat"
    d = datasets.load_csv(fn1, columns, has_header=False)
    #d = d.mask(d["T"] >= 10)
    yunit= 1.e-8
    #print(d)
    sub.errorbar(d["T"], d["a"] / yunit, yerr= d["err"] / yunit * NSE, marker="x", color="#1f4299", markersize=marker_size, markerfacecolor="none", linestyle="none")
    
    
    # Sub fig d
    sub = sub_d
    sub.text(0.9, 0.8, "(d)", transform=sub.transAxes, ha="right", va="center", size="large")
    
    sub.tick_params(axis='both', which='both', direction="in", pad=1, bottom=True, top=False, left=False, right=True, labelleft=False, labelright=True, labeltop=False, labelbottom=True)
    sub.set_xlabel("$T / \mathrm{K}$")
    sub.set_ylabel("$a / (\mu_0 / \mathrm{T})^{2} / 10^{-3}$")
    sub.xaxis.set_label_position("bottom")
    sub.yaxis.set_label_position("right")
    
    xminor_locator = AutoMinorLocator(5)
    sub.xaxis.set_minor_locator(xminor_locator)
    yminor_locator = AutoMinorLocator(5)
    sub.yaxis.set_minor_locator(yminor_locator)
        
    #fn1 = r"data/quadraticVar.dat"
    #d = datasets.load_csv(fn1, columns, has_header=False)
    d = d.mask(d["T"] >= 10)
    yunit= 1.e-8 * 0.001
    #print(d)
    sub.errorbar(d["T"], d["a"] / yunit, yerr= d["err"] / yunit * NSE, marker="x", color="#1f4299", markersize=marker_size, markerfacecolor="none", linestyle="none")
    
    fig.set_tight_layout(tight)
    #fig.savefig(r'quadratic_out.svg', format='svg')
    fig.savefig(r'quadratic.pdf', format='pdf')