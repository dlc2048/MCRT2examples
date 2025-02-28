import matplotlib.pyplot as plt
import numpy as np

from rt2.scoring import MeshDensity

tot  = MeshDensity('mc_all.mdn') * 1000
em   = MeshDensity('mc_em.mdn') * 1000
ion  = MeshDensity('mc_hadron.mdn') * 1000
h1   = MeshDensity('mc_hydrogen.mdn') * 1000
he   = MeshDensity('mc_he.mdn') * 1000
li   = MeshDensity('mc_li.mdn') * 1000

other = ion - h1 - he - li

x = np.linspace(0,20,101)
x = 0.5 * (x[1:] + x[:-1])

plt.plot(x, np.mean(tot.data[45:55,45:55], axis=(0,1)))
plt.plot(x, np.mean(em.data[45:55,45:55], axis=(0,1)))
plt.plot(x, np.mean(ion.data[45:55,45:55], axis=(0,1)))
plt.plot(x, np.mean(h1.data[45:55,45:55], axis=(0,1)))
plt.plot(x, np.mean(he.data[45:55,45:55], axis=(0,1)))
plt.plot(x, np.mean(li.data[45:55,45:55], axis=(0,1)))
plt.legend(['Total', 'EM', 'Ion', 'Proton', 'Helium', 'Lithium'])

plt.title('15 ppm B-10 water + 10 keV neutron')

plt.xlabel('Depth from surface [cm]')
plt.ylabel('Energy [keV/cm3/hist]')
plt.savefig('graph')

plt.show()

