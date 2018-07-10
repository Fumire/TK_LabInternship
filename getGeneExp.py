def geneExpFromCosmic(fileName, wanted=None, cutNormal=False):
    geneList = dict()
    expFile = open(fileName, "r")

    assert expFile.readline()

    while True:
        line = expFile.readline()
        if not line: break
        line = line.split("\t")

        gene, val = line[2], float(line[4])

        if wanted != None and gene not in wanted: continue
        if cutNormal and line[3] == "normal": continue
        if gene in geneList: geneList[gene].append(val)
        else: geneList[gene] = [val]
    expFile.close()
    return geneList

def geneExpOutlier(fileName, threshold=10000):
    geneList = dict()
    expFile = open(fileName, "r")

    assert expFile.readline()

    while True:
        line = expFile.readline()
        if not line: break
        line = line.split("\t")

        gene, val = line[2], float(line[4])
        if val < threshold: continue
        if gene in geneList: geneList[gene].append(val)
        else: geneList[gene] = [val]
    expFile.close()
    return geneList

def geneExpOnlyValue(fileName, maxlen=1000):
    geneList = list()
    expFile = open(fileName, "r")

    assert expFile.readline()

    while True:
        line = expFile.readline()
        if not line: break
        line = line.split("\t")
        geneList.append(float(line[4]))
    geneList.sort(reverse=True)
    return geneList[:maxlen]

if __name__ == "__main__":
    name = "../COSMIC/CosmicCompleteGeneExpression.tsv"
    #data = geneExpFromCosmic(name); print(len(data));
    val = geneExpOnlyValue(name); print(val)
