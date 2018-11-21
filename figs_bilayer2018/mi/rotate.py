import numpy as np

import elflab.analysis.signal_processing as signal
import elflab.datasets as datasets

import matplotlib.pyplot as plt

fn = r"raw\20141215m_sb14_MI_0T_2K_300K_71kHz_1mA_300ms_ph0.csv"
out = r"0degree\0T_warm.csv"


degree = 0.


if __name__ == '__main__':
    d = datasets.load_csv(fn, column_mapping={0:"T", 1:"X", 2:"Y"}, has_header=False)
    
    # Rotate    
    d["X2"] = d["X"] * np.cos(degree / 180. * np.pi) + d["Y"] * np.sin(degree / 180. * np.pi)
    d["Y2"] = d["Y"] * np.cos(degree / 180. * np.pi) - d["X"] * np.sin(degree / 180. * np.pi)
    
    # Averaging methods take into account of correlation within 10 x time constant
    averager, err_est = signal.decorrelate_neighbour_averager(30, np.nanmean, estimate_error=True)
    
    d = datasets.downsample(d, 240, method=averager, error_est=err_est)
    
    fig, ax1 = plt.subplots()
    ax1.set_xlabel("$T$ / K")
    plot1 = ax1.errorbar(d["T"], d["X2"] / 1.e-6, 2.0 * d.errors["X2"] / 1.e-6, fmt='go', label="Re($V$)")
    ax1.set_ylabel('Re($V$) $\mu$V', color='g')
    
    ax2 = ax1.twinx()
    plot2 = ax2.errorbar(d["T"], d["Y2"] / 1.e-6, 2.0 * d.errors["Y2"] / 1.e-6, fmt='bx', label="Im($V$)")
    ax2.set_ylabel('Im($V$) $\mu$V', color='b')
    
    #plt.xlim([2,42])
    #ax1.set_ylim([1.77, 1.97])
    #ax2.set_ylim([-1.42, -1.18])
    datasets.save_csv(d, out, columns = ("T", "X2", "Y2"))
    
    
    plt.legend(handles=[plot1, plot2])
    
    plt.tight_layout()
    plt.show()