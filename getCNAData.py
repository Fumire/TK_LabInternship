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
    patient = CNAwithPatient(name, False)
    mutation = CNAwithHugo(name, False)
    print(len(patient), len(mutation))
