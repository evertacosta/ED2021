import numpy as np
import matplotlib.pyplot as plt



def graficar(t, y_analitica, y_om, title):
    fig, ax = plt.subplots()
    ax.plot(t, y_analitica)
    ax.plot(t, y_om)
    ax.title(title)
    ax.legend()






def raizes(T1, T2):
    """
    Calcula las raizes solucion correspondiente a la ecuacion diferencial
    :param T1: Tiempo de estabilizacion T1 entregado por el usuario
    :param T2: Tiempo de estabilizacion T2 entregado por el usuario
    :return: Raizes solucion de la ecuacion diferencial
    """
    T1 = T1
    T2 = T2

    raiz1 = -5/T1
    raiz2 = -5/T2

    return raiz1, raiz2


def coeficientes(r, m):
    """
    :param r:
    :param m:
    :return:
    """
    b = r * 1/m
    k = 1/m
    s = -(r**2)

    return b, k, s


def solucion_sistema(b1, k1, s1, b2, k2, s2):

    aa = np.array([[b1, k1], [b2, k2]])
    bb = np.array([s1, s2])

    solucion = np.linalg.solve(aa, bb)

    return solucion


def sobreamortiguado(T1, T2, m):

    r1, r2 = raizes(T1, T2)

    b1, k1, s1 = coeficientes(r1, m)

    b2, k2, s2 = coeficientes(r2, m)
    solution = np.around(solucion_sistema(b1, k1, s1, b2, k2, s2), 2)

    # retorna b, k
    return solution[0], solution[1]


def sigma(Ts):
    return -5/Ts


def omega(Ps):
    """
    :param Ps:
    :return:
    """
    return (2*np.pi)/Ps


# Constante de amortiguaminto
def b(sigma, m):
    return -(sigma*2*m)


# constante del resorte
def k(omega, b, m):
    return m*(omega**2)+((b**2)/(4*m))


def subamortiguado(Ts, Ps, m):

    s = sigma(Ts)

    o = omega(Ps)

    cb = b(s, m)

    ck = k(o, cb, m)

    # retorna b, k
    return np.around(cb, 2), np.around(ck, 2)



