import getCNAData as cna
import time
import sys
import statistics
from scipy.stats import iqr

now = time.strftime("%m%d%H%M%S")
dataCosmic = cna.onlyCNAFromCosmic("../COSMIC/CosmicCompleteCNA.tsv", 2)
dataImpact = cna.CNAonlyGene("../msk_impact_2017/data_CNA.txt")
ans = dict()

for gene, val in dataCosmic.items():
    name = gene.split("+")[0]
    if name not in dataImpact: continue
    if name in ans: ans[name].append(val)
    else: ans[name] = [val]
del dataCosmic
del dataImpact
print("Load Data", len(ans))

gene = list(ans.keys())
gene.sort()

title = "statIMPACTandCosmic_"
if len(sys.argv) > 1:
    title = sys.argv[1] + "_"

with open(title + now + ".txt", "w") as f:
    for val in gene:
        f.write(val + "\n")
        f.write("- min: " + str(min(ans[val])) + "\n")
        f.write("- max: " + str(max(ans[val])) + "\n")
        f.write("- mean: " + str(statistics.mean(ans[val])) + "\n")
        f.write("- median: " + str(statistics.median(ans[val])) + "\n")
        f.write("- stdev: " + str(statistics.stdev(ans[val])) + "\n")
        f.write("- IQR: " + str(iqr(ans[val])) + "\n")
        f.write("\n")
