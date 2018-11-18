NSE = 2.0 # Standard error multiplier


import numpy as np

from matplotlib import rcParams, gridspec, ticker

rcParams['backend'] = 'Cairo'
rcParams['text.usetex'] = True
rcParams['text.latex.preamble'] = r'\usepackage{amssymb}'

import matplotlib.pyplot as plt
from matplotlib.ticker import AutoMinorLocator

from elflab import constants, datasets
import elflab.projects.ppms.analysis as ppmsana

vdp = constants.pi / constants.ln2  # van der Pauw prefix
quantum_resistance = constants.h / constants.e / constants.e # h/e^2


columns = {0:"T", 1:"a", 2:"err"}



if __name__ == '__main__':    
    # Figure configs
    plt.rc('font', family='serif')
    plt.rc('font', size=12)
    plt.rc('ps', usedistiller="xpdf")
    
    paperwidth = 8.5
    fig = plt.figure(dpi=1200)
    fig.set_size_inches([0.95 * paperwidth, 0.3/0.4*0.95 * paperwidth])
    #fig.set_size_inches([3.375, 2.1])
    
    marker_size = 6
    
    # Sub figure layout
    gs1 = gridspec.GridSpec(2, 2)
    gs1.update(wspace=0.0, hspace=0.0)
    sub_a = fig.add_subplot(gs1[0, 0])
    sub_b = fig.add_subplot(gs1[0, 1])
    sub_c = fig.add_subplot(gs1[1, 0:2])
    #sub_d = fig.add_subplot(gs1[1, 1])
    
    # Sub fig a
    sub = sub_a
    sub.text(0.9, 0.2, "(a)", transform=sub.transAxes, ha="right", va="center")
    
    sub.tick_params(axis='both', which='both', direction="in", pad=1, bottom=False, top=True, left=True, right=False, labelleft=True, labelright=False, labeltop=True, labelbottom=False)
    sub.set_xlabel(r"$H$ (T $/\mu_0$)")
    sub.set_ylabel(r"$\Delta{}R(H) / R(0) (\%)$")
        
    fn1 = r"data/quadratic5kOe.dat"
    d = datasets.load_csv(fn1, columns, has_header=False)
    d = d.mask(d["T"] >= 7)
    yunit= 1.e-8
    #print(d)
    sub.errorbar(d["T"], d["a"] / yunit, yerr= d["err"] / yunit * NSE, marker="x", markersize=marker_size, markerfacecolor="none", linestyle="none")
    
    # Sub fig c
    sub = sub_c
    sub.text(0.9, 0.2, "(c)", transform=sub.transAxes, ha="right", va="center")
    
    sub.set_xlabel("$T / \mathrm{K}$")
    sub.set_ylabel("$a$")
        
    fn1 = r"data/quadratic5kOe.dat"
    d = datasets.load_csv(fn1, columns, has_header=False)
    d = d.mask(d["T"] >= 7)
    yunit= 1.e-8
    #print(d)
    sub.errorbar(d["T"], d["a"] / yunit, yerr= d["err"] / yunit * NSE, marker="x", markersize=marker_size, markerfacecolor="none", linestyle="none")
    
    
    
    fig.set_tight_layout(True)
    #fig.savefig(r'quadratic.svg', format='svg')
    fig.savefig(r'quadratic.pdf', format='pdf')