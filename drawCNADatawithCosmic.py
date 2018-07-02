import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import getCNAData as cna
import time

data = cna.onlyCNAFromCosmic("../COSMIC/CosmicCompleteCNA.tsv")
ans = dict()
now = time.strftime("%m%d%H%M%S")

seq = 0
for gene, val in data.items():
    name = gene.split("+")[0]
    #if val == 0: continue
    if (name, val) in ans: ans[(name, val)] += 1
    else: ans[(name, val)] = 1
    #if seq == 10000: break
    #else: seq += 1
del data
print("Load Data")

x = list()
y = list()
color = list()

gene = list(ans.keys())
gene.sort()

for val in gene:
    x.append(val[0])
    y.append(val[1])
    color.append(ans[val])
del ans
print("Load ans")

x = np.array(x)
y = np.array(y)

plt.figure()

plt.scatter(x, y, s=color, c=color, alpha=0.5)
plt.colorbar()

plt.xlabel("Gene")
plt.ylabel("CNA")
plt.xticks([])

fig = plt.gcf()
fig.set_size_inches(24, 18)
plt.show()
fig.savefig("COSMIC_"+now+".png")
