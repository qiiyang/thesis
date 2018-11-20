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
    fig.set_size_inches([0.6 * paperwidth, 0.3 * paperwidth])
        
    sub = fig.add_subplot(111)
    
    sub.set_xlabel(r"$\Phi / \Phi_0$")
    yl = sub.set_ylabel(r"$I_c(\Phi)$")
    yl.set_rotation(0)

    sub.xaxis.set_label_position("bottom")
    #sub.xaxis.set_label_coords(1, 1.15)
    sub.yaxis.set_label_position("left")
    sub.yaxis.set_label_coords(0.45, 1.0)

    # Move left y-axis and bottim x-axis to centre, passing through (0,0)
    sub.spines['left'].set_position(('data', 0.0))
    sub.spines['bottom'].set_position(('data', 0.0))

    # Eliminate upper and right axes
    sub.spines['right'].set_color('none')
    sub.spines['top'].set_color('none')

    # Show ticks in the left and lower axes only    
    sub.tick_params(axis='both', which='both', direction="out", pad=5, bottom=True, top=False, left=False, right=False, labelleft=False, labelright=False, labeltop=False, labelbottom=True)
    
    column_map = {0: "2theta", 1: "counts"}
    
    xs = np.arange(-2.7, 2.7, 0.01)
    ys = np.abs(np.cos(xs * np.pi))
    
    #sub.set_yticks(np.arange(0.2, 1.1, 0.2))
    #sub.set_xticks([-2, -1, 1, 2])
    #sub.text(0, -0.1, "0", transform=sub.transData, ha="center", va="center")
    
    sub.plot(xs, ys, marker=None, linestyle='-', color="#2671b2")
    
    fig.tight_layout()
    
    fig.savefig(r'squid_ic.pdf', format='pdf')
    #fig.savefig(r'squid_ic.eps', format='eps')
    