import matplotlib as mpl
mpl.use("Agg")
mpl.rcParams.update({'font.size': 30})
import matplotlib.pyplot as plt
import numpy as np
import time
import sys
import getGeneExp as exp
import getCNAData as cna
import get1000Data as hgp
import pickle
import zipfile
from scipy.stats import linregress
import os

now = time.strftime("%m%d%H%M%S")
dataCNA = dict()
dataExp = dict()

if False:
    data = cna.onlyCNAFromCosmic("../COSMIC/CosmicCompleteCNA.tsv", 2) 
    dataExp = exp.geneExpInlier("../COSMIC/CosmicCompleteGeneExpression.tsv")
    key1000 = set(hgp.getSegmentDiploidHugo())

    for key in data:
        gene = key.split("+")[0].split("_")[0]
        if gene in dataCNA:
            dataCNA[gene].append(data[key])
        else:
            dataCNA[gene] = [data[key]]
    del data

    keysCNA = set(dataCNA.keys())
    keysExp = set(dataExp.keys())
    together = keysCNA & keysExp & key1000

    for key in keysCNA-together:
        del dataCNA[key]
    for key in keysExp-together:
        del dataExp[key]

    for key in dataCNA:
        dataCNA[key].sort()
    for key in dataExp:
        dataExp[key].sort()

    with open("./var/" + sys.argv[0] + ".pckl", "wb") as f: pickle.dump((dataCNA, dataExp), f, pickle.HIGHEST_PROTOCOL)
else:
    with open("./var/" + sys.argv[0] + ".pckl", "rb") as f: dataCNA, dataExp = pickle.load(f)
print(sys.argv, "Load Complete", len(dataCNA), len(dataExp))

title = "CNV_Exp_"
if len(sys.argv) > 1:
    title = sys.argv[1] + "_"
with open(title + now + ".csv", "a") as f:
    f.write("gene,slope,intercept,r^2\n")
keys = sorted(list(dataCNA.keys())[:])
pngFiles = list()
for key in keys:
    plt.figure()
    print(sys.argv, key, len(dataCNA[key]), len(dataExp[key]))
    x = list()
    y = list()
    a, b = len(dataCNA[key]), len(dataExp[key])
    k = a if a<b else b
    for i in range(k):
        x.append(dataCNA[key][(a*i)//k])
        y.append(dataExp[key][(b*i)//k])
        plt.scatter(x[-1], y[-1], c='b', alpha=0.4)
    test = np.linspace(x[0], x[-1], 1000)
    del dataExp[key]
    del dataCNA[key]

    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    plt.plot(test, slope*test+intercept, 'r', linewidth=2)
    with open(title + now + ".csv", "a") as f:
        f.write(key + ",")
        f.write("%.6f" % slope + ",")
        f.write("%.6f" % intercept + ",")
        f.write("%.6f" % (r_value**2) + ",")
        f.write("\n")
    plt.text(max(x)/2, 0.5, "y = %.2fx + %.2f" % (slope, intercept))
    plt.text(max(x)/2, 0.0, "r^2 = %.2f" % (r_value**2))
    plt.xlabel("CNV")
    plt.ylabel("Gene Expression (Z-score)")
    plt.title("CNV vs. Gene Expression (" + key + ")")

    fig = plt.gcf()
    fig.set_size_inches(24, 18)
    if len(sys.argv) > 1:
        title = sys.argv[1] + "_"
    fig.savefig(title + "_" + key + "_" + now + ".png")
    pngFiles.append(title + "_" + key + "_" + now + ".png")
    plt.close()
print(sys.argv, "Plot done", "\a")

wzip = zipfile.ZipFile("./" + title + now + '.zip', mode='w')
for png in pngFiles:  wzip.write(png, compress_type = zipfile.ZIP_DEFLATED)
wzip.close()
os.system("mv ./" + title + "*.png ./pic/")
print(sys.argv, "All Complete", "\a")
