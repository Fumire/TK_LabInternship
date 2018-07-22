def getFileNames(filename):
    nameList = list()
    nameFile = open("./var/" + filename, "r")
    while True:
        line = nameFile.readline()
        if not line: break
        nameList.append(line.strip())
    nameFile.close()
    return nameList

def getSegmentDiploidHugo():
    ans = list()
    openFileList = getFileNames("cnvSegmentsDiploidBeta.txt")

    for openFile in openFileList:
        thisFile = open("../1000Gene/cnvSegmentsDiploidBeta/" + openFile, "r")
        while True:
            line = thisFile.readline()
            if not line: break
            elif line[0] in ["#", "\n", ">"]: continue
            line = line.split("\t")

            if line[9] == '': continue
            hugo = line[9].split(";")
            for gene in hugo:
                if gene not in ans: ans.append(gene)
        thisFile.close()
    ans.sort()
    return ans

def getSegmentNondiploidHugo():
    ans = list()
    openFileList = getFileNames("cnvSegmentsNondiploidBeta.txt")

    for openFile in openFileList:
        thisFile = open("../1000Gene/cnvSegmentsNondiploidBeta/" + openFile, "r")
        while True:
            line = thisFile.readline()
            if not line: break
            elif line[0] in ["#", "\n", ">"]: continue
            line = line.split("\t")

            if line[9] == '': continue
            hugo = line[9].split(";")
            for gene in hugo:
                if gene not in ans: ans.append(gene)
            thisFile.close()
    ans.sort()
    return ans

def getSegmentDiploidCNA():
    ans = {"-":[], "=":[], "+":[]}
    openFileList = getFileNames("cnvSegmentsDiploidBeta.txt")

    for openFile in openFileList:
        thisFile = open("../1000Gene/cnvSegmentsDiploidBeta/" + openFile, "r")
        while True:
            line = thisFile.readline()
            if not line: break
            elif line[0] in ["#", "\n", ">"]: continue
            line = line.split("\t")

            if line[6] in ans: ans[line[6]].append(int(line[5]))
        thisFile.close()
    return ans

def getSegmentNondiploidCNA():
    ans = {"-":[], "=":[], "+":[]}
    openFileList = getFileNames("cnvSegmentsNondiploidBeta.txt")

    for openFile in openFileList:
        thisFile = open("../1000Gene/cnvSegmentsNondiploidBeta/" + openFile, "r")
        while True:
            line = thisFile.readline()
            if not line: break
            elif line[0] in ["#", "\n", ">"]: continue
            line = line.split("\t")

            if line[6] in ans: ans[line[6]].append(int(line[5]))
        thisFile.close()
    return ans

if __name__ == "__main__":
    p = getSegmentDiploidHugo(); print(len(p), p[:10]);
    p = getSegmentDiploidHugo(); print(len(p), p[:10]);

    p = getSegmentDiploidCNA()
    print(len(p["-"]), len(p["="]), len(p["+"]))
    a1, a2 = min(p["="]), max(p["="])
    for i in range(a1, a2+1): print(i, p["="].count(i))

    p = getSegmentNondiploidCNA()
    print(len(p["-"]), len(p["="]), len(p["+"]))
    a1, a2 = min(p["="]), max(p["="])
    for i in range(a1, a2+1): print(i, ["="].count(i))