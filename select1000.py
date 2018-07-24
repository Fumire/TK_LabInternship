from get1000Data import *

openFileList = getFileNames("cnvSegmentsDiploidBeta.txt")
for openFile in openFileList:
    thisFile = open("../1000Gene/cnvSegmentsDiploidBeta/" + openFile, "r")
    while True:
        line = thisFile.readline()
        if not line: break
        elif line[0] in ["#", "\n", ">"]: continue
        if containOne(line.split("\t")[0]): continue

        if "1\t=" in line or "2\t+" in line:
            print(line.split("\t"))
