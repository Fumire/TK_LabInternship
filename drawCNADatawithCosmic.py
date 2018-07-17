import matplotlib as mpl
mpl.use("Agg")
mpl.rcParams.update({'font.size': 20})
import matplotlib.pyplot as plt
import numpy as np
import getCNAData as cna
import time
import sys

now = time.strftime("%m%d%H%M%S")
data = cna.onlyCNAFromCosmic("../COSMIC/CosmicCompleteCNA.tsv")
ans = dict()

for gene, val in data.items():
    name = gene.split("+")[1]
    if val == 0: continue
    if abs(val) < 10**2: continue
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
    big.append((ans[val]**2) * 100)
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
plt.ylabel("CNA (Log Scale)")
plt.xticks([])
plt.yscale('log')

fig = plt.gcf()
fig.set_size_inches(24, 18)

title = "COSMIC_"
if len(sys.argv) > 1:
    title = sys.argv[1] + "_"
fig.savefig(title + now + ".png")
