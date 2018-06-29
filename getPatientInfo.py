def interpret(kind, value):
    if "NA": return None
    answer = {"SEX": {True: "Male", False: "Female"},
            "VITAL_STATUS": {True: "ALIVE", False: "DECEASED"},
            "SMOKING_HISTORY": {1: "Prev/Curr Smoker", 0: "Never", -1: "Unknown"},
            "OS_STATUS": {True: "LIVING", False: "DECEASED"}
            }
    return answer[kind][value]

def getPatientInfo(fileName, review=True):
    patient = dict()
    infomations = list()
    infomationsFile = open(fileName, "r")

    for _ in range(4): assert infomationsFile.readline()

    infomations = infomationsFile.readline().split()
    
    while True:
        line = infomationsFile.readline()
        if not line: break
        line = line.strip().split("\t")
        
        name = None
        for i, val_i in enumerate(line):
            if i == 0:
                assert val_i not in patient
                patient[val_i] = dict()
                name = val_i
            elif i == 1:
                if val_i == "Male": patient[name][infomations[i]] = True
                elif val_i == "Female": patient[name][infomations[i]] = False
                else: raise WrongSexInfo
            elif i == 2 or i == 5:
                if val_i == "ALIVE" or val_i == "LIVING": patient[name][infomations[i]] = True
                elif val_i == "DECEASED": patient[name][infomations[i]] = False
                elif val_i == "NA": patient[name][infomations[i]] = val_i
                else: raise WrongAliveInfo
            elif i == 3:
                if val_i == "Prev/Curr Smoker": patient[name][infomations[i]] = 1
                elif val_i == "Never": patient[name][infomations[i]] = 0
                elif val_i == "Unknown": patient[name][infomations[i]] = 0
                elif val_i == "NA": patient[name][infomations[i]] = val_i
                else: raise WrongSmokingInfo
            elif i == 4:
                if val_i == "NA": patient[name][infomations[i]] = val_i
                else: patient[name][infomations[i]] = float(val_i)
            else: raise WrongInfo
    infomationsFile.close()
    return patient

if __name__ == "__main__":
    info = getPatientInfo("./msk_impact_2017/data_clinical_patient.txt")
    print(len(info))
