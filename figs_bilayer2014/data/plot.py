import csv, math

import numpy as np
import matplotlib.pyplot as plt

from elflab import datasets
from elflab.analysis import errors
import elflab.projects.ppms.analysis as ppmsana
import elflab.analysis.transport as transport
import elflab.analysis.temporal_drift as tdrift

fn = r"20121020_04_RvH_10K_Ch1.10P.Al2O3.InterXX_Ch2.10Pa.EuS10.Al2O3.InterXX_Ch3.10Pb.EuS10.Al2O3.InterXX.dat"
ch = 1

H0 = 5.e2
H1 = 5.e3

zero_H = 120.0

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
    
    d = d.mask(np.abs(d["H"]) <= H1).sort("H")
    #R0 = d.interpolator("H", "R")(0.)
    R0 = np.mean(d["R"][np.abs(d["H"]) < zero_H])
    #print(R0)
    err2 = d.error2_interpolator("H", "R")(0.)
    
    
    d["mr"] = d["R"] / R0 - 1.0
    #d.errors["mr"] = np.sqrt(np.square(d.errors["R"] / R0) + np.square(d["R"])*err2 / R0**4)
    d.errors["mr"] = d.errors["R"] / R0
    
    ratio = 2.0
    errsq = np.mean(d.errors["mr"]**2)
    mrsq = ratio * errsq + 1.0
    
    H2 = H1 * 3.0 / 2.0
    d0 = d
    while (mrsq > ratio * errsq) and (H2 > H0):
        H2 = H2 *2.0 / 3.0
        d = d.mask(np.abs(d["H"]) <= H2)
        xs = np.power(d["H"], 2)
        ys = d["mr"]
        ps, rsqs, _, _ = np.linalg.lstsq(np.array([xs,]).T, ys, rcond=None)
        n = xs.shape[0]
        p = ps[0]
        mrsq = rsqs[0] / (n-1)
        std = np.std(xs)
        errsq = np.mean(d.errors["mr"]**2)
    
    dp = np.sqrt(mrsq + errsq) / np.sqrt(n) / std
    print(p, ",", dp, ",", H2, ",")
    
    plt.errorbar(d0["H"], d0["mr"], yerr= d0.errors["mr"] * 2, marker="x", color="b", linestyle="none")
    plt.plot(d["H"], d["H"]*d["H"]*p, marker=None, color="k", linestyle="-")
    
    plt.xlabel("$H$ / Oe")
    plt.ylabel("$R / \Omega$")

    plt.show()