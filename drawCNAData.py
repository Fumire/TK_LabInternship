import matplotlib as mpl
mpl.use('Agg')
mpl.rcParams.update({'font.size': 20})
import matplotlib.pyplot as plt
import numpy as np
import getCNAData as cna
import time
import sys

data = cna.CNAwithHugo("../msk_impact_2017/data_CNA.txt", True)
#data = cna.onlyCNAFromCosmic("../COSMIC/CosmicCompleteCNA.tsv")
HUGOs = list(data.keys())
ans = dict()
now = time.strftime("%m%d%H%M%S")

for i, gene in enumerate(HUGOs):
    for j in data[gene].values():
        if (i,j) in ans: ans[(i,j)] += 1
        else: ans[(i,j)] = 1
del data

x = list()
y = list()
color = list()
big = list()

for val in ans:
    x.append(val[0])
    y.append(val[1])
    color.append(ans[val])
    big.append(ans[val])

x = np.array(x)
y = np.array(y)

plt.figure()

plt.scatter(x, y, s=big, c=color, alpha=0.5)
plt.colorbar()

plt.xlabel("Gene")
plt.ylabel("CNA")

#plt.xticks(x, list(data.keys()))
plt.xticks([])

fig = plt.gcf()
fig.set_size_inches(12, 9)
plt.show()
title = "CNA_data_"
if len(sys.argv) > 1:
    title = sys.argv[1] + "_"
fig.savefig(title + now + '.png')
