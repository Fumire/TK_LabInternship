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
    #if name not in dataImpact: continue
    if val not in ans: ans[val] = 1
    else: ans[val] += 1
del dataCosmic
del dataImpact
print(sys.argv[0], "Load Data", len(ans))

x = list(ans.keys())
x.sort()
y = [ans[i] for i in x]
bins = []
for i in x:
    bins.append(i-0.25-min(x))
    bins.append(i+0.25-min(x))
y = np.array(y)
bins = np.array(bins)

plt.figure()

plt.hist(y, bins)
#plt.scatter(x, y)

plt.title("Histogram")
plt.grid(True)

fig = plt.gcf()
fig.set_size_inches(24, 18)
plt.show()

title = "hist_"
if len(sys.argv) > 1:
    title = sys.argv[1] + "_"
fig.savefig(title + now + ".png")
