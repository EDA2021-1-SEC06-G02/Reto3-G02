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
from DISClib.Algorithms.Sorting import mergesort as Merge
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos

# Funciones para creacion de datos

def newMusicRecomender():
    MusicRecomender = {'EventosEscucha': None, 'Carac': None, 'Artists':None, 'Pistas':None, 'TempoGeneros':None, 'TempoGeneros2':None, 'SentimentsValues':None, 'Hashtags': None}
    MusicRecomender['Artists'] = m.newMap(numelements=5000, maptype='CHAINING', loadfactor=4.0, comparefunction=compareArtist)
    MusicRecomender['EventosEscucha'] = lt.newList('ARRAY_LIST', cmpfunction=compareIds)
    MusicRecomender['Pistas'] = m.newMap(numelements=32000, maptype='CHAINING', loadfactor=4.0, comparefunction=compareHashTag)
    MusicRecomender['Hashtags'] = om.newMap(omaptype='RBT', comparefunction=compareDates)
    MusicRecomender['SentimentsValues'] = m.newMap(numelements=5000, maptype='CHAINING', loadfactor=4.0, comparefunction=compareHashTag)

    return MusicRecomender

def newEventEntry():
    entry = {'lstEvent': None}
    entry['lstEvent'] = lt.newList('ARRAY_LIST', compareValues)
    return entry

def newHashtagEntry():
    entry = {'TracksID':None}
    entry['TracksID'] = m.newMap(numelements=2, maptype='PROBING', loadfactor=0.5, comparefunction=compareID)
    return entry

def newArtistEntry(id):
    Arentry = {'ArtistId': None}
    Arentry['ArtistId'] = id
    return Arentry

def newIDEntry(id):
    IDentry = {'LstEvent':None}
    IDentry['LstEvent'] = lt.newList('ARRAY_LIST')
    return IDentry

# Funciones para agregar informacion al catalogo

def addEventoEscucha(MusicRecomender, EventoEscucha):
    lt.addLast(MusicRecomender['EventosEscucha'], EventoEscucha)
    m.put(MusicRecomender['Pistas'],EventoEscucha['track_id'],EventoEscucha)
    return MusicRecomender

def addEventoEscucha2(MusicRecomender, HashtagsEventos):
    DateKey=CreateDate(HashtagsEventos['created_at'])
    entry = om.get(MusicRecomender['Hashtags'], DateKey)
    if entry is None:
        HashEntry = newHashtagEntry()
    else:
        HashEntry = me.getValue(entry)
    addHashtagInfo(HashEntry, HashtagsEventos)
    om.put(MusicRecomender['Hashtags'], DateKey, HashEntry)
    return MusicRecomender

def addEventoEscucha3(MusicRecomender, SentimentsData):
    Hashtag = SentimentsData['hashtag']
    existHashTag = m.contains(MusicRecomender['SentimentsValues'], Hashtag)
    if existHashTag:
        entry = m.get(MusicRecomender['SentimentsValues'], Hashtag)
        Hash = me.getValue(entry)
    else:
        Hash = newSentimentsValues(Hashtag)
        m.put(MusicRecomender['SentimentsValues'], Hashtag, Hash)
    lt.addLast(Hash['ValuesHastags'], SentimentsData)
    return MusicRecomender

def addArtist(MusicRecomender, Entry):
    artist = Entry['artist_id']
    m.put(MusicRecomender['Artists'],artist,Entry)

def newSentimentsValues(name):
    Values = {"ValuesHastags": None}
    Values['ValuesHastags'] = lt.newList('ARRAY_LIST')
    return Values


def addHashtagInfo(HashEntry, HashtagsEventos):
    Trackentry = m.get(HashEntry['TracksID'], HashtagsEventos['track_id'])
    if (Trackentry is None):
        entry = newTrackInfoEntry(HashtagsEventos)
    else:
        entry = me.getValue(Trackentry)
        lt.addLast(entry['lstHashtags'],HashtagsEventos['hashtag'])
    m.put(HashEntry['TracksID'], HashtagsEventos['track_id'], entry)
    return Trackentry

def newTrackInfoEntry(HashtagsEventos):
    TrackInfoEntry = {'lstHashtags':None}
    TrackInfoEntry['lstHashtags'] = lt.newList('ARRAY_LIST')
    lt.addLast(TrackInfoEntry['lstHashtags'],HashtagsEventos['hashtag'])
    return TrackInfoEntry

