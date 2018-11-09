import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

rcParams['backend'] = 'PS'
rcParams['text.usetex'] = True
rcParams['text.latex.preamble'] = r'\usepackage{amssymb}'



if __name__ == '__main__':
    g = 0.5
    y0 = 0.0
    y1 = 1.0
    x1 = 1.0
    
    dx = 0.45
    
    n = 30
    
    
    # Figure configs
    plt.rc('font', family="Calibri")
    plt.rc('font', size=12)
    plt.rc('ps', usedistiller="xpdf")
    
    paperwidth = 8.5
    fig = plt.figure(dpi=1200)
    fig.set_size_inches([0.6 * paperwidth, 0.3 * paperwidth])
        
    sub = fig.add_subplot(111)
    
    sub.set_xlabel(r"$E$")
    #yl = sub.set_ylabel(r"$g(E)$")
    #yl.set_rotation(0)

    sub.xaxis.set_label_position("bottom")
    sub.xaxis.set_label_coords(1, -0.05)
    sub.yaxis.set_label_position("left")
    sub.yaxis.set_label_coords(0.45, 1.0)

    # Move left y-axis and bottim x-axis to centre, passing through (0,0)
    sub.spines['left'].set_position(('data', 0.0))
    sub.spines['bottom'].set_position(('data', 0.0))

    # Eliminate upper and right axes
    sub.spines['right'].set_color('none')
    sub.spines['top'].set_color('none')

    # Show ticks in the left and lower axes only    
    sub.tick_params(axis='both', which='both', direction="out", pad=5, bottom=False, top=False, left=False, right=False, labelleft=False, labelright=False, labeltop=False, labelbottom=False)
    
    
    #xs = np.arange(-2.7, 2.7, 0.01)
    #ys = np.abs(np.cos(xs * np.pi))
    
    #sub.set_yticks(np.arange(0.2, 1.1, 0.2))
    #sub.set_xticks([-2, -1, 1, 2])
    #sub.text(0, -0.1, "0", transform=sub.transData, ha="center", va="center")
    
    #sub.plot(xs, ys, marker=None, linestyle='-', color="#2671b2")
    
    sub.set_xlim([-x1, x1])
    sub.set_ylim([y0, y1])
    sub.axhline(y=g, linestyle='-', color="#2671b2")
    
    sub.axvline(x=dx, linestyle='--', color="k")
    sub.axvline(x=-dx, linestyle='--', color="k")
    
    xs = (np.random.ranf((n,)) - 0.5) * 2.0 * x1
    ys = np.ones(n) * 0.25
    ind = xs < 0.0
    sub.plot(xs[ind], ys[ind], marker='o', linestyle='none', color="#f19101", label="occupied")
    ind = xs >= 0.0
    sub.plot(xs[ind], ys[ind], marker='x', linestyle='none', color="#f19101", label="unoccupied")
    
    fig.legend()
    
    
    fig.tight_layout()
    
    #fig.savefig(r'mott_out.pdf', format='pdf')
    fig.savefig(r'mott_out.svg', format='svg')
    