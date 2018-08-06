import matplotlib as mpl
mpl.use("Agg")
mpl.rcParams.update({'font.size': 30})
import matplotlib.pyplot as plt
import numpy as np
import getCNAData as cna
import time
import sys
import pickle
import scipy.stats

now = time.strftime("%m%d%H%M%S")
ans = dict()

if True:
    data = cna.onlyCNAFromCosmic("../COSMIC/CosmicCompleteCNA.tsv")
    for gene, val in data.items():
        name = gene.split("+")[1]
        if val == 0:
            continue
        if abs(val) < 10**1: continue
        if (name, val) in ans:
            ans[(name, val)] += 1
        else:
            ans[(name, val)] = 1
    del data
    print("Load Data")

    with open('./var/' + sys.argv[0] + '.pckl', 'wb') as f:
        pickle.dump(ans, f, pickle.HIGHEST_PROTOCOL)
else:
    with open('./var/' + sys.argv[0] + '.pckl', 'rb') as f:
        ans = pickle.load(f)

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

plt.title("CNV with COSMIC")
plt.xlabel("Gene")
plt.ylabel("CNV (Log Scale)")
plt.xticks([])
plt.yscale('log')

fig = plt.gcf()
fig.set_size_inches(24, 18)

title = "COSMIC_"
if len(sys.argv) > 1:
    title = sys.argv[1] + "_"
fig.savefig(title + now + ".png")
