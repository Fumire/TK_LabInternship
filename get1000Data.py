import threading

def getFileNames(filename):
    nameList = list()
    nameFile = open("./var/" + filename, "r")
    while True:
        line = nameFile.readline()
        if not line: break
        nameList.append(line.strip())
    nameFile.close()
    return nameList

def containOne(chrName):
    for ch in ["chrX", "chrY", "chrM"]:
        if ch == chrName: return True
    else: return False

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
            if containOne(line[0]): continue

            if line[9] == '': continue
            hugo = line[9].split(";")
            for gene in hugo:
                if gene not in ans: ans.append(gene)
        thisFile.close()
    ans.sort()
    return ans

def countSegmentDiploidHugo():
    ans = dict()
    openFileList = getFileNames("cnvSegmentsDiploidBeta.txt")

    for openFile in openFileList:
        thisFile = open("../1000Gene/cnvSegmentsDiploidBeta/" + openFile, "r")
        while True:
            line = thisFile.readline()
            if not line: break
            elif line[0] in ["#", "\n", ">"]: continue
            line = line.split("\t")
            if containOne(line[0]): continue

            if line[9] == "": continue
            hugo = line[9].split(";")
            val = (line[5], line[6])
            for gene in hugo:
                if gene not in ans: ans[gene] = dict()
                if val not in ans[gene]: ans[gene][val] = 1
                else: ans[gene][val] += 1
        thisFile.close()
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
            if containOne(line[0]): continue

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
        #getCalledCNV("../1000Gene/cnvSegmentsDiploidBeta/" + openFile, ans, 6); continue;
        while True:
            line = thisFile.readline()
            if not line: break
            elif line[0] in ["#", "\n", ">"]: continue

            line = line.split("\t")
            if containOne(line[0]): continue

            if line[6] in ans: ans[line[6]].append(int(line[5]))
        thisFile.close()
    return ans

def onlyCNAFromSegmentDiploid():
    ans = list()
    openFileList = getFileNames("cnvSegmentsDiploidBeta.txt")

    for openFile in openFileList:
        thisFile = open("../1000Gene/cnvSegmentsDiploidBeta/" + openFile, "r")
        while True:
            line = thisFile.readline()
            if not line: break
            elif line[0] in ["#", "\n", ">"]: continue

            line = line.split("\t")
            if containOne(line[0]): continue
            elif line[6] not in ["-", "=", "+"]: continue
            ans.append(int(line[5]))
        thisFile.close()
    return ans

def getDetailsDiploidCNA():
    ans = {"-":[], "=":[], "+":[]}
    openFileList = getFileNames("cnvDetailsDiploidBeta.txt")

    for openFile in openFileList:
        thisFile = open("../1000Gene/cnvDetailsDiploidBeta/" + openFile, "r")
        while True:
            line = thisFile.readline()
            if not line: break
            elif line[0] in ["#", "\n", ">"]: continue

            line = line.split("\t")
            if containOne(line[0]): continue

            if line[8] in ans: ans[line[8]].append(int(line[7]))
        thisFile.close()
    return ans

def onlyCNAFromDetailsDiploidCNA():
    ans = list()
    openFileList = getFileNames("cnvDetailsDiploidBeta.txt")

    for openFile in openFileList:
        thisFile = open("../1000Gene/cnvDetailsDiploidBeta/" + openFile, "r")
        while True:
            line = thisFile.readline()
            if not line: break
            elif line[0] in ["#", "\n", ">"]: continue

            line = line.split("\t")
            if containOne(line[0]): continue
            if line[8] not in ["-", "=", "+"]: continue
            ans.append(int(line[7]))
        thisFile.close()
    return ans

if __name__ == "__main__":
    p = getSegmentDiploidHugo(); print(len(p), p[:10]);

    p = getSegmentDiploidCNA()
    print(len(p["-"]), len(p["="]), len(p["+"]))
    for ch in ["-", "=", "+"]:
        print(ch)
        a1, a2 = min(p[ch]), max(p[ch])
        for i in range(a1, a2+1): print(i, p[ch].count(i))

    p = countSegmentDiploidHugo()
    print(len(onlyCNAFromSegmentDiploid()))
    print(sum(list(map(len, (p[gene] for gene in p)))))
    exit()

    p = getDetailsDiploidCNA()
    print(len(p["-"]), len(p["="]), len(p["+"]))
    for ch in ["-", "=", "+"]:
        print(ch)
        a1, a2 = min(p[ch]), max(p[ch])
        for i in range(a1, a2+1): print(i, p[ch].count(i))
