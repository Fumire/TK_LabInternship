import matplotlib as mpl
mpl.use("Agg")
mpl.rcParams.update({'font.size': 20})
import matplotlib.pyplot as plt
import numpy as np
import getCNAData as cna
import time
import sys
from statistics import mean, median, stdev
from scipy.stats import iqr
from matplotlib.ticker import PercentFormatter

now = time.strftime("%m%d%H%M%S")
dataCosmic = cna.onlyCNAFromCosmic("../COSMIC/CosmicCompleteCNA.tsv", 2)
dataImpact = cna.CNAonlyGene("../msk_impact_2017/data_CNA.txt")
ans = list()

for gene, v in dataCosmic.items():
    name = gene.split("+")[0]
    val = abs(v)
    if name not in dataImpact: continue
    if val > 80: continue
    ans.append(val)
del dataCosmic
del dataImpact
print(sys.argv[0], "Load Data", len(ans))

plt.figure()

n, bins, patches = plt.hist(ans, 80, density=True)

plt.title("Histogram")
plt.grid(True)
plt.xlabel("CNA")
plt.ylabel("Frequency (%)")

fig = plt.gcf()
fig.set_size_inches(24, 18)
plt.show()

title = "hist_"
if len(sys.argv) > 1:
    title = sys.argv[1] + "_"
fig.savefig(title + now + ".png")
