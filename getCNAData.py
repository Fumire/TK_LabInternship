def CNAFromCosmic(fileName):
    geneList = dict()
    cnaFile = open(fileName, "r")

    indexList = cnaFile.readline().split("\t")

    while True:
        line = cnaFile.readline()
        if not line: break
        line = line.split("\t")
        gene = line[0] + "+" + line[1]
        assert gene not in geneList
        geneList[gene] = dict()
        for i, val_i in enumerate(line):
            if i < 2: continue
            geneList[gene][indexList[i]] = val_i
    cnaFile.close()
    return geneList

def onlyCNAFromCosmic(fileName, see=None):
    geneList = dict()
    cnaFile = open(fileName, "r")

    for _ in range(1): assert cnaFile.readline()

    while True:
        line = cnaFile.readline()
        if not line: break

        line = line.split("\t")
        gene = line[0] + "+" + line[1]
        if see is not None: gene = line[see] + "+" + gene

        assert gene not in geneList

        if line[14] == '': line[14] = 0
        if line[15] == '': line[15] = 0

        if line[16] == "gain": geneList[gene] = (float(line[14]))
        elif line[16] == "loss": geneList[gene] = -(float(line[14]))
        else: assert False
    cnaFile.close()
    return geneList

def handCNAFromCosmic(fileName):
    data = onlyCNAFromCosmic(fileName)
    ans = dict()

    for gene, val in data.items():
        name = gene.split("+")[1]
        if (name, val) in ans: ans[(name, val)] += 1
        else: ans[(name, val)] = 1

    return ans

def CNAwithPatient(fileName, review=True):
    patient = dict()
    nameList = list()

    cnaFile = open(fileName, "r")

    for name in cnaFile.readline().split():
        assert name not in patient
        patient[name] = dict()
        nameList.append(name)

    while True:
        line = cnaFile.readline()
        if not line: break
        line = line.split()
        Hugo = line[0]
        for i, val_i in enumerate(line):
            if i == 0: continue
            if review and float(val_i) == 0.0: continue
            patient[nameList[i]][Hugo] = float(val_i)
    cnaFile.close()

    if review:
        for name in nameList:
            if len(patient[name]) == 0: del(patient[name])

    return patient

def CNAonlyGene(fileName):
    nameList = list()
    cnaFile = open(fileName, "r")

    assert cnaFile.readline()

    while True:
        line = cnaFile.readline()
        if not line: break
        line = line.split("\t")[0]
        if line not in nameList: nameList.append(line)
    cnaFile.close()
    return nameList

def CNAwithHugo(fileName, review=True):
    mutation = dict()
    nameList = list()

    cnaFile = open(fileName, "r")

    nameList = cnaFile.readline().split()

    while True:
        line = cnaFile.readline()
        if not line: break
        line = line.split()
        Hugo = line[0]
        assert Hugo not in mutation
        mutation[Hugo] = dict()

        for i, val_i in enumerate(line):
            if i == 0: continue
            if review and float(val_i) == 0: continue
            mutation[Hugo][nameList[i]] = float(val_i)

        if review:
            if len(mutation[Hugo]) == 0: del(mutation[Hugo])
    cnaFile.close()
    return mutation

if __name__ == "__main__":
    name = "../msk_impact_2017/data_CNA.txt"
    #patient = CNAwithPatient(name, False); print(len(patient));
    #mutation = CNAwithHugo(name, False); print(len(mutation));
    #cosmic = onlyCNAFromCosmic("../COSMIC/CosmicCompleteCNA.tsv"); print(len(cosmic)); del cosmic;
    handle = onlyCNAFromCosmic("../COSMIC/CosmicCompleteCNA.tsv");
