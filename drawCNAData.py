import matplotlib as mpl
mpl.use('Agg')
mpl.rcParams.update({'font.size': 20})
import matplotlib.pyplot as plt
import numpy as np
import getCNAData as cna
import time
import sys
import pickle

ans = dict()
now = time.strftime("%m%d%H%M%S")

if True:
    #data = cna.onlyCNAFromCosmic("../COSMIC/CosmicCompleteCNA.tsv")
    data = cna.CNAwithHugo("../msk_impact_2017/data_CNA.txt", False)
    HUGOs = sorted(list(data.keys()))
    for i, gene in enumerate(HUGOs):
        for j in map(lambda x: x+2, data[gene].values()):
            if (i, j) in ans:
                ans[(i, j)] += 1
            else:
                ans[(i, j)] = 1
    del data
    with open('./var/' + sys.argv[0] + '.pckl', 'wb') as f:
        pickle.dump(ans, f, pickle.HIGHEST_PROTOCOL)
else:
    with open('./var/' + sys.argv[0] + '.pckl', 'rb') as f:
        ans = pickle.load(f)

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
plt.ylabel("CNV")
plt.title("CNV with MSKCC-IMPACT")

#plt.xticks(x, list(data.keys()))
plt.xticks([])

fig = plt.gcf()
fig.set_size_inches(12, 9)
plt.show()
title = "CNA_data_"
if len(sys.argv) > 1:
    title = sys.argv[1] + "_"
fig.savefig(title + now + '.png')
