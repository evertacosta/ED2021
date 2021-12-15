import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np
import pandas as pd

def getangles(e):
    theta = np.arctan(e)

    u = np.cos(theta)
    v = np.sin(theta)

    return u,v


fig1 = plt.figure(constrained_layout=True)
spec2 = gridspec.GridSpec(ncols=2, nrows=3, figure=fig1)

ax1 = fig1.add_subplot(spec2[0, :])
ax2 = fig1.add_subplot(spec2[1, 0])
ax3 = fig1.add_subplot(spec2[1, 1])
ax4 = fig1.add_subplot(spec2[2, 0])
ax5 = fig1.add_subplot(spec2[2, 1])

x, y = np.meshgrid(np.arange(-2, 10, 0.25), np.arange(-2, 3, 0.25))
t = np.linspace(-1, 10, 500)

#solucion particular de la ecuacion numero uno
soleq1 = (13/9)-((13/9)*np.exp(-3*t))
#solucion particular de la ecuacion numero dos
soleq2 = (5/9)+((1/30)*((3*np.cos(t))+np.sin(t)))-((59/90)*np.exp(-3*t))



ax1.plot(t, soleq1, label='soleq1')
ax1.plot(t, soleq2, label='soleq2', color='green')
ax1.set_ylim(-2,2)
ax1.set_title('Soluciones')
ax1.legend()


ecuacion1 = (13/3)-(3*y)
ax2.set_title('Mapa de pendientes eq1')
u1, v1 = getangles(ecuacion1)
ax2.quiver(x, y, u1, v1, pivot='middle')
ax2.xaxis.set_visible(False)

ecuacion2 = (5/3)+(np.cos(y)/3)-(3*y)
ax3.set_title('Mapa de pendientes eq2')
u2, v2 = getangles(ecuacion2)
ax3.quiver(x, y, u2, v2, pivot='middle', scale_units='xy')
ax3.xaxis.set_visible(False)

ax4.plot(t, soleq1, label='soleq1')
ax4.quiver(x, y, u1, v1, pivot='middle')
ax4.set_ylim(-2,2)

ax5.plot(t, soleq2, label='soleq1', color='green')
ax5.quiver(x, y, u2, v2, pivot='middle', scale_units='xy')
ax5.set_ylim(-2,2)

# headers del archivo CSV
headers = ['time', 'Z', 'Y']
# creamos el dataframe
df = pd.read_csv('Trabajo1_Grupo10_om.csv', names=headers, sep=',', header=0)


fig2, axf = plt.subplots(constrained_layout=True)

axf.plot(t, soleq1, label='soleq1')
axf.plot(t, soleq2, label='soleq2')

#soluciones de openmodelica
axf.plot(df['time'], df['Y'], label='OMeq2', linewidth=3, linestyle="--", color="blue")
axf.plot(df['time'], df['Z'], label='OMeq1', linewidth=3, linestyle="--", color="green")

axf.set_ylim(-2,2)
axf.legend()

fig1.suptitle('Figura 1', fontsize=10)
fig2.suptitle('Figura 2', fontsize=10)

plt.show()
