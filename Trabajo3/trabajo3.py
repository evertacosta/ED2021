import numpy as np


def raizes(T1, T2):

    T1 = T1
    T2 = T2

    raiz1 = -5/T1
    raiz2 = -5/T2

    return raiz1, raiz2

def coeficientes(m, r):
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

    b1, k1, s1 = coeficientes(m, r1)

    b2, k2, s2 = coeficientes(m, r2)



    return solucion_sistema(b1, k1, s1, b2, k2, s2)


def sigma(Ts):
    return -5/Ts


def omega(Ps):
    return (2*np.pi)/Ps


def b(sigma, m):
    return -(sigma*2*m)

#def k(b,m):

