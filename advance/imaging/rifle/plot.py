import matplotlib.pyplot as plt
import numpy as np

from rt2.scoring import MeshTrack

xray    = MeshTrack('mc_xray_image.mtr').extract()
neutron = MeshTrack('mc_neutron_image.mtr').extract()

xray_img,    xray_unc,    xray_extent    = xray.image(10, axis=0)
neutron_img, neutron_unc, neutron_extent = neutron.image(10, axis=0)


plt.figure(figsize=(12, 4))
plt.title('XRAY')
plt.imshow(xray_img, cmap='gray', origin='lower', extent=xray_extent)
plt.xlabel('Off-axis distance Z [cm]')
plt.ylabel('Off-axis distance Y [cm]')

cbar = plt.colorbar()
cbar.set_label('Photon fluence [#/cm2/hist]')

plt.savefig('xray.png')
plt.show()


plt.figure(figsize=(12, 4))
plt.title('NEUTRON')
plt.imshow(neutron_img, cmap='gray', origin='lower', extent=neutron_extent)
plt.xlabel('Off-axis distance Z [cm]')
plt.ylabel('Off-axis distance Y [cm]')

cbar = plt.colorbar()
cbar.set_label('Neutron fluence [#/cm2/hist]')

plt.savefig('neutron.png')
plt.show()

