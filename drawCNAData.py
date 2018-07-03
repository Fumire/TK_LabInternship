import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import getCNAData as cna
import time

data = cna.CNAwithHugo("../msk_impact_2017/data_CNA.txt",True)
#data = cna.onlyCNAFromCosmic("../COSMIC/CosmicCompleteCNA.tsv")
HUGOs = list(data.keys())
ans = dict()
now = time.strftime("%m%d%H%M%S")

for i, gene in enumerate(HUGOs):
    for j in data[gene].values():
        if (i,j) in ans:
            ans[(i,j)] += 1
        else:
            ans[(i,j)] = 1
del data

x = list()
y = list()
color = list()
data = list(ans.keys())
data.sort()

for val in ans: 
    x.append(val[0])
    y.append(val[1])
    color.append(ans[val])

x = np.array(x)
y = np.array(y)

plt.figure()

plt.scatter(x, y, s=color, c=color, alpha=0.5)
plt.colorbar()

plt.xlabel("Gene")
plt.ylabel("CNA")

#plt.xticks(x, list(data.keys()))

fig = plt.gcf()
fig.set_size_inches(24, 18)
plt.show()
fig.savefig('CNA_data_'+now+'.png')
