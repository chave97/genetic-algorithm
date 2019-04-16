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
        self.seleccionados=[]
        self.suma_objet=0
   
    def generar_poblacion(self):
        for cantpob in range(10):
            valor_gen_int=random.randint(0,FNC_OBJ)
            valor_gen_bin=bin(valor_gen_int)[2:].zfill(30)
            cromo=list(valor_gen_bin)
            cromo1=Cromosoma(cromo,valor_gen_int,valor_gen_bin)
            self.poblacion+=[cromo1]
    
    def calcular_fobjetivo(self):                           #Calculo de función objetivo
        for cromosoma in self.poblacion:
            entero=cromosoma.valor_entero
            cromosoma.valor_func_obj=entero/(FNC_OBJ)**2
    
    def suma_de_objetivo(self):
        for cromosoma in self.poblacion:
            self.suma_objet+=cromosoma.valor_func_obj

    def calcular_fitness(self):                  #Calculo fitness, pasando como parametro la suma de las funciones objetivos de la poblacion
        for cromosoma in self.poblacion:
            f_obj=cromosoma.valor_func_obj
            cromosoma.valor_fitness = f_obj/self.suma_objet
    
    def mostrar_contenido(self):                            #Muestra contenido del cromosoma
        for cromosoma in range(len(self.poblacion)):
            print("Cromosoma {}: ".format(cromosoma)+''.join(self.poblacion[cromosoma].contenido))
    
    def calcular_max_min(self):
        func_obj=[]
        func_obj_sum=0
        for cromosoma in self.poblacion:
            func_obj+=[cromosoma.valor_func_obj]
            func_obj_sum+=cromosoma.valor_func_obj
        self.max_func_obj=max(func_obj)
        self.min_func_obj=min(func_obj)
        self.prom_func_obj=func_obj_sum/(len(self.poblacion))

    def seleccion(self):
        #Metodo de la ruleta
        indice=[]
        for giro in range(10):
            suma=0
            aleatorio = random.random()
            for cromosoma in range(len(self.poblacion)):
                suma+=self.poblacion[cromosoma].valor_fitness
                if suma>=aleatorio:
                    indice+=[cromosoma]
                    self.seleccionados+=[self.poblacion[cromosoma]]
                    break
        for cromosomas in self.seleccionados:
            print("Se seleccionaron los cromosomas: "+str(''.join(cromosomas.contenido)))
        print("Cromosomas seleccionados: "+str(indice))    
    
    def prob_cross(self):
        rand=random.random()
        prob=0.75
        if rand<=prob:
            return True
        else:
            return False
    
    def crossover(self):
        indice=0
        for pareja in range(5):
            if self.prob_cross():
                corte=random.randint(1,29)
                print("Se corta en pos: "+str(corte))
                padre1=self.seleccionados[indice]
                print("Padre1: "+''.join(padre1.contenido))
                padre2=self.seleccionados[indice+1]
                print("Padre2: "+''.join(padre2.contenido))
                parte_izquierda = [padre1.contenido[:corte]]+[padre2.contenido[:corte]]
                parte_derecha = [padre1.contenido[corte:]]+[padre2.contenido[corte:]]
                self.seleccionados[indice].contenido=[]+parte_izquierda[0]+parte_derecha[1]
                self.seleccionados[indice+1].contenido=[]+parte_izquierda[1]+parte_derecha[0]
                print("Padre1 cambiado: "+''.join(self.seleccionados[indice].contenido))
                print("Padre2 cambiado: "+''.join(self.seleccionados[indice+1].contenido))
                indice+=2
            else:
                print("La pareja {} no se reproducira!".format(pareja))

    def mutacion(self):
        for seleccionado in self.seleccionados:
            muta=random.random()
            if muta < 0.05:
                corte=random.randint(1,29)
                if seleccionado.contenido[corte] == '0':
                    seleccionado.contenido[corte] == '1'
                else:
                    seleccionado.contenido[corte]== '0'
            else:
                mutacion=False
                print("El cromosoma seleccionado: " +''.join(seleccionado.contenido) +"NO se reprodujo")
    
    def nueva_poblacion(self):
        self.poblacion=[]+self.seleccionados


class Cromosoma():
    def __init__(self,contenido,valor_entero,valor_binario):
        self.contenido=contenido                            #Cromosoma
        self.valor_entero=valor_entero                      #Inicializo valor entero que representan los genes
        self.valor_binario=valor_binario                    #Inicializo valor binario que representan los genes (str)
        self.valor_func_obj=0                               #Inicializo valor de la funcion objetivo evaluada en el cromosoma
        self.valor_fitness=0
    

def escribir_archivo(poblacion,tirada):
    poblacion.calcular_max_min()
    cabecera=[["Ronda","Maximo","Minimo","Promedio"]]
    cabecera.append([str(tirada),str(poblacion.max_func_obj),str(poblacion.min_func_obj),str(poblacion.prom_func_obj)])
    archivo=open("./registro.csv","a")
    with archivo:
        escribir=csv.writer(archivo,dialect="excel",delimiter=';')
        escribir.writerows(cabecera)
#----------------------------------------Programa Principal -------------------------------------------------

pobla=Poblacion()
pobla.generar_poblacion()
print("-"*40+"Poblacion inicial"+"-"*40)
pobla.mostrar_contenido()
print("-"*100)
for tiradas in range(1):
    print("-"*40+"Tirada {}".format(tiradas)+"-"*40)
    #Calculo funcion objetivo de c/cromosoma
    pobla.calcular_fobjetivo()
    #Sumo la funcion objetivo de todos los cromosomas
    pobla.suma_de_objetivo()
    #Calculo fitness de c/cromosoma
    pobla.calcular_fitness()
    pobla.mostrar_contenido()
    print("-"*100)
    pobla.calcular_max_min()
    pobla.seleccion()
    pobla.crossover()
    pobla.mutacion()
    pobla.nueva_poblacion()
    print("-"*40+"Poblacion nueva"+"-"*40)
    pobla.mostrar_contenido()
    print("-"*100)