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

def poisson(k, lamb):
    return (lamb**k/factorial(k)) * np.exp(-lamb)

now = time.strftime("%m%d%H%M%S")
dataCosmic = cna.onlyCNAFromCosmic("../COSMIC/CosmicCompleteCNA.tsv", 2)
dataImpact = cna.CNAonlyGene("../msk_impact_2017/data_CNA.txt")
ans = list()

for gene, v in dataCosmic.items():
    name = gene.split("+")[0]
    val = abs(v)
    if name not in dataImpact: continue
    #if val > 80: continue
    ans.append(val)
del dataCosmic
del dataImpact
print(sys.argv[0], "Load Data", len(ans))

plt.figure()
n, bins, patches = plt.hist(ans, 80, range=[0, 80], density=True)
binsMiddles = 0.5 * (bins[1:] + bins[:-1])
params, covMatrix = curve_fit(poisson, binsMiddles, n)

xPlot = np.linspace(0, 80, 1000)
print(*params)
plt.plot(xPlot, poisson(xPlot, *params), "r-", lw=2)

plt.title("Fit Poission Distribution")
plt.grid(True)
plt.xlabel("CNA")
plt.ylabel("Frequency (%)")
plt.text(20, 0.125, "lambda = %.2f" % (params))

plt.show()

fig = plt.gcf()
fig.set_size_inches(24, 18)
plt.show()

title = "fit_"
if len(sys.argv) > 1:
    title = sys.argv[1] + "_"
fig.savefig(title + now + ".png")
