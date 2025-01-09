from textwrap import wrap

import numpy as np
import matplotlib.pyplot as plt


class Neutron:
    def __init__(self, file_name: str):
        first_hit  = True
        draw       = []
        with open(file_name) as file:
            for line in file:
                if first_hit:
                    repr_raw  = wrap(line, 16)
                    first_hit = False
                    continue
                draw += [list(map(float, line.split()))]
        self._draw = np.array(draw)

        rraw = []
        for i in range(3, len(repr_raw)):
            rraw += [repr_raw[i].split()[0]]
        self._repr = rraw

    def elow(self):
        return self._draw[:,1]

    def ehigh(self):
        return self._draw[:,2]

    def nbranch(self):
        return len(self._repr)

    def repr(self, i: int):
        return self._repr[i]

    def xs(self, i: int):
        return self._draw[:,i+3]


def plotNeutron(xs: Neutron, file_name: str, unit: str):
    plt.figure()
    legend = []
    for i in range(xs.nbranch()):
        legend += [xs.repr(i)]
        plt.step(xs.ehigh(), xs.xs(i), where='post')
    plt.xlabel('Energy [MeV]')
    plt.ylabel('Cross-Section {}'.format(unit))
    plt.xscale('log')
    plt.yscale('log')
    plt.legend(legend, loc='upper right')
    plt.savefig(file_name)
    plt.show()


# Macro

tungsten = Neutron('mc_neutron_tungsten.xs')
water    = Neutron('mc_neutron_water.xs')

plotNeutron(tungsten, 'macro_tungsten.png', '[1/cm]')
plotNeutron(water   , 'macro_water.png'   , '[1/cm]')

# Micro

W182 = Neutron('mc_neutron_micro_74182.xs')
W183 = Neutron('mc_neutron_micro_74183.xs')
W184 = Neutron('mc_neutron_micro_74184.xs')
W186 = Neutron('mc_neutron_micro_74186.xs')

H1   = Neutron('mc_neutron_micro_1001.xs')
H2   = Neutron('mc_neutron_micro_1002.xs')
O16  = Neutron('mc_neutron_micro_8016.xs')
O17  = Neutron('mc_neutron_micro_8017.xs')

plotNeutron(W182, 'micro_W182.png', '[barn]')
plotNeutron(W183, 'micro_W183.png', '[barn]')
plotNeutron(W184, 'micro_W184.png', '[barn]')
plotNeutron(W186, 'micro_W186.png', '[barn]')

plotNeutron(H1 , 'micro_H1.png' , '[barn]')
plotNeutron(H2 , 'micro_H2.png' , '[barn]')
plotNeutron(O16, 'micro_O16.png', '[barn]')
plotNeutron(O17, 'micro_O17.png', '[barn]')
