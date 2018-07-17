def geneExpFromCosmic(fileName, wanted=None, cutNormal=False, maxlen=None):
    geneList = dict()
    expFile = open(fileName, "r")

    assert expFile.readline()

    while True:
        line = expFile.readline()
        if not line: break
        line = line.split("\t")

        gene, val = line[2], float(line[4])

        if wanted is not None:
            if gene not in wanted: continue
        if cutNormal is not False:
            if line[3] == "normal": continue
            elif line[3] == "over" or line[3] == "under": pass
            else: assert False

        if gene in geneList: geneList[gene].append(val)
        else: geneList[gene] = [val]
        if maxlen is not None:
            if maxlen == 0: break
            else: maxlen -= 1
    expFile.close()
    for gene in geneList: geneList[gene].sort()
    return geneList

def geneExpInlier(fileName, threshold=6):
    geneList = dict()
    expFile = open(fileName, "r")

    assert expFile.readline()

    while True:
        line = expFile.readline()
        if not line: break
        line = line.split("\t")
        gene, val = line[2], float(line[4])
        if abs(val) >= threshold: continue
        if gene in geneList: geneList[gene].append(val)
        else: geneList[gene] = [val]
    expFile.close()
    return geneList

def geneExpOutlier(fileName, threshold=6):
    geneList = dict()
    expFile = open(fileName, "r")

    assert expFile.readline()

    while True:
        line = expFile.readline()
        if not line: break
        line = line.split("\t")

        gene, val = line[2], float(line[4])
        if abs(val) < threshold: continue
        elif abs(val) == threshold: assert False
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
