import matplotlib as mpl
mpl.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import getCNAData as cna
import time

now = time.strftime("%m%d%H%M%S")
data = cna.onlyCNAFromCosmic("../COSMIC/CosmicCompleteCNA.tsv")
ans = dict()

for gene, val in data.items():
    name = gene.split("+")[1]
    #if val == 0: continue
    if abs(val) < 100: continue
    if (name, val) in ans: ans[(name, val)] += 1
    else: ans[(name, val)] = 1
del data
print("Load Data")

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
    big.append(ans[val] * 100)
del ans
print("Load ans")

x = np.array(x)
y = np.array(y)
color = np.array(color)
big = np.array(big)

plt.figure()

plt.scatter(x, y, s=big, c=color, alpha=0.5)
plt.colorbar()

plt.title("Log Scale")
plt.xlabel("Gene")
plt.ylabel("CNA")
plt.xticks([])
plt.yscale('log')

fig = plt.gcf()
fig.set_size_inches(24, 18)
plt.show()
fig.savefig("COSMIC_"+now+".png")
