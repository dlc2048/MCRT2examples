import numpy as np
import matplotlib.pyplot as plt

from rt2.scoring import MeshDensity

estepe001 = MeshDensity('mc_estepe_001_dose_i.mdn')
estepe005 = MeshDensity('mc_estepe_005_dose_i.mdn')

zmin = estepe001.extent()[4]
zmax = estepe001.extent()[5]

zbins = np.linspace(zmin, zmax, num=estepe001.shape()[2] + 1)

plt.figure()
plt.step(zbins[:-1], estepe001.data[100, 100])
plt.step(zbins[:-1], estepe005.data[100, 100])

plt.xlabel('Depth from Surface [cm]')
plt.ylabel('Energy Deposition [MeV/cm3/hist]')

plt.legend(['estepe=0.01', 'estepe=0.05'])

plt.savefig('image.png')

plt.show()
