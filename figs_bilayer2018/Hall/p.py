import csv

import numpy as np
import matplotlib.pyplot as plt

import elflab.projects.ppms.analysis as ppmsana
import elflab.analysis.transport as transport

from elflab import datasets
import elflab.analysis.signal_processing as signal


tight = dict({"pad": 0.5})

columns = ("H", "R")


if __name__ == '__main__':
    H_step = 5000.0
    H_start = -H_step / 2.0

    fig = plt.figure()
    ax = fig.add_subplot(212)
    
    ax.set_xlabel("$H$ / Oe")
    ax.set_ylabel("$R_{xy} / \Omega$")
    ax.set_xlim([H_start, 90000.])
    #plt.ylim([-50., 700])
    
    
    """
    # BL3 / 10PEuS10

    fn = r"raw\20121023_01_RvH_2K_Ch1.10P.Al2O3.InterXY_Ch2.10Pa.EuS10.Al2O3.InterXY_Ch3.10Pb.EuS10.Al2O3.InterXY.dat"
    data = ppmsana.import_dc(fn)[1]
    down, up = transport.split_MR_down_up(data)
  
    upsym = transport.antisymmetrize_MR(up, down)
    downsym = transport.antisymmetrize_MR(down, up)

    plt.plot(upsym["H"], -upsym["R"], linestyle='None', color="C0", marker="+", label="BL3")
    plt.plot(downsym["H"], -downsym["R"], linestyle='None', color="C0", marker="+")
    """
    

    # S4 / SB02

    fn = r"raw\20140321_01_RvH_2K_Ch1SB01.Rxy1423_Ch2SB02.Rxy1423_Ch3SB02.Rxy2314.dat"
    data = ppmsana.import_dc(fn)[1]
    down, up = transport.split_MR_down_up(data)
  
    upsym = transport.antisymmetrize_MR(up, down)
    downsym = transport.antisymmetrize_MR(down, up)
    
    mask = upsym["H"] >= H_start
    a = upsym.mask(mask)
    mask = downsym["H"] >= H_start
    b = downsym.mask(mask)
    
    c = datasets.merge(a, b)  
    
    averager, err_est = signal.decorrelate_neighbour_averager(4, np.nanmean, estimate_error=True)
    d = datasets.consolidate(c, "H", H_step, averager, error_est=err_est)

    ax.errorbar(d["H"], d["R"], yerr=d.errors["R"] * 2, linestyle='None', color="C0", marker="x", label="S4")
    #ax.plot(d["H"], d["R"], linestyle='None', color="C1", marker="x", label="S1")
    
    out = "s4.dat"
    datasets.save_csv(d, out, columns=columns)

    # S3 / SB01

    fn = r"raw\20140321_01_RvH_2K_Ch1SB01.Rxy1423_Ch2SB02.Rxy1423_Ch3SB02.Rxy2314.dat"
    data = ppmsana.import_dc(fn)[0]
    down, up = transport.split_MR_down_up(data)
  
    upsym = transport.antisymmetrize_MR(up, down)
    downsym = transport.antisymmetrize_MR(down, up)
    
    mask = upsym["H"] >= H_start
    a = upsym.mask(mask)
    mask = downsym["H"] >= H_start
    b = downsym.mask(mask)
    
    c = datasets.merge(a, b) 
    
    averager, err_est = signal.decorrelate_neighbour_averager(4, np.nanmean, estimate_error=True) 
    d = datasets.consolidate(c, "H", H_step, averager, error_est=err_est)

    ax.errorbar(d["H"], d["R"], yerr=d.errors["R"] * 2, linestyle='None', color="C1", marker="x", label="S3")
    #ax.plot(d["H"], d["R"], linestyle='None', color="C1", marker="x", label="S1")
    
    out = "s3.dat"
    datasets.save_csv(d, out, columns=columns)

    # S2 / SB12

    fn = r"raw\20140618a_RvH_2K9T_Ch1SB11.3645_Ch2SB12.3645_Ch3OFF.dat"
    data = ppmsana.import_dc(fn)[1]
    down, up = transport.split_MR_down_up(data)
  
    upsym = transport.antisymmetrize_MR(up, down)
    downsym = transport.antisymmetrize_MR(down, up)
    
    mask = upsym["H"] >= H_start
    a = upsym.mask(mask)
    mask = downsym["H"] >= H_start
    b = downsym.mask(mask)
    
    c = datasets.merge(a, b)  
    
    fn = r"raw\20140618a_RvH_2K9T_Ch1SB11.3645_Ch2SB12.3645_Ch3OFF.dat"
    data = ppmsana.import_dc(fn)[1]
    down, up = transport.split_MR_down_up(data)
  
    upsym = transport.antisymmetrize_MR(up, down)
    downsym = transport.antisymmetrize_MR(down, up)
    
    mask = upsym["H"] >= H_start
    a = upsym.mask(mask)
    mask = downsym["H"] >= H_start
    b = downsym.mask(mask)

    c = datasets.merge(c, a)
    c = datasets.merge(c, b)
    
    fn = r"raw\20140618b_RvH_2K9T_Ch1SB11.3645_Ch2SB12.3645_Ch3OFF.dat"
    data = ppmsana.import_dc(fn)[1]
    down, up = transport.split_MR_down_up(data)
  
    upsym = transport.antisymmetrize_MR(up, down)
    downsym = transport.antisymmetrize_MR(down, up)
    
    mask = upsym["H"] >= H_start
    a = upsym.mask(mask)
    mask = downsym["H"] >= H_start
    b = downsym.mask(mask)

    c = datasets.merge(c, a)
    c = datasets.merge(c, b)
    
    fn = r"raw\20140618d_rvh_2k9t_ch1sb11.3645_ch2sb12.3645_ch3off.dat"
    data = ppmsana.import_dc(fn)[1]
    down, up = transport.split_MR_down_up(data)
  
    upsym = transport.antisymmetrize_MR(up, down)
    downsym = transport.antisymmetrize_MR(down, up)
    
    mask = upsym["H"] >= H_start
    a = upsym.mask(mask)
    mask = downsym["H"] >= H_start
    b = downsym.mask(mask)

    c = datasets.merge(c, a)
    c = datasets.merge(c, b)
    
    averager, err_est = signal.decorrelate_neighbour_averager(16, np.nanmean, estimate_error=True)
    d = datasets.consolidate(c, "H", H_step, averager, error_est=err_est)

    ax.errorbar(d["H"], d["R"], yerr=d.errors["R"] * 2, linestyle='None', color="C2", marker="x", label="S2")
    #ax.plot(c["H"], c["R"], linestyle='None', color="C3", marker="x", label="S2'")
    
    out = "s2.dat"
    datasets.save_csv(d, out, columns=columns)

    
    # S1 / SB11
    ax2 = fig.add_subplot(211)
    
    ax2.set_xlabel("$H$ / Oe")
    ax2.set_ylabel("$R_{xy} / \Omega$")
    ax2.set_xlim([H_start, 90000.])

    fn = r"raw\20140618a_RvH_2K9T_Ch1SB11.3645_Ch2SB12.3645_Ch3OFF.dat"
    data = ppmsana.import_dc(fn)[0]
    down, up = transport.split_MR_down_up(data)
  
    upsym = transport.antisymmetrize_MR(up, down)
    downsym = transport.antisymmetrize_MR(down, up)
    
    a = upsym
    b = downsym
    
    c = datasets.merge(a, b)  
    
    fn = r"raw\20140618a_RvH_2K9T_Ch1SB11.3645_Ch2SB12.3645_Ch3OFF.dat"
    data = ppmsana.import_dc(fn)[0]
    down, up = transport.split_MR_down_up(data)
  
    upsym = transport.antisymmetrize_MR(up, down)
    downsym = transport.antisymmetrize_MR(down, up)
    
    a = upsym
    b = downsym

    c = datasets.merge(c, a)
    c = datasets.merge(c, b)
    
    fn = r"raw\20140618b_RvH_2K9T_Ch1SB11.3645_Ch2SB12.3645_Ch3OFF.dat"
    data = ppmsana.import_dc(fn)[0]
    down, up = transport.split_MR_down_up(data)
  
    upsym = transport.antisymmetrize_MR(up, down)
    downsym = transport.antisymmetrize_MR(down, up)
    
    a = upsym
    b = downsym

    c = datasets.merge(c, a)
    c = datasets.merge(c, b)
    
    fn = r"raw\20140618d_rvh_2k9t_ch1sb11.3645_ch2sb12.3645_ch3off.dat"
    data = ppmsana.import_dc(fn)[0]
    down, up = transport.split_MR_down_up(data)
  
    upsym = transport.antisymmetrize_MR(up, down)
    downsym = transport.antisymmetrize_MR(down, up)
    
    a = upsym
    b = downsym

    c = datasets.merge(c, a)
    c = datasets.merge(c, b)
    
    params, cov = np.polyfit(c["H"], c["R"], 1, cov=True)
    
    a = params[0]
    b = params[1]
    print(params)
    
    ax2.plot(c["H"], c["R"], linestyle='None', color="#00ff0033", marker="x", label="S1'")
    
    reject = 250.0
    mask = np.logical_and(c["H"] >= H_start, np.abs(c["R"] - a * c["H"]) <= reject)
    c = c.mask(mask)
    
    averager, err_est = signal.decorrelate_neighbour_averager(16, np.nanmean, estimate_error=True)
    d = datasets.consolidate(c, "H", H_step, averager, error_est=err_est)

    ax2.errorbar(d["H"], d["R"], yerr=d.errors["R"] * 2, linestyle='None', color="C3", marker="x", label="S1")
    ax2.plot(c["H"], c["R"], linestyle='None', color="#00000033", marker="x", label="S1'")
    #ax.plot(c["H"], c["H"] * a, linestyle='-', color="b", marker=None, label="")
    
    #ax.errorbar(d["H"], d["R"], yerr=d.errors["R"] * 2, linestyle='None', color="C3", marker="x", label="S1")
    
    out = "s1.dat"
    datasets.save_csv(d, out, columns=columns)


    
    #fig.set_tight_layout(tight)
    
    plt.legend()
    
    plt.tight_layout()
    plt.show()