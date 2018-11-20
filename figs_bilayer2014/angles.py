NSE = 1.0 # Standard error multiplier

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
from elflab.analysis import errors
import elflab.projects.ppms.analysis as ppmsana
import elflab.analysis.transport as transport
import elflab.analysis.temporal_drift as tdrift

tight = {"pad": 0.3, "h_pad": 0.0, "w_pad": 0.0}

# Common parameters
H_unit = 1.e4
mr_unit = 0.01
ch = 1
zero_H = 200.0

lw = 2
lw2 = 1.5
mew2 = 1
H2 = 1.1e4
xlim = [-9, 9]
xlim2 = [-H2/H_unit, H2/H_unit]
dH1 = 500

def plot(fn, co, cos, ls, mk, label, subs):
    sub_a, sub_b, sub_c, sub_d = subs

    data = ppmsana.import_dc(fn)[ch]
    
    data = datasets.downsample(data, 3, np.nanmedian, error_est=errors.combined)
    corrected = tdrift.linear(data, "R", data["time"][0], data["R"][0], data["time"][-1], data["R"][-1])
    
    
    down, up = transport.split_MR_down_up(corrected)
  
    upsym = transport.symmetrize_MR(up, down)
    downsym = transport.symmetrize_MR(down, up)
    
    d = datasets.merge(upsym, downsym)
    
    d = d.sort("H")
    d0 = d.mask(np.abs(d["H"]) < zero_H)
    n = d0["R"].shape[0]
    #print(n)
    R0 = np.mean(d0["R"])
    err2  = errors.combined(d0["R"], d0.errors["R"])
    
    
    d["mr"] = d["R"] / R0 - 1.0
    d.errors["mr"] = (d.errors["R"] + err2) / R0
    d1 = datasets.consolidate(d, "H", dH1, np.nanmean, error_est=errors.combined)
    
    sub_a.plot(d1["H"] / H_unit, d1["mr"] / mr_unit, marker=None, color=co, linestyle=ls, lw = lw, label=label)
    sub_c.plot(d1["H"] / H_unit * cos, d1["mr"] / mr_unit, marker=None, color=co, linestyle=ls, lw = lw, label=label)
    
    d = d1.mask(np.abs(d1["H"]) < H2)
    sub_b.errorbar(d["H"] / H_unit, d["mr"] / mr_unit, yerr=d.errors["mr"] / mr_unit, marker=mk, markerfacecolor="none", color=co, linestyle="none", lw = lw2, mew=mew2, label=label)
        
    d = d1.mask(np.abs(d1["H"] * cos) < H2)
    sub_d.errorbar(d["H"] / H_unit * cos, d["mr"] / mr_unit, yerr=d.errors["mr"] / mr_unit, marker=mk, markerfacecolor="none", color=co, linestyle="none", lw = lw2, mew=mew2, label=label)
    


