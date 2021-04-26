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
    MusicRecomender = model.newMusicRecomender()
    File = cf.data_dir + File
    input_file = csv.DictReader(open(File, encoding="utf-8"), delimiter=",")
    for Entry in input_file:
        model.addEventoEscucha(MusicRecomender, Entry)
    return MusicRecomender
    
def addData(MusicRecomender,Requerimiento,limInf=0,LimDer=1,CaracContenido="instrumentalness"):
    return model.addEventosRBT(MusicRecomender,Requerimiento,CaracContenido,limInf,LimDer)
# Funciones de ordenamiento

# Funciones de consulta sobre el catálogo

def getEventosEscuchaByRange(analyzer, initialInfo, finalInfo):
    return model.getEventosByRange(analyzer,initialInfo,finalInfo)

def EventosEscuchaSize(MusicRecomender):
    return model.EventosEscuchaSize(MusicRecomender)

def indexHeight(MusicRecomender):
    return model.indexHeight(MusicRecomender)


def indexSize(MusicRecomender):
    return model.indexSize(MusicRecomender)


def minKey(MusicRecomender):
    return model.minKey(MusicRecomender)


def maxKey(MusicRecomender):
    return model.maxKey(MusicRecomender)
