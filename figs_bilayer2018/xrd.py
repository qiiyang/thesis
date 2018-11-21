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


tight = {"pad": 0.3, "h_pad": 0.0, "w_pad": 0.0}


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
    plt.rc('font', family='Times New Roman')
    plt.rc('font', size=12)
    plt.rc('ps', usedistiller="xpdf")
    
    paperwidth = 8.5
    fig = plt.figure(dpi=1200)
    p = 0.62
    fig.set_size_inches([p * paperwidth, 0.2/0.4* p * paperwidth])
    
    # Sub figure layout
    gs1 = gridspec.GridSpec(1, 1)
    gs1.update(wspace=0.0, hspace=0.0)
    
    sub_a = fig.add_subplot(gs1[0, 0])
    
    # Sub fig a
    #post_process = mean_filter
    post_process = gaus_slope
    
    # text
    #sub_a.text(0.02, 0.9, "(a)", transform=sub_a.transAxes, ha="left", size="large")
    
    sub_a.text(3.2, 8.5e3, "S1", ha="left", va="center", color=pal.xrd1)
    sub_a.text(3.2, 4.7e3, "S2", ha="left", va="center", color=pal.xrd2)
    sub_a.text(3.2, 3e3, "S3", ha="left", va="center", color=pal.xrd3)
    sub_a.text(3.2, 2e3, "S4", ha="left", va="center", color=pal.xrd4)
    sub_a.text(3.2, 1.4e3, "EuS", ha="left", va="center", color=pal.xrd_eus, bbox=dict(facecolor="#ffffff", edgecolor='none', pad=0))
    
    # peak labels
    sub_a.text(9.0, 9e2, "003", ha="left", va="center", color=pal.xrd_peak_label)
    sub_a.text(17.76, 9e2, "006", ha="left", va="center", color=pal.xrd_peak_label)
    sub_a.text(26.6, 9e2, "009", ha="left", va="center", color=pal.xrd_peak_label)
    sub_a.text(44.3, 9e2, "0015", ha="right", va="center", color=pal.xrd_peak_label)
    sub_a.text(53.85, 9e2, "0018", ha="right", va="center", color=pal.xrd_peak_label)
    
    
    # peak references
    sub_a.axvline(x=8.7024, linestyle="--", color=pal.xrd_peak_label, linewidth=1, zorder=1) # 003
    sub_a.axvline(x=17.4555, linestyle="--", color=pal.xrd_peak_label, linewidth=1, zorder=1)    # 006
    sub_a.axvline(x=26.3127, linestyle="--", color=pal.xrd_peak_label, linewidth=1, zorder=1)    # 009
    #sub_a.axvline(x=35.3333, linestyle="--", color=pal.xrd_peak_label, linewidth=1, zorder=1)   # 0012
    sub_a.axvline(x=44.5868, linestyle="--", color=pal.xrd_peak_label, linewidth=1, zorder=1)    # 0015
    sub_a.axvline(x=54.1608, linestyle="--", color=pal.xrd_peak_label, linewidth=1, zorder=1)    # 0018
    
    sub_a.set_xlabel(r"$2\theta$ (degrees)", labelpad=2)
    sub_a.set_ylabel(r"$counts$ (arb. unit)", labelpad=2)
    
    #sub_a.tick_params('both', labelleft=False, direction="in", bottom=True, top=True, left=True, right=True)
    sub_a.tick_params('both', which="both", direction="in", bottom=True, top=True, left=True, right=True, labelbottom=True, labeltop=False)
    sub_a.xaxis.set_label_position("bottom")
    sub_a.set_xlim([2, 56])
    xminor_locator = AutoMinorLocator(10)
    sub_a.xaxis.set_minor_locator(xminor_locator)
    
    sub_a.set_yscale("log")
    sub_a.set_ylim([10**2.9, 10**4.3])
    #yminor_locator = AutoMinorLocator(5)
    #sub_a.yaxis.set_minor_locator(yminor_locator)
    
    column_map = {0: "2theta", 1: "counts"}
    
    # EuS
    
    fn1 = r"xrd\20170706_EuS12_Si_100_5d120d_hybrid.ASC"
    data = post_process(datasets.load_csv(fn1, column_map, has_header=False, delimiter=' ', skipinitialspace=True))
    sub_a.plot(data["2theta"], data["counts"] * 10.0**1.0, color=pal.xrd_eus, marker=None, linewidth=lw, label="EuS only", zorder=2)
    
    # S4 / SB02
    fn1 = r"xrd\20140319_Sb2Te3_EuS_Si100_SB02_xpert2_5d120d.ASC"
    data = post_process(datasets.load_csv(fn1, column_map, has_header=False, delimiter=' ', skipinitialspace=True))
    sub_a.plot(data["2theta"], data["counts"] * 10.0**0.65, color=pal.xrd4, marker=None, linewidth=lw, label="S4", zorder=2)
    
    # S3 / SB01
    fn1 = r"xrd\20140315_Sb2Te3_EuS_Si100_SB01_5d120d.ASC"
    data = post_process(datasets.load_csv(fn1, column_map, has_header=False, delimiter=' ', skipinitialspace=True))
    sub_a.plot(data["2theta"], data["counts"] * 10.0**1.51, color=pal.xrd3, marker=None, linewidth=lw, label="S3", zorder=2)
    
    # S2 / SB12
    fn1 = r"xrd\20140613_Sb2Te3_EuS_Si100_SB12_5d120d.ASC"
    data = post_process(datasets.load_csv(fn1, column_map, has_header=False, delimiter=' ', skipinitialspace=True))
    sub_a.plot(data["2theta"], data["counts"] * 10.0**1.65, color=pal.xrd2, marker=None, linewidth=lw, label="S2", zorder=2)
    
    # S1 / SB11
    fn1 = r"xrd\20140612_Sb2Te3_EuS_Si100_SB11_5d120d.ASC"
    data = post_process(datasets.load_csv(fn1, column_map, has_header=False, delimiter=' ', skipinitialspace=True))
    sub_a.plot(data["2theta"], data["counts"] * 10.0**1.9, color=pal.xrd1, marker=None, linewidth=lw, label="S1", zorder=2)
        
        
    fig.set_tight_layout(tight)
    
    fig.savefig(r'xrd.pdf', format='pdf')
    