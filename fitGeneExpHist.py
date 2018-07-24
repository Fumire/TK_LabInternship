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
from scipy.stats import ks_2samp
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
size = len(ans)
print(sys.argv, "Load data", size)

plt.figure()
n, bins, patches = plt.hist(ans, bins=6*10+1, range=[-6.5, 6.5], density=True)
print(sys.argv, "Draw Histogram")

title = "GeneExpFit_"
if len(sys.argv) > 1:
    title = sys.argv[1] + "_"
#distNames = ['norm', 'gamma', 'beta', 'rayleigh', 'pareto']
distNames = [ 'alpha', 'anglit', 'arcsine', 'beta', 'betaprime', 'bradford', 'burr', 'cauchy', 'chi', 'chi2', 'cosine', 'dgamma', 'dweibull', 'erlang', 'expon', 'exponweib', 'exponpow', 'f', 'fatiguelife', 'fisk', 'foldcauchy', 'foldnorm', 'frechet_r', 'frechet_l', 'genlogistic', 'genpareto', 'genexpon', 'genextreme', 'gausshyper', 'gamma', 'gengamma', 'genhalflogistic', 'gilbrat', 'gompertz', 'gumbel_r', 'gumbel_l', 'halfcauchy', 'halflogistic', 'halfnorm', 'hypsecant', 'invgamma', 'invgauss', 'invweibull', 'johnsonsb', 'johnsonsu', 'ksone', 'kstwobign', 'laplace', 'logistic', 'loggamma', 'loglaplace', 'lognorm', 'lomax', 'maxwell', 'mielke', 'nakagami', 'ncx2', 'ncf', 'nct', 'norm', 'pareto', 'pearson3', 'powerlaw', 'powerlognorm', 'powernorm', 'rdist', 'reciprocal', 'rayleigh', 'rice', 'recipinvgauss', 'semicircular', 't', 'triang', 'truncexpon', 'truncnorm', 'tukeylambda', 'uniform', 'vonmises', 'wald', 'weibull_min', 'weibull_max', 'wrapcauchy']

for distName in distNames:
    print(sys.argv, distName)
    dist = getattr(scipy.stats, distName)
    param = dist.fit(bins)
    x = np.linspace(-6.0, 6.0, 100)
    p = dist.pdf(x, *param[:-2])
    plt.plot(x, p, linewidth=2, label=distName)
    print(sys.argv, distName, ks_2samp(n, p))
    with open(title + now + ".txt", "a") as f:
        f.write(str(distName) + "\n")
        f.write(str(ks_2samp(ans, p)) + "\n")
        f.write(str(param[:-2]) + "\n")
        f.write("\n")

plt.grid(True)
plt.title("Histogram and Fitting of Gene Expression")
plt.xlabel("Gene Expression (Z-score)")
plt.ylabel("Frequency")
plt.legend(loc='upper right')

fig = plt.gcf()
fig.set_size_inches(24, 18)
fig.savefig(title + now + ".png")
