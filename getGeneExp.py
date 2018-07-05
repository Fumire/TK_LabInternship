def geneExpFromCosmic(fileName, wanted=None):
    geneList = dict()
    expFile = open(fileName, "r")

    assert expFile.readline()

    while True:
        line = expFile.readline()
        if not line: break
        line = line.split("\t")

        gene, val = line[2], float(line[4])

        if wanted != None and gene not in wanted: continue
        if gene in geneList: geneList[gene].append(val)
        else: geneList[gene] = [val]
    expFile.close()
    return geneList

if __name__ == "__main__":
    name = "../COSMIC/CosmicCompleteGeneExpression.tsv"
    data = geneExpFromCosmic(name)
    print(len(data))
