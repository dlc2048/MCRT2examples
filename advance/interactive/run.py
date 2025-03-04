import subprocess
import time

import numpy as np
import matplotlib.pyplot as plt

from rt2.scoring import MeshDensity, MeshTrack


def replicate(pos: np.ndarray, vec: np.ndarray):
    origin = open('interact_base.inp')
    out    = open('interact_child.inp', mode='w')
    out.write('$POS$  {}  {}  {}\n'.format(pos[0], pos[1], pos[2]))
    out.write('$DIR$  {}  {}  {}\n'.format(vec[0], vec[1], vec[2]))
    for line in origin:
        out.write(line)
    out.close()


def transformMatrix(theta: float):
    cost = np.cos(theta)
    sint = np.sin(theta)
    return np.array(
        [[1,0   ,0    ],
         [0,cost,-sint],
         [0,sint, cost]]
        )


pos  = np.empty(3)
vec  = np.empty(3)
dist = 50

# start RT2interactive
proc = subprocess.Popen(['RT2interactive', '-i', 'mc.inp'],
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        text=True
                        )

# output mirror
while proc.poll() is None:
    message = proc.stdout.readline()
    print(message,end='')
    if message == 'Ready\n':
        break

# rotate 30 degree from 0 to 360
for deg in range(0, 360, 30):
    rad = deg * np.pi / 180
    mat = transformMatrix(rad)
    # pos
    pos[0] = 0
    pos[1] = 0
    pos[2] = -dist
    # vec init
    vec[0] = 0
    vec[1] = 0
    vec[2] = 1
    # rotate
    pos = mat.dot(pos)
    vec = mat.dot(vec)

    # make input
    replicate(pos, vec)
    # launch
    
    proc.stdin.write('-i interact_child.inp\n')
    proc.stdin.flush()
    
    while proc.poll() is None:
        message = proc.stdout.readline()
        print(message,end='')
        if message == 'finished\n':
            break
    
    # get result
    depo = MeshDensity('mc_depo.mdn')

    flux = MeshTrack('mc_xray.mtr')

    plt.imshow(depo.data[50], cmap='jet', origin='lower', extent=(-20,20,-20,20))
    plt.xlabel('Z Position [cm]')
    plt.ylabel('Y Position [cm]')
    plt.savefig('depo_{}.png'.format(deg))
    plt.show()
    
