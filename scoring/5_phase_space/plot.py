import numpy as np
import matplotlib.pyplot as plt

from rt2.scoring import PhaseSpace

file = PhaseSpace('mc_bremss.phs')
data = file.data()

photon = data[data['pid'] == 0]

# print first 10 phase-space

for i in range(10):
    print("PS{}\tcost={:.6}\t\tenergy={:.6}".format(i, photon[i]['w'], photon[i]['e']))

# energy histogram
ebins = np.linspace(0,10,101)
plt.hist(photon['e'], bins=ebins)

plt.xlabel('Energy [MeV]')
plt.ylabel('Counts')
plt.tight_layout()
plt.savefig('graph.png')
plt.show()
