import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

sobreamortiguado_sin_excitacion = pd.read_csv('./trabajo_3_sobreamortiguado_sin_excitacion.csv')

subamortiguado_sin_excitacion = pd.read_csv('./trabajo_3_subamortiguado_sin_excitacion.csv')

def graficar(t_analitica, x_analitica, t_om, x_om, title):
    fig, ax = plt.subplots()
    ax.plot(t_analitica, x_analitica, label='Analitico Python', lw=4, color='#ff7f0e')
    ax.plot(t_om, x_om, label='OM', ls='--', color='#17becf')
    ax.set_xlabel('time')
    ax.set_ylabel('x')
    ax.fill_between(t_analitica, x_analitica, alpha=0.3)
    ax.set_title(title)
    ax.legend()


if __name__ == "__main__":

    t1 = np.linspace(0, 15, 3000)

    sobreamortiguado_x = ((9/2)*np.exp(-(5/9)*t1)) - ((7/2)*np.exp(-(5/7)*t1))

    graficar(t1, sobreamortiguado_x, sobreamortiguado_sin_excitacion['time'], sobreamortiguado_sin_excitacion['mass.s'],
             'Sobreamortiguado sin excitación')

    t2 = np.linspace(0, 6, 3000)

    subamortiguado_x = np.exp(-5/4*t2) * (np.cos(4*np.pi*t2) + ((5/(16*np.pi))*np.sin(4*np.pi*t2)))

    graficar(t2, subamortiguado_x, subamortiguado_sin_excitacion['time'], subamortiguado_sin_excitacion['mass.s'],
             'Subamortiguado sin excitacion')


