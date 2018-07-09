def RNASeqwithGene(fileName, review=True):
    geneList = dict()
    organList = list()

    RNASeqFile = open(fileName, "r")

    for _ in range(2): assert RNASeqFile.readline()

    for organ in RNASeqFile.readline().split("\t"):
        assert organ not in geneList
        organList.append(organ)

    while True:
        line = RNASeqFile.readline()
        if not line: break
        line = line.split("\t")
        gene = line[0]
        assert gene not in geneList
        geneList[gene] = dict()
        for i, val_i in enumerate(line):
            if i == 0: continue
            if i == 1:
                geneList[gene][organList[i]] = val_i
                continue
            if review and float(val_i) == 0: continue
            geneList[gene][organList[i]] = float(val_i)
    RNASeqFile.close()

    if review:
        geneName = list(geneList.keys())
        for gene in geneName:
            if len(geneList[gene]) == 1:
                del(geneList[gene])

    return geneList

def RNASeqwithOrgan(fileName, review=True):
    organList = dict()
    organName = list()
    RNASeqFile = open(fileName, "r")

    for _ in range(2): assert RNASeqFile.readline()

    for organ in RNASeqFile.readline().split("\t")[2:]:
        assert organ not in organList
        organList[organ] = dict()
        organName.append(organ)

    while True:
        line = RNASeqFile.readline()
        if not line: break
        line = line.split("\t")
        gene = line[0]
        for i, val_i in enumerate(line[2:]):
            assert gene not in organList[organName[i]]
            if review and float(val_i) == 0: continue
            organList[organName[i]][gene] = float(val_i)
    RNASeqFile.close()

    if review:
        for organ in organName:
            if len(organList[organ]) == 0: del(organList[organ])

    return organList

def RNASeqOrganName(fileName):
    organList = dict()
    RNASeqFile = open(fileName, "r")

    for _ in range(2): assert RNASeqFile.readline()

    for i, ch_i in enumerate(RNASeqFile.readline().split("\t")[2:]):
        assert ch_i not in organList
        organList[ch_i] = i
    RNASeqFile.close()

    return organList

def RNASeqGeneName(fileName):
    geneList = dict()
    RNASeqFile = open(fileName, "r")

    for _ in range(2): assert RNASeqFile.readline()

    seq = 0
    while True:
        line = RNASeqFile.readline()
        if not line: break
        gene = line.split("\t")[:2]
        gene = str(gene[0]) + "+" + str(gene[1])
        try: assert gene not in geneList
        except:
            print(gene, geneList[gene], seq)
            seq += 1
        geneList[gene] = seq
        seq += 1
    RNASeqFile.close()

    return geneList

def selectedGene(fileName, geneNum):
    geneList = dict()
    organList = list()
    RNASeqFile = open(fileName, "r")

    for _ in range(2): assert RNASeqFile.readline()

    for organ in RNASeqFile.readline().split("\t"):
        organList.append(organ)

    for _ in range(geneNum, 0, -1): assert RNASeqFile.readline()

    for i, val_i in enumerate(RNASeqFile.readline().split("\t")):
        if i<2: geneList[organList[i]] = val_i
        else: geneList[organList[i]] = float(val_i)
    RNASeqFile.close()
    return geneList

def selectedOrgan(fileName, organNum):
    organList = dict()
    RNASeqFile = open(fileName, "r")

    for _ in range(2+1): assert RNASeqFile.readline()

    while True:
        line = RNASeqFile.readline()
        if not line: break
        line = line.split("\t")
        organList[line[0]] = float(line[organNum+2])
    RNASeqFile.close()
    return organList

def selectedGeneOrgan(fileName, geneNum, organNum):
    with open(fileName, "r") as RNASeqFile:
        for _ in range(2+1): assert RNASeqFile.readline()
        for _ in range(geneNum, 0, -1): assert RNASeqFile.readline()
        return float(RNASeqFile.readline().split("\t")[2+organNum])

if __name__ == "__main__":
    #name = "../GTEx/RNA-Seq/GTEx_Analysis_2016-01-15_v7_RNASeQCv1.1.8_gene_tpm.gct"
    name = "../GTEx/RNA-Seq/GTEx_Analysis_2016-01-15_v7_STARv2.4.2a_junctions.gct"
    organList = RNASeqOrganName(name); print(len(organList));
    geneList = RNASeqGeneName(name); print(len(geneList));
    selGene = selectedGene(name, 1234); print(len(selGene));
    selOrgan = selectedOrgan(name, 33); print(len(selOrgan));
    selGeneOrgan = selectedGeneOrgan(name, 1234, 33); print(selGeneOrgan);
