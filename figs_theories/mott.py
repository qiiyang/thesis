import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['backend'] = 'PS'
rcParams['text.usetex'] = True
rcParams['text.latex.preamble'] = r'\usepackage{amssymb}'



if __name__ == '__main__':
    y1 = 1.0
    x1 = 1.0
    de0 = 0.3
    de1 = 0.5
    
    n = 120
    
    
    # Figure configs
    #plt.rc('font', family="Calibri")
    plt.rc('font', size=12)
    plt.rc('ps', usedistiller="xpdf")
    
    paperwidth = 8.5
    fig = plt.figure(dpi=1200)
    fig.set_size_inches([0.6 * paperwidth, 0.6 * paperwidth])
        
    sub = fig.add_subplot(111)
    
    sub.set_xlabel(r"$x$", fontsize="large")
    sub.set_ylabel(r"energy", fontsize="large")

    # Show ticks in the left and lower axes only    
    sub.tick_params(axis='both', which='both', direction="out", pad=5, bottom=False, top=False, left=False, right=False, labelleft=False, labelright=False, labeltop=False, labelbottom=False)
    
    
    #xs = np.arange(-2.7, 2.7, 0.01)
    #ys = np.abs(np.cos(xs * np.pi))
    
    #sub.set_yticks(np.arange(0.2, 1.1, 0.2))
    #sub.set_xticks([-2, -1, 1, 2])
    #sub.text(0, -0.1, "0", transform=sub.transData, ha="center", va="center")
    
    #sub.plot(xs, ys, marker=None, linestyle='-', color="#2671b2")
    
    sub.set_xlim([-x1, x1])
    sub.set_ylim([-y1, y1])
    
    sub.axhline(y=0.0, linestyle='-', color="k")
    sub.axhline(y=de0, linestyle='--', color="k")
    sub.axhline(y=-de0, linestyle='--', color="k")
    sub.axhline(y=de1, linestyle='--', color="#2671b2")
    sub.axhline(y=-de1, linestyle='--', color="#2671b2")
    
    xs = (np.random.ranf((n,)) - 0.5) * 2.0 * x1
    ys = (np.random.ranf((n,)) - 0.5) * 2.0 * y1
    ind = ys < 0.0
    sub.plot(xs[ind], ys[ind], marker='x', linestyle='none', color="#f19101", label="filled states")
    ind = ys >= 0.0
    sub.plot(xs[ind], ys[ind], marker='o', linestyle='none', markerfacecolor="none", color="#f19101", label="empty states")
    
    l = fig.legend(loc="upper right", framealpha=1.0)
    
    
    
    fig.tight_layout()
    
    #fig.savefig(r'mott_out.pdf', format='pdf')
    fig.savefig(r'mott_out.svg', format='svg')
    