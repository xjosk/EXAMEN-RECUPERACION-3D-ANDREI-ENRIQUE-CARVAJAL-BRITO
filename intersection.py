"""
Intersection example
"""
#Examen de recuperación evalucación 3D, Andrei Enrique Carvajal Brito, 1/02/2021
#No. control: 1839022
#importa libreria

import matplotlib.pyplot as plt 
import numpy as np
from math import sin, cos, radians,sqrt
import tools3D as tools3d
import keyboard

#_________FAVOR DE INSTALAR LA LIBRERIA DE KEYBOARD pip install keybaord PARA CORRECTO FUNCIONAMIENTO :)

#______Coordenadas iniciales
xg=[]
yg=[]
zg=[]

#Cordenadas centrales
xc=80
yc=40
zc=40

#Plano y linea de sistema
"""x=[40,30,80,40]
y=[60,10,60,60]
z=[-10,10,10,-10,15,0]"""



#____Plotear el sistema 
#def plotPlaneLine(xg,yg,zg,xh,yh,xhg,yhg,hitcolor):
def plotPlaneLine(xg,yg,zg,A,A1,A2,validar):
    plt.axis([0,200,200,0])
    plt.axis('on')
    plt.grid(True)

    plt.plot([xg[0],xg[1]],[yg[0],yg[1]],color='k')#plano
    plt.plot([xg[0],xg[2]],[yg[0],yg[2]],color='k')
    plt.plot([xg[1],xg[2]],[yg[1],yg[2]],color='k')

    #triangulos extras
    plt.plot([xg[1],xg[3]],[yg[1],yg[3]],linestyle=':',color='r')
    plt.plot([xg[0],xg[3]],[yg[0],yg[3]],linestyle=':',color='g')
    plt.plot([xg[2],xg[3]],[yg[2],yg[3]],linestyle=':',color='y')
    plt.scatter(xg[3],yg[3], s=25, color='r')
    
    #Etiquetar los ejes
    plt.xlabel("Eje X")
    plt.ylabel("Eje Y")

    #Título
    plt.title("Recuperación evaluación 3D")

    #Mostrar el Area base, Area 1 y Area 2 y si se encuentra dentro o fuera del plano
    plt.text(10,60,"A=")
    plt.text(25,60,A)

    plt.text(10,45,"A1=")
    plt.text(25,45,A1)
    
    plt.text(10,30,"A2=")
    plt.text(25,30,A2)

    plt.text(10,75,"A1+A2=")
    plt.text(40,75,A1+A2)

    plt.text(10,15,validar)
    plt.text(10,90,"Andrei Enrique Carvajal Brito")

    plt.show()

#Hit point para hacer la piramide
def hitpoint(xg,yg,zg):
    #__AREA DE A
    
    #Calcular las distancias, esto se logra utilizando la formula SQRT((x2-x2)^2+(y2-y1)^2), utilizando los índices

    #Calcular la distancia del punto 0 al 1
    a=xg[0]-xg[1]
    b=yg[0]-yg[1]

    d01=sqrt(a*a+b*b)

    #Calcular la distancia del punto 0 al 2
    a=xg[0]-xg[2]
    b=yg[0]-yg[2]

    d02=sqrt(a*a+b*b)

    #Calcular la distancia del punto 1 al 2
    a=xg[1]-xg[2]
    b=yg[1]-yg[2]

    d12=sqrt(a*a+b*b)

    #Calcular el area de A
    s=(d01+d12+d02)/2
    A=sqrt(abs(s*(s-d01)*(s-d12)*(s-d02)))


    #___AREA DE A1

    #Calcular la distancia del punto 1 al 3
    a=xg[1]-xg[3]
    b=yg[1]-yg[3]

    d13=sqrt(a*a+b*b)

    #Calcular la distancia del punto 0 al 2
    a=xg[0]-xg[3]
    b=yg[0]-yg[3]

    d03=sqrt(a*a+b*b)

    #Calcular el area de A1

    s=(d01+d13+d03)/2
    A1=sqrt(abs(s*(s-d01)*(s-d13)*(s-d03)))


    #___AREA DE A2
    a=xg[2]-xg[3]
    b=yg[2]-yg[3]

    d23=sqrt(a*a+b*b)

    #Calcular el area de A2
    s=(d01+d13+d03)/2
    A2=sqrt(abs(s*(s-d23)*(s-d02)*(s-d03)))

    #Hacer la suma para validar si el hitpoint se encuentra dentro del plano
    sumarea=A1+A2

    if(sumarea<A):
        validar='Se encuentra dentro'
    else:
        validar='Se encuentra afuera'

    #Llamar a la función que plotea y llenar los valores del array 
    plotPlaneLine(xg,yg,zg,A,A1,A2,validar)
    

####_____Pedir al usuario si quiere continuar o salir del programa
print("Presiona ENTER para continuar o ESC para salir")
while True:

    #ENTER para entrar
    if keyboard.is_pressed('ENTER'):
        input()
        #Hitpoint en X
        axis=int(input("Valor del hitpoint x"))

        #Valores en X de las coordenadas
        x=[40,30,80, axis]

        axis=int(input("Valor del hitpoint y"))


        #Valores en Y de las coordenadas
        y=[60,10,60, axis]

        z=[-10,10,10,-10]

        #Sumar los valores centrales para centrar el triangulo
        for i in range(len(x)):
            xg.append(x[i]+xc)
            yg.append(y[i]+yc)
            zg.append(z[i]+zc)

        #Llamar a la función hitpoint
        hitpoint(xg,yg,zg)

    if keyboard.is_pressed('Esc'):
        print("Saliendo del programa")
        break