"-----------------ALGORITMO GENÉTICO BÁSICO (CANÓNICO)-----------------"""

import random                                                               #Importo libreria de valores random
import csv                                                                  #Libreria para archivo .CSV

"""-----------------------------------FUNCIONES--------------------------------------------------------------"""


def pobl_ini(poblacion):                                                    #Función para generar población inicial
    for h in range(10):
        cromosoma = []
        funcion_objetivo= 2**30-1                                           #Valor de la función objetivo
        genes=random.randint(0,funcion_objetivo)                            #genes = valor entero random
        genes=bin(genes)[2:].zfill(30)                                      #Convierto a binario el decimal y elimino '0b'
        for i in range(len(genes)):                                         #A cada 'GEN' de genes lo paso a un arreglo: cromosoma (auxiliar)
            cromosoma.append(genes[i])
        poblacion.append(cromosoma)                                         #Agrego cromosoma (cromosoma) a la población


def func_obj(poblacion,valobjetivo,valentero):                              #Función objetivo: f(x)=x/(2**30)-1
    for i in range(len(poblacion)):                                         #Recorre la población en busca de cromosomas
        cromosoma_str = ''
        for p in range(len(poblacion[i])):                                  #Paso cromosoma a string
            cromosoma_str+=poblacion[i][p]
        cromosoma_int=int(cromosoma_str,2)                                  #Transformo cromosoma(string) a decimal
        funcion=(cromosoma_int/((2**30)-1))**2                              #Valor de la func_obj para cromosoma
        valobjetivo.append(funcion)
        valentero.append(cromosoma_int)

def fitness(valorobjetivo,valorfitness):                                    #Parametros: Lista de valores fuc_obj. Lista vacia para valor de fitness
    suma_func_obj=0
    for i in valorobjetivo:
        suma_func_obj+=i                                                    #Sumatoria de func_obj de cada cromosoma
    for b in range(len(valorobjetivo)):
        fit=valorobjetivo[b]/suma_func_obj                                  #Calculo de fitness del cromosoma 'b' de la población
        valorfitness.append(fit)

def ruleta(valor_fitness,cromosoma_ruleta,seleccion,poblacion):             #Método de ruleta: Función de valor agregado
    for giro in range(10):                                                   #Se 'gira' 4 veces la ruleta
        suma=0
        indice=0
        aleatorio = random.random()                                       #Valor random de giro de la ruleta
        for i in range(len(valor_fitness)):                                 #Suma de cada fitness hasta llegar al valor aleatorio
            suma=suma+valor_fitness[i]
            indice=i                                                        #Guardo el índice
            if suma>=aleatorio:                                            #El índice es el anterior dado que el actual seria un cromosoma cuya suma de fitness es mayor al aleatorio
                seleccion.append(indice)
                auxi = [] + poblacion[i]
                cromosoma_ruleta.append(auxi)  # Agrega el cromosoma determinado por la ruleta a la lista 'seleccion'
                break                                                  #Fin del bucle al encontrar cromosoma
    for n in range(len(cromosoma_ruleta)):                                  #Paso cromosoma(lista) a string para ahorrar espacio
        a=''
        for k in range(30):
           a=a+cromosoma_ruleta[n][k]
        archivo=open(directorio,'a')
        archivo.write("El cromosoma: "+str(seleccion[n])+": "+str(a)+" se reproducirá"+"\n")
        archivo.close()

def prob_cross():                                                           #Determina la probabilidad de cruce entre los cromosomas padres
    rand=random.random()
    prob=0.75
    if rand<=prob:
        return True
    else:
        return False

def crossover(x):                                                           #Paso x = cromosoma_ruleta
    if prob_cross() == True:                                                #Se consulta la probabilidad para la primer pareja de cromosomas
        corte = random.randint(1, 29)
        archivo = open(directorio, 'a')
        archivo.write("\nLa primera pareja de cromosomas seleccionados por la ruleta se cortarán en la posicion: " + str(corte) + "\n\n")
        archivo.close()
        for i in range(corte,30):
            aux=x[0][i]
            x[0][i]=x[1][i]                                                 #Crossover de los primeros 2 padres
            x[1][i]=aux
    else:
        archivo = open(directorio, 'a')
        archivo.write("\nLa primera pareja de cromosomas seleccionados por la ruleta no se reproducirá\n\n")
        archivo.close()
    if prob_cross() == True:                                                #Se consulta la probabilidad para la segunda pareja de cromosomas
        corte = random.randint(1, 29)
        archivo = open(directorio, 'a')
        archivo.write("\nLa segunda pareja de cromosomas seleccionados por la ruleta se cortarán en la posicion: " + str(corte) + "\n\n")
        archivo.close()
        for i in range(corte,30):
            aux=x[2][i]
            x[2][i]=x[3][i]                                                 #Crossover de los 2 ultimos padres
            x[3][i]=aux
    else:
        archivo = open(directorio, 'a')
        archivo.write("\nLa segunda pareja de cromosomas seleccionados por la ruleta no se reproducirá\n\n")
        archivo.close()
    if prob_cross() == True:                                                #Se consulta la probabilidad para la segunda pareja de cromosomas
        corte = random.randint(1, 29)
        archivo = open(directorio, 'a')
        archivo.write("\nLa tercera pareja de cromosomas seleccionados por la ruleta se cortarán en la posicion: " + str(corte) + "\n\n")
        archivo.close()
        for i in range(corte,30):
            aux=x[4][i]
            x[4][i]=x[5][i]                                                 #Crossover de los 2 ultimos padres
            x[5][i]=aux
    else:
        archivo = open(directorio, 'a')
        archivo.write("\nLa tercera pareja de cromosomas seleccionados por la ruleta no se reproducirá\n\n")
        archivo.close()
    if prob_cross() == True:                                                #Se consulta la probabilidad para la segunda pareja de cromosomas
        corte = random.randint(1, 29)
        archivo = open(directorio, 'a')
        archivo.write("\nLa cuarta pareja de cromosomas seleccionados por la ruleta se cortarán en la posicion: " + str(corte) + "\n\n")
        archivo.close()
        for i in range(corte,30):
            aux=x[6][i]
            x[6][i]=x[7][i]                                                 #Crossover de los 2 ultimos padres
            x[7][i]=aux
    else:
        archivo = open(directorio, 'a')
        archivo.write("\nLa cuarta pareja de cromosomas seleccionados por la ruleta no se reproducirá\n\n")
        archivo.close()
    if prob_cross() == True:                                                #Se consulta la probabilidad para la segunda pareja de cromosomas
        corte = random.randint(1, 29)
        archivo = open(directorio, 'a')
        archivo.write("\nLa quinta pareja de cromosomas seleccionados por la ruleta se cortarán en la posicion: " + str(corte) + "\n\n")
        archivo.close()
        for i in range(corte,30):
            aux=x[8][i]
            x[8][i]=x[9][i]                                                 #Crossover de los 2 ultimos padres
            x[9][i]=aux
    else:
        archivo = open(directorio, 'a')
        archivo.write("\nLa quinta pareja de cromosomas seleccionados por la ruleta no se reproducirá\n\n")
        archivo.close()
    for p in range(len(x)):
        valor = random.random()
        if valor < 0.05:                                                     #Mutación
            corte=random.randint(1,29)
            if x[p][corte]=='0':
                x[p][corte]='1'
            else:
                x[p][corte]='0'
        else:
            mutacion=False


def ver_pobla(valorobjetivo,valorfitness,poblacion):                        #Función para ver la población generada
    for p in range(len(poblacion)):
        a=''
        for n in range(30):                                                 #Paso cromosoma(lista) a string para ahorrar espacio
            a = a + poblacion[p][n]
        archivo=open(directorio, 'a')
        archivo.write("Cromosoma "+str(p)+" : "+str(a)+" | Entero: "+str(val_cromo_entero[p])+" | Función Objetivo: "+str(valorobjetivo[p])+" | Fitness: "+str(valorfitness[p])+"\n")
        archivo.close()





"""--------------------------------------PROGRAMA PRINCIPAL------------------------------------------"""

tirada = (150)
val_obj = []                                                   # Lista con los valores de la función objeto de c/cromosoma de la población
val_fit = []                                                  # Lista con los valores de la función fitness de c/cromosoma de la población
val_cromo_entero = []
poblacion=[]                                                                #Lista con la población de cromosomas
pobl_ini(poblacion)                                                         # Defición de población inicial


max_min_prom = list(range(tirada))

for u in range(len(max_min_prom)):                                          #Creo lista donde se guardaran los datos para el archivo .csv
    del (max_min_prom[u])
    max_min_prom.insert(u, list(range(4)))


for generacion in range(tirada):

    #Las variables de abajo cambienlas dependiendo el SO que usen. El {0}.format(generacion) no lo borren, solo cambien los directorios que están entrecomillados
    # archivo{0}.format(generacion) es el nombre del archivo con los datos de cada generación, le pueden cambiar el nombre, pero el {0}.format...dejenlo como está.
    directorio = '/home/agus9/Documentos/hola1/rondas/ronda{0}.txt'.format(generacion)    #Este es el caso de directorios en Windows
    #Editen de la misma el directorio de este arhivo .csv, es el archivo que se genera para que lo puedan abrir con EXCEL.
    directorio_csv = '/home/agus9/Documentos/hola1/archivo.csv'

    archivo = open(directorio,'w+')                                        #Limpio archivo
    archivo.close()

    cromo_ruleta=[]                                                         #Lista con los cromosomas padres seleccionados para reproducirse
    seleccion=[]                                                            #Lista con la posición de los cromosomas seleccionados en la población


    func_obj(poblacion,val_obj,val_cromo_entero)                            #Calculo de func_obj de c/cromosoma de la población
    fitness(val_obj,val_fit)                                                #Calculo de fitness de c/cromosoma de la población
    archivo = open(directorio, 'a')
    archivo.write("----------Población Inicial------------\n\n")
    archivo.close()
    ver_pobla(val_obj,val_fit,poblacion)                                    #Muestra la población Inicial
    archivo = open(directorio, 'a')
    archivo.write("\n\n---------Se realiza selección por método ruleta-------------\n\n")
    archivo.close()
    ruleta(val_fit,cromo_ruleta,seleccion,poblacion)                        #Selección de padres a reproducirse
    secruza=prob_cross()                                                    #Determina la probabilidad de crossover
    crossover(cromo_ruleta)                                                 #Se realiza crossover(reproducción)

    poblacion=[]

    for i in range(10):                                                      #Se agregan los cromosomas hijos a la población
        auxiliar = [] + cromo_ruleta[i]
        poblacion.append(auxiliar)

    val_obj=[]
    val_cromo_entero=[]
    val_fit=[]

    func_obj(poblacion, val_obj, val_cromo_entero)                          # Calculo de func_obj de c/cromosoma de la POBLACIÓN MODIFICADA
    fitness(val_obj, val_fit)                                               # Calculo de fitness de c/cromosoma de la POBLACIÓN MODIFICADA

    archivo = open(directorio, 'a')
    archivo.write("\n----------------Población modificada por reproducción de padres-----------------\n\n")
    archivo.close()
    ver_pobla(val_obj,val_fit,poblacion)                                    #Muestra la población modificada


    for a in range(len(val_obj)):                                           #Busco el índice del cromosoma con mayor valor objetivo
        if val_obj[a]==max(val_obj):
            indice_max=a


    for p in range(len(val_obj)):                                           #Busco el índice del cromosoma con menor valor objetivo
        if val_obj[p]==min(val_obj):
            indice_min=p

    prome=0
    for y in range(len(val_obj)):                                           #Busco el valor objetivo promedio de cada cromosoma
        prome+=val_obj[y]
    prome=prome/10


    max_min_prom[generacion][0]=generacion                                  #Asigno los valores para pasar a EXCEL
    max_min_prom[generacion][1]=str(max(val_obj))
    max_min_prom[generacion][2]=str(min(val_obj))
    max_min_prom[generacion][3]=str(prome)


    archivo = open(directorio, 'a')
    archivo.write("\n\nEl cromosoma "+str(indice_max)+" es el máximo valor objetivo de la ronda {0}, y su funcion objetivo es: ".format(generacion)+str(val_obj[indice_max])+"\n\n")
    archivo.write("\n\nEl cromosoma "+str(indice_min)+" es el mínimo valor objetivo de la ronda {0} , y su funcion objetivo es: ".format(generacion)+str(val_obj[indice_min])+"\n\n")
    archivo.write("---------------------------------------------------------------------------------------------------------------------------------\n")
    archivo.write("---------------------------------------------RONDA {0}-------------------------------------------------------------------------------".format(generacion)+"\n")
    archivo.write("---------------------------------------------------------------------------------------------------------------------------------\n\n\n")
    archivo.close()



archivo=open(directorio_csv,'w+')                                           #Abro archivo .csv y paso los valores para usar en EXCEL

max_min_prom.insert(0,["Ronda","Maximo","Minimo","Promedio"])
with archivo:
    escribo=csv.writer(archivo,dialect="excel",delimiter=';')
    escribo.writerows(max_min_prom)
