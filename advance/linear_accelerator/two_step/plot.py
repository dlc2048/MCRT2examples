import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

from rt2.scoring import Cross, MeshTrack, MeshDensity

# flux, first step
flux = MeshTrack('mc_first_xray.mtr')
img  = np.transpose(flux.data[50,:,:,0])
plt.imshow(img, norm=LogNorm(), cmap='jet', origin='lower', extent=(-100,100,-100,100))
plt.title('Photon Flux (first)')
plt.xlabel('Y Position [cm]')
plt.ylabel('Z Position [cm]')

cbar = plt.colorbar()
cbar.set_label('Flux [#/cm2/hist]')

plt.savefig('flux_first.png')

plt.show()

# flux, second step
flux = MeshTrack('mc_second_xray.mtr')
img  = np.transpose(flux.data[50,:,:,0])
plt.imshow(img, norm=LogNorm(), cmap='jet', origin='lower', extent=(-100,100,-100,100))
plt.title('Photon Flux (second)')
plt.xlabel('Y Position [cm]')
plt.ylabel('Z Position [cm]')

cbar = plt.colorbar()
cbar.set_label('Flux [#/cm2/hist]')

plt.savefig('flux_second.png')

plt.show()

# spectrum
spect = Cross('mc_first_xspect_phantom.crs')

ebin = spect.ebin()

plt.step(ebin[1:], spect.data, 'r')

plt.xlabel('Photon Energy [MeV]')
plt.ylabel('Fluence [#/cm2/MeV/hist]')

plt.savefig('spect.png')

plt.show()

levels = [10, 20, 30, 40, 50, 60, 70, 80, 90]

depo = MeshDensity('mc_second_depo_elect.mdn') + MeshDensity('mc_second_depo_gamma.mdn') + MeshDensity('mc_second_depo_posit.mdn')
img  = np.transpose(depo.data[50])
img  = img / np.max(img) * 100

plt.gca().set_aspect('equal')
plt.contour(img, cmap='jet', extent=(-50,50,-100,0), levels=levels, origin='lower', linestyles='solid', nchunk=3)
plt.xlabel('Y Position [cm]')
plt.ylabel('Z Position [cm]')

plt.savefig('dose.png')

plt.show()


