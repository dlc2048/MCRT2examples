import matplotlib.pyplot as plt
import numpy as np

from rt2.scoring import MeshTrack

xray    = MeshTrack('mc_image.mtr').extract()

xray_img,    xray_unc,    xray_extent    = xray.image(-10, axis=2)

plt.figure()
plt.title('XRAY')
plt.imshow(xray_img, cmap='gray', origin='lower', extent=xray_extent)
plt.xlabel('Off-axis distance Y [cm]')
plt.ylabel('Off-axis distance X [cm]')

cbar = plt.colorbar()
cbar.set_label('Photon fluence [#/cm2/hist]')

plt.savefig('xray.png')
plt.show()