def CrearTablaTempos(MusicRecomender):
    i = 0
    while i < 2:
        if i == 0:
            llave = 'TempoGeneros'
        else:
            llave = 'TempoGeneros2'
        MusicRecomender[llave]= m.newMap(numelements=9, maptype='CHAINING', loadfactor=4.0, comparefunction=compareGenero)
        tempo_lst = lt.newList('ARRAY_LIST')
        lt.addLast(tempo_lst,60)
        lt.addLast(tempo_lst,90)
        m.put(MusicRecomender[llave],"reggae",tempo_lst)
        tempo_lst = lt.newList('ARRAY_LIST')
        lt.addLast(tempo_lst,70)
        lt.addLast(tempo_lst,100)
        m.put(MusicRecomender[llave],"down-tempo",tempo_lst)
        tempo_lst = lt.newList('ARRAY_LIST')
        lt.addLast(tempo_lst,90)
        lt.addLast(tempo_lst,120)
        m.put(MusicRecomender[llave],"chill-out",tempo_lst)
        tempo_lst = lt.newList('ARRAY_LIST')
        lt.addLast(tempo_lst,85)
        lt.addLast(tempo_lst,115)
        m.put(MusicRecomender[llave],"hip-hop",tempo_lst)
        tempo_lst = lt.newList('ARRAY_LIST')
        lt.addLast(tempo_lst,120)
        lt.addLast(tempo_lst,125)
        m.put(MusicRecomender[llave],"jazz and funk",tempo_lst)
        tempo_lst = lt.newList('ARRAY_LIST')
        lt.addLast(tempo_lst,100)
        lt.addLast(tempo_lst,130)
        m.put(MusicRecomender[llave],"pop",tempo_lst)
        tempo_lst = lt.newList('ARRAY_LIST')
        lt.addLast(tempo_lst,60)
        lt.addLast(tempo_lst,80)
        m.put(MusicRecomender[llave],"r&b",tempo_lst)
        tempo_lst = lt.newList('ARRAY_LIST')
        lt.addLast(tempo_lst,110)
        lt.addLast(tempo_lst,140)
        m.put(MusicRecomender[llave],"rock",tempo_lst)
        tempo_lst = lt.newList('ARRAY_LIST')
        lt.addLast(tempo_lst,100)
        lt.addLast(tempo_lst,160)
        m.put(MusicRecomender[llave],"metal",tempo_lst)
        i += 1

def addEventosRBT(MusicRecomender,Requerimiento,tipoCaraCont,limInf,limSup):
    MusicRecomender['Artists'] = m.newMap(numelements=5000, maptype='CHAINING', loadfactor=4.0, comparefunction=compareArtist)
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
            updateCaracIndex(MusicRecomender, EventoEscucha, tipoCaraCont, Requerimiento, limInf, limSup)
        elif Requerimiento==5:
            tipoCaraCont="Date"
            updateCaracIndex(MusicRecomender, EventoEscucha, tipoCaraCont, Requerimiento, limInf, limSup)
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

def addNuevoGenero(catalog,nombre,Min,Max):
    nombre = nombre.lower()
    tempo_lst = lt.newList('ARRAY_LIST')
    lt.addLast(tempo_lst,Min)
    lt.addLast(tempo_lst,Max)
    m.put(catalog["TempoGeneros"],nombre,tempo_lst)

def updateCaracIndex(MusicRecomender, EventoEscucha, tipoCaraCont,Requerimiento, limInfe,LimSup):
    if Requerimiento==3:
        value = float(EventoEscucha[tipoCaraCont])
        if value<=limInfe or value>=LimSup:
            return MusicRecomender['Caracs']
    if Requerimiento==5:
        value = CreateDate(EventoEscucha['created_at'])
        limInfe = ConvertLimits(limInfe)
        LimSup = ConvertLimits(LimSup)
        if value<limInfe or value>LimSup:
            return MusicRecomender['Caracs']
    else:
        value = float(EventoEscucha[tipoCaraCont])
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
    IDentry = m.get(MapID, EventoEscucha['track_id'])
    if (IDentry is None):
        entry = newIDEntry(EventoEscucha['track_id'])
    else:
        entry=me.getValue(IDentry)
    lt.addLast(entry['LstEvent'],EventoEscucha)
    m.put(MapID, EventoEscucha['track_id'], entry)

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

