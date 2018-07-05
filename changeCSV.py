import sys

for name in sys.argv[1:]:
    txtFileName = name.strip()
    csvFileName = txtFileName[:txtFileName.rfind(".")] + ".csv"

    txtFile = open(txtFileName, "r")
    csvFile = open(csvFileName, "w")

    #while True:
    for _ in range(200):
        line = txtFile.readline()
        if not line: break
        elif line[0] == "#":
            #csvFile.write(line)
            continue;
        else:
            line = line.replace("\t", ",")
            csvFile.write(line)

    txtFile.close()
    csvFile.close()