if __name__ == '__main__':
    #xticks = range(10, 42, 10)
    #xminorLocator = MultipleLocator(5)
    #xminor_locator = AutoMinorLocator(2)
    
    mi_columns = {0:"H", 1:"mr", 3:"err"}
    
    # Figure configs
    plt.rc('font', family='Times New Roman')
    plt.rc('font', size=12)
    plt.rc('ps', usedistiller="xpdf")
    
    paperwidth = 8.5
    fig = plt.figure(dpi=1200)
    fig.set_size_inches([0.8 * paperwidth, 0.26/0.4*0.8 * paperwidth])
    #fig.set_size_inches([3.375, 2.1])
    
    marker_size = 6
    
    # Sub figure layout
    gs1 = gridspec.GridSpec(2, 2)
    gs1.update(wspace=0.0, hspace=0.0)
    sub_a = fig.add_subplot(gs1[0, 0])
    sub_b = fig.add_subplot(gs1[0, 1])
    sub_c = fig.add_subplot(gs1[1, 0])
    sub_d = fig.add_subplot(gs1[1, 1])
    subs = (sub_a, sub_b, sub_c, sub_d)
    
    # Sub fig a
    sub = sub_a
    sub.text(0.15, 0.2, "(a)", transform=sub.transAxes, ha="right", va="center", size="large")
    
    sub.tick_params(axis='both', which='both', direction="in", bottom=False, top=True, left=True, right=False, labelleft=True, labelright=False, labeltop=True, labelbottom=False)
    sub.set_xlabel(r"$H (T / \mu_0)$")
    sub.set_ylabel(r"$\Delta R(H) / R(0) / 10^{-2}$")
    sub.xaxis.set_label_position("top")
    sub.xaxis.set_label_coords(1, 1.15)
    sub.yaxis.set_label_position("left")
    sub.yaxis.set_label_coords(-0.12, 0.0)
    
    sub.set_xlim(xlim)
    #sub.set_xticks(xticks)
    xminor_locator = AutoMinorLocator(5)
    sub.xaxis.set_minor_locator(xminor_locator)
    
    #sub.set_ylim([-15, 29])
    #sub.set_yticks(range(-10, 29, 10))
    yminor_locator = AutoMinorLocator(5)
    sub.yaxis.set_minor_locator(yminor_locator)
    
    # Sub fig b
    sub = sub_b
    sub.text(0.25, 0.8, "(b)", transform=sub.transAxes, ha="right", va="center", size="large")
    
    sub.tick_params(axis='both', which='both', direction="in", bottom=False, top=True, left=False, right=True, labelleft=False, labelright=True, labeltop=True, labelbottom=False)
    #sub.set_xlabel(r"$H (T / \mu_0)$")
    sub.set_ylabel(r"$\Delta R(H) / R(0) / 10^{-2}$")
    #sub.xaxis.set_label_position("top")
    #sub.xaxis.set_label_coords(1, 1.15)
    sub.yaxis.set_label_position("right")
    sub.yaxis.set_label_coords(1.19, 0.0)
    
    sub.set_xlim(xlim2)
    #sub.set_xticks(xticks)
    xminor_locator = AutoMinorLocator(10)
    sub.xaxis.set_minor_locator(xminor_locator)
    
    #sub.set_ylim([-15, 29])
    #sub.set_yticks(range(-10, 29, 10))
    yminor_locator = AutoMinorLocator(5)
    sub.yaxis.set_minor_locator(yminor_locator)
    
    # Sub fig c
    sub = sub_c
    sub.text(0.15, 0.2, "(c)", transform=sub.transAxes, ha="right", va="center", size="large")
    
    sub.tick_params(axis='both', which='both', direction="in", bottom=True, top=False, left=True, right=False, labelleft=True, labelright=False, labeltop=False, labelbottom=True)
    sub.set_xlabel(r"$H \cdot \cos(\theta^*) (T / \mu_0)$")
    #sub.set_ylabel(r"$\Delta R(H) / R(0) / 10^{-2}$")
    sub.xaxis.set_label_position("bottom")
    sub.xaxis.set_label_coords(1, -0.15)
    #sub.yaxis.set_label_position("left")
    #sub.yaxis.set_label_coords(-0.18, 0.5)
    
    sub.set_xlim(xlim)
    #sub.set_xticks(xticks)
    xminor_locator = AutoMinorLocator(5)
    sub.xaxis.set_minor_locator(xminor_locator)
    
    #sub.set_ylim([-15, 29])
    #sub.set_yticks(range(-10, 29, 10))
    yminor_locator = AutoMinorLocator(5)
    sub.yaxis.set_minor_locator(yminor_locator)
    
    # Sub fig d
    sub = sub_d
    sub.text(0.25, 0.8, "(d)", transform=sub.transAxes, ha="right", va="center", size="large")
    
    sub.tick_params(axis='both', which='both', direction="in", bottom=True, top=False, left=False, right=True, labelleft=False, labelright=True, labeltop=False, labelbottom=True)
    #sub.set_xlabel(r"$H (T / \mu_0)$")
    #sub.set_ylabel(r"$\Delta R(H) / R(0) / 10^{-2}$")
    #sub.xaxis.set_label_position("bottom")
    #sub.xaxis.set_label_coords(1, 1.15)
    #sub.yaxis.set_label_position("right")
    #sub.yaxis.set_label_coords(1.16, 0.5)
    
    sub.set_xlim(xlim2)
    #sub.set_xticks(xticks)
    xminor_locator = AutoMinorLocator(10)
    sub.xaxis.set_minor_locator(xminor_locator)
    
    #sub.set_ylim([-15, 29])
    #sub.set_yticks(range(-10, 29, 10))
    yminor_locator = AutoMinorLocator(5)
    sub.yaxis.set_minor_locator(yminor_locator)
    
    # 0d
    fn = r"angles/20130516_13_RvH_4K_0D_Ch1.temp_Ch2.11P.EuS11.Al2O3.xx_Ch3.11P.EuS11.Al2O3.xy.dat"
    co = "#6b1799"
    cos = np.cos(0.0 * np.pi / 180.0)
    ls = "-"
    mk = "o"
    label = r"$0^\circ$"
    plot(fn, co, cos, ls, mk, label, subs)
    
    
    # 30d
    fn = r"angles/20130516_11_RvH_4K_30D_Ch1.temp_Ch2.11P.EuS11.Al2O3.xx_Ch3.11P.EuS11.Al2O3.xy.dat"
    co = "#1f4299"
    cos = np.cos(27.0 * np.pi / 180.0)
    ls = "--"
    mk = "s"
    label = r"$30^\circ$"
    plot(fn, co, cos, ls, mk, label, subs)
    
    # 45d
    #fn = r"angles/20130516_10_RvH_4K_45D_Ch1.temp_Ch2.11P.EuS11.Al2O3.xx_Ch3.11P.EuS11.Al2O3.xy.dat"
    fn = r"angles/20130518_05_RvH_4K_225D_Ch1.temp_Ch2.11P.EuS11.Al2O3.xx_Ch3.11P.EuS11.Al2O3.xy.dat"
    co = "#12b812"
    cos = np.cos(42.0 * np.pi / 180.0)
    ls = "-"
    mk = "^"
    label = r"$45^\circ$"
    plot(fn, co, cos, ls, mk, label, subs)
    
    # 60d
    #fn = r"angles/20130516_09_RvH_4K_60D_Ch1.temp_Ch2.11P.EuS11.Al2O3.xx_Ch3.11P.EuS11.Al2O3.xy.dat"
    fn = r"angles/20130518_04_RvH_4K_240D_Ch1.temp_Ch2.11P.EuS11.Al2O3.xx_Ch3.11P.EuS11.Al2O3.xy.dat"
    co = "#e6c217"
    cos = np.cos(55.0 * np.pi / 180.0)
    ls = "--"
    mk = "v"
    label = r"$60^\circ$"
    plot(fn, co, cos, ls, mk, label, subs)
    
    # 70d
    #fn = r"angles/20130516_08_RvH_4K_70D_Ch1.temp_Ch2.11P.EuS11.Al2O3.xx_Ch3.11P.EuS11.Al2O3.xy.dat"
    fn = r"angles/20130518_03_RvH_4K_250D_Ch1.temp_Ch2.11P.EuS11.Al2O3.xx_Ch3.11P.EuS11.Al2O3.xy.dat"
    co = "#e67517"
    cos = np.cos(61.0 * np.pi / 180.0)
    ls = "-"
    mk = "d"
    label = r"$70^\circ$"
    plot(fn, co, cos, ls, mk, label, subs)
    
    # 89d
    #fn = r"angles/20130516_07_RvH_4K_90D_Ch1.temp_Ch2.11P.EuS11.Al2O3.xx_Ch3.11P.EuS11.Al2O3.xy.dat"
    fn = r"angles/20130518_02_RvH_4K_270D_Ch1.temp_Ch2.11P.EuS11.Al2O3.xx_Ch3.11P.EuS11.Al2O3.xy.dat"
    co = "#e61717"
    mk = "x"
    cos = np.cos(72.0 * np.pi / 180.0)
    ls = "--"
    label = r"$89^\circ$"
    plot(fn, co, cos, ls, mk, label, subs)
    
    #legend = sub_b.legend(title=r"$\theta=$", handlelength=1.5, handletextpad=0.5, ncol=1, loc='upper left', bbox_to_anchor=(1.25, 1.0))
    legend = sub_a.legend(title=r"$\theta=$", handlelength=1.5, handletextpad=0.5, ncol=1, loc='upper left', bbox_to_anchor=(2.25, 1.0))
    legend = sub_d.legend(handlelength=1.5, handletextpad=0.5, ncol=1, loc='upper left', bbox_to_anchor=(1.25, 1.0))
    fig.set_tight_layout(tight)
    
    fig.savefig(r'angles.pdf', format='pdf')