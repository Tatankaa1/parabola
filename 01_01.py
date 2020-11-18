#
#  Generación de grafico.
#  www: https://youtu.be/i8ruymr85Gg
#

#  -- IMPORTAR MÓDULOS. --
import math
import numpy as np
from matplotlib import pyplot as plt

#  -- GENERAR LOS DATOS PARA EL GRÁFICO. --
x = np.array(range(20))*0.2
y = np.zeros(len(x))
for i in range(len(x)):
    y[i] = math.sin(x[i])

#  -- PLOT GRAFICO. --
plt.plot(x,y)
plt.show()