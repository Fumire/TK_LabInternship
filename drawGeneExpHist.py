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
from matplotlib.ticker import PercentFormatter
from scipy.optimize import curve_fit
from scipy.misc import factorial
import scipy.stats

now = time.strftime("%m%d%H%M%S")
expFile = "../COSMIC/CosmicCompleteGeneExpression.tsv"
data = exp.geneExpFromCosmic(expFile, cutNormal=True)
ans = list()

for gene, v in data.items():
    #ans.extend(list(map(abs, v)))
    #ans.extend(list(filter(lambda x: x < 6, map(abs, v))))
    ans.extend(list(filter(lambda x: x < 6 and x > -6, v)))
del data
print(sys.argv, "Load data", len(ans))

plt.figure()
#n, bins, patches = plt.hist(ans, density=True)
n, bins, patches = plt.hist(ans, density=True)
print(sys.argv, "Draw Histogram")

plt.grid(True)

fig = plt.gcf()
fig.set_size_inches(24, 18)
plt.show()

title = "GeneExpHist_"
if len(sys.argv) > 1:
    title = sys.argv[1] + "_"
fig.savefig(title + now + ".png")
