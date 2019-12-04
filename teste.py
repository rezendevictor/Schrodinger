from sympy.physics.quantum.constants import *
from mpmath import *
import cmath as mt
import algebric as al
import matplotlib
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
import numpy as np
from celluloid import Camera
x_inicial = -4

##(x,x final,t_max,n_max)
vector_matrix = al.psi_sum(x_inicial,-x_inicial,10,9)
#vector_matrix4 = al.psi_sum(x_inicial,-x_inicial,10,0)
#vector_matrix3 = al.psi_sum(x_inicial,-x_inicial,10,3)
#vector_matrix2 = al.psi_sum(x_inicial,-x_inicial,10,2)
#vector_matrix1 = al.psi_sum(x_inicial,-x_inicial,10,1)
vector_plot = []

### Getting data converted
# Working with the graph amd animation
fig = plt.figure()
ax = plt.axes()
plt.title('Solução Numérica ')
plt.xlabel('Posicao')
plt.ylabel('|\u03A8(x,t)|²')
camera = Camera(fig)
scale_x = 1000
ticks_x = ticker.FuncFormatter(lambda x, pos: '{0:g}'.format(x/(scale_x)+x_inicial ))
ax.xaxis.set_major_formatter(ticks_x)
ax.grid()

lab = 0
for x in range(len(vector_matrix)):
    lab+=1
    plt.plot(vector_matrix[x],'tab:blue')
    camera.snap()


animation = camera.animate()

animation.save("Solucao.gif" ,writer = 'imagemagick')


#plt.legend(loc='best')
plt.show()
