import csv
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
    fig.set_size_inches([0.6 * paperwidth, 0.45 * paperwidth])
        
    sub = fig.add_subplot(111)
    
    sub.set_xlabel(r"sample position~(cm)")
    sub.set_ylabel(r"voltage~(V)")

    # Show ticks in the left and lower axes only    
    sub.tick_params(axis='both', which='both', direction="in", pad=5, bottom=True, top=True, left=True, right=True, labelleft=True, labelright=False, labeltop=False, labelbottom=True)
    
    # initialize lists for reading
    xl = []
    yl = []
    fl = []
    # reading data
    with open("lastscan.dat", "r", newline='') as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if (len(row) > 0) and (row[1] == ""):    # a valid data line only if the comment entry is ""
                try:
                    xl.append(float(row[7]))
                except ValueError:
                    xl.append(np.nan)
                    
                try:
                    yl.append(float(row[8]))
                except ValueError:
                    yl.append(np.nan)
                    
                try:
                    fl.append(float(row[12]))
                except ValueError:
                    fl.append(np.nan)
    
    #sub.axhline(y=0.5, linestyle='-', color="k")
    
    sub.plot(xl, yl, marker="x", linestyle="none", color="#2671b2")
    sub.plot(xl, fl, marker=None, linestyle="-", color="#f19101")
    
    fig.tight_layout()
    
    fig.savefig(r'lastscan.pdf', format='pdf')
    #fig.savefig(r'lastscan.eps', format='eps')
    