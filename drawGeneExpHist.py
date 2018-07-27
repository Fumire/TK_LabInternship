import getGeneExp as exp
import matplotlib as mpl
mpl.use("Agg")
mpl.rcParams.update({'font.size': 30})
import matplotlib.pyplot as plt
import numpy as np
import time
import sys
from statistics import mean, median, stdev
from scipy.stats import norm, ks_2samp, iqr
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
    #data = exp.geneExpInlier(expFile)

    for gene, v in data.items():
        ans.extend(list(filter(lambda x: x <= 6 and x >= -6, v)))
    del data
    with open('./var/' + sys.argv[0] + '.pckl', 'wb') as f:
        pickle.dump(ans, f, pickle.HIGHEST_PROTOCOL)
else:
    with open('./var/' + sys.argv[0] + '.pckl', 'rb') as f:
        ans = pickle.load(f)
print(sys.argv, "Load data", len(ans))

plt.figure()
n, bins, patches = plt.hist(ans, bins=6*5*2+1, range=[-6.5, 6.5], density=True)
print(sys.argv, "Draw Histogram")

mu, std = norm.fit(ans)
x = np.linspace(-6.0, 6.0, 1000)
p = norm.pdf(x, mu, std)
plt.plot(x, p, 'r', linewidth=2)
plt.text(4, 0.150, "mu = %.2f" % mu)
plt.text(4, 0.125, "std = %.2f" % std)
st = ks_2samp(n, p)
plt.text(4, 0.175, "st = %.2f" % st[0])
plt.text(4, 0.200, "n = %d" % len(ans))
print(sys.argv, "Fit Complete", mu, std, st)

plt.grid(True)
plt.title("Histogram of Gene Expression")
plt.xlabel("Gene Expression (Z-score)")
plt.ylabel("Frequency")

fig = plt.gcf()
fig.set_size_inches(24, 18)

title = "GeneExpHist_"
if len(sys.argv) > 1:
    title = sys.argv[1] + "_"
fig.savefig(title + now + ".png")
