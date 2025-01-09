import numpy as np
import matplotlib.pyplot as plt
from rt2.scoring import Cross

vac_on  = Cross('mc_on_nai.det')
vac_off = Cross('mc_off_nai.det')

plt.step(vac_on.ebin()[1:],  vac_on.data)
plt.step(vac_off.ebin()[1:], vac_off.data)
plt.yscale('log')

plt.xlabel('Energy [MeV]')
plt.ylabel('Channel Counts [#/hist]')

plt.legend(['Relaxation On', 'Relaxation Off'])

plt.savefig('graph.png')

plt.show()
