import csv, math

import numpy as np
import matplotlib.pyplot as plt

from elflab import datasets
from elflab.analysis import errors
import elflab.projects.ppms.analysis as ppmsana
import elflab.analysis.transport as transport
import elflab.analysis.temporal_drift as tdrift

fn = r"20121020_02_RvH_2K_Ch1.10P.Al2O3.InterXX_Ch2.10Pa.EuS10.Al2O3.InterXX_Ch3.10Pb.EuS10.Al2O3.InterXX.dat"
ch = 1

H1 = 5.e3
H2 = 5.e3

if __name__ == '__main__':

    data = ppmsana.import_dc(fn)[ch]
    
    corrected = tdrift.linear(data, "R", data["time"][0], data["R"][0], data["time"][-1], data["R"][-1])
    down, up = transport.split_MR_down_up(corrected)
  
    upsym = transport.symmetrize_MR(up, down)
    downsym = transport.symmetrize_MR(down, up)
    
    d = datasets.merge(upsym, downsym)
    
    #a = d.mask(np.abs(d["H"]) <= 1.e4)
    
    #a = datasets.consolidate(a, "H", 20, np.nanmean, errors.from_samples)
    #d = datasets.merge(a, b).sort("H")
    
    # calculate R(0)
    
    d = d.sort("H")
    R0 = d.interpolator("H", "R")(0.)
    #print(R0)
    err2 = d.error2_interpolator("H", "R")(0.)
    
    
    d = d.mask(np.abs(d["H"]) <= H2)
    d["mr"] = d["R"] / R0 - 1.0
    #d.errors["mr"] = np.sqrt(np.square(d.errors["R"] / R0) + np.square(d["R"])*err2 / R0**4)
    d.errors["mr"] = d.errors["R"] / R0
    
    xs = np.power(d["H"][np.abs(d["H"]) <= H1], 2)
    ys = d["mr"][np.abs(d["H"]) <= H1]
    ps, rsqs, _, _ = np.linalg.lstsq(np.array([xs,]).T, ys, rcond=None)
    p = ps[0]
    rsq = rsqs[0]
    std = np.std(xs)
    n = xs.shape[0]
    errsq = np.mean(d.errors["mr"]**2)
    #print (errsq, rsq / (n-1))
    dp = np.sqrt(rsq / (n-1) + errsq) / np.sqrt(n) / std
    print(p, ",", dp)
    
    plt.errorbar(d["H"], d["mr"], yerr= d.errors["mr"] * 2, marker="x", color="b", linestyle="none")
    plt.plot(d["H"], d["H"]*d["H"]*p, marker=None, color="k", linestyle="-")
    
    plt.xlabel("$H$ / Oe")
    plt.ylabel("$R / \Omega$")

    plt.show()