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
    MusicRecomender = {'EventosEscucha': None, 'Carac': None}
    MusicRecomender['EventosEscucha'] = lt.newList('ARRAY_LIST', compareIds)
    #MusicRecomender['Caracs'] = om.newMap(omaptype='RBT', comparefunction=compareValues)
    return MusicRecomender

def newArtistEntry(EventoEscucha):
    entry = {'Artisits': None, 'lstArtisits': None}
    #entry['Artisits'] = m.newMap(numelements=10000, maptype='PROBING', loadfactor=0.5, comparefunction=compareArtist)
    entry['lstArtisits'] = lt.newList('ARRAY_LIST', compareValues)
    return entry

def newArtistSingularEntry(id, EventoEscucha):
    Caraentry = {'ArtisitSingular': None, 'lstSongsArtist': None}
    Caraentry['ArtisitSingular'] = id
    Caraentry['lstSongsArtist'] = lt.newList('ARRAY_LIST')
    return Caraentry

# Funciones para agregar informacion al catalogo

def addEventoEscucha(MusicRecomender, EventoEscucha):
    lt.addLast(MusicRecomender['EventosEscucha'], EventoEscucha)
    return MusicRecomender

def addEventosRBT(MusicRecomender,tipoCaraCont):
    MusicRecomender['Caracs'] = om.newMap(omaptype='RBT', comparefunction=compareValues)
    i=1
    while i<=lt.size(MusicRecomender['EventosEscucha']):
        EventoEscucha = lt.getElement(MusicRecomender['EventosEscucha'],i)
        updateCaracIndex(MusicRecomender['Caracs'], EventoEscucha,tipoCaraCont)
        i+=1
    return MusicRecomender

def updateCaracIndex(map, EventoEscucha,tipoCaraCont):
    value = float(EventoEscucha[tipoCaraCont])
    entry = om.get(map, value)
    if entry is None:
        Artistentry = newArtistEntry(EventoEscucha)
        om.put(map, value, Artistentry)
    else:
        Artistentry = me.getValue(entry)
    addArtisitIndex(Artistentry, EventoEscucha)
    return map

def addArtisitIndex(Artistentry, EventoEscucha):
    lst = Artistentry['lstArtisits']
    lt.addLast(lst, EventoEscucha)
    """ArtisitIndex = Artistentry['Artisits']
    Arentry = m.get(ArtisitIndex, EventoEscucha['artist_id'])
    if (Arentry is None):
        entry = newArtistSingularEntry(EventoEscucha['artist_id'], EventoEscucha)
        lt.addLast(entry['lstSongsArtist'], EventoEscucha)
        m.put(ArtisitIndex, EventoEscucha['artist_id'], entry)
    else:
        entry = me.getValue(Arentry)
        lt.addLast(entry['lstSongsArtist'], EventoEscucha)"""
    return Artistentry


# Funciones de consulta

def crimesSize(analyzer):
    """
    Número de crimenes
    """
    return lt.size(analyzer['EventosEscucha'])


def indexHeight(analyzer):
    """
    Altura del arbol
    """
    return om.height(analyzer['Caracs'])


def indexSize(analyzer):
    """
    Numero de elementos en el indice
    """
    return om.size(analyzer['Caracs'])


def minKey(analyzer):
    """
    Llave mas pequena
    """
    return om.minKey(analyzer['Caracs'])


def maxKey(analyzer):
    """
    Llave mas grande
    """
    return om.maxKey(analyzer['Caracs'])


# Funciones utilizadas para comparar elementos dentro de una lista

# Funciones de ordenamiento

#Funciones de comparacion

def compareIds(id1, id2):
    """
    Compara dos crimenes
    """
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
