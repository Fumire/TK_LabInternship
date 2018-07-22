import getGeneExp as exp

total = 0
over = 0

expFile = "../COSMIC/CosmicCompleteGeneExpression.tsv"
data = exp.geneExpFromCosmic(expFile)

for gene, val in data.items():
    for v in val:
        if abs(v) > 6: over += 1
    total += len(val)

print(over/total*100)
print(over, total)
