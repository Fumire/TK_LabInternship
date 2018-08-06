import matplotlib as mpl
mpl.use('Agg')
mpl.rcParams.update({'font.size': 20})
import matplotlib.pyplot as plt
import numpy as np
import getCNAData as cna
import time
import sys

ans = dict()
now = time.strftime("%m%d%H%M%S")

if True:
    data = cna.onlyCNAFromCosmicPair("../COSMIC/CosmicCompleteCNA.tsv", 2)
    HUGOs = list(data.keys())
    for i, gene in enumerate(HUGOs):
        for j in data[gene].values():
            if (i, j) in ans:
                ans[(i, j)] += 1
            else:
                ans[(i, j)] = 1
    del data
    with open('./var/' + sys.argv[0] + '.pckl', 'wb') as f:
        pickle.dump(ans, f, pickle.HIGHEST_PROTOCOL)
else:
    with open('./var/' + sys.argv[0] + '.pckl', 'rb') as f:
        ans = pickle.load(f)
