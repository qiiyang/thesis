import csv, math

import numpy as np
import matplotlib.pyplot as plt

from elflab import datasets
from elflab.analysis import errors
import elflab.projects.ppms.analysis as ppmsana
import elflab.analysis.transport as transport
import elflab.analysis.temporal_drift as tdrift

fn = r"raw\20140615f_RvH_30K_Ch1SB11.3456_Ch2SB11.3456_Ch3OFF.csv"
ch = 0
out = r"s3_30K.csv"

columns = ["H", "mr"]

if __name__ == '__main__':

    data = ppmsana.import_dc(fn)[ch]
    
    corrected = tdrift.linear(data, "R", data["time"][0], data["R"][0], data["time"][-1], data["R"][-1])
    down, up = transport.split_MR_down_up(corrected)
  
    upsym = transport.symmetrize_MR(up, down)
    downsym = transport.symmetrize_MR(down, up)
    
    d = datasets.merge(upsym, downsym)
    
    a = d.mask(np.abs(d["H"]) <= 1.e4)
    b = d.mask(np.abs(d["H"]) > 1.e4)
    
    a = datasets.consolidate(a, "H", 200, np.nanmean, errors.from_samples)
    b = datasets.consolidate(b, "H", 1000, np.nanmean, errors.from_samples)
    d = datasets.merge(a, b).sort("H")
    
    # calculate R(0)
    R0 = d.interpolator("H", "R")(0.)
    print(R0)
    err2 = d.error2_interpolator("H", "R")(0.)
    
    
    d["mr"] = d["R"] / R0 - 1.0
    d.errors["mr"] = np.sqrt(np.square(d.errors["R"] / R0) + np.square(d["R"])*err2 / R0**4)
    
    datasets.save_csv(d, out, columns = columns)
    
    plt.errorbar(d["H"], d["mr"], yerr= d.errors["mr"] * 2, marker="x", color="b", linestyle="none")
    
    #plt.legend(("Re($V_{out}$)", "Im($V_{out}$)"))
    plt.xlabel("$H$ / Oe")
    plt.ylabel("$R / \Omega$")

    plt.show()