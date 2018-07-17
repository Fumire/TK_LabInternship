import matplotlib as mpl
mpl.use("Agg")
mpl.rcParams.update({'font.size': 30})
import matplotlib.pyplot as plt
import numpy as np
import getCNAData as cna
import time
import sys
from statistics import mean, median, stdev
from scipy.stats import iqr
from matplotlib.ticker import PercentFormatter
from scipy.optimize import curve_fit
from scipy.misc import factorial
import scipy.stats
import math

def poissonDist(n, lamb):
    n = np.array(n)
    return ((lamb**n)/factorial(n)) * np.exp(-lamb)

now = time.strftime("%m%d%H%M%S")
dataCosmic = cna.onlyCNAFromCosmic("../COSMIC/CosmicCompleteCNA.tsv", 2)
dataImpact = cna.CNAonlyGene("../msk_impact_2017/data_CNA.txt")
ans = list()

def consistName(name):
    if name in dataImpact: return False
    flag = True
    for gene in dataImpact:
        if gene in name:
            flag = False
            break
    return flag

for gene, v in dataCosmic.items():
    name = gene.split("+")[0]
    if consistName(name): continue
    #if name not in dataImpact: continue
    #ans.append(abs(v))
    ans.append(v)
del dataCosmic
del dataImpact

tmp = ans[:]
ans = [(i-min(tmp)) for i in tmp]

Q1, Q3 = np.percentile(ans, 25), np.percentile(ans, 75)
print(sys.argv, "Q1&Q3", Q1, Q3)
#ans.sort()
#for i in range(len(ans)):
#    if i < valIQR: continue
#    ans[i:] = []
#    break

print(sys.argv[0], "Load Data", len(ans))

plt.figure()
n, bins, patches = plt.hist(ans, bins=20, range=[0, 20], density=True)
#n, bins, patches = plt.hist(ans, density=True)
print(sys.argv[0], "Draw Histogram")
binsMiddles = 0.5 * (bins[1:] + bins[:-1])
params, covMatrix = curve_fit(poissonDist, binsMiddles, n)

xPlot = np.linspace(0, 20, 1000)
plt.plot(xPlot, poissonDist(xPlot, *params), "r-", lw=2)
print(sys.argv[0], "Draw Poission")

plt.title("Fit Poission Distribution")
plt.grid(True)
plt.xlabel("CNV")
plt.ylabel("Frequency")
plt.text(10, 0.125, "lambda = %.2f" % (params))

fig = plt.gcf()
fig.set_size_inches(24, 18)

title = "fit_"
if len(sys.argv) > 1:
    title = sys.argv[1] + "_"
fig.savefig(title + now + ".png")
