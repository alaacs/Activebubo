import ogr
from sys import path
from os import getcwd
path.append(getcwd())
from math import pi
from datetime import datetime
#from preprocessing import *
def calculateDistance(pnt1, pnt2):
    earth_mean_radius = 6371
    return pnt1.Distance(pnt2) * earth_mean_radius * pi/180

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
    return owlDict

#This function calculates statistics based on the group_by parameter
#group_by parameter can be "month", "day", "year"
def calculateOwlStats(owlInfo, speed_field, group_by = "month"):
    index = 0
    stats = {}
    for obs in owlInfo:
        if(index == 0):
            index += 1
            previousFeat = obs
            continue
        if(previousFeat is not None):
            if(group_by == "month"):
                currentCycle = str(obs['timestamp'].month) +"-"+ str(obs['timestamp'].year)#f"{obs['timestamp']:%m}" + "-" + f"{obs['timestamp']:%Y}"
            elif (group_by == "day"):
                currentCycle = str(obs['timestamp'].day) +"-" + str(obs['timestamp'].month) +"-"+ str(obs['timestamp'].year)
            else :#should be by year
                currentCycle = str(obs['timestamp'].year)
            distance = calculateDistance(obs['feature'].geometry(), previousFeat['feature'].geometry())
            if(currentCycle not in stats):
                stats[currentCycle] = {}
                stats[currentCycle]['observationCount'] = 0
                stats[currentCycle]['totalDistance']  = 0
                stats[currentCycle]['totalSpeed']  = 0
                stats[currentCycle]['averageSpeed'] = 0
            stats[currentCycle]['observationCount'] += 1
            stats[currentCycle]['totalDistance'] += distance
            stats[currentCycle]['totalSpeed'] += obs['feature'][speed_field]
            stats[currentCycle]['averageSpeed'] = stats[currentCycle]['totalSpeed']/stats[currentCycle]['observationCount']
        index += 1
        previousFeat = obs
    return stats

def parseOwlDataForBoxplots(owlData, property):
    #create an array of 12 element for 12 months
    resultData = [[],[],[],[],[],[],[],[],[],[],[],[]]
    for owlKey in owlData:
        owlMonths = owlData[owlKey]
        for month in owlMonths:
            #for each month add one entry for the owl distance in this month regardress of the year
            monthNumberString = month.split('-')[0].strip()
            monthIndex = int(monthNumberString) - 1
            monthData = owlMonths[month]
            resultData[monthIndex].append(monthData[property])
    return resultData
def parseOwlDataToAvgPerOwlPerMonth(owlData):
    resultData = {'months':[1,2,3,4,5,6,7,8,9,10,11,12], 'owls': []}
    for owlKey in owlData:
        owlMonths = owlData[owlKey]
        currentOwlData = {'label':owlKey, 'averageDistances': [None, None, None, None, None, None, None, None, None, None, None, None],\
            'averageSpeeds':[None, None, None, None, None, None, None, None, None, None, None, None]}
        monthsOccurances = [0,0,0,0,0,0,0,0,0,0,0,0]
        for month in owlMonths:
            monthNumberString = month.split('-')[0].strip()
            monthIndex = int(monthNumberString) - 1
            monthsOccurances[monthIndex] += 1
            monthData = owlMonths[month]
            if(currentOwlData['averageDistances'][monthIndex] is None):
                currentOwlData['averageDistances'][monthIndex] = monthData['totalDistance']/monthData['observationCount']
            else: currentOwlData['averageDistances'][monthIndex] += monthData['totalDistance']/monthData['observationCount']
            if(currentOwlData['averageSpeeds'][monthIndex] is None):
                currentOwlData['averageSpeeds'][monthIndex] = monthData['averageSpeed']
            else: currentOwlData['averageSpeeds'][monthIndex] += monthData['averageSpeed']
        for x in range(12):
            if(currentOwlData['averageDistances'][x] is not None):
                currentOwlData['averageDistances'][x] = currentOwlData['averageDistances'][x]/monthsOccurances[x]
                currentOwlData['averageSpeeds'][x] = currentOwlData['averageSpeeds'][x]/monthsOccurances[x]
        resultData['owls'].append(currentOwlData)
    return resultData

def parseOwlDataToAverageByMonth(owlData):
    resultData = {'months':None, 'averageDistances':None, 'averageSpeeds':None}
    monthsOccurances = [0,0,0,0,0,0,0,0,0,0,0,0]
    resultData['months'] = [1,2,3,4,5,6,7,8,9,10,11,12]
    resultData['averageDistances'] = [0,0,0,0,0,0,0,0,0,0,0,0]
    resultData['averageSpeeds'] = [0,0,0,0,0,0,0,0,0,0,0,0]
    for owlKey in owlData:
        owlMonths = owlData[owlKey]
        for month in owlMonths:
            monthNumberString = month.split('-')[0].strip()
            monthIndex = int(monthNumberString) - 1
            monthsOccurances[monthIndex] += 1
            monthData = owlMonths[month]
            currentAvgDist = resultData['averageDistances'][monthIndex]
            currentAvgSpeed = resultData['averageSpeeds'][monthIndex]
            resultData['averageDistances'][monthIndex] = currentAvgDist + monthData['totalDistance']/monthData['observationCount']
            resultData['averageSpeeds'][monthIndex] = currentAvgSpeed + monthData['averageSpeed']
    for x in range(12):
        resultData['averageDistances'][x] = resultData['averageDistances'][x]/monthsOccurances[x]
        resultData['averageSpeeds'][x] = resultData['averageSpeeds'][x]/monthsOccurances[x]
    return resultData

def getOwlsAggregateData(shapefile_path, timestamp_field, speed_field, owl_id_field, filters, group_by = "month"):
    driver = ogr.GetDriverByName("ESRI Shapefile")
    data_source = driver.Open(shapefile_path, 0)
    layer = data_source.GetLayer(0)
    layer.SetAttributeFilter(filters)
    #layer = preprocess(layer)
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
        stats = calculateOwlStats(owlLists[key], speed_field, group_by)
        statDict[key] = stats
        #print(stats)
    return statDict

#in_path = "D:\\Mastergeotech\\Munster\\Python\\Project\\movebank\\eagle_owl\\Eagle owl Reinhard Vohwinkel MPIO\\points.shp"
