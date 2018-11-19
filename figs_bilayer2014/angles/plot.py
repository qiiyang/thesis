import csv, math

import numpy as np
import matplotlib.pyplot as plt

from elflab import datasets
from elflab.analysis import errors
import elflab.projects.ppms.analysis as ppmsana
import elflab.analysis.transport as transport
import elflab.analysis.temporal_drift as tdrift

ch = 1

zero_H = 200.0

if __name__ == '__main__':
    
    plt.xlabel("$H$ / Oe")
    plt.ylabel("$\Delta R(H)  / R(0)$")
    
    
    # 0d
    fn = r"20130516_13_RvH_4K_0D_Ch1.temp_Ch2.11P.EuS11.Al2O3.xx_Ch3.11P.EuS11.Al2O3.xy.dat"

    data = ppmsana.import_dc(fn)[ch]
    
    data = datasets.downsample(data, 3, np.nanmedian, error_est=errors.combined)
    corrected = tdrift.linear(data, "R", data["time"][0], data["R"][0], data["time"][-1], data["R"][-1])
    
    
    down, up = transport.split_MR_down_up(corrected)
  
    upsym = transport.symmetrize_MR(up, down)
    downsym = transport.symmetrize_MR(down, up)
    
    d = datasets.merge(upsym, downsym)
    
    d = d.sort("H")
    d0 = d.mask(np.abs(d["H"]) < zero_H)
    n = d0["R"].shape[0]
    #print(n)
    R0 = np.mean(d0["R"])
    err2  = np.std(d0["R"]) / np.sqrt(n-1)
    
    
    d["mr"] = d["R"] / R0 - 1.0
    d.errors["mr"] = (d.errors["R"] + err2) / R0
    d = datasets.downsample(d, 3, np.nanmean)
    
    plt.plot(d["H"], d["mr"], marker=None, color="#6b1799", linestyle="-", label="$0\degree$")
    
    
    # 30d
    fn = r"20130516_11_RvH_4K_30D_Ch1.temp_Ch2.11P.EuS11.Al2O3.xx_Ch3.11P.EuS11.Al2O3.xy.dat"

    data = ppmsana.import_dc(fn)[ch]
    
    data = datasets.downsample(data, 3, np.nanmedian, error_est=errors.combined)
    corrected = tdrift.linear(data, "R", data["time"][0], data["R"][0], data["time"][-1], data["R"][-1])
    
    
    down, up = transport.split_MR_down_up(corrected)
  
    upsym = transport.symmetrize_MR(up, down)
    downsym = transport.symmetrize_MR(down, up)
    
    d = datasets.merge(upsym, downsym)
    
    d = d.sort("H")
    d0 = d.mask(np.abs(d["H"]) < zero_H)
    n = d0["R"].shape[0]
    R0 = np.mean(d0["R"])
    err2  = np.std(d0["R"]) / np.sqrt(n-1)
    
    
    d["mr"] = d["R"] / R0 - 1.0
    d.errors["mr"] = (d.errors["R"] + err2) / R0
    d = datasets.downsample(d, 3, np.nanmean)
    
    plt.plot(d["H"] * np.cos(30.0 / 180.0 * np.pi), d["mr"], marker=None, color="#1f4299", linestyle="--", label="$30\degree$")
    
    
    # 45d
    fn = r"20130516_10_RvH_4K_45D_Ch1.temp_Ch2.11P.EuS11.Al2O3.xx_Ch3.11P.EuS11.Al2O3.xy.dat"

    data = ppmsana.import_dc(fn)[ch]
    
    data = datasets.downsample(data, 3, np.nanmedian, error_est=errors.combined)
    corrected = tdrift.linear(data, "R", data["time"][0], data["R"][0], data["time"][-1], data["R"][-1])
    
    
    down, up = transport.split_MR_down_up(corrected)
  
    upsym = transport.symmetrize_MR(up, down)
    downsym = transport.symmetrize_MR(down, up)
    
    d = datasets.merge(upsym, downsym)
    
    d = d.sort("H")
    d0 = d.mask(np.abs(d["H"]) < zero_H)
    n = d0["R"].shape[0]
    R0 = np.mean(d0["R"])
    err2  = np.std(d0["R"]) / np.sqrt(n-1)
    
    
    d["mr"] = d["R"] / R0 - 1.0
    d.errors["mr"] = (d.errors["R"] + err2) / R0
    d = datasets.downsample(d, 3, np.nanmean)
    
    plt.plot(d["H"] * np.cos(42.0 / 180.0 * np.pi), d["mr"], marker=None, color="#12b812", linestyle="-", label="$45\degree$")
    
    
    # 60d
    fn = r"20130516_09_RvH_4K_60D_Ch1.temp_Ch2.11P.EuS11.Al2O3.xx_Ch3.11P.EuS11.Al2O3.xy.dat"

    data = ppmsana.import_dc(fn)[ch]
    
    data = datasets.downsample(data, 3, np.nanmedian, error_est=errors.combined)
    corrected = tdrift.linear(data, "R", data["time"][0], data["R"][0], data["time"][-1], data["R"][-1])
    
    
    down, up = transport.split_MR_down_up(corrected)
  
    upsym = transport.symmetrize_MR(up, down)
    downsym = transport.symmetrize_MR(down, up)
    
    d = datasets.merge(upsym, downsym)
    
    d = d.sort("H")
    d0 = d.mask(np.abs(d["H"]) < zero_H)
    n = d0["R"].shape[0]
    R0 = np.mean(d0["R"])
    err2  = np.std(d0["R"]) / np.sqrt(n-1)
    
    
    d["mr"] = d["R"] / R0 - 1.0
    d.errors["mr"] = (d.errors["R"] + err2) / R0
    d = datasets.downsample(d, 3, np.nanmean)
    
    plt.plot(d["H"] * np.cos(54.0 / 180.0 * np.pi), d["mr"], marker=None, color="#e6c217", linestyle="--", label="$60\degree$")
    
    # 70d
    fn = r"20130516_08_RvH_4K_70D_Ch1.temp_Ch2.11P.EuS11.Al2O3.xx_Ch3.11P.EuS11.Al2O3.xy.dat"

    data = ppmsana.import_dc(fn)[ch]
    
    data = datasets.downsample(data, 3, np.nanmedian, error_est=errors.combined)
    corrected = tdrift.linear(data, "R", data["time"][0], data["R"][0], data["time"][-1], data["R"][-1])
    
    
    down, up = transport.split_MR_down_up(corrected)
  
    upsym = transport.symmetrize_MR(up, down)
    downsym = transport.symmetrize_MR(down, up)
    
    d = datasets.merge(upsym, downsym)
    
    d = d.sort("H")
    d0 = d.mask(np.abs(d["H"]) < zero_H)
    n = d0["R"].shape[0]
    R0 = np.mean(d0["R"])
    err2  = np.std(d0["R"]) / np.sqrt(n-1)
    
    
    d["mr"] = d["R"] / R0 - 1.0
    d.errors["mr"] = (d.errors["R"] + err2) / R0
    d = datasets.downsample(d, 3, np.nanmean)
    
    plt.plot(d["H"] * np.cos(63.0 / 180.0 * np.pi), d["mr"], marker=None, color="#e67517", linestyle="-", label="$70\degree$")
    
    # 90d
    fn = r"20130516_07_RvH_4K_90D_Ch1.temp_Ch2.11P.EuS11.Al2O3.xx_Ch3.11P.EuS11.Al2O3.xy.dat"

    data = ppmsana.import_dc(fn)[ch]
    
    data = datasets.downsample(data, 3, np.nanmedian, error_est=errors.combined)
    corrected = tdrift.linear(data, "R", data["time"][0], data["R"][0], data["time"][-1], data["R"][-1])
    
    
    down, up = transport.split_MR_down_up(corrected)
  
    upsym = transport.symmetrize_MR(up, down)
    downsym = transport.symmetrize_MR(down, up)
    
    d = datasets.merge(upsym, downsym)
    
    d = d.sort("H")
    d0 = d.mask(np.abs(d["H"]) < zero_H)
    n = d0["R"].shape[0]
    R0 = np.mean(d0["R"])
    err2  = np.std(d0["R"]) / np.sqrt(n-1)
    
    
    d["mr"] = d["R"] / R0 - 1.0
    d.errors["mr"] = (d.errors["R"] + err2) / R0
    d = datasets.downsample(d, 3, np.nanmean)
    
    plt.plot(d["H"] * np.cos(72.0 / 180.0 * np.pi), d["mr"], marker=None, color="#e61717", linestyle="--", label="$90\degree$")
    
    plt.legend()
    plt.show()