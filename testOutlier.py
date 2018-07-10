import getGeneExp as exp

name = "../COSMIC/CosmicCompleteGeneExpression.tsv"
data = exp.geneExpOutlier(name, 10000)

for gene in data:
    print(gene, ":", end=" ")
    data[gene].sort(reverse=True)
    for val in data[gene]:
        print(val, end=" ")
    print()
