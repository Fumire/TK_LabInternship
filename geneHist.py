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

def poissonDist(n, lamb):
    return ((lamb**n)/factorial(n)) * np.exp(-lamb)

now = time.strftime("%m%d%H%M%S")
dataCosmic = cna.onlyCNAFromCosmic("../COSMIC/CosmicCompleteCNA.tsv", 2)
dataImpact = cna.CNAonlyGene("../msk_impact_2017/data_CNA.txt")
ans = dict()

def consistName(name):
    if name in dataImpact: return False
    flag = True
    for gene in dataImpact:
        if gene in name:
            flag = False
            break
    return flag

for gene, v in dataCosmic.items():
    name = gene.split("+")[0].split("_")[0]
    if consistName(name): continue
    if name in ans: ans[name].append(abs(v))
    else: ans[name] = [abs(v)]
del dataCosmic
del dataImpact
print(sys.argv, "Load Complete")

genes = list(ans.keys())
for gene in genes:
    Q1, Q3 = np.percentile(ans[gene], 25), np.percentile(ans[gene], 75)
    plt.figure()
    n, bins, patches = plt.hist(ans[gene], bins=20, range=[0,20], density=True)

    #binsMiddles = 0.5 * (bins[1:] + bins[:-1])
    #params, covMatrix = curve_fit(poissonDist, binsMiddles, n)
    #xPlot = np.linspace(0, 20, 1000)
    #plt.plot(xPlot, poissonDist(xPlot, *params), "r-", lw=2)

    plt.title(gene)
    plt.grid(True)
    plt.xlabel("CNV")
    plt.ylabel("Frequency (%)")
    plt.text(10, 0.125, "lambda = %.2f" % (params))

    fig = plt.gcf()
    fig.set_size_inches(24, 18)

    title = "_" + gene + "_"
    if len(sys.argv) > 1: title = sys.argv[1] + title
    else: title = "gene" + title
    fig.savefig(title + now + ".png")
    del ans[gene]
