from rt2.scoring import MeshDensity

from matplotlib.ticker import MultipleLocator, IndexLocator, FuncFormatter
import matplotlib.pyplot as plt
import numpy as np

da  = MeshDensity('mc_all.mdn')
h   = MeshDensity('mc_hydrogen.mdn')
he  = MeshDensity('mc_helium.mdn')
li  = MeshDensity('mc_lithium.mdn')
be  = MeshDensity('mc_beryllium.mdn')
b   = MeshDensity('mc_boron.mdn')
c   = MeshDensity('mc_carbon.mdn')
c12 = MeshDensity('mc_c12.mdn')

e   = MeshDensity('mc_electron.mdn')

sec = da - c12

x = np.linspace(0,40,2001)
x = (x[1:] + x[:-1]) * 0.5

all_arr = da.data[0,0]
c12_arr = c12.data[0,0]
sec_arr = sec.data[0,0]

norm = np.max(all_arr)

fig, ax = plt.subplots()

ax.plot(x, all_arr / norm)
ax.plot(x, c12_arr / norm)
ax.plot(x, sec_arr / norm)
ax.set_title("RT2 Dose Distribution")
ax.set_xlabel("Depth from surface (cm)")
ax.set_ylabel("Relative Dose")
ax.set_xlim(0,40)
ax.set_ylim(0,1.1)

ax.xaxis.set_major_locator(MultipleLocator(10))
ax.xaxis.set_minor_locator(MultipleLocator(2))
ax.yaxis.set_major_locator(MultipleLocator(0.2))
ax.yaxis.set_minor_locator(MultipleLocator(0.05))

ax2 = ax.twinx()
ax2.set_yticks(ax.get_yticks())
ax2.set_ylim(ax.get_ylim())
ax2.set_yticklabels([])
ax2.yaxis.set_minor_locator(MultipleLocator(0.05))

ax.legend(['Total', 'Primary', 'Fragments'])

plt.savefig('prim_sec')
plt.show()

csec = c - c12

h_arr     = h.data[0,0]
he_arr    = he.data[0,0]
li_arr    = li.data[0,0]
be_arr    = be.data[0,0]
b_arr     = b.data[0,0]
csec_arr  = csec.data[0,0]
e_arr     = e.data[0,0]

fig, ax = plt.subplots()

ax.plot(x, h_arr    / norm)
ax.plot(x, he_arr   / norm)
ax.plot(x, li_arr   / norm)
ax.plot(x, be_arr   / norm)
ax.plot(x, b_arr    / norm)
ax.plot(x, csec_arr / norm)
ax.plot(x, e_arr    / norm)

ax.vlines(27.35, 0, 0.06, 'r', '--')

ax.set_title("RT2 Secondary Dose Distribution")
ax.set_xlabel("Depth from surface (cm)")
ax.set_ylabel("Relative Dose")
ax.set_xlim(0,40)
ax.set_ylim(0,0.06)

ax.xaxis.set_major_locator(MultipleLocator(10))
ax.xaxis.set_minor_locator(MultipleLocator(2))
ax.yaxis.set_major_locator(MultipleLocator(0.02))
ax.yaxis.set_minor_locator(MultipleLocator(0.005))

ax2 = ax.twinx()
ax2.set_yticks(ax.get_yticks())
ax2.set_ylim(ax.get_ylim())
ax2.set_yticklabels([])
ax2.yaxis.set_minor_locator(MultipleLocator(0.005))

ax.legend(['H', 'He', 'Li', 'Be', 'B', 'C(except C-12)', 'e-'])

plt.savefig('components')
plt.show()


h1 = MeshDensity('mc_h1.mdn')
h2 = MeshDensity('mc_h2.mdn')
h3 = MeshDensity('mc_h3.mdn')
h1_arr = h1.data[0,0]
h2_arr = h2.data[0,0]
h3_arr = h3.data[0,0]

fig, ax = plt.subplots()

