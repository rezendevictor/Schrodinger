#Bibliotecas necessarias para execucao
import math as mt
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
## Definicao variaveis a serem usadas ao longo do problema
h_bar = 1
m = 1
w = 1
t_pace = 0.1
x_pace = 0.001


## Calcula Csi no espaco
def Csi_calc(x):
    return mt.sqrt((m*w)/h_bar)*x

def E(n,t):
    return complex(0,1)*(n+0.5)*t*w


## Calcula Psu=i, dividindo a equacao em 3 partes:
def psi(n,x,her):
    A = (m*w)/(mt.pi*h_bar)
    A_r= A**(1/4)
    B = 1/mt.sqrt((2**n)*mt.factorial(n))
    C = her[n] *mt.e**((-Csi_calc(x)**2)/2)
    return A_r*B*C

## Calcula Hermite no espaco
def hermite(x,her,n,i=1):
    if i == n :
        return
    else:
        h = 2*x*her[i] - 2*i*her[i-1]
        her.append(h)
        i+=1
        Hermite_gen(x,her,n,i)




def hermite(x):
    Csi = Csi_calc(x)
    Hermite = []
    Hermite.append(1)
    Hermite.append(2*Csi)
    Hermite.append((4*(Csi**2)) - 2)
    Hermite.append((8*(Csi**3))-12*Csi)
    Hermite.append((16*(Csi**4))-48*(Csi**2)+12)
    Hermite.append(32*(Csi**5)-160*(Csi**3)+120*Csi)
    Hermite.append(64*(Csi**6)-480*(Csi**4)+720*(Csi**2)-120)
    Hermite.append(128*(Csi**7)-1344*(Csi**5)+3360*(Csi**3)-1680*Csi)
    Hermite.append(256*(Csi**8)-3584*(Csi**6)+13440*(Csi**4)-13440*(Csi**2)+1680)
    Hermite.append(512*(Csi**9)-9216*(Csi**7)+48384*(Csi**5)-80640*(Csi**3)+30240*Csi)
    Hermite.append(1024*(Csi**10)-23040*(Csi**8)+161280*(Csi**6)-403200*(Csi**4)+302400*(Csi**2) - 30240)
    return Hermite

def cal_vec(vector_matrix):
    vector_plot = []
    for x in range(len(vector_matrix)+1):
        vector_plot.append([])
    i = 0
    for linha in vector_matrix:
        for elemento in linha:
            vector_sai = 0
            vector_sai = ((elemento.real**2)+(elemento.imag**2))
            vector_plot[i].append(vector_sai)
        i+=1

    vector_plot.pop()

    return vector_plot

##Define um vetor com o somatorio
vec_t = []

def psi_sum(initial_x = 0,
        cap_x = 0,cap_t = 1,cap_n = 0):

    for x in range(0,int(cap_t/t_pace)+1):
        vec_t.append([])
    c = 1/mt.sqrt(cap_n+1)
    vector = []
    i = 0
    t = 0
    while(t <= cap_t ):
        x = initial_x

        while(x <= cap_x):
            n = 0
            value = 0
            her = hermite(x)
            while(n <= cap_n):
                sum_n = c* psi(n,x,her)*mt.e**E(n,t)
                value += sum_n
                n+=1
            vec_t[i].append(value)
            x+=x_pace
        i+=1
        t+=t_pace
        vec_psi = cal_vec(vec_t)
    return vec_psi







