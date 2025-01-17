﻿"""
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
from DISClib.ADT import map as m
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
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
    respuesta = None
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
        elif CaracContenido==10:
            nombre1 = input("Ingrese el nombre del genero: ").strip()
            nombre2 = nombre1.strip().lower()
            resultado = controller.getDatosGenero(catalog,nombre2)
            if resultado:
                if not(nombre1 in CadenaResultado):
                    if not(CadenaResultado==""):
                        CadenaResultado = CadenaResultado+", "
                    CadenaResultado = CadenaResultado+nombre1
            else: 
                respuesta = "No existe"
                print("El genero", nombre2, "no existe\n")
    return CadenaResultado,respuesta

def ValoresGeneros(catalog,genero):
    genero = genero.lower()
    datos_genero = controller.getDatosGenero(catalog,genero)
    Min = lt.getElement(datos_genero,1)
    Max = lt.getElement(datos_genero,2)
    return Min,Max

def addNuevoGenero(catalog,nombre,Min,Max):
    controller.addNuevoGenero(catalog,nombre,Min,Max)

def Requerimiento4(catalog,Requerimiento,CaracContenido):
    Generos = CaracContenido.split(",")
    total_eventos = 0
    i=0
    while i<len(Generos):
        Min,Max=ValoresGeneros(catalog,Generos[i].strip())
        catalog = controller.addData(catalog,Requerimiento,Min,Max,'tempo')
        totalEvento,TotalArtist,lista = controller.getEventosEscuchaByRange(catalog, Min, Max,Requerimiento)
        total_eventos += totalEvento 
        printArtistas(lista,Generos[i].strip(),TotalArtist,totalEvento)
        i+=1
    print("Total de reproducciones de todos los generos: "+str(total_eventos))

def Requerimiento5(catalog,catalog2,Requerimiento,Generos,initialInfo,finalInfo):
    total_eventos = 0
    mayor = 0
    DatosMayor = {}
    infoMayor = 0
    i=1
    print(" ")
    ordenes = lt.newList('ARRAY_LIST')
    while i<= lt.size(Generos):
        genero = lt.getElement(Generos,i).strip()
        Min,Max=ValoresGeneros(catalog,genero)
        Requerimiento=4
        catalog = controller.addData2(catalog,catalog2,Requerimiento,Min,Max,"tempo")
        RequerimientoTrue=5
        totalEvento,TotalArtist,lista = controller.getEventosEscuchaByRange(catalog, Min, Max,Requerimiento,RequerimientoTrue)
        total_eventos += totalEvento
        if totalEvento>mayor:
            DatosMayor=lista
            mayor=totalEvento
        i+=1
        info=(genero,totalEvento)
        lt.addLast(ordenes,info)
    ordenes=controller.OrdenarGeneros(ordenes)
    i=1
    while i<lt.size(ordenes):
        datos = lt.getElement(ordenes,i)
        if i==1:
            infoMayor=datos
        printGenero(i,datos[0],datos[1])
        i+=1
    result,tot = controller.Requerimiento5_2(DatosMayor,catalog,initialInfo,finalInfo)
    print(infoMayor[0]," tiene un total de: ",tot," tracks unicas")
    i = 1
    maximun=11
    if lt.size(result)<10:
        maximun=lt.size(result)
    while i<maximun:
        print("TOP ",i," track: ",lt.getElement(result,i)[0][0]," con ", lt.getElement(result,i)[1]," hashtags y un VADER = ",lt.getElement(result,i)[0][1])
        i+=1
    return total_eventos

def printDatosCargados():
    print("___Se cargaron___")
    print("} " + str(lt.size(catalog["EventosEscucha"])) + " eventos de escucha.")
    print("} " + str(lt.size(catalog["Artists"])) + " artistas unicos.")
    print("} " + str(lt.size(controller.getPistas(catalog))) + " pistas unicas.")
    PrintEventos()

def PrintEventos():
    if(lt.size(catalog['EventosEscucha']) <=10):
        i = 1
        for elemento in lt.iterator(catalog['EventosEscucha']):
            texto = str(i) + "- " + "id: " + str(elemento["id"])
            for caracteristica in elemento:
                if not(caracteristica == "instrumentalness"):
                    texto += ", " + str(elemento[caracteristica])
            print(texto)
            i += 1
    else:
        a = 1
        i = 1
        while i <= 5:
            texto = str(a) + "- " + "id: " + str((lt.getElement(catalog['EventosEscucha'],i))["id"])
            for caracteristica in lt.getElement(catalog['EventosEscucha'],i):
                if not(lt.getElement(catalog['EventosEscucha'],i)["id"] == "instrumentalness"):
                    texto += ", " + str(caracteristica) + ": " + str(lt.getElement(catalog['EventosEscucha'],i)[caracteristica])
            print(texto)
            i += 1
            a += 1
        i = lt.size(catalog['EventosEscucha'])
        while i > (lt.size(catalog["EventosEscucha"])-5):
            texto = str(a) + "- " + "id: " + str((lt.getElement(catalog['EventosEscucha'],i))["id"])
            for caracteristica in lt.getElement(catalog['EventosEscucha'],i):
                if not(lt.getElement(catalog['EventosEscucha'],i)["id"] == "instrumentalness"):
                    texto += ", " + str(caracteristica) + ": " + str(lt.getElement(catalog['EventosEscucha'],i)[caracteristica])
            print(texto)
            i -= 1
            a += 1
        print(" ")

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
    
def printArtistas(lista,genero,artistas,eventos):
    formato_1 = "Reproducciones de {}: {} con {} artistas unicos"
    formato_2 = "_______Algunos artistas de {}_______"
    formato_3 = "Artista {}: {}"
    print(formato_1.format(genero,eventos,artistas))
    print(formato_2.format(genero))
    i = 1
    while i <= 10 and i <=lt.size(lista):
        artista_id = lt.getElement(lista,i)
        print(formato_3.format(i,artista_id))
        i +=1
    print(" ")

def printGenero(numero,genero,reproducciones):
    formato_1 = "{}- {} con {} reproducciones"
    print(formato_1.format(numero,genero,reproducciones))

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
        t1 = time.process_time()
        catalog = controller.loadData()
        printDatosCargados()
        t2 = time.process_time()
        time_mseg = (t2 - t1)*1000
        print ("Tiempo de ejecucion: ",time_mseg," milisegundos.")

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
        CaracContenido,r = CambioDeValores(CaracContenido,Requerimiento)
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
        totalEvento,lista = controller.getEventosEscuchaByRange2(catalog, LimInf2, LimSup2)
        t2 = time.process_time()
        time_mseg = (t2 - t1)*1000
        print(" ")
        print ("Tiempo de ejecucion: ",time_mseg," milisegundos.")
        print("Total Tracks Unicos:",totalEvento)
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
        totalEvento,lista = controller.getEventosEscuchaByRange2(catalog, limInfTempo, limSupTempo)
        t2 = time.process_time()
        time_mseg = (t2 - t1)*1000
        print(" ")
        print ("Tiempo de ejecucion: ",time_mseg," milisegundos.")
        print("Total Tracks Unicos:",totalEvento)
        print("----Tracks---")
        printPistas(lista,Requerimiento)

    elif int(inputs[0]) == 5:
        Requerimiento = 4
        verifica=True
        Preseguir = 1
        CadenaResultado=""
        while verifica:
            GenerosConsultaID = 0
            while GenerosConsultaID>11 or  GenerosConsultaID<1:
                print("\n1- Reggae")
                print("2- Down-tempo")
                print("3- Chill-out")
                print("4- Hip-hop")
                print("5- Jazz and Funk")
                print("6- Pop")
                print("7- R&B")
                print("8- Rock")
                print("9- Metal")
                print("10- Escribirlo Manualmente")
                print("11- Crear Nuevo Genero")
                GenerosConsultaID = int(input("Seleccione el género que desea consultar:      "))
                print(" ")
            if GenerosConsultaID == 11:
                print("______Crear Nuevo Genero______")
                nombre = input("Nombre: ")
                Min = float(input("Tempo Minimo: "))
                Max = float(input("Tempo Maximo: "))
                addNuevoGenero(catalog,nombre,Min,Max)
                print("¡Genero creado exitosamente!\n")
                print("\nEstos son los géneros que desea consultar por el momento: ",CadenaResultado)
            else:
                resultado = None
                if CadenaResultado=="":
                    CadenaResultado,resultado = CambioDeValores(GenerosConsultaID,Requerimiento)
                else:
                    CadenaResultado,resultado = CambioDeValores(GenerosConsultaID,Requerimiento,CadenaResultado)
                print("\nEstos son los géneros que desea consultar por el momento: ",CadenaResultado)
                if (resultado == None):
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
        verifica=False
        while not(verifica):
            verifica=True
            print("La introducción de la hora debe realizarse con el formate de 24 horas")
            horaInicio = input("Ingrese desde que hora quiere emepezar a consultar:  ")
            MinInicio = input("Ingrese desde que minutos quiere emepezar a consultar:  ")
            horaFin = input("Ingrese hasta que hora quiere consultar:   ")
            MinFin = input("Ingrese hasta que minutos quiere consultar:   ")
            if int(horaInicio)>23 or int(horaInicio)<0:
                print("Ha ingresado alguna hora que no es valida, intentelo nuevamente")
                verifica=False
            elif int(MinInicio)>60 or int(MinInicio)<0:
                print("Ha ingresado alguna hora que no es valida, intentelo nuevamente")
                verifica=False
            elif int(horaFin)>23 or int(horaFin)<0:
                print("Ha ingresado alguna hora que no es valida, intentelo nuevamente")
                verifica=False
            elif int(MinFin)>60 or int(MinFin)<0:
                print("Ha ingresado alguna hora que no es valida, intentelo nuevamente")
                verifica=False
        initialInfo = horaInicio+":"+MinInicio+":"+"00"
        finalInfo = horaFin+":"+MinFin+":"+"00"
        print("las horas de consulta serán desde: ",initialInfo," hasta: ", finalInfo, "\n")
        Requerimiento=5
        t1 = time.process_time()
        catalog = controller.addData(catalog,Requerimiento,initialInfo,finalInfo)
        catalog2 = {"Caracs": catalog['Caracs']}
        generos = controller.getGeneros(catalog)
        Requerimiento=4
        totalEvento = Requerimiento5(catalog,catalog2,Requerimiento,generos,initialInfo,finalInfo)
        t2 = time.process_time()
        time_mseg = (t2 - t1)*1000
        print("Hay un total de " + str(totalEvento) + " reproducciones entre " + str(initialInfo) + " y " + str(finalInfo))
        print(" ")
        print ("Tiempo de ejecucion: ",time_mseg," milisegundos.")

    else:
        print("\nApagando el sistema...")
        print("Hasta luego\n")
        sys.exit(0)
sys.exit(0)