ax.plot(x, h_arr  / norm)
ax.plot(x, h1_arr / norm)
ax.plot(x, h2_arr / norm)
ax.plot(x, h3_arr / norm)
ax.set_title("RT2 Dose Distribution")
ax.set_xlabel("Depth from surface (cm)")
ax.set_ylabel("Relative Dose")
ax.set_xlim(0,40)
ax.set_ylim(0,0.03)

ax.xaxis.set_major_locator(MultipleLocator(10))
ax.xaxis.set_minor_locator(MultipleLocator(2))
ax.yaxis.set_major_locator(MultipleLocator(0.005))
ax.yaxis.set_minor_locator(MultipleLocator(0.001))

ax2 = ax.twinx()
ax2.set_yticks(ax.get_yticks())
ax2.set_ylim(ax.get_ylim())
ax2.set_yticklabels([])
ax2.yaxis.set_minor_locator(MultipleLocator(0.001))

ax.legend(['H', 'H-1 (proton)', 'H-2 (deuteron)', 'H-3 (triton)'])

plt.savefig('hydrogen')
plt.show()


he3 = MeshDensity('mc_he3.mdn')
he4 = MeshDensity('mc_he4.mdn')
he6 = MeshDensity('mc_he6.mdn')
he3_arr = he3.data[0,0]
he4_arr = he4.data[0,0]
he6_arr = he6.data[0,0]

fig, ax = plt.subplots()

ax.plot(x, he_arr  / norm)
ax.plot(x, he3_arr / norm)
ax.plot(x, he4_arr / norm)
ax.plot(x, he6_arr / norm)
ax.set_title("RT2 Dose Distribution")
ax.set_xlabel("Depth from surface (cm)")
ax.set_ylabel("Relative Dose")
ax.set_xlim(0,40)
ax.set_ylim(0,0.05)

ax.xaxis.set_major_locator(MultipleLocator(10))
ax.xaxis.set_minor_locator(MultipleLocator(2))
ax.yaxis.set_major_locator(MultipleLocator(0.01))
ax.yaxis.set_minor_locator(MultipleLocator(0.002))

ax2 = ax.twinx()
ax2.set_yticks(ax.get_yticks())
ax2.set_ylim(ax.get_ylim())
ax2.set_yticklabels([])
ax2.yaxis.set_minor_locator(MultipleLocator(0.002))

ax.legend(['He', 'He-3', 'He-4 (a)', 'He-6'])

plt.savefig('helium')
plt.show()

li6 = MeshDensity('mc_li6.mdn')
li7 = MeshDensity('mc_li7.mdn')
li8 = MeshDensity('mc_li8.mdn')
li6_arr = li6.data[0,0]
li7_arr = li7.data[0,0]
li8_arr = li8.data[0,0]

fig, ax = plt.subplots()

ax.plot(x, li_arr  / norm)
ax.plot(x, li6_arr / norm)
ax.plot(x, li7_arr / norm)
ax.plot(x, li8_arr / norm)
ax.set_title("RT2 Dose Distribution")
ax.set_xlabel("Depth from surface (cm)")
ax.set_ylabel("Relative Dose")
ax.set_xlim(0,40)
ax.set_ylim(0,0.011)

ax.xaxis.set_major_locator(MultipleLocator(10))
ax.xaxis.set_minor_locator(MultipleLocator(2))
ax.yaxis.set_major_locator(MultipleLocator(0.002))
ax.yaxis.set_minor_locator(MultipleLocator(0.0005))

ax2 = ax.twinx()
ax2.set_yticks(ax.get_yticks())
ax2.set_ylim(ax.get_ylim())
ax2.set_yticklabels([])
ax2.yaxis.set_minor_locator(MultipleLocator(0.0005))

ax.legend(['Li', 'Li-6', 'Li-7', 'Li-8'])

plt.savefig('lithium')
plt.show()


