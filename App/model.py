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
    MusicRecomender = {'EventosEscucha': None, 'Carac': None, 'Artists':None, 'SentimentsValues':None, 'Hashtags': None}
    MusicRecomender['EventosEscucha'] = lt.newList('ARRAY_LIST', cmpfunction=compareIds)
#    MusicRecomender['SentimentsValues'] = m.newMap(numelements=5000, maptype='CHAINING', loadfactor=4.0, comparefunction=compareDates)
    MusicRecomender['Hashtags'] = m.newMap(numelements=5000, maptype='CHAINING', loadfactor=4.0, comparefunction=compareHashTag)

    return MusicRecomender

def newEventEntry():
    entry = {'lstEvent': None}
    entry['lstEvent'] = lt.newList('ARRAY_LIST', compareValues)
    return entry

def newArtistEntry(id):
    Arentry = {'ArtistId': None}
    Arentry['ArtistId'] = id
    return Arentry

def newIDEntry(id):
    IDentry = {'EventId': None}
    IDentry['EventId'] = id
    return IDentry

# Funciones para agregar informacion al catalogo

def addEventoEscucha(MusicRecomender, EventoEscucha):
    lt.addLast(MusicRecomender['EventosEscucha'], EventoEscucha)
    return MusicRecomender

def addEventosRBT(MusicRecomender,Requerimiento,tipoCaraCont,limInf,limSup):
    MusicRecomender['Artists'] = m.newMap(numelements=5000, maptype='CHAINING', loadfactor=4.0, comparefunction=compareArtist)
    #MusicRecomender['ID'] = m.newMap(numelements=5000, maptype='CHAINING', loadfactor=4.0, comparefunction=compareID)
    MusicRecomender['Caracs'] = om.newMap(omaptype='RBT', comparefunction=compareValues)
    i=1
    while i<=lt.size(MusicRecomender['EventosEscucha']):
        EventoEscucha = lt.getElement(MusicRecomender['EventosEscucha'],i)
        if Requerimiento==1:
            updateCaracIndex(MusicRecomender, EventoEscucha,tipoCaraCont,Requerimiento,limInf,limSup)
        elif Requerimiento==2:
            updateCaracIndex(MusicRecomender, EventoEscucha,tipoCaraCont,Requerimiento,limInf,limSup)
        elif Requerimiento==3:
            updateCaracIndex(MusicRecomender, EventoEscucha,tipoCaraCont,Requerimiento,limInf,limSup)
        elif Requerimiento==4:
            tipoCaraCont="tempo"
            updateCaracIndex(MusicRecomender, EventoEscucha, tipoCaraCont, Requerimiento, limInf, limSup)
        elif Requerimiento==5:
            pass
        else:
            updateCaracIndex(MusicRecomender, EventoEscucha,tipoCaraCont,Requerimiento, limInf, limSup)
        i+=1
    return MusicRecomender

def addEventosRBT2(MusicRecomender,catalog2,Requerimiento,tipoCaraCont,limInf,limSup):
    MusicRecomender['Artists'] = m.newMap(numelements=5000, maptype='CHAINING', loadfactor=4.0, comparefunction=compareArtist)
    MusicRecomender['Caracs'] = om.newMap(omaptype='RBT', comparefunction=compareValues)
    for elemento in lt.iterator(om.valueSet(catalog2['Caracs'])):
        for EventoEscucha in lt.iterator(elemento["lstEvent"]):
            updateCaracIndex(MusicRecomender, EventoEscucha,tipoCaraCont,Requerimiento,limInf,limSup)
    return MusicRecomender

def updateCaracIndex(MusicRecomender, EventoEscucha, tipoCaraCont,Requerimiento, limInfe,LimSup):
    value = float(EventoEscucha[tipoCaraCont])
    if Requerimiento==3:
        if value<=limInfe or value>=LimSup:
            return MusicRecomender['Caracs']
    else:
        if value<limInfe or value>LimSup:
            return MusicRecomender['Caracs']
    Artists=MusicRecomender['Artists']
    entry = om.get(MusicRecomender['Caracs'], value)
    if entry is None:
        EventEntry = newEventEntry()
    else:
        EventEntry = me.getValue(entry)
    addEventIndex(Artists,EventEntry, EventoEscucha)
    om.put(MusicRecomender['Caracs'], value, EventEntry)
    return MusicRecomender['Caracs']

def addEventIndex(Artists,EventEntry,EventoEscucha):
    lst=EventEntry['lstEvent']
    lt.addLast(lst, EventoEscucha)
    Arentry = m.get(Artists, EventoEscucha['artist_id'])
    if (Arentry is None):
        entry = newArtistEntry(EventoEscucha['artist_id'])
        m.put(Artists, EventoEscucha['artist_id'], entry)
    return EventEntry

def addIDUniqueEvent(MapID,EventoEscucha):
    IDentry = m.get(MapID, EventoEscucha['id'])
    if (IDentry is None):
        entry = newIDEntry(EventoEscucha['id'])
        m.put(MapID, EventoEscucha['id'], entry)

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
    totEvent = 0
    for lstEvent in lt.iterator(lst):
        totEvent += lt.size(lstEvent['lstEvent'])          
    sizeTabla= lt.size(m.keySet(analyzer['Artists']))
    return totEvent,sizeTabla,lst

def getEventosByRange2(analyzer, initialInfo, finalInfo):
    lst = om.values(analyzer['Caracs'], initialInfo, finalInfo)
    lista1 = lt.newList('ARRAY_LIST', cmpfunction=compareIds)
    for lstEvent in lt.iterator(lst):
        for evento in lt.iterator(lstEvent['lstEvent']):
            if not(lt.isPresent(lista1,evento['track_id'])>0):
                lt.addLast(lista1,evento)
    totEvent = lt.size(lista1)
    return totEvent,lista1

# Funciones de ordenamiento

#Funciones de comparacion

def compareIds(ID,Lista):
    if (ID.lower() in Lista['track_id'].lower()):
        return 0
    return -1


def compareValues(value1, value2):
    if (value1 == value2):
        return 0
    elif (value1 > value2):
        return 1
    else:
        return -1

def compareHashTag(HT1, HT2):
    HT = me.getKey(HT2)
    if (HT1 == HT):
        return 0
    elif (HT1 > HT):
        return 1
    else:
        return -1      

def compareID(ID1, ID2):
    ID = me.getKey(ID2)
    if (ID1 == ID):
        return 0
    elif (ID1 > ID):
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
