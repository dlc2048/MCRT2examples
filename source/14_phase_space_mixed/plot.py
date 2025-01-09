import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

from rt2.scoring import Cross, MeshTrack

flux_g  = MeshTrack('mc_flux_g.mtr')
spect_g = Cross('mc_spect_g.crs')

plt.figure()
plt.step(spect_g.ebin()[1:], spect_g.data)
plt.xlabel('Energy [MeV]')
plt.ylabel('Flux [#/cm2/MeV/hist]')
plt.savefig('spect_gamma.png')
plt.show()

img, unc, extent = flux_g.extract().image(2, axis=2)

plt.figure()
plt.imshow(img, cmap='jet', origin='lower', extent=extent)
plt.xlabel('Y position [cm]')
plt.ylabel('X position [cm]')
cbar = plt.colorbar()
cbar.set_label('Flux [#/cm2/hist]')
plt.savefig('flux_gamma.png')
plt.show()


flux_e  = MeshTrack('mc_flux_e.mtr')
spect_e = Cross('mc_spect_e.crs')

plt.figure()
plt.step(spect_e.ebin()[1:], spect_e.data)
plt.xlabel('Energy [MeV]')
plt.ylabel('Flux [#/cm2/MeV/hist]')
plt.savefig('spect_electron.png')
plt.show()

img, unc, extent = flux_e.extract().image(2, axis=2)

plt.figure()
plt.imshow(img, cmap='jet', origin='lower', extent=extent)
plt.xlabel('Y position [cm]')
plt.ylabel('X position [cm]')
cbar = plt.colorbar()
cbar.set_label('Flux [#/cm2/hist]')
plt.savefig('flux_electron.png')
plt.show()
