import matplotlib.pyplot as plt
import numpy as np


plt.style.use('seaborn')


def solucion_sistema2x3(row1, row2, b):
    a = np.array([row1, row2])
    b = np.array(b)
    x = np.linalg.solve(a, b)

    return x[0], x[1]


def y_ecuacion_caracteristica(x):
    c1, c2 = solucion_sistema2x3([np.cos(3), np.sin(3)], [-3*np.sin(3), 3*np.cos(3)], [2, 1])
    return (c1*np.cos(3*x))+(c2*np.sin(3*x))


def ec():
    fig, ax1 = plt.subplots()

    x1 = np.linspace(-10, 12, 5000)

    y_ec = y_ecuacion_caracteristica(x1)

    plt.plot(x1, y_ec, label='EC', lw=4, color='#ff7f0e')

    ax1.set_ylim(-4, 5)
    ax1.set_xlim(-10, 12)
    ax1.legend()
    ax1.set_title('Solucion por ecuacion caracteristica(EC)')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')


def y_series(i, x, a0, a1, c):

    y1 = np.zeros(len(x))
    y2 = np.zeros(len(x))

    contador = 0

    for n in range(1, i+1):
        if contador == i:
            break

        y1 += ((((-1)**(n+1))*(9**(n-1)))/(np.math.factorial((2*n)-2))) * ((x-c)**((2*n)-2))
        contador += 1

        if contador == i:
            break

        y2 += (((((-1)**(n+1))*(9**(n-1)))/(np.math.factorial((2*n)-1))) * ((x-c)**((2*n)-1)))
        contador += 1

    y = (a0*y1) + (a1*y2)

    return y


def ec_vs_series_enesimo(n):

    fig, ax1 = plt.subplots()

    x1 = np.linspace(-10, 12, 5000)

    y_ec = y_ecuacion_caracteristica(x1)

    y_series_n100 = y_series(n, x1, 2, 1, 1)

    plt.plot(x1, y_ec, label='EC', lw=4, color='#ff7f0e')
    ax1.plot(x1, y_series_n100, label='n = {}'.format(n), ls='--', color='#17becf')

    ax1.set_ylim(-4, 5)
    ax1.set_xlim(-10, 12)
    ax1.legend()
    ax1.set_title('Solucion por ecuacion caracteristica(EC) vs solucion por series de potencias n={}'.format(n))
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')


def ec_vs_series():

    fig, ax1 = plt.subplots()

    x1 = np.linspace(-2, 4, 1000)

    y_ec = y_ecuacion_caracteristica(x1)

    y_series_n1 = y_series(1, x1, 2, 1, 1)
    y_series_n2 = y_series(2, x1, 2, 1, 1)
    y_series_n3 = y_series(3, x1, 2, 1, 1)
    y_series_n5 = y_series(5, x1, 2, 1, 1)
    y_series_n7 = y_series(7, x1, 2, 1, 1)

    plt.plot(x1, y_ec, lw=3, label='EC', c='black')
    ax1.plot(x1, y_series_n1, label='n = 1')
    ax1.plot(x1, y_series_n2, label='n = 2')
    ax1.plot(x1, y_series_n3, label='n = 3')
    ax1.plot(x1, y_series_n5, label='n = 5')
    ax1.plot(x1, y_series_n7, label='n = 7')

    ax1.set_ylim(-3, 4)
    ax1.set_xlim(-2, 4)
    ax1.legend()
    ax1.set_title('Solucion por ecuacion caracteristica(EC) vs soluciones por series de potencias')
    ax1.set_xlabel('x')
    ax1.set_ylabel('y')


if __name__ == "__main__":
    ec()
    ec_vs_series_enesimo(100)
    ec_vs_series()
