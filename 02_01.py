# Ejemplo:2 con Mat***
# youtube: https://youtu.be/hUfHUPPCxZ4
#

# ##   1.0. Libreria:
#
import matplotlib.pyplot as plt
import numpy as np                 # Libreria paquetes cientifica.
# from matplotlib import pyplot as plt

# ##   2.0. Definir Funciones y variables:
#
def h(x):
    return np.sin(x)

x=np.linspace(0, 10, 100)

# ##   4.0. Graficar o Imprimir:
#
plt.plot(x, h(x))