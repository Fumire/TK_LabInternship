import matplotlib as mpl
mpl.use("Agg")
mpl.rcParams.update({'font.size': 20})
import matplotlib.pyplot as plt
import numpy as np
import getCNAData as cna
import time
import sys

now = time.strftime("%m%d%H%M%s")
dataCosmic = cna.onlyCNAFromCosmic("../COSMIC/CosmicCompleteCNA.tsv", 2)
dataImpact = cna.CNAonlyGene("../msk_impact_2017/data_CNA.txt")
ans = dict()

for gene, val in dataCosmic.items():
    name = gene.split("+")[0]
    if val == 0:
        continue
    if name not in dataImpact:
        continue
    if (name, val) in ans:
        ans[(name, val)] += 1
    else:
        ans[(name, val)] = 1
del dataCosmic
del dataImpact
print(sys.argv[0], "Load Data", len(ans))

x = list()
y = list()
color = list()
big = list()

gene = list(ans.keys())
gene.sort()

for val in gene:
    x.append(val[0])
    y.append(val[1])
    color.append(ans[val])
    big.append(ans[val] * 10)
del ans
print("Load ans")

x = np.array(x)
y = np.array(y)
color = np.array(color)
big = np.array(big)

plt.figure()

plt.scatter(x, y, s=big, c=color, alpha=0.5)
plt.colorbar()

plt.title("Only Gene both in MSK-IMPACT and COSMIC")
plt.xlabel("Gene")
plt.ylabel("CNA")
plt.xticks([])
plt.grid(True)

fig = plt.gcf()
fig.set_size_inches(24, 18)
plt.show()
title = "IMPACTandCOSMIC_"
if len(sys.argv) > 1:
    title = sys.argv[1] + "_"
fig.savefig(title + now + ".png")
