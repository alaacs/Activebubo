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


output=selectIncludedOwls(in_path)
print(output)
