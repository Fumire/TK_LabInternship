import matplotlib as mpl
mpl.use("Agg")
mpl.rcParams.update({'font.size': 30})
import matplotlib.pyplot as plt
import numpy as np
import getCNAData as cna
import get1000Data as hgp
import time
import sys
from statistics import mean, median, stdev
from scipy.stats import iqr
from matplotlib.ticker import PercentFormatter
from scipy.optimize import curve_fit
from scipy.misc import factorial
import scipy.stats
import math
import pickle
import zipfile
import os
from scipy.stats import ks_2samp

def poissonDist(n, lamb):
    n = np.array(n)
    n = abs(n)
    return ((lamb**n)/factorial(n)) * np.exp(-lamb)

now = time.strftime("%m%d%H%M%S")
ans = dict()
if False:
    dataCosmic = cna.onlyCNAFromCosmic("../COSMIC/CosmicCompleteCNA.tsv", 2)
    dataImpact = cna.CNAonlyGene("../msk_impact_2017/data_CNA.txt")
    data1000 = hgp.getSegmentDiploidHugo()

    def consistName(name):
        if name not in dataImpact:
            return True
        if name not in data1000:
            return True
        return False

    for gene, v in dataCosmic.items():
        name = gene.split("+")[0].split("_")[0]
        val = abs(v)
        if consistName(name): continue
        if name in ans: ans[name].append(val)
        else: ans[name] = [val]
    del dataCosmic
    del dataImpact
    del data1000
    with open('./var/' + sys.argv[0] + '.pckl', 'wb') as f: pickle.dump(ans, f, pickle.HIGHEST_PROTOCOL)
else:
    with open('./var/' + sys.argv[0] + '.pckl', 'rb') as f: ans = pickle.load(f)
print(sys.argv, "Load Complete", "\a")

genes = list(ans.keys())
genes.sort()
pngFiles = list()

fileTitle = "gene_"
if len(sys.argv) > 1: fileTitle = sys.argv[1] + "_"

for i, gene in enumerate(genes):
    Q1, Q3 = np.percentile(ans[gene], 25), np.percentile(ans[gene], 75)

    plt.figure()
    #head = math.ceil(max(ans[gene])) if max(ans[gene]) < 10 else 10
    head = 10
    n, bins, patches = plt.hist(ans[gene], bins=head+1, range=[-0.5, head+0.5], density=True)

    binsMiddles = 0.5 * (bins[1:] + bins[:-1])
    params, covMatrix = curve_fit(poissonDist, binsMiddles, n, maxfev=1000)
    xPlot = np.linspace(0, head, 100)
    plt.plot(xPlot, poissonDist(xPlot, *params), "r-", lw=2)
    st = ks_2samp(n, poissonDist(xPlot, *params))
    with open(fileTitle + now + ".txt", "a") as f:
        f.write(gene + " " + str(st) + "\n")

    plt.title(gene)
    plt.grid(True)
    plt.xlabel("CNV")
    plt.ylabel("Frequency")
    plt.text(head//2, 0.125, "lambda = %.2f" % (params))
    plt.text(head//2, 0.150, "n = %d" % len(ans[gene]))
    plt.text(head//2, 0.175, "st = %.2f" % st[0])

    fig = plt.gcf()
    fig.set_size_inches(24, 18)

    title = "_" + gene + "_"
    if len(sys.argv) > 1: title = sys.argv[1] + title
    else: title = "gene" + title

    fig.savefig(title + now + ".png")
    pngFiles.append("./" + title + now + ".png")
    print(i, gene, len(ans[gene]), Q1, Q3, min(ans[gene]), max(ans[gene]))
    del ans[gene]
    plt.close()
print(sys.argv, "Plot done", "\a")

wzip = zipfile.ZipFile("./" + fileTitle + now + '.zip', mode='w')
for png in pngFiles:  wzip.write(png, compress_type = zipfile.ZIP_DEFLATED)
wzip.close()
os.system("mv ./" + fileTitle + "*.png ./pic/")
print(sys.argv, "Finish", "\a")
