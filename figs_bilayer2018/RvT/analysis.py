import csv

import numpy as np
from matplotlib import rcParams
#rcParams['backend'] = 'PS'
rcParams['text.usetex'] = True
rcParams['text.latex.preamble'] = r'\usepackage{amssymb}'
import matplotlib.pyplot as plt

import elflab.projects.ppms.analysis as ppmsana
import elflab.analysis.transport as transport
from elflab import constants, datasets

tight = dict({"pad": 0.5})

vdp = constants.pi / constants.ln2  # van der Pauw prefix
quantum_resistance = constants.h / constants.e / constants.e # h/e^2



#outf = r"SB11RvT"

if __name__ == '__main__':
    columns = ("T", "Rs", "err_Rs")
    
    #plt.rc('font', family='serif')
    #plt.rc('lines', linewidth=2, antialiased=True)
    #plt.rc('ps', usedistiller="xpdf")
    
    #fig = plt.figure(figsize=(3.375, 2.1), dpi=1200)
    fig = plt.figure()
    ax = fig.add_subplot(111)
    
    ax.set_xscale("log")
    ax.set_yscale("log")
    ax.set_xlabel(r"$T \mathrm{(K)}$")
    ax.set_ylabel(r"$R_{\Box} (h/e^2)$")
    """
    # BL3 / 10P
    fn1 = "20121020_01_RvT_down_Ch1.10P.Al2O3.InterXX_Ch2.10Pa.EuS30.Al2O3.InterXX_Ch3.10Pb.EuS30.Al2O3.InterXX.dat"
    data = ppmsana.import_dc(fn1)[1]
    ax.plot(data["T"], data["R"] * vdp / quantum_resistance, "rx", label="BL3")
    """
    
    # S4 / SB02
    fn1 = r"raw\20140320_01_RvT_down_Ch1SB01.Rxx1234_Ch2NONE_Ch3SB02.Rxx1234.csv"
    fn2 = r"raw\20140323_01_RvT_up_Ch1SB01.Rxx1324_Ch2NONE_Ch3SB02.Rxx1324.csv"
    out = r"S4.dat"
    
    down = ppmsana.import_dc(fn1)[2]
    up = ppmsana.import_dc(fn2)[2]
    data = transport.van_der_Pauw_set(down, up, "T")
    data["Rs"] = data["R"] / quantum_resistance
    data["err_Rs"] = data.errors["R"] / quantum_resistance
    data.errors = None
    datasets.save_csv(data, out, columns = columns)
    
    ax.plot(data["T"], data["Rs"], linestyle='None', color="C3", marker="v", label="S4")
    
    
    # S3 / SB01
    fn1 = r"raw\20140320_01_RvT_down_Ch1SB01.Rxx1234_Ch2NONE_Ch3SB02.Rxx1234.csv"
    fn2 = r"raw\20140323_01_RvT_up_Ch1SB01.Rxx1324_Ch2NONE_Ch3SB02.Rxx1324.csv"
    out = r"S3.dat"
    
    down = ppmsana.import_dc(fn1)[0]
    up = ppmsana.import_dc(fn2)[0]
    data = transport.van_der_Pauw_set(down, up, "T")
    data["Rs"] = data["R"] / quantum_resistance
    data["err_Rs"] = data.errors["R"] / quantum_resistance
    data.errors = None
    datasets.save_csv(data, out, columns = columns)
    
    ax.plot(data["T"], data["Rs"], linestyle='None', color="C0", marker="x", label="S3")
    
    
    # S2 / SB12
    fn1 = r"raw\20140615a_RvT_down_Ch1SB11.3456_Ch2SB11.3456_Ch3SB12.3645.csv"
    out = r"S2.dat"
    data = ppmsana.import_dc(fn1)[1]
    data["Rs"] = data["R"] * vdp / quantum_resistance
    data["err_Rs"] = data.errors["R"] * vdp / quantum_resistance
    data.errors = None
    datasets.save_csv(data, out, columns = columns)
    ax.plot(data["T"], data["Rs"], linestyle='None', color="C1", marker="o", label="S2")
    
        
    # S1 / SB11
    fn1 = r"raw\20140615a_RvT_down_Ch1SB11.3456_Ch2SB11.3456_Ch3SB12.3645.csv"
    out = r"S1.dat"
    data = ppmsana.import_dc(fn1)[0]
    data["Rs"] = data["R"] * vdp / quantum_resistance
    data["err_Rs"] = data.errors["R"] * vdp / quantum_resistance
    data.errors = None
    datasets.save_csv(data, out, columns = columns)
    ax.plot(data["T"], data["Rs"], linestyle='None', color="C2", marker="^", label="S1")
    
    plt.legend()
    
    fig.set_tight_layout(tight)
    plt.show()
    #fig.savefig('temp.pdf', format='pdf')
    