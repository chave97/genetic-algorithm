#Algoritmo Genético usando Objetos

import random
import csv
#--------------CONSTANTES-----------------
FNC_OBJ = 2**30-1
#-----------CLASES Y FUNCIONES------------

class Poblacion():
    def __init__(self):
        self.poblacion=[]
        self.max_func_obj=0
        self.min_func_obj=0
        self.prom_func_obj=0
   
    def generar_poblacion(self):
        for cantpob in range(10):
            valor_gen_int=random.randint(0,FNC_OBJ)
            valor_gen_bin=bin(valor_gen_int)[2:].zfill(30)
            cromo=list(valor_gen_bin)
            cromo1=Cromosoma(cromo,valor_gen_int,valor_gen_bin)
            self.poblacion+=[cromo1]
   
    def calcular_max_min(self):
        func_obj=[]
        func_obj_sum=0
        for cromosoma in self.poblacion:
            func_obj+=[cromosoma.valor_func_obj]
            func_obj_sum+=cromosoma.valor_func_obj
        self.max_func_obj=max(func_obj)
        self.min_func_obj=min(func_obj)
        self.prom_func_obj=func_obj_sum/(len(self.poblacion))

class Cromosoma():
    def __init__(self,contenido,valor_entero,valor_binario):
        self.contenido=contenido                            #cromosoma
        self.valor_entero=valor_entero                                 #inicializo valor entero que representan los genes
        self.valor_binario=valor_binario                                #inicializo valor binario que representan los genes (str)
        self.valor_func_obj=0                               #inicializo valor de la funcion objetivo evaluada en el cromosoma
        self.valor_fitness=0

    def mostrar_contenido(self):                            #Muestra contenido del cromosoma
        print(self.contenido)

    def agregar_gen(self,gen):                              #Agrega gen al cromosoma
        self.contenido+=[gen]

    def calcular_fobjetivo(self):                           #Calculo de función objetivo
        entero=self.valor_entero
        self.valor_func_obj=entero/(FNC_OBJ)**2

    def calcular_fitness(self,suma_f_obj):                  #Calculo fitness, pasando como parametro la suma de las funciones objetivos de la poblacion
        f_obj=self.valor_func_obj
        self.valor_fitness = f_obj/suma_f_obj
    

def escribir_archivo(poblacion):
    poblacion.calcular_max_min()
    cabecera=[["Ronda","Maximo","Minimo","Promedio"]]
    cabecera.append(["0",str(poblacion.max_func_obj),str(poblacion.min_func_obj),str(poblacion.prom_func_obj)])
    archivo=open("./registro.csv","w+")
    with archivo:
        escribir=csv.writer(archivo,dialect="excel",delimiter=';')
        escribir.writerows(cabecera)
#----------------------------------------Programa Principal -------------------------------------------------

pobla=Poblacion()
pobla.generar_poblacion()
f_obj=0
suma_f_obj=0
for cromosomas in range(len(pobla.poblacion)):
    print("Cromosoma {}: ".format(cromosomas)+str(pobla.poblacion[cromosomas].contenido))
    print("Valor representativo entero: "+str(pobla.poblacion[cromosomas].valor_entero))
    print("Valor representativo binario: "+str(pobla.poblacion[cromosomas].valor_binario))
    pobla.poblacion[cromosomas].calcular_fobjetivo()
    suma_f_obj+=pobla.poblacion[cromosomas].valor_func_obj
    print("Valor de funcion objetivo: "+str(pobla.poblacion[cromosomas].valor_func_obj))

print(suma_f_obj)
suma_f_fit=0
for cromosomas in range(len(pobla.poblacion)):
    pobla.poblacion[cromosomas].calcular_fitness(suma_f_obj)
    print("Valor fitness del cromosoma {}: ".format(cromosomas)+str(pobla.poblacion[cromosomas].valor_fitness))
    suma_f_fit+=pobla.poblacion[cromosomas].valor_fitness

print("Fitness total: ",suma_f_fit)
escribir_archivo(pobla)