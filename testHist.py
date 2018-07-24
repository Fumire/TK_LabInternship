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

def poissonDist(n, lamb):
    n = np.array(n)
    n = abs(n)
    return ((lamb**n)/factorial(n)) * np.exp(-lamb)

now = time.strftime("%m%d%H%M%S")
ans = list()

if False:
    dataCosmic = cna.onlyCNAFromCosmic("../COSMIC/CosmicCompleteCNA.tsv", 2)
    #dataCosmic = cna.onlyCNAFromCosmic("../CellLine/CosmicCLP_CompleteCNA.tsv", 2)
    dataImpact = cna.CNAonlyGene("../msk_impact_2017/data_CNA.txt")
    data1000 = hgp.getSegmentDiploidHugo()
    def consistName(name):
        if name in dataImpact: return False
        if name in data1000: return False
        for gene in dataImpact:
            if gene in name:
                return False
        for gene in data1000:
            if gene in name:
                return False
        return True

    for gene, v in dataCosmic.items():
        name = gene.split("+")[0]
        if consistName(name): continue
        ans.append(v)
    del dataCosmic
    del dataImpact
    with open('./var/' + sys.argv[0] + '.pckl', 'wb') as f: pickle.dump(ans, f, pickle.HIGHEST_PROTOCOL)
else:
    with open('./var/' + sys.argv[0] + '.pckl', 'rb') as f: ans = pickle.load(f)

#tmp = ans[:]
#ans = [(i-min(tmp)) for i in tmp]

Q1, Q3 = np.percentile(ans, 25), np.percentile(ans, 75)
print(sys.argv, "Q1&Q3", Q1, Q3)
#ans.sort()
#for i in range(len(ans)):
#    if i < valIQR * 1.5: continue
#    ans[i:] = []
#    break

print(sys.argv[0], "Load Data", len(ans))

plt.figure()
n, bins, patches = plt.hist(ans, bins=20+1, range=[-0.5, 20.5], density=True)
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
plt.text(5, 0.125, "lambda = %.2f" % (params))
plt.text(5, 0.150, "n = %d" % len(ans))
for i in range(len(n)):
    if n[i] == 0: plt.text(bins[i]+0.5, 0, "x")

fig = plt.gcf()
fig.set_size_inches(24, 18)

title = "fit_"
if len(sys.argv) > 1:
    title = sys.argv[1] + "_"
fig.savefig(title + now + ".png")
