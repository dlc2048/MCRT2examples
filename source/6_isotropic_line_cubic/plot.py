import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

from rt2.scoring import Cross, MeshTrack

flux  = MeshTrack('mc_flux.mtr')
spect = Cross('mc_spect.crs')

plt.figure()
plt.step(spect.ebin()[1:], spect.data)
plt.xlabel('Energy [MeV]')
plt.ylabel('Flux [#/cm2/MeV/hist]')
plt.savefig('spect.png')
plt.show()

img, unc, extent = flux.extract().image(0, axis=2)

plt.figure()
plt.imshow(img, cmap='jet', origin='lower', norm=LogNorm(), extent=extent)
plt.xlabel('Y position [cm]')
plt.ylabel('X position [cm]')
cbar = plt.colorbar()
cbar.set_label('Flux [#/cm2/hist]')
plt.savefig('flux.png')
plt.show()
