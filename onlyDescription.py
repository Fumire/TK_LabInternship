import sys

txtFileName = sys.argv[1]
dscFileName = txtFileName[:txtFileName.rfind(".")] + "_description.txt"

txtFile = open(txtFileName, "r")
dscFile = open(dscFileName, "w")

while True:
    line = txtFile.readline()
    if not line: break
    elif line[0] == "#":
        dscFile.write(line[1:])
    else:
        continue

txtFile.close()
dscFile.close()
