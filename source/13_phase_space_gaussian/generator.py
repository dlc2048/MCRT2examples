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

sig_x = 10
sig_y = 5

data['pid'] = 0  # photon

data['x'] = np.random.normal(loc=x, scale=sig_x, size=n)
data['y'] = np.random.normal(loc=y, scale=sig_y, size=n)
data['z'] = z

data['u'] = 0
data['v'] = 0
data['w'] = 1  # +z direction

data['wee'] = 1  # weight
data['e']   = e

# write data
file = PhaseSpace()
file.append(data)
file.write('ps.bin')
