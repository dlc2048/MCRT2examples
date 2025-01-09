import numpy as np
import matplotlib.pyplot as plt

from rt2.scoring import Detector


gebw  = Detector('mc_gebw.det')
gebwo = Detector('mc_gebwo.det')

ebin_gebw  = gebw.ebin()
ebin_gebwo = gebwo.ebin()

plt.step(ebin_gebwo[1:], gebwo.data, 'b')
plt.step(ebin_gebw[1:],  gebw.data, 'magenta')

plt.xlabel('Energy [MeV]')
plt.ylabel('Count [#/hist]')

plt.legend(['Without GEB', 'With GEB'])
plt.yscale('log')

plt.savefig('graph.png')
plt.show()
