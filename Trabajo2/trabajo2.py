import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# tiempo para interruptor cerrado
t1 = np.linspace(0, 2, 1000)
# tiempo para el interruptor abierto
t2 = np.linspace(2, 10, 1000)

# funcion que graficara la solucion de las ecuaciones
def gra(t1, t2):
    # solucion para el interruptor cerrado
    vc_cerrado = (10/3) - (10/3)*np.exp(-(3/2)*t1)
    # solucion para el interruptor abierto
    vc_abierto = 8.61*np.exp(-t2/2)

    fig, ax1 = plt.subplots()

    ax1.plot(t1, vc_cerrado, label='cerrado')
    ax1.plot(t2, vc_abierto, label='abierto')
    ax1.fill_between(t1,vc_cerrado, alpha=0.3)
    ax1.fill_between(t2,vc_abierto, alpha=0.3)

    ax1.set_title('Python')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Vc')

    ax1.legend()
    ax1.grid()

    plt.show()


# link del archivo csv generado por OM guardado en github
csv_link_raw = 'https://raw.githubusercontent.com/evertacosta/ED2021/main/Trabajo2/trabajo2_om_data.csv'

# Funcion que realiza la comparacion
def comparacion(t1, t2, csv_url):
    # leemos el archivo csv
    df = pd.read_csv(csv_url)

    # solucion para el interruptor cerrado
    vc_cerrado = (10/3) - (10/3)*np.exp(-(3/2)*t1)
    # solucion para el interruptor abierto
    vc_abierto = 8.61*np.exp(-t2/2)

    fig2, ax1 = plt.subplots()

    ax1.plot(t1, vc_cerrado, label='cerrado', lw=4)
    ax1.plot(t2, vc_abierto, label='abierto', lw=4)

    # graficamos los puntos del archivo csv de OM
    ax1.plot(df['time'], df['Y'], label='OM', ls='--', color='#17becf')

    ax1.fill_between(t1,vc_cerrado, alpha=0.3)
    ax1.fill_between(t2,vc_abierto, alpha=0.3)
    ax1.set_title('Python vs OpenModelica')
    ax1.set_xlabel('Time')
    ax1.set_ylabel('Vc')
    ax1.legend()
    ax1.grid()

    plt.show()

comparacion(t1, t2, csv_link_raw)