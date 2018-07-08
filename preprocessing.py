from sys import path
import os
import ogr
from math import hypot
from datetime import datetime

in_path = "D:\\Bulk\\Uni\\Muenster\\Python_for_GIS\\FinalProject\\movebank\\eagle_owl\\owl\\points.shp"

#T  This function excludes owls that will not be considered by our core algorithm (eg: due to data incompleteness)
def selectIncludedOwls(shp):
    driver = ogr.GetDriverByName("ESRI Shapefile")
    data_source = driver.Open(shp, 0)
    layer = data_source.GetLayer(0)
    feature = layer.GetNextFeature()
    owls = []
    while feature:
      owls.append(feature.GetFieldAsString('ind_ident'))
      feature = layer.GetNextFeature()
    #use set to get distinct owlsList
    owlsList=(set(owls))
    # print(owlsList)
    # for owl in owlsList:
    #     print(owl)
    includedOwlsList=[]
    includedOwlsList = [e for e in owlsList if e not in ('Eagle Owl eobs 1754 / DEW A 0349', 'Eagle Owl eobs 1292 / DEW A0798', 'Eagle Owl eobs 3895 / DEW A1808', 'Eagle Owl eobs 3896 / DEW A1809', 'Eagle Owl eobs 3897 / DER PS29371', 'Eagle Owl eobs 3898 / DER PS29373', 'Eagle Owl eobs 5158 / DEW A1824')]

    for owl in includedOwlsList:
        print(owl)

    print("Owls!", owls[1])


output=selectIncludedOwls(in_path)
print(output)
