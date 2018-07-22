import getGeneExp as exp
import matplotlib as mpl
mpl.use("Agg")
mpl.rcParams.update({'font.size': 30})
import matplotlib.pyplot as plt
import numpy as np
import time
import sys
from statistics import mean, median, stdev
from scipy.stats import iqr
from scipy.stats import norm
from matplotlib.ticker import PercentFormatter
from scipy.optimize import curve_fit
from scipy.misc import factorial
import scipy.stats
import pickle

now = time.strftime("%m%d%H%M%S")
ans = list()
if False:
    expFile = "../COSMIC/CosmicCompleteGeneExpression.tsv"
    data = exp.geneExpFromCosmic(expFile)

    for gene, v in data.items():
        ans.extend(list(filter(lambda x: x<= 6 and x >= -6, v)))
    del data
    with open('./var/' + sys.argv[0] + '.pckl', 'wb') as f: pickle.dump(ans, f, pickle.HIGHEST_PROTOCOL)
else:
    with open('./var/' + sys.argv[0] + '.pckl', 'rb') as f: ans = pickle.load(f)
print(sys.argv, "Load data", len(ans))

plt.figure()
n, bins, patches = plt.hist(ans, bins=6*10+1, range=[-6.5, 6.5])
print(sys.argv, "Draw Histogram")

distNames = ['gamma', 'beta', 'rayleigh', 'norm', 'pareto']
for distName in distNames:
    dist = getattr(scipy.stats, distName)
    param = dist.fit(ans)
    pdf_fitted = dist.pdf(x, *param[:-2], loc=param[-2], scale=param[-1]) * size
    plt.plot(pdf_fitted, label=distName)
    plt.xlim(0, 47)

plt.grid(True)
plt.title("Histogram and Fitting of Gene Expression")
plt.xlabel("Gene Expression (Z-score)")
plt.ylabel("Frequency")
plt.legend(loc='upper right')

fig = plt.gcf()
fig.set_size_inches(24, 18)

title = "GeneExpFit_"
if len(sys.argv) > 1:
    title = sys.argv[1] + "_"
fig.savefig(title + now + ".png")
