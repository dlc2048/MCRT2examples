import numpy as np

from rt2.scoring  import PhaseSpace
from rt2.particle import DTYPE_PHASE_SPACE

# set empty numpy array for score phase-space
n = 5000000
data = np.empty(n, dtype=DTYPE_PHASE_SPACE)

# monodirection +z, 0,0,0 center and x,y gaussian

x = 0
y = 0
z = 0

e = 1.25  # 1.25 MeV photon

sig_x_g = 10
sig_y_g = 5

sig_x_e = 2
sig_y_e = 8

# 80% photon / 20% electron
thres = 0.8
mask = np.random.random(n) < thres

data['pid'][mask]  = 0   # photon
data['pid'][~mask] = -1  # electron

data['x'] = np.random.normal(loc=x, scale=1, size=n)
data['y'] = np.random.normal(loc=y, scale=1, size=n)
data['z'] = z

data['x'][mask]  *= sig_x_g
data['y'][mask]  *= sig_y_g
data['x'][~mask] *= sig_x_e
data['y'][~mask] *= sig_y_e

data['u'] = 0
data['v'] = 0
data['w'] = 1  # +z direction

data['wee'] = 1  # weight
data['e']   = e

# write data
file = PhaseSpace()
file.append(data)
file.write('ps.bin')
