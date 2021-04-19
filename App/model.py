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
    #MusicRecomender['Caracs'] = m.newMap(numelements=9, maptype='PROBING', comparefunction=compareCarac)
    MusicRecomender['Caracs'] = om.newMap(omaptype='RBT', comparefunction=compareValues)
    return MusicRecomender

def newCaracEntry(EventoEscucha):
    entry = {'CaracCont': None, 'lstEvenEscu': None}
    #entry['CaracCont'] = om.newMap(omaptype='RBT', comparefunction=compareValues)
    entry['CaracCont'] = m.newMap(numelements=7, maptype='PROBING', comparefunction=compareValues)
    entry['lstEvenEscu'] = lt.newList('ARRAY_LIST', compareValues)
    return entry


"""def newCaracContEntry(CaracContgrp, EventoEscucha):
    Caraentry = {'CaracContenido': None, 'lstCaracCont': None}
    Caraentry['CaracContenido'] = CaracContgrp
    Caraentry['lstCaracCont'] = lt.newList('ARRAY_LIST')
    return Caraentry"""

Valores=lt.newList('ARRAY_LIST')
lt.addLast(Valores,'instrumentalness')
lt.addLast(Valores,'Acousticness')
lt.addLast(Valores,'Liveness')
lt.addLast(Valores,'Speechiness')
lt.addLast(Valores,'Energy')
lt.addLast(Valores,'Danceability')
lt.addLast(Valores,'Valence')
lt.addLast(Valores,'Tempo')

# Funciones para agregar informacion al catalogo

def addEventoEscucha(MusicRecomender, EventoEscucha):
    lt.addLast(MusicRecomender['EventosEscucha'], EventoEscucha)
    updateCaracIndex(MusicRecomender['Caracs'], EventoEscucha)
    return MusicRecomender

def updateCaracIndex(map, EventoEscucha):
    value = float(EventoEscucha['instrumentalness'])
    entry = om.get(map, value)
    if entry is None:
        Caraentry = newCaracEntry(EventoEscucha)
        om.put(map, value, Caraentry)
    else:
        Caraentry = me.getValue(entry)
    addDateIndex(Caraentry, EventoEscucha)
    return map

def addDateIndex(CaracEntry, EventoEscucha):
    lst = CaracEntry['lstEvenEscu']
    lt.addLast(lst, EventoEscucha)
    """CaracIndex = CaracEntry['CaracCont']
    Carentry = m.get(CaracIndex, EventoEscucha['instrumentalness'])
    if (Carentry is None):
        entry = newCaracContEntry(EventoEscucha['instrumentalness'], EventoEscucha)
        lt.addLast(entry['lstCaracCont'], EventoEscucha)
        m.put(CaracIndex, EventoEscucha['instrumentalness'], entry)
    else:
        entry = me.getValue(Carentry)
        lt.addLast(entry['lstCaracCont'], EventoEscucha)"""
    return CaracEntry


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


def compareCarac(Carac1, Carac2):
    Caract = me.getKey(Carac2)
    if (Carac1 == Caract):
        return 0
    elif (Carac1 > Caract):
        return 1
    else:
        return -1
