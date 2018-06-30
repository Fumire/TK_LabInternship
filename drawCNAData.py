import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import getCNAData as cna

data = cna.CNAwithHugo(True)
HUGOs = list(data.keys())
ans = dict()

for i, gene in enumerate(HUGOs):
    for j in data[gene].values():
        if (i,j) in ans:
            ans[(i,j)] += 1
        else:
            ans[(i,j)] = 1

x = list()
y = list()
color = list()

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
plt.show()
fig.savefig('CNA_data.png')
