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

now = time.strftime("%m%d%H%M%S")
dataCosmic = cna.onlyCNAFromCosmic("../COSMIC/CosmicCompleteCNA.tsv", 2)
dataImpact = cna.CNAonlyGene("../msk_impact_2017/data_CNA.txt")
ans = dict()

for gene, val in dataCosmic.items():
    name = gene.split("+")[0]
    if name not in dataImpact: continue
    if name in ans: ans[name].append(val)
    else: ans[name] = [val]
del dataCosmic
del dataImpact
print(sys.argv[0], "Load Data", len(ans))

gene = list(ans.keys())
gene.sort()
statVal = dict()

x = list()
y = [list() for x in range(6)]

for val in gene:
    x.append(val)
    y[0].append(min(ans[val]))
    y[1].append(max(ans[val]))
    y[2].append(mean(ans[val]))
    y[3].append(median(ans[val]))
    y[4].append(stdev(ans[val]))
    y[5].append(iqr(ans[val]))

x = np.array(x)
for i in range(6): y[i] = np.array(y[i])

plt.figure()

#plt.scatter(x, y[0], color="red", alpha=0.5, label="min")
#plt.scatter(x, y[1], color="red", alpha=0.5, label="MAX")
plt.scatter(x, y[2], color="blue", label="mean")
plt.scatter(x, y[3], color="green", label="median")
plt.errorbar(x, y[2], yerr=y[4], color="blue", linestyle="None")
plt.scatter(x, y[5], color="red", label="IQR")

plt.title("Statistics")
plt.xlabel("Gene")
plt.ylabel("CNA")
plt.xticks([])
plt.legend()
plt.grid(True)

fig = plt.gcf()
fig.set_size_inches(96, 18)
plt.show()

title = "Stat_"
if len(sys.argv) > 1:
    title = sys.argv[1] + "_"
fig.savefig(title + now + ".png")