def getEventosByRange(analyzer, initialInfo, finalInfo,Requerimiento,RequerimientoTrue):
    if Requerimiento==5:
        initialInfo = ConvertLimits(initialInfo)
        finalInfo = ConvertLimits(finalInfo)
    Eventos_unicos = m.newMap(numelements=5000, maptype='CHAINING', loadfactor=4.0, comparefunction=compareHashTag)
    lst = om.values(analyzer['Caracs'], initialInfo, finalInfo)
    totEvent = 0
    for lstEvent in lt.iterator(lst):
        for Event in lt.iterator(lstEvent['lstEvent']):
            llave = Event["track_id"].strip() + "," + Event["user_id"].strip() + "," + Event["created_at"].strip()
            m.put(Eventos_unicos,llave,Event)
    lst = m.keySet(Eventos_unicos)
    totEvent = lt.size(lst)
    sizeTabla= lt.size(m.keySet(analyzer['Artists']))
    if Requerimiento != 1 and not(RequerimientoTrue==5):
        lst = m.keySet(analyzer['Artists'])
        return totEvent,sizeTabla,lst
    if RequerimientoTrue==5:
        lst = Eventos_unicos
    return totEvent,sizeTabla,lst
 
def getEventosByRange2(analyzer, initialInfo, finalInfo):
    Mapa = m.newMap(numelements=5000, maptype='CHAINING', loadfactor=4.0, comparefunction=compareArtist)
    lst = om.values(analyzer['Caracs'], initialInfo, finalInfo)
    lista1 = lt.newList('ARRAY_LIST', cmpfunction=compareIds)
    for lstEvent in lt.iterator(lst):
        for evento in lt.iterator(lstEvent['lstEvent']):
            m.put(Mapa,evento['track_id'],evento)
    lista1 = m.valueSet(Mapa)
    totEvent = lt.size(lista1)
    return totEvent,lista1

def getDatosGenero(analyzer, genero):
    generos = analyzer["TempoGeneros"]
    tempo_genero = m.get(generos,genero)
    if (tempo_genero is None):
        return None
    return me.getValue(tempo_genero)

def getGeneros(analyzer):
    generos = m.keySet(analyzer["TempoGeneros2"])
    return generos

def getPistas(analyzer):
    pistas = m.keySet(analyzer["Pistas"])
    return pistas

def Requerimiento5(catalog,Requerimiento):
    pass

def CreateDate(data):
    horas=data.split()[1].split(":")
    horaSeg=(int(horas[0]))*3600
    minSeg=(int(horas[1]))*60
    horaFin=horaSeg+minSeg+(int(horas[2]))
    return horaFin

def ConvertLimits(lim):
    horas=lim.split(":")
    horaSeg=(int(horas[0]))*3600
    minSeg=(int(horas[1]))*60
    horaFin=horaSeg+minSeg+(int(horas[2]))
    return horaFin

def Requerimiento5_2(lista,Catalog):
    TracksUnique = lt.newList('ARRAY_LIST',cmpfunction=compareIds2)
    i = 1
    while i < lt.size(lista):
        obj = lt.getElement(lista,i)
        track = obj.split(",")[0]
        if not(lt.isPresent(TracksUnique,track)>0):
            lt.addLast(TracksUnique,track)
        i+=1
    return TracksUnique

def cosas(RequerimientoTrue,Event):
    if RequerimientoTrue==5:
        TracksUnique = m.newMap(numelements=5000, maptype='CHAINING', loadfactor=4.0, comparefunction=compareID)
    if RequerimientoTrue==5:
                addIDUniqueEvent(TracksUnique,Event)
    pass

# Funciones de ordenamiento

def OrdenarGeneros(ordenes):
    ordenes=OrdenSimple(ordenes)
    return ordenes

def OrdenSimple(listaOrdenada):
    sub_list = lt.subList(listaOrdenada, 0, lt.size(listaOrdenada))
    sub_list = sub_list.copy()
    sorted_list = sa.sort(sub_list, cmpNums)
    return sorted_list

#Funciones de comparacion

def cmpNums(num1, num2):
    return (num1[1] > num2[1])

def compareIds(ID,Lista):
    if (ID.lower() in Lista['track_id'].lower()):
        return 0
    return -1

def compareIds2(ID,Lista):
    if (ID in Lista):
        return 0
    return -1

"""def compareHashTags(Hash,Lista):
    if (Hash.lower() in Lista.lower()):
        return 0
    return -1"""

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

def compareDates(Date1, Date2):
    if (Date1 == Date2):
        return 0
    elif (Date1 > Date2):
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

def compareGenero(Genero1, Genero2):
    Genero = me.getKey(Genero2)
    if (Genero1 == Genero):
        return 0
    elif (Genero1 > Genero):
        return 1
    else:
        return -1
