import numpy as np
import matplotlib.pyplot as plt


class CrossSectionInterface:
    def __init__(self, file_name: str):
        first_hit  = True
        draw       = []
        with open(file_name) as file:
            for line in file:
                if first_hit:
                    first_hit = False
                    continue
                draw += [list(map(float, line.split()))]
        self._draw = np.array(draw)

    def energy(self):
        return self._draw[:,0]


class Genion(CrossSectionInterface):
    def __init__(self, file_name: str):
        super().__init__(file_name)

    def dedx(self):
        return self._draw[:,1]

    def range(self):
        return self._draw[:,2]

    def tmxs(self):
        return self._draw[:,3]

    def total(self):
        return self._draw[:,4]

    def delta(self):
        return self._draw[:,5]

    def inc(self):
        return self._draw[:,6]


# Photon XS

t_proton = Genion('mc_genion_1001_tungsten.xs')
w_proton = Genion('mc_genion_1001_water.xs')

t_carbon = Genion('mc_genion_6012_tungsten.xs')
w_carbon = Genion('mc_genion_6012_water.xs')


def plotGenion(xs: Genion, filename: str):
    plt.figure()
    plt.plot(xs.energy(), xs.total())
    plt.plot(xs.energy(), xs.delta())
    plt.plot(xs.energy(), xs.inc())
    plt.xlabel('Energy [MeV]')
    plt.ylabel('Cross-Section [1/cm]')
    plt.xscale('log')
    # plt.yscale('log')
    plt.legend(['Total', 'Delta Production', 'Inelastic'])

    plt.twinx()
    plt.plot(xs.energy(), xs.dedx(), 'r--')
    # plt.yscale('log')
    plt.ylabel('Stopping Power [MeV/cm]')

    plt.savefig(filename)
    plt.show()


plotGenion(t_proton, 'proton_tungsten.png')
plotGenion(w_proton, 'proton_water.png')

plotGenion(t_carbon, 'carbon_tungsten.png')
plotGenion(w_carbon, 'carbon_water.png')
