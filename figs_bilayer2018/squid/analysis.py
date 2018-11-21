SQUID_COLUMNS = ["time","T", "H","M","err_M"]

import numpy as np
from scipy.optimize import curve_fit

import matplotlib.pyplot as plt

import elflab.projects.mpms.analysis as mpms
from elflab import datasets

def vs_temperature():
    out = r"MvT.dat"

    fn1 = r"20141216_04_SB12_OoS_MvT_up.rso.dat"
    data = mpms.loadfile_rso(fn1)
    
    # linear regression
    mask = data["T"] > 50.
    x = data["T"][mask]
    y = data["M"][mask]
    N = len(x)
    
    params, cov = np.polyfit(x,y, 1, cov=True)
    print("data points used in regression: N = \n{}\nslope, intercept:\n".format(N))
    print(params)
    print("\ncovariance matrix:\n")
    print(cov)
    
    a = params[0]
    b = params[1]
    
    va = cov[0][0]
    vb = cov[1][1]
    vab = cov[0][1]
    
    data["M"] = data["M"] - a * data["T"] - b
    data["err_M"] = np.sqrt(data["err_M"]**2 + (va * data["T"]**2 + 2 * vab * data["T"] + vb) * N / (N-2))
    datasets.save_csv(data, out, columns=SQUID_COLUMNS)
    
    plt.errorbar(data["T"], data["M"], yerr=data["err_M"], marker="x", linestyle="None")
    
    plt.tight_layout()
    plt.show()
    
def vs_field():

    fn1 = r"20141216_03_SB12_OS_2K2T.rso.dat"
    data = mpms.loadfile_rso(fn1)
    
    mask = data["H"] > 10000.
    x = data["H"][mask]
    y = data["M"][mask]
    N1 = len(x)
    
    params, cov = np.polyfit(x,y, 1, cov=True)
    print("Positive Fields:\ndata points used in regression: N = \n{}\nslope, intercept:\n".format(N1))
    print(params)
    print("\ncovariance matrix:\n")
    print(cov)
    
    a1 = params[0]
    b1 = params[1]
    
    va1 = cov[0][0]
    vb1 = cov[1][1]
    vab1 = cov[0][1]
    
    mask = data["H"] < -10000.
    x = data["H"][mask]
    y = data["M"][mask]
    N2 = len(x)
    
    params, cov = np.polyfit(x,y, 1, cov=True)
    print("\n\nNegative Fields:\ndata points used in regression: N = \n{}\nslope, intercept:\n".format(N2))
    print(params)
    print("\ncovariance matrix:\n")
    print(cov)
    
    a2 = params[0]
    b2 = params[1]
    
    va2 = cov[0][0]
    vb2 = cov[1][1]
    vab2 = cov[0][1]
    
    # remove intercept from both segments, then re-estimate the slope
    mask = data["H"] > 10000.
    data["M"][mask] = data["M"][mask] - b1
    mask = data["H"] < -10000.
    data["M"][mask] = data["M"][mask] - b2
    
    mask = np.logical_or(data["H"] > 10000., data["H"] < -10000.)
    
    x = data["H"][mask]
    y = data["M"][mask]
    N = len(x)
    
    params, cov = np.polyfit(x,y, 1, cov=True)
    print("\n\nCombined data:\ndata points used in regression: N = \n{}\nslope, intercept:\n".format(N))
    print(params)
    print("\ncovariance matrix:\n")
    print(cov)
    
    a = params[0]
    b = params[1]
    
    va = cov[0][0]
    vb = cov[1][1]
    vab = cov[0][1]
    
    print("\n\nmean slope =")
    print(a)
    print("\nerr = \n")
    print((va * N / (N-4))**0.5)
    
    fn = r"20141216_03_SB12_OS_2K2T.a.dat"
    out = r"MvHa.dat"
    data = mpms.loadfile_rso(fn)
    data["M"] = data["M"] - a * data["H"]
    data["err_M"] = np.sqrt(data["err_M"]**2 + (va * data["H"]**2 + 2 * vab * data["H"] + vb) * N / (N-4))
    datasets.save_csv(data, out, columns=SQUID_COLUMNS)
    plt.errorbar(data["H"], data["M"], yerr=data["err_M"], color="C0", marker="x", linestyle="None")
    
    
    fn = r"20141216_03_SB12_OS_2K2T.b.dat"
    out = r"MvHb.dat"
    data = mpms.loadfile_rso(fn)
    data["M"] = data["M"] - a * data["H"]
    data["err_M"] = np.sqrt(data["err_M"]**2 + (va * data["H"]**2 + 2 * vab * data["H"] + vb) * N / (N-4))
    datasets.save_csv(data, out, columns=SQUID_COLUMNS)
    plt.errorbar(data["H"], data["M"], yerr=data["err_M"], color="C4", marker="^", linestyle="None")
    
    plt.tight_layout()
    plt.show()
    #"""

def curie_weiss():
    def f(t, m0, tc, b):
        return m0 / (t - tc) + b
        
    fn1 = r"MvT.dat"
    data = datasets.load_csv(fn1, {0:"time",1:"T", 2:"H",3:"M",4:"err_M"})
    
    # data-fitting
    mask = np.logical_and(data["T"] > 14.3, data["T"] < 16.1)
    x = 1. / data["M"][mask]
    y = data["T"][mask]
    N = len(x)
    
    params, cov = np.polyfit(x,y, 1, cov=True)
    print("Curie-Weiss Law Fitting:\nT = C * (1/M) + T_C\ndata points used in regression: N = \n{}\nslope, intercept:\n".format(N))
    print(params)
    print("\ncovariance matrix:\n")
    print(cov)
    
    print("T_C err = {}\n".format((cov[1][1] * N / (N-2))**0.5))
    
    # copied results
    c = params[0]
    tc = params[1]
    
    # generate model
    x = np.arange(14.5, 30.0, 0.05)
    y = c / (x - tc)
    
    curie = datasets.DataSet({"x": x, "y":y})
    
    out = r"curie.dat"
    datasets.save_csv(curie, out, columns=["x", "y"])
    
    plt.errorbar(data["T"], data["M"], yerr=data["err_M"], marker="x", linestyle="None")
    plt.plot(x, y, marker=None, linestyle="-", color="k")
    plt.tight_layout()
    plt.show()
    
def plot():
    fn1 = r"MvT.dat"
    data = datasets.load_csv(fn1, {0:"time",1:"T", 2:"H",3:"M",4:"err_M"})
    
    plt.errorbar(data["T"], 1. / data["M"], yerr=data["err_M"] / data["M"]**2, marker="x", linestyle="None")
    plt.tight_layout()
    plt.show()
    
 
if __name__ == "__main__":
    #plot()
    #vs_temperature()
    vs_field()
    #curie_weiss()
    
    