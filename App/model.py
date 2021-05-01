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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import map as m
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

# Funciones para creacion de datos

def newMusicRecomender():
    MusicRecomender = {'EventosEscucha': None, 'Carac': None, 'Artists':None}
    MusicRecomender['EventosEscucha'] = lt.newList('ARRAY_LIST', cmpfunction=compareIds)
    return MusicRecomender

def newEventEntry(EventoEscucha):
    entry = {'lstEvent': None}
    entry['lstEvent'] = lt.newList('ARRAY_LIST', compareValues)
    return entry

def newArtistEntry(id):
    Arentry = {'ArtistId': None, 'ArtistIsPresent': bool}
    Arentry['ArtistId'] = id
    Arentry['ArtistIsPresent'] = False
    return Arentry

# Funciones para agregar informacion al catalogo

def addEventoEscucha(MusicRecomender, EventoEscucha):
    lt.addLast(MusicRecomender['EventosEscucha'], EventoEscucha)
    return MusicRecomender

def addEventosRBT(MusicRecomender,Requerimiento,tipoCaraCont,limInf,LimDer):
    MusicRecomender['Artists'] = m.newMap(numelements=5000, maptype='CHAINING', loadfactor=4.0, comparefunction=compareArtist)
    MusicRecomender['Caracs'] = om.newMap(omaptype='RBT', comparefunction=compareValues)
    i=1
    while i<=lt.size(MusicRecomender['EventosEscucha']):
        EventoEscucha = lt.getElement(MusicRecomender['EventosEscucha'],i)
        if Requerimiento==1:
            updateCaracIndex(MusicRecomender, EventoEscucha,tipoCaraCont,Requerimiento,limInf,LimDer)
        elif Requerimiento==2:
            pass
        elif Requerimiento==3:
            pass
        elif Requerimiento==4:
            tipoCaraCont="tempo"
            updateCaracIndex(MusicRecomender, EventoEscucha, tipoCaraCont, Requerimiento, limInf, LimDer)
        elif Requerimiento==5:
            pass
        else:
            updateCaracIndex(MusicRecomender, EventoEscucha,tipoCaraCont,Requerimiento, limInf, LimDer)
        i+=1
    return MusicRecomender

def updateCaracIndex(MusicRecomender, EventoEscucha, tipoCaraCont,Requerimiento, limInfe,LimSup):
    value = float(EventoEscucha[tipoCaraCont])
    if Requerimiento==1:
        if value<limInfe or value>LimSup:
            return MusicRecomender['Caracs']
    elif Requerimiento==4:
        if value<limInfe or value>LimSup:
            return MusicRecomender['Caracs']
    Artists=MusicRecomender['Artists']
    entry = om.get(MusicRecomender['Caracs'], value)
    if entry is None:
        EventEntry = newEventEntry(EventoEscucha)
        om.put(MusicRecomender['Caracs'], value, EventEntry)
    else:
        EventEntry = me.getValue(entry)
    addEventIndex(Artists,EventEntry, EventoEscucha)
    return MusicRecomender['Caracs']

def addEventIndex(Artists,EventEntry, EventoEscucha):
    lst = EventEntry['lstEvent']
    lt.addLast(lst, EventoEscucha)
    Arentry = m.get(Artists, EventoEscucha['artist_id'])
    if (Arentry is None):
        entry = newArtistEntry(EventoEscucha['artist_id'])
        m.put(Artists, EventoEscucha['artist_id'], entry)
    return EventEntry

# Funciones de consulta

def EventosEscuchaSize(analyzer):
    return lt.size(analyzer['EventosEscucha'])


def indexHeight(analyzer):
    return om.height(analyzer['Caracs'])


def indexSize(analyzer):
    return om.size(analyzer['Caracs'])


def minKey(analyzer):
    return om.minKey(analyzer['Caracs'])


def maxKey(analyzer):
    return om.maxKey(analyzer['Caracs'])


# Funciones utilizadas para comparar elementos dentro de una lista

def getEventosByRange(analyzer, initialInfo, finalInfo):
    lst = om.values(analyzer['Caracs'], initialInfo, finalInfo)
    totEvens = 0
    for lstEvent in lt.iterator(lst):
        totEvens += lt.size(lstEvent['lstEvent'])
    sizeTabla=lt.size(m.keySet(analyzer['Artists']))
    return totEvens,sizeTabla

# Funciones de ordenamiento

#Funciones de comparacion

def compareIds(id1, id2):
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1


def compareValues(value1, value2):
    if (value1 == value2):
        return 0
    elif (value1 > value2):
        return 1
    else:
        return -1


def compareArtist(Artist1, Artist2):
    Artist = me.getKey(Artist2)
    if (Artist1 == Artist):
        return 0
    elif (Artist1 > Artist):
        return 1
    else:
        return -1
