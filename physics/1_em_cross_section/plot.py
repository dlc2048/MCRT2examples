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


class Photon(CrossSectionInterface):
    def __init__(self, file_name: str):
        super().__init__(file_name)

    def total(self):
        return self._draw[:,1]

    def rayleigh(self):
        return self._draw[:,2]

    def photo(self):
        return self._draw[:,3]

    def compt(self):
        return self._draw[:,4]

    def pair(self):
        return self._draw[:,5]


class Electron(CrossSectionInterface):
    def __init__(self, file_name: str):
        super().__init__(file_name)

    def dedx(self):
        return self._draw[:,1]

    def range(self):
        return self._draw[:,2]

    def total(self):
        return self._draw[:,3]

    def moller(self):
        return self._draw[:,4]

    def bremss(self):
        return self._draw[:,5]


class Positron(Electron):
    def __init__(self, file_name: str):
        super().__init__(file_name)

    def moller(self):
        assert(False)

    def bhabha(self):
        return self._draw[:,4]

    def annihi(self):
        return self._draw[:,6]


# Photon XS

t_gamma = Photon('mc_gamma_tungsten.xs')
w_gamma = Photon('mc_gamma_water.xs')

def plotPhoton(xs: Photon, filename: str):
    plt.figure()
    plt.plot(xs.energy(), xs.total())
    plt.plot(xs.energy(), xs.rayleigh())
    plt.plot(xs.energy(), xs.photo())
    plt.plot(xs.energy(), xs.compt())
    plt.plot(xs.energy(), xs.pair())
    plt.xlabel('Energy [MeV]')
    plt.ylabel('Cross-Section [1/cm]')
    plt.xscale('log')
    plt.yscale('log')
    plt.legend(['Total', 'Rayleigh', 'Photoelectric', 'Compton', 'Pair'])
    plt.savefig(filename)
    plt.show()

plotPhoton(t_gamma, 'photon_tungsten.png')
plotPhoton(w_gamma, 'photon_water.png')

# Electron XS

t_electron = Electron('mc_electron_tungsten.xs')
w_electron = Electron('mc_electron_water.xs')


def plotElectron(xs: Electron, filename: str):
    plt.figure()
    plt.plot(xs.energy(), xs.total())
    plt.plot(xs.energy(), xs.moller())
    plt.plot(xs.energy(), xs.bremss())
    plt.xlabel('Energy [MeV]')
    plt.ylabel('Cross-Section [1/cm]')
    plt.xscale('log')
    #plt.yscale('log')
    plt.legend(['Total', 'Moller', 'Bremsstrahlung'])

    plt.twinx()
    plt.plot(xs.energy(), xs.dedx(), 'r--')
    #plt.yscale('log')
    plt.ylabel('Stopping Power [MeV/cm]')

    plt.savefig(filename)
    plt.show()
    

plotElectron(t_electron, 'electron_tungsten.png')
plotElectron(w_electron, 'electron_water.png')

# Positron XS

t_positron = Positron('mc_positron_tungsten.xs')
w_positron = Positron('mc_positron_water.xs')


def plotPositron(xs: Positron, filename: str):
    plt.figure()
    plt.plot(xs.energy(), xs.total())
    plt.plot(xs.energy(), xs.bhabha())
    plt.plot(xs.energy(), xs.bremss())
    plt.plot(xs.energy(), xs.annihi())
    plt.xlabel('Energy [MeV]')
    plt.ylabel('Cross-Section [1/cm]')
    plt.xscale('log')
    #plt.yscale('log')
    plt.legend(['Total', 'Bhabha', 'Bremsstrahlung', 'Annihilation'])

    plt.twinx()
    plt.plot(xs.energy(), xs.dedx(), 'r--')
    #plt.yscale('log')
    plt.ylabel('Stopping Power [MeV/cm]')

    plt.savefig(filename)
    plt.show()
    

plotPositron(t_positron, 'positron_tungsten.png')
plotPositron(w_positron, 'positron_water.png')
