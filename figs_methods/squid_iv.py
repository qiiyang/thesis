import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['backend'] = 'PS'
rcParams['text.usetex'] = True
rcParams['text.latex.preamble'] = r'\usepackage{amssymb}'



if __name__ == '__main__':
    
    # Figure configs
    plt.rc('font', family='serif')
    plt.rc('font', size=12)
    plt.rc('ps', usedistiller="xpdf")
    
    paperwidth = 8.5
    fig = plt.figure(dpi=1200)
    fig.set_size_inches([0.5 * paperwidth, 0.35 * paperwidth])
        
    sub = fig.add_subplot(111)
    
    sub.set_xlabel(r"$V$")
    sub.set_ylabel(r"$I$")

    # Show ticks in the left and lower axes only    
    sub.tick_params(axis='both', which='both', direction="out", pad=5, bottom=False, top=False, left=False, right=False, labelleft=False, labelright=False, labeltop=False, labelbottom=False)
    
    #column_map = {0: "2theta", 1: "counts"}
    
    x1 = 1.0
    dx = 0.01
    a = 0.02
    
    sub.set_xlim([0, x1])
    sub.set_ylim([0, x1])
    
    xs = np.arange(0, x1, dx)
    ys = xs
    sub.plot(xs, ys, marker=None, linestyle='--', color="k")
    
    I0 = 0.1
    ys = np.arange(I0-dx, x1, dx)
    xs = - a / (ys - I0) + ys
    ys = ys[xs>=0]
    xs = xs[xs>=0]
    xs[0] = 0.0
    ys[0] = 0.0
    xs[1] = 0.0
    sub.plot(xs, ys, marker=None, linestyle='-', color="#2671b2", zorder=10)
    
    I0 = 0.35
    ys = np.arange(I0-dx, x1, dx)
    xs = - a / (ys - I0) + ys
    ys = ys[xs>=0]
    xs = xs[xs>=0]
    xs[0] = 0.0
    ys[0] = 0.0
    xs[1] = 0.0
    sub.plot(xs, ys, marker=None, linestyle='-', color="#f19101", zorder=11)
    
    #sub.axhline(y=0.5, linestyle='-', color="k")
    
    fig.tight_layout()
    
    #fig.savefig(r'squid_iv.pdf', format='pdf')
    fig.savefig(r'squid_iv.eps', format='eps')
    