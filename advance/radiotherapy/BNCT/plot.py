import matplotlib.pyplot as plt
import matplotlib.lines as mlines
from matplotlib.gridspec import GridSpec
import numpy as np

from rt2.scoring import MeshDensity
from rt2.voxel import Voxel
from rt2.algorithm import Affine

plt.rcParams['font.family'] = 'Arial'

# CT data
ct   = Voxel('voxel.vxl')
# NIFTI affine
affine = Affine(
    np.array(
        [[-1, 0, 0, 0],
         [0, -1, 0, 0],
         [0,  0, 1, 0],
         [0,  0, 0, 1]]
        )
    )
ct.transform(affine)
ct.flip(axis=1)
head = ct[:,:,180:180+42]

# air mask
mask = head.mask('RFAIR')

rt2_em = (
    MeshDensity("mc_md1.mdn") +    
    MeshDensity("mc_md2.mdn") +
    MeshDensity("mc_md3.mdn")
    )
rt2_em.data[mask] = 0

rt2_ion = (
    MeshDensity("mc_md4.mdn") +    
    MeshDensity("mc_md5.mdn")
    )
rt2_ion.data[mask] = 0

rt2_total = rt2_em + rt2_ion

fluka_em    = MeshDensity("ref_31_dose_em.mdn")    * 1e3  # MeV
fluka_em.data[mask] = 0
fluka_total = MeshDensity("ref_30_dose.mdn") * 1e3  # MeV
fluka_total.data[mask] = 0
fluka_ion = fluka_total - fluka_em

levels = [10, 20, 30, 40, 50, 60, 70, 80, 90]

fig = plt.figure(figsize=(9,11.5))
gs = GridSpec(3, 2, height_ratios=[1.3,1.3,1])
ax1 = fig.add_subplot(gs[0])
ax2 = fig.add_subplot(gs[1])
ax3 = fig.add_subplot(gs[2])
ax4 = fig.add_subplot(gs[3])
ax5 = fig.add_subplot(gs[4])
ax6 = fig.add_subplot(gs[5])


#### 2d contour zx ####

pos  = 14
axis = 1

# em

img1, err1, extent = rt2_ion.image(pos, axis)
img2, err2, extent = fluka_ion.image(pos, axis)
img_ct, extent_ct = ct.image(pos, axis)

img1 = img1 / np.max(rt2_ion.data) * 100
img2 = img2 / np.max(rt2_ion.data) * 100

extent = (extent[0] - 23.7, extent[1] - 23.7, extent[2] - 169.4, extent[3] - 169.4)
extent_ct = (extent_ct[0] - 23.7, extent_ct[1] - 23.7, extent_ct[2] - 169.4, extent_ct[3] - 169.4)

ax1.set_aspect(1)
ax1.imshow(img_ct, cmap='gray', extent=extent_ct, origin='lower', alpha=0.5)
cs = ax1.contour(img2, cmap="jet", extent=extent, levels=levels,
                origin='lower', linestyles='solid', nchunk=3)
ax1.contour(img1, extent=extent, levels=levels,
                origin='lower', colors='k', linestyles='dotted', nchunk=3)

ax1.set_xticklabels([])
ax1.set_ylabel("Vertical Position (cm)")

handles = []
labels = []
for i in range(len(levels)):
    color = cs.collections[i].get_edgecolor()
    handles += [mlines.Line2D([], [], color=color, label="{} %".format(levels[i]))]
    labels += ['{} %'.format(levels[i])]
ax1.legend(handles, labels)
ax1.text(.03, .97, '(a)', ha='left', va='top',
         transform=ax1.transAxes, fontsize=14)
ax1.set_xlim(-7, 7)
ax1.set_ylim(-7, 7)


#### 2d contour yz ####

pos  = 23.7
axis = 0

# em

img1, err1, extent = rt2_ion.image(pos, axis)
img2, err2, extent = fluka_ion.image(pos, axis)
img_ct, extent_ct = ct.image(pos, axis)

img1 = img1 / np.max(rt2_ion.data) * 100
img2 = img2 / np.max(rt2_ion.data) * 100

extent = (extent[2] - 14, extent[3] - 14, extent[0] - 169.4, extent[1] - 169.4)
extent_ct = (extent_ct[2] - 14, extent_ct[3] - 14, extent_ct[0] - 169.4, extent_ct[1] - 169.4)

img1 = np.transpose(img1)
img2 = np.transpose(img2)
img_ct = np.transpose(img_ct)

ax2.set_aspect(1)
ax2.set_xlim(-7, 7)
ax2.set_ylim(-7, 7)

ax2.imshow(img_ct, cmap='gray', extent=extent_ct, origin='lower', alpha=0.5)
cs = ax2.contour(img2, cmap="jet", extent=extent, levels=levels,
                origin='lower', linestyles='solid', nchunk=3)
ax2.contour(img1, extent=extent, levels=levels,
                origin='lower', colors='k', linestyles='dotted', nchunk=3)

ax2.set_xticklabels([])
ax2.set_yticklabels([])

handles = []
labels = []
for i in range(len(levels)):
    color = cs.collections[i].get_edgecolor()
    handles += [mlines.Line2D([], [], color=color, label="{} %".format(levels[i]))]
    labels += ['{} %'.format(levels[i])]
# ax2.legend(handles, labels)
ax2.text(.03, .97, '(b)', ha='left', va='top',
         transform=ax2.transAxes, fontsize=14)


#### 2d contour zx ####

pos  = 14
axis = 1

img1, err1, extent = rt2_em.image(pos, axis)
img2, err2, extent = fluka_em.image(pos, axis)
img_ct, extent_ct = ct.image(pos, axis)

img1 = img1 / np.max(rt2_em.data) * 100
img2 = img2 / np.max(rt2_em.data) * 100

extent = (extent[0] - 23.7, extent[1] - 23.7, extent[2] - 169.4, extent[3] - 169.4)
extent_ct = (extent_ct[0] - 23.7, extent_ct[1] - 23.7, extent_ct[2] - 169.4, extent_ct[3] - 169.4)

ax3.set_aspect(1)
ax3.imshow(img_ct, cmap='gray', extent=extent_ct, origin='lower', alpha=0.5)
cs = ax3.contour(img2, cmap="jet", extent=extent, levels=levels,
                origin='lower', linestyles='solid', nchunk=3)
ax3.contour(img1, extent=extent, levels=levels,
                origin='lower', colors='k', linestyles='dotted', nchunk=3)

ax3.set_xticklabels([])
ax3.set_ylabel("Vertical Position (cm)")

handles = []
labels = []
for i in range(len(levels)):
    color = cs.collections[i].get_edgecolor()
    handles += [mlines.Line2D([], [], color=color, label="{} %".format(levels[i]))]
    labels += ['{} %'.format(levels[i])]
# ax1.legend(handles, labels)
ax3.text(.03, .97, '(c)', ha='left', va='top',
         transform=ax3.transAxes, fontsize=14)
ax3.set_xlim(-7, 7)
ax3.set_ylim(-7, 7)


#### 2d contour yz ####

pos  = 23.7
axis = 0

# em

img1, err1, extent = rt2_em.image(pos, axis)
img2, err2, extent = fluka_em.image(pos, axis)
img_ct, extent_ct = ct.image(pos, axis)

img1 = img1 / np.max(rt2_em.data) * 100
img2 = img2 / np.max(rt2_em.data) * 100

extent = (extent[2] - 14, extent[3] - 14, extent[0] - 169.4, extent[1] - 169.4)
extent_ct = (extent_ct[2] - 14, extent_ct[3] - 14, extent_ct[0] - 169.4, extent_ct[1] - 169.4)

img1 = np.transpose(img1)
img2 = np.transpose(img2)
img_ct = np.transpose(img_ct)

ax4.set_aspect(1)
ax4.set_xlim(-7, 7)
ax4.set_ylim(-7, 7)

ax4.imshow(img_ct, cmap='gray', extent=extent_ct, origin='lower', alpha=0.5)
cs = ax4.contour(img2, cmap="jet", extent=extent, levels=levels,
                origin='lower', linestyles='solid', nchunk=3)
ax4.contour(img1, extent=extent, levels=levels,
                origin='lower', colors='k', linestyles='dotted', nchunk=3)

ax4.set_xticklabels([])
ax4.set_yticklabels([])

handles = []
labels = []
for i in range(len(levels)):
    color = cs.collections[i].get_edgecolor()
    handles += [mlines.Line2D([], [], color=color, label="{} %".format(levels[i]))]
    labels += ['{} %'.format(levels[i])]
# ax2.legend(handles, labels)
ax4.text(.03, .97, '(d)', ha='left', va='top',
         transform=ax4.transAxes, fontsize=14)



#### 1d, depth-dose ####

xmean        = np.arange(0,254,1) * 0.2137 - 23.7

rt2_total_1d = rt2_total.data[:,65,32]
rt2_ion_1d   = rt2_ion.data[:,65,32]
rt2_em_1d    = rt2_em.data[:,65,32]

fluka_total_1d = fluka_total.data[:,65,32]
fluka_ion_1d   = fluka_ion.data[:,65,32]
fluka_em_1d    = fluka_em.data[:,65,32]

twin = ax5.twinx()
ax5.plot(xmean, fluka_total_1d * 1e4, "b")
ax5.plot(xmean, rt2_total_1d * 1e4,   "k^", markersize=2)
ax5.plot(xmean, fluka_ion_1d * 1e4,   "g")
ax5.plot(xmean, rt2_ion_1d * 1e4,     "k>", markersize=2)
ax5.plot(xmean, fluka_em_1d * 1e4,    "m")
ax5.plot(xmean, rt2_em_1d * 1e4,      "ko", markersize=2)
ax5.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
ax5.set_ylabel("Dose (10$^{-4}$ MeV/g/hist)")
ax5.set_xlabel("Lateral Position (cm)")
ax5.legend(["FLUKA, Total", "RT$^2$, Total", "FLUKA, Ion",
            "RT$^2$, Ion", "FLUKA, Gamma", "RT$^2$, Gamma"])

rel_dif = np.divide((rt2_total_1d - fluka_total_1d), np.max(fluka_total.data),
                    out=np.zeros_like(fluka_total_1d), where=fluka_total_1d!=0) * 100

twin.plot(xmean, rel_dif, "r--")
twin.set_ylim(bottom=-5, top=10)
twin.set_yticklabels([])
twin.hlines(y=0, xmin=-100, xmax=100, colors='r')
ax5.set_xlim(-7, 7)
ax5.set_ylim(0,6)
ax5.text(.03, .97, '(e)', ha='left', va='top',
         transform=ax5.transAxes, fontsize=14)

#### 1d, lateral-dose ####

xmean        = np.arange(0,127,1) * 0.2137 - 14

rt2_total_1d = rt2_total.data[110,:,32]
rt2_ion_1d   = rt2_ion.data[110,:,32]
rt2_em_1d    = rt2_em.data[110,:,32]

fluka_total_1d = fluka_total.data[110,:,32]
fluka_ion_1d   = fluka_ion.data[110,:,32]
fluka_em_1d    = fluka_em.data[110,:,32]

twin = ax6.twinx()
ax6.plot(xmean, fluka_total_1d * 1e4, "b")
ax6.plot(xmean, rt2_total_1d * 1e4,   "k^", markersize=2)
ax6.plot(xmean, fluka_ion_1d * 1e4,   "g")
ax6.plot(xmean, rt2_ion_1d * 1e4,     "k>", markersize=2)
ax6.plot(xmean, fluka_em_1d * 1e4,    "m")
ax6.plot(xmean, rt2_em_1d * 1e4,      "ko", markersize=2)
ax6.ticklabel_format(axis='y', style='sci', scilimits=(0,0))
ax6.set_ylabel("Dose (MeV/g/hist)")
ax6.set_xlabel("Longitudinal Position (cm)")
#ax6.legend(["FLUKA, Total", "This Work, Total", "FLUKA, Ion",
#            "This Work, Ion", "FLUKA, Gamma", "This Work, Gamma"])

rel_dif = np.divide((rt2_total_1d - fluka_total_1d), np.max(fluka_total.data),
                    out=np.zeros_like(fluka_total_1d), where=fluka_total_1d!=0) * 100

twin.plot(xmean, rel_dif, "r--")
twin.set_ylim(bottom=-5, top=10)
twin.hlines(y=0, xmin=-50, xmax=50, colors='r')
twin.set_ylabel("Dose difference (%)")
ax6.set_xlim(-7,7)
ax6.set_ylim(0,6)
ax6.set_yticklabels([])
ax6.text(.03, .97, '(f)', ha='left', va='top',
         transform=ax6.transAxes, fontsize=14)

plt.tight_layout()
plt.savefig('bench.svg')
plt.show()
