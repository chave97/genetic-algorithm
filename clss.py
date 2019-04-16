import random

FNC_OBJ=2**30-1

class Poblacion():                                      #Clase Población
    def __init__(self):
        self.poblacion=[]
        self.max_func_obj=0
        self.min_func_obj=0
        self.prom_func_obj=0
        self.seleccionados=[]
        self.suma_objet=0
   
    def generar_poblacion(self):                        #Genero la primera población de cromosomas
        for cantpob in range(10):
            valor_gen_int=random.randint(0,FNC_OBJ)
            valor_gen_bin=bin(valor_gen_int)[2:].zfill(30)
            cromo=list(valor_gen_bin)
            cromo1=Cromosoma(cromo,valor_gen_int,valor_gen_bin)
            self.poblacion+=[cromo1]
    
    def calcular_fobjetivo(self):                       #Calculo de función objetivo de un cromosoma
        for cromosoma in self.poblacion:
            entero=cromosoma.valor_entero
            cromosoma.valor_func_obj=entero/(FNC_OBJ)**2
    
    def suma_de_objetivo(self):                         #Suma de valores de la funcion objetivo (para realizar luego fitness)
        for cromosoma in self.poblacion:
            self.suma_objet+=cromosoma.valor_func_obj

    def calcular_fitness(self):                         #Calculo fitness de cada cromosoma
        for cromosoma in self.poblacion:
            f_obj=cromosoma.valor_func_obj
            cromosoma.valor_fitness = f_obj/self.suma_objet
    
    def mostrar_contenido(self):                        #Muestra contenido del cromosoma
        for cromosoma in range(len(self.poblacion)):
            print("Cromosoma {}: ".format(cromosoma)+''.join(self.poblacion[cromosoma].contenido))
    
    def calcular_max_min(self):                         #Calculo maximos, minimos y promedios de la funcion objetivo de una poblacion
        func_obj=[]
        func_obj_sum=0
        for cromosoma in self.poblacion:
            func_obj+=[cromosoma.valor_func_obj]
            func_obj_sum+=cromosoma.valor_func_obj
        self.max_func_obj=max(func_obj)
        self.min_func_obj=min(func_obj)
        self.prom_func_obj=func_obj_sum/(len(self.poblacion))

    def seleccion(self):                                #Metodo de seleccion de la ruleta
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
    
    def prob_cross(self):                                 #Calculo de probabilidad de cruce simple
        rand=random.random()
        prob=0.75
        if rand<=prob:
            return True
        else:
            return False
    
    def crossover(self):                                   #Realizo crossover entre los cromosomas seleccionados
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

    def mutacion(self):                                    #Genero probabilidad de mutacion para los cromosomas seleccionados por la ruleta
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
        self.poblacion=[]+self.seleccionados                #Reemplazo/Actualizo nueva poblacion


class Cromosoma():
    def __init__(self,contenido,valor_entero,valor_binario):
        self.contenido=contenido                            #Cromosoma
        self.valor_entero=valor_entero                      #Inicializo valor entero que representan los genes
        self.valor_binario=valor_binario                    #Inicializo valor binario que representan los genes (str)
        self.valor_func_obj=0                               #Inicializo valor de la funcion objetivo evaluada en el cromosoma
        self.valor_fitness=0