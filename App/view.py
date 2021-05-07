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
import random as ran
from DISClib.ADT import list as lt
import time
assert cf


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
def CambioDeValores(CaracContenido,Requerimiento,CadenaResultado=""):
    CadenaResultado
    if Requerimiento==1:
        if CaracContenido==1:
            CadenaResultado = "instrumentalness"
        elif CaracContenido==2:
            CadenaResultado = "liveness"
        elif CaracContenido==3:
            CadenaResultado = "speechiness"
        elif CaracContenido==4:
            CadenaResultado = "danceability"
        elif CaracContenido==5:
            CadenaResultado = "valence"
        elif CaracContenido==6:
            CadenaResultado = "loudness"
        elif CaracContenido==7:
            CadenaResultado = "tempo"
        elif CaracContenido==8:
            CadenaResultado = "acousticness"
        elif CaracContenido==9:
            CadenaResultado = "energy"
        elif CaracContenido==10:
            CadenaResultado = "mode"
        elif CaracContenido==11:
            CadenaResultado = "key"
    elif Requerimiento==4:
        if CaracContenido==1:
            if not("Reggae" in CadenaResultado):
                if not(CadenaResultado==""):
                    CadenaResultado = CadenaResultado+", "
                CadenaResultado = CadenaResultado+"Reggae"
        elif CaracContenido==2:
            if not("Down-tempo" in CadenaResultado):
                if not(CadenaResultado==""):
                    CadenaResultado = CadenaResultado+", "
                CadenaResultado = CadenaResultado+"Down-tempo"
        elif CaracContenido==3:
            if not("Chill-out" in CadenaResultado):
                if not(CadenaResultado==""):
                    CadenaResultado = CadenaResultado+", "
                CadenaResultado = CadenaResultado+"Chill-out"
        elif CaracContenido==4:
            if not("Hip-hop" in CadenaResultado):
                if not(CadenaResultado==""):
                    CadenaResultado = CadenaResultado+", "
                CadenaResultado = CadenaResultado+"Hip-hop"
        elif CaracContenido==5:
            if not("Jazz and Funk" in CadenaResultado):
                if not(CadenaResultado==""):
                    CadenaResultado = CadenaResultado+", "
                CadenaResultado = CadenaResultado+"Jazz and Funk"
        elif CaracContenido==6:
            if not("Pop" in CadenaResultado):
                if not(CadenaResultado==""):
                    CadenaResultado = CadenaResultado+", "
                CadenaResultado = CadenaResultado+"Pop"
        elif CaracContenido==7:
            if not("R&B" in CadenaResultado):
                if not(CadenaResultado==""):
                    CadenaResultado = CadenaResultado+", "
                CadenaResultado = CadenaResultado+"R&B"
        elif CaracContenido==8:
            if not("Rock" in CadenaResultado):
                if not(CadenaResultado==""):
                    CadenaResultado = CadenaResultado+", "
                CadenaResultado = CadenaResultado+"Rock"
        elif CaracContenido==9:
            if not("Metal" in CadenaResultado):
                if not(CadenaResultado==""):
                    CadenaResultado = CadenaResultado+", "
                CadenaResultado = CadenaResultado+"Metal"
    return CadenaResultado

def ValoresGeneros(genero):
    Min=0
    Max=0
    if genero=="Reggae":
        Min=60
        Max=90
    elif genero=="Down-tempo":
        Min=70
        Max=100
    elif genero=="Chill-out":
        Min=90
        Max=120
    elif genero=="Hip-hop":
        Min=85
        Max=115
    elif genero=="Jazz and Funk":
        Min=120
        Max=125
    elif genero=="Pop":
        Min=100
        Max=130
    elif genero=="R&B,":
        Min=60
        Max=80
    elif genero=="Rock":
        Min=110
        Max=140
    elif genero=="Metal":
        Min=100
        Max=160
    return Min,Max

def Requerimiento4(catalog,Requerimiento,CaracContenido):
    Generos = CaracContenido.split(",")
    i=0
    while i<len(Generos):
        Min,Max=ValoresGeneros(Generos[i].strip())
        catalog = controller.addData(catalog,Requerimiento,Min,Max)
        totalEvento,TotalArtist = controller.getEventosEscuchaByRange(catalog, Min, Max)
        print("\nTotal de Eventos de escuha en el rango dado: ",totalEvento)
        print("\nTotal de Artistas en el rango dado: ",TotalArtist)
        i+=1

def printPistas(lista, Requerimiento):
    formato_1 = "Track {}: {} con instrumentalness de {} y tempo de {}"
    formato_2 = "Track {}: {} con energy de {} y danceability de {}"
    if (lt.size(lista) <= 5):
        i = 1
        while i <= lt.size(lista):
            track_id = lt.getElement(lista,i)["track_id"]
            if(Requerimiento == 2):
                ener = lt.getElement(lista,i)["energy"]
                dance = lt.getElement(lista,i)["danceability"]
                print(formato_2.format(i,track_id,ener,dance))
            if(Requerimiento == 3):
                instru = lt.getElement(lista,i)["instrumentalness"]
                tempo = lt.getElement(lista,i)["tempo"]
                print(formato_1.format(i,track_id,instru,tempo))
            i += 1
    else:
        numeros = []
        while len(numeros) != 5:
            numero = ran.randint(1,lt.size(lista))
            if not(numero in numeros):
                numeros.append(numero)
        i = 1
        while i <= len(numeros):
            track_id = lt.getElement(lista,numeros[i-1])['track_id']
            if(Requerimiento == 2):
                ener = lt.getElement(lista,numeros[i-1])['energy']
                dance = lt.getElement(lista,numeros[i-1])['danceability']
                print(formato_2.format(i,track_id,ener,dance))
            if(Requerimiento == 3):
                instru = lt.getElement(lista,numeros[i-1])["instrumentalness"]
                tempo = lt.getElement(lista,numeros[i-1])["tempo"]
                print(formato_1.format(i,track_id,instru,tempo))
            i += 1
    
    


def printMenu():
    print(" ")
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
        Requerimiento = 1
        CaracContenido = 0
        while CaracContenido>11 or  CaracContenido<1:
            print(" ")
            print("===Caracteristicas de Contenido===")
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
        CaracContenido = CambioDeValores(CaracContenido,Requerimiento)
        t1 = time.process_time()
        catalog = controller.addData(catalog,Requerimiento,initialInfo,finalInfo,CaracContenido)
        totalEvento,totalArtist,lista = controller.getEventosEscuchaByRange(catalog, initialInfo, finalInfo)
        t2 = time.process_time()
        time_mseg = (t2 - t1)*1000
        print(" ")
        print ("Tiempo de ejecucion: ",time_mseg," milisegundos.")
        print("Total Eventos Reproducción:",totalEvento)
        print("Total Artistas Unicos:",totalArtist)
    
    elif int(inputs[0]) == 3:
        print("Ingrese el rango de Energy:")
        LimInf1 = float(input("Rango inferior:  "))
        LimSup1 = float(input("Rango superior:  "))
        print("Ingrese el rango de Danceability:")
        LimInf2 = float(input("Rango inferior:  "))
        LimSup2 = float(input("Rango superior:  "))
        Requerimiento = 2
        t1 = time.process_time()
        catalog = controller.addData(catalog,Requerimiento,LimInf1,LimSup1,'energy')
        catalog2 = {"Caracs": catalog['Caracs']}
        catalog = controller.addData2(catalog,catalog2,Requerimiento,LimInf2,LimSup2,'danceability')
        totalEvento,lista = controller.Requerimiento2(catalog, LimInf2, LimSup2)
        t2 = time.process_time()
        time_mseg = (t2 - t1)*1000
        print(" ")
        print ("Tiempo de ejecucion: ",time_mseg," milisegundos.")
        print("Total Eventos Unicos:",totalEvento)
        print("----Tracks---")
        printPistas(lista,Requerimiento)

    elif int(inputs[0]) == 4:
        print("***Ingrese el rango de Instrumentalness:")
        limInfInstru = float(input("Rango inferior: "))
        limSupInstru = float(input("Rango superior: "))
        print("***Ingrese el rango de Tempo:")
        limInfTempo = float(input("Rango inferior: "))
        limSupTempo = float(input("Rango superior: "))
        Requerimiento = 3
        t1 = time.process_time()
        catalog = controller.addData(catalog,Requerimiento,limInfInstru,limSupInstru,"instrumentalness")
        catalog2 = {"Caracs": catalog['Caracs']}
        catalog = controller.addData2(catalog,catalog2,Requerimiento,limInfTempo,limSupTempo,"tempo")
        totalEvento,totalArtist,lista = controller.getEventosEscuchaByRange2(catalog, limInfTempo, limSupTempo)
        t2 = time.process_time()
        time_mseg = (t2 - t1)*1000
        print(" ")
        print ("Tiempo de ejecucion: ",time_mseg," milisegundos.")
        print("Total Eventos Unicos:",totalEvento)
        print("----Tracks---")
        printPistas(lista,Requerimiento)

    elif int(inputs[0]) == 5:
        Requerimiento = 4
        verifica=True
        CadenaResultado=""
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
            print("10- Escribirlo Manualmente")
            GenerosConsultaID = int(input("Seleccione el género que desea consultar:      "))
            if CadenaResultado=="":
                CadenaResultado = CambioDeValores(GenerosConsultaID,Requerimiento)
            else:
                CadenaResultado = CambioDeValores(GenerosConsultaID,Requerimiento,CadenaResultado)
            print("Estos son los géneros que desea consultar por el momento: ",CadenaResultado)
            print("¿Desea Agregar otro genero para consultar?:      ")
            print("1- SI")
            print("2- NO")
            Preseguir=int(input("Ingrese su selección:      "))
            if Preseguir==2:
                verifica=False
        t1 = time.process_time()
        Requerimiento4(catalog,Requerimiento,CadenaResultado)
        t2 = time.process_time()
        time_mseg = (t2 - t1)*1000
        print ("Tiempo de ejecucion: ",time_mseg," milisegundos.")

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