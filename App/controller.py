"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
import model
import csv


"""
El controlador se encarga de mediar entre la vista y el modelo.
"""

# Inicialización del Catálogo de libros

# Funciones para la carga de datos

def loadData():
    File = "context_content_features-small.csv"
    File2= "user_track_hashtag_timestamp-small.csv"
    File3= "sentiment_values.csv"
    MusicRecomender = model.newMusicRecomender()
    File = cf.data_dir + File
    File2 = cf.data_dir + File2
    File3 = cf.data_dir + File3
    input_file = csv.DictReader(open(File, encoding="utf-8"), delimiter=",")
    for Entry in input_file:
        model.addEventoEscucha(MusicRecomender, Entry)
    input_file = csv.DictReader(open(File2, encoding="utf-8"), delimiter=",")
    for Entry in input_file:
        model.addEventoEscucha2(MusicRecomender, Entry)
    input_file = csv.DictReader(open(File3, encoding="utf-8"), delimiter=",")
    for Entry in input_file:
        model.addEventoEscucha3(MusicRecomender, Entry)
    model.CrearTablaTempos(MusicRecomender)    
    return MusicRecomender
    
def addData(MusicRecomender,Requerimiento,limInf=0,LimDer=1,CaracContenido="instrumentalness"):
    return model.addEventosRBT(MusicRecomender,Requerimiento,CaracContenido,limInf,LimDer)

def addData2(MusicRecomender,catalog2,Requerimiento,limInf=0,LimDer=1,CaracContenido="instrumentalness"):
    return model.addEventosRBT2(MusicRecomender,catalog2,Requerimiento,CaracContenido,limInf,LimDer)

def addNuevoGenero(catalog,nombre,Min,Max):
    model.addNuevoGenero(catalog,nombre,Min,Max)
# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

def getEventosEscuchaByRange(analyzer, initialInfo, finalInfo, Requerimiento=1):
    return model.getEventosByRange(analyzer,initialInfo,finalInfo,Requerimiento)

def getEventosEscuchaByRange2(analyzer, initialInfo, finalInfo):
    return model.getEventosByRange2(analyzer,initialInfo,finalInfo)

def getDatosGenero(analyzer, genero):
    return model.getDatosGenero(analyzer, genero)

def getGeneros(analyzer):
    return model.getGeneros(analyzer)

def EventosEscuchaSize(MusicRecomender):
    return model.EventosEscuchaSize(MusicRecomender)

def indexHeight(MusicRecomender):
    return model.indexHeight(MusicRecomender)


def indexSize(MusicRecomender):
    return model.indexSize(MusicRecomender)

def Requerimiento5(catalog,Requerimiento):
    model.Requerimiento5(catalog,Requerimiento)

def minKey(MusicRecomender):
    return model.minKey(MusicRecomender)


def maxKey(MusicRecomender):
    return model.maxKey(MusicRecomender)