be7  = MeshDensity('mc_be7.mdn')
be9  = MeshDensity('mc_be9.mdn')
be10 = MeshDensity('mc_be10.mdn')
be7_arr  = be7.data[0,0]
be9_arr  = be9.data[0,0]
be10_arr = be10.data[0,0]

fig, ax = plt.subplots()

ax.plot(x, be_arr   / norm)
ax.plot(x, be7_arr  / norm)
ax.plot(x, be9_arr  / norm)
ax.plot(x, be10_arr / norm)
ax.set_title("RT2 Dose Distribution")
ax.set_xlabel("Depth from surface (cm)")
ax.set_ylabel("Relative Dose")
ax.set_xlim(0,40)
ax.set_ylim(0,0.017)

ax.xaxis.set_major_locator(MultipleLocator(10))
ax.xaxis.set_minor_locator(MultipleLocator(2))
ax.yaxis.set_major_locator(MultipleLocator(0.002))
ax.yaxis.set_minor_locator(MultipleLocator(0.0005))

ax2 = ax.twinx()
ax2.set_yticks(ax.get_yticks())
ax2.set_ylim(ax.get_ylim())
ax2.set_yticklabels([])
ax2.yaxis.set_minor_locator(MultipleLocator(0.0005))

ax.legend(['Be', 'Be-7', 'Be-9', 'Be-10'])

plt.savefig('beryllium')
plt.show()


b10  = MeshDensity('mc_b10.mdn')
b11  = MeshDensity('mc_b11.mdn')
b10_arr  = b10.data[0,0]
b11_arr  = b11.data[0,0]

fig, ax = plt.subplots()

ax.plot(x, b_arr   / norm)
ax.plot(x, b10_arr / norm)
ax.plot(x, b11_arr / norm)
ax.set_title("RT2 Dose Distribution")
ax.set_xlabel("Depth from surface (cm)")
ax.set_ylabel("Relative Dose")
ax.set_xlim(0,40)
ax.set_ylim(0,0.06)

ax.xaxis.set_major_locator(MultipleLocator(10))
ax.xaxis.set_minor_locator(MultipleLocator(2))
ax.yaxis.set_major_locator(MultipleLocator(0.01))
ax.yaxis.set_minor_locator(MultipleLocator(0.002))

ax2 = ax.twinx()
ax2.set_yticks(ax.get_yticks())
ax2.set_ylim(ax.get_ylim())
ax2.set_yticklabels([])
ax2.yaxis.set_minor_locator(MultipleLocator(0.002))

ax.legend(['B', 'B-10', 'B-11'])

plt.savefig('boron')
plt.show()


c9   = MeshDensity('mc_c9.mdn')
c10  = MeshDensity('mc_c10.mdn')
c11  = MeshDensity('mc_c11.mdn')
c9_arr   = c9.data[0,0]
c10_arr  = c10.data[0,0]
c11_arr  = c11.data[0,0]

fig, ax = plt.subplots()

ax.plot(x, csec_arr / norm)
ax.plot(x, c9_arr   / norm)
ax.plot(x, c10_arr  / norm)
ax.plot(x, c11_arr  / norm)
ax.set_title("RT2 Dose Distribution")
ax.set_xlabel("Depth from surface (cm)")
ax.set_ylabel("Relative Dose")
ax.set_xlim(0,40)
ax.set_ylim(0,0.065)

ax.xaxis.set_major_locator(MultipleLocator(10))
ax.xaxis.set_minor_locator(MultipleLocator(2))
ax.yaxis.set_major_locator(MultipleLocator(0.02))
ax.yaxis.set_minor_locator(MultipleLocator(0.005))

ax2 = ax.twinx()
ax2.set_yticks(ax.get_yticks())
ax2.set_ylim(ax.get_ylim())
ax2.set_yticklabels([])
ax2.yaxis.set_minor_locator(MultipleLocator(0.005))

ax.legend(['C (except C-12)', 'C-9', 'C-10', 'C-11'])

plt.savefig('carbon')
plt.show()

