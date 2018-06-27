from multiprocessing.pool import ThreadPool

def RNASeqwithGene(fileName, review=True):
    geneList = dict()
    organList = list()

    RNASeqFile = open(fileName, "r")
    
    for _ in range(2): RNASeqFile.readline()

    for organ in RNASeqFile.readline().split("\t")[:]:
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
    
    for _ in range(2): RNASeqFile.readline()

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

if __name__ == "__main__":
    name = "./GTEx/RNA-Seq/GTEx_Analysis_2016-01-15_v7_RNASeQCv1.1.8_gene_median_tpm.gct"
    pool1 = ThreadPool(processes=1)
    pool2 = ThreadPool(processes=2)

    asyncResult1 = pool1.apply_async(RNASeqwithGene, (name, False))
    asyncResult2 = ThreadPool(processes=1).apply_async(RNASeqwithOrgan, (name, False))

    withGene = asyncResult1.get()
    withOrgan = asyncResult2.get()
    print(len(withOrgan), len(withGene))
