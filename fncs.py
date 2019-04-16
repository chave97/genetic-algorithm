import csv

def escribir_archivo(poblacion,tirada):                     #Escribo datos de las poblaciones en hojas de calculo
    archivo=open("./registro.csv","a")
    with archivo:
        cabecera=[[str(tirada),str(poblacion.max_func_obj),str(poblacion.min_func_obj),str(poblacion.prom_func_obj)]]
        escribir=csv.writer(archivo,dialect="excel",delimiter=';')
        escribir.writerows(cabecera)
    print("Archivo actualizado")

def escribir_archivo_inicio():                              #Escribo datos de la primera poblacion generada en la hoja de calculo
    archivo=open("./registro.csv","a")
    with archivo:
        cabecera=[["Ronda","Maximo","Minimo","Promedio"]]
        escribir=csv.writer(archivo,dialect="excel",delimiter=";")
        escribir.writerows(cabecera)

def limpiar_archivo():
    archivo=open("./registro.csv","w")
    with archivo:
        print("Archivo limpio")