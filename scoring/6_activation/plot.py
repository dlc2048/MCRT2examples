import numpy as np
import matplotlib.pyplot as plt

from rt2.scoring  import Activation
from rt2.material import AtomList

file = Activation('mc_act.atv')
data = file.data
za   = file.za

z    = za // 1000
a    = za %  1000

def naming(z: int, a: int) -> str:
    return "{}-{}".format(AtomList.symbol(z), a)

legend = list(map(naming, z, a))

plt.bar(legend, data)
plt.ylabel('Activity [#/cm3/hist]')
plt.yscale('log')
plt.savefig('acivity')
plt.show()
