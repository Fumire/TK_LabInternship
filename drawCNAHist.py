import matplotlib as mpl
mpl.use("Agg")
mpl.rcParams.update({'font.size': 30})
import matplotlib.pyplot as plt
import numpy as np
import getCNAData as cna
import get1000Data as hgp
import time
import sys
from statistics import mean, median, stdev
from scipy.stats import iqr
from matplotlib.ticker import PercentFormatter
from scipy.optimize import curve_fit
from scipy.misc import factorial
import scipy.stats
import math
import pickle

now = time.strftime("%m%d%H%M%S")
ans = list()

def poissonDist(n, lamb):
    n = np.array(n)
    n = abs(n)
    return ((lamb**n)/factorial(n)) * np.exp(-lamb)

if True:
    #dataHGP = hgp.onlyCNAFromSegmentDiploid()
    dataHGP = hgp.onlyCNAFromDetailsDiploidCNA()
    ans = list(filter(lambda x: x != 2, dataHGP))
    #ans = dataHGP[:]
    with open('./var/' + sys.argv[0] + '.pckl', 'wb') as f: pickle.dump(ans, f, pickle.HIGHEST_PROTOCOL)
else:
    with open('./var/' + sys.argv[0] + '.pckl', 'rb') as f: ans = pickle.load(f)

Q1, Q3 = np.percentile(ans, 25), np.percentile(ans, 75)
print(sys.argv, "Q1&Q3", Q1, Q3)
print(sys.argv[0], "Load Data", len(ans))

plt.figure()
n, bins, patches = plt.hist(ans, bins=10+1, range=[-0.5, 10.5], density=True)
print(sys.argv[0], "Draw Histogram")

binsMiddles = 0.5 * (bins[1:] + bins[:-1])
params, covMatrix = curve_fit(poissonDist, binsMiddles, n)
xPlot = np.linspace(0, 10, 1000)
plt.plot(xPlot, poissonDist(xPlot, *params), "r-", lw=2)
print(sys.argv[0], "Draw Poission")

plt.title("Fit Poission Distribution")
plt.grid(True)
plt.xlabel("CNV")
plt.ylabel("Frequency")
plt.text(5, 0.125, "lambda = %.2f" % (params))
plt.text(5, 0.150, "n = %d" % (len(ans)))
for i in range(len(n)):
    if n[i] == 0: plt.text(bins[i]+0.5, 0, "x")

fig = plt.gcf()
fig.set_size_inches(24, 18)

title = "HistCNA_"
if len(sys.argv) > 1:
    title = sys.argv[1] + "_"
fig.savefig(title + now + ".png")
