"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
import time
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
def CambioDeValores(CaracContenido):
    if CaracContenido==1:
        return "instrumentalness"
    elif CaracContenido==2:
        return "liveness"
    elif CaracContenido==3:
        return "speechiness"
    elif CaracContenido==4:
        return "danceability"
    elif CaracContenido==5:
        return "valence"
    elif CaracContenido==6:
        return "loudness"
    elif CaracContenido==7:
        return "tempo"
    elif CaracContenido==8:
        return "acousticness"
    elif CaracContenido==9:
        return "energy"
    elif CaracContenido==10:
        return "mode"
    elif CaracContenido==11:
        return "key"


def printMenu():
    print("Bienvenido")
    print("1- Cargar datos al catálogo")
    print("2- Requerimiento 1")
    print("3- Requerimiento 2")
    print("4- Requerimiento 3")
    print("5- Requerimiento 4")
    print("6- Requerimiento 5")

catalog = None

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Cargando información de los archivos ....")
        catalog = controller.loadData()

    elif int(inputs[0]) == 2:
        CaracContenido = 0
        while CaracContenido>11 or  CaracContenido<1:
            print("1- instrumentalness")
            print("2- liveness")
            print("3- speechiness")
            print("4- danceability")
            print("5- valence")
            print("6- loudness")
            print("7- tempo")
            print("8- acousticness")
            print("9- energy")
            print("10- mode")
            print("11- key")
            CaracContenido = int(input("Seleccione la característica de contenido que desea consultar:      "))
        initialInfo = float(input("Rango inferior: "))
        finalInfo = float(input("Rango superior: "))
        CaracContenido = CambioDeValores(CaracContenido)
        Requerimiento = 1
        t1 = time.process_time()
        catalog = controller.addData(catalog,CaracContenido,Requerimiento,initialInfo,finalInfo)
        totalEvento,TotalArtist = controller.getEventosEscuchaByRange(catalog, initialInfo, finalInfo)
        t2 = time.process_time()
        time_mseg = (t2 - t1)*1000
        print ("Tiempo de ejecucion: ",time_mseg," milisegundos.")
        print("\nTotal de Eventos de escuha en el rango dado: ",totalEvento)
        print("\nTotal de Artistas en el rango dado: ",TotalArtist)
    
    elif int(inputs[0]) == 3:
        pass

    elif int(inputs[0]) == 4:
        pass        

    elif int(inputs[0]) == 5:
        verifica=True
        while verifica:
            print("1- Reggae")
            print("2- Down-tempo")
            print("3- Chill-out")
            print("4- Hip-hop")
            print("5- Jazz and Funk")
            print("6- Pop")
            print("7- R&B")
            print("8- Rock")
            print("9- Metal")
            print("11- Escribirlo Manualmente")
            GenerosConsultaID = int(input("Seleccione la característica de contenido que desea consultar:      "))
            print("¿Desea Agregar otro genero para consultar?:      ")
            print("1- SI")
            print("2- NO")
            Preseguir=int(input("Ingrese su selección:      "))
            if Preseguir==2:
                verifica=False
        Requerimiento = 4
        t1 = time.process_time()
        catalog = controller.addData(catalog,Requerimiento,initialInfo,finalInfo)
        totalEvento,TotalArtist = controller.getEventosEscuchaByRange(catalog, initialInfo, finalInfo)
        t2 = time.process_time()
        time_mseg = (t2 - t1)*1000
        print ("Tiempo de ejecucion: ",time_mseg," milisegundos.")
        print("\nTotal de Eventos de escuha en el rango dado: ",totalEvento)
        print("\nTotal de Artistas en el rango dado: ",TotalArtist)

    elif int(inputs[0]) == 6:
        pass

    else:
        sys.exit(0)
sys.exit(0)



"""print('Eventos cargados: ' + str(controller.EventosEscuchaSize(catalog)))
print('Altura del arbol: ' + str(controller.indexHeight(catalog)))
print('Elementos en el arbol: ' + str(controller.indexSize(catalog)))
print('Menor Llave: ' + str(controller.minKey(catalog)))
print('Mayor Llave: ' + str(controller.maxKey(catalog)))"""