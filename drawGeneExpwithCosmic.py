import matplotlib as mpl
mpl.use("Agg")
mpl.rcParams.update({'font.size': 20})
import matplotlib.pyplot as plt
import numpy as np
import time
import sys
import getGeneExp as exp

now = time.strftime("%m%d%H%M%S")
expFile = "../COSMIC/CosmicCompleteGeneExpression.tsv"
data = exp.geneExpFromCosmic(expFile, ["INMT"])
print(sys.argv[0], "Load Data", len(data))

plt.figure()

genes = list(data.keys())
genes.sort()

for i, gene in enumerate(genes):
    for val in data[gene]:
        plt.scatter(i, val, alpha=0.5)

plt.title("Gene Expression")
plt.xlabel("Gene")
plt.ylabel("Expression Level")
plt.xticks([])

fig = plt.gcf()
fig.set_size_inches(24, 18)
plt.show()

title = "GeneExp_"
if len(sys.argv) > 1:
    title = sys.argv[1] + "_"
fig.savefig(title + now + ".png")
