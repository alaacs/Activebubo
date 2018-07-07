import ogr
from sys import path
from os import getcwd
path.append(getcwd())
from math import hypot
from datetime import datetime
#from preprocessing import *
def calculateDistance(pnt1, pnt2):
    return pnt1.Distance(pnt2)

#This function splits the layer into a dictionary for each owl and its corresponding SORTED features by timestamp
def getOwlLists(layer, owl_id_field, timestamp_field):
    owlUniqueIds = set(feat[owl_id_field] for feat in layer)
    layer.ResetReading()
    print(owlUniqueIds)
    owlDict = {}
    for id in owlUniqueIds:
        owlDict[id] = []
    for feat in layer:
        owlDict[feat[owl_id_field]].append({'feature': feat, 'timestamp':  datetime.strptime(feat[timestamp_field], '%Y-%m-%d %H:%M:%S')})
    for key in owlDict.keys():
        owlDict[key] = sorted(owlDict[key], key = lambda feat: feat['timestamp'])
    #print("owlDict")
    return owlDict

#This function calculates statistics based on the group_by parameter
#group_by parameter can be "month", "day", "year"
def calculateOwlStats(owlList, speed_field, group_by = "month"):
    index = 0
    stats = {}
    #print("obs")
    #print(owlList[0])
    for obs in owlList:
        if(index == 0):
            index += 1
            previousFeat = obs
            # print("feature")
            # print(obs['feature'])
            # print("feature timestamp")
            # print(obs['feature']['timestamp'])
            # print("feature speed")
            # print(obs['feature']['speed'])
            continue
        if(previousFeat is not None):
            #if(group_by == "month"):
            #print(obs)
            if(group_by == "month"):
                currentCycle = str(obs['timestamp'].month) +"-"+ str(obs['timestamp'].year)#f"{obs['timestamp']:%m}" + "-" + f"{obs['timestamp']:%Y}"
            elif (group_by == "day"):
                str(obs['timestamp'].day) +"-" + str(obs['timestamp'].month) +"-"+ str(obs['timestamp'].year)
            else :#should by year
                str(obs['timestamp'].year)
            distance = obs['feature'].geometry().Distance(previousFeat['feature'].geometry())
            if(currentCycle not in stats):
                stats[currentCycle] = {}
                stats[currentCycle]['observationCount'] = 0
                stats[currentCycle]['totalDistance']  = 0
                stats[currentCycle]['totalSpeed']  = 0
            stats[currentCycle]['observationCount'] += 1
            stats[currentCycle]['totalDistance'] += distance
            stats[currentCycle]['totalSpeed'] += obs['feature'][speed_field]
        index += 1
        previousFeat = obs
    return stats

def getOwlsAggregateData(shapefile_path, timestamp_field, speed_field, owl_id_field, filters, group_by = "month"):
    driver = ogr.GetDriverByName("ESRI Shapefile")
    data_source = driver.Open(in_path, 0)
    layer = data_source.GetLayer(0)
    layer.SetAttributeFilter(filters)
    attributes = layer.GetLayerDefn()
    timestamp_field_found = False
    speed_field_found = False
    #Check if fields exist in the shapefile
    for i in range(attributes.GetFieldCount()):
        current_field = attributes.GetFieldDefn(i).GetName()
        if(current_field == timestamp_field): timestamp_field_found = True
        if(current_field == speed_field): speed_field_found = True
    if(not timestamp_field_found or not speed_field_found):
        raise ValueError("One or more of the field(%s,%s) don't exist in the shapefile"%(timestamp_field, speed_field))
    owlLists = getOwlLists(layer,owl_id_field, timestamp_field)
    statDict = {}
    for key in owlLists:
        stats = calculateOwlStats(owlLists[key], speed_field)
        statDict[key] = stats
        #print(stats)
    return statDict

in_path = "D:\\Mastergeotech\\Munster\\Python\\Project\\movebank\\eagle_owl\\Eagle owl Reinhard Vohwinkel MPIO\\points.shp"
stats = getOwlsAggregateData(in_path, "timestamp", "speed", "tag_ident", "tag_ident in ('1750', '1751', '1753', '1754', '3899', '4045', '5158', '4846', '4848')" )
print(stats)
