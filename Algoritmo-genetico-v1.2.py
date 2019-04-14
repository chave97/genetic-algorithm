#Algoritmo Genético usando Objetos

import random
import csv
#--------------CONSTANTES-----------------
FNC_OBJ = 2**30-1
#-----------CLASES Y FUNCIONES------------

class Cromosoma():
    def __init__(self,contenido,valor_entero,valor_binario):
        self.contenido=contenido                            #cromosoma
        self.valor_entero=0                                 #inicializo valor entero que representan los genes
        self.valor_binario=0                                #inicializo valor binario que representan los genes (str)
        self.valor_func_obj=0                               #inicializo valor de la funcion objetivo evaluada en el cromosoma
        self.valor_fitness=0

    def mostrar_contenido(self):                            #Muestra contenido del cromosoma
        print(self.contenido)

    def agregar_gen(self,gen):                              #Agrega gen al cromosoma
        self.contenido+=[gen]

    def calcular_fobjetivo(self):                           #Calculo de función objetivo
        int=self.valor_entero
        self.valor_func_obj=int/(FNC_OBJ)**2

    def calcular_fitness(self,suma_f_obj):                  #Calculo fitness, pasando como parametro la suma de las funciones objetivos de la poblacion
        f_obj=self.valor_func_obj
        self.valor_fitness = f_obj/suma_f_obj

def Generar_poblacion(poblacion):
    for cantpob in range(10):
        valor_gen_int=random.randint(0,FNC_OBJ)
        valor_gen_bin=bin(valor_gen_int)[2:0].zfill(30)
        cromo=list(valor_gen_bin)
        cromo1=Cromosoma(cromo,valor_gen_int,valor_gen_bin)
        poblacion+=[cromo1]
    return poblacion

pob=[]

Generar_poblacion(pob)

for cromosomas in pob:
    cromosomas.mostrar_contenido()
