#------------------------------------------------------------------------------------------------------------

from clss import *                                          #Importo clases del modulo clss.py
from fncs import *                                          #Importo funciones del modulo fncs.py

#-------------------------------Programa Principal ----------------------------------------------------------
limpiar_archivo()                                           #Limpio hoja de calculo
pobla=Poblacion()                                           #Instancia de la clase Poblacion
pobla.generar_poblacion()              
#Muestro poblacion Inicial
print("-"*40+"Poblacion inicial"+"-"*40)
pobla.mostrar_contenido()                                   #Muestro poblacion y sus cromosomas
escribir_archivo_inicio()                                   #Agrego primeras lineas a la hoja de calculo
pobla.calcular_fobjetivo()                                  #Calculo funcion objetivo de c/cromosoma
pobla.suma_de_objetivo()
pobla.calcular_fitness()                                    #Calculo funcion objetivo de c/cromosoma
pobla.calcular_max_min()
escribir_archivo(pobla,"Inicial")                           #Escribo los datos de la primera poblacion en hoja de calculo
print("-"*100)
#Fin poblacion Inicial
for tiradas in range(20):
    #Realizo funciones sobre la población actual
    pobla.seleccion()
    pobla.crossover()
    pobla.mutacion()
    pobla.nueva_poblacion()
    #Muestro nueva población modificada y realizo funciones sobre la misma
    print("-"*40+"Poblacion nueva"+"-"*40)
    pobla.calcular_fobjetivo()
    pobla.suma_de_objetivo()
    pobla.calcular_fitness()
    pobla.mostrar_contenido()
    print("-"*100)
    #Guardo los datos de la nueva población en archivo
    pobla.calcular_max_min()
    escribir_archivo(pobla,tiradas)                                     
    