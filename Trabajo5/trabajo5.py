import matplotlib.pyplot as plt
import numpy as np


plt.style.use('seaborn')


def solucion_sistema2x3(row1, row2, b):
    a = np.array([row1, row2])
    b = np.array(b)
    x = np.linalg.solve(a, b)

    return x[0], x[1]


c1, c2 = solucion_sistema2x3([np.cos(3), np.sin(3)],[-3*np.sin(3), 3*np.cos(3)], [2, 1])


def aja(x, i, a0, a1, puntos, c):

    y1 = np.zeros(puntos)
    y2 = np.zeros(puntos)

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


fig, ax1 = plt.subplots()

x1 = np.linspace(-2, 4, 1000)
x2 = np.linspace(-2, 4, 1000)

porseries1 = aja(x2, 1, 2, 1, 1000, 1)
porseries2 = aja(x2, 2, 2, 1, 1000, 1)
porseries3 = aja(x2, 3, 2, 1, 1000, 1)
porseries5 = aja(x2, 5, 2, 1, 1000, 1)
porseries7 = aja(x2, 7, 2, 1, 1000, 1)

plt.plot(x1, (c1*np.cos(3*x1))+(c2*np.sin(3*x1)), lw=3, label='Analitica')

ax1.plot(x2, porseries1, label='n = 1')
ax1.plot(x2, porseries2, label='n = 2')
ax1.plot(x2, porseries3, label='n = 3')
ax1.plot(x2, porseries5, label='n = 5')
ax1.plot(x2, porseries7, label='n = 7')

ax1.set_ylim(-3, 4)
ax1.set_xlim(-2, 4)

ax1.legend()
ax1.set_title('aja')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
