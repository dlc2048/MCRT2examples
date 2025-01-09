import numpy as np
import matplotlib.pyplot as plt
from rt2.scoring import Cross

dop_on  = Cross('mc_on_nai.det')
dop_off = Cross('mc_off_nai.det')

plt.step(dop_off.ebin()[1:], dop_off.data)
plt.step(dop_on.ebin()[1:],  dop_on.data)

plt.yscale('log')

plt.xlabel('Energy [MeV]')
plt.ylabel('Channel Counts [#/hist]')

plt.legend(['Doppler Off', 'Doppler On'])

plt.savefig('graph.png')

plt.show()
