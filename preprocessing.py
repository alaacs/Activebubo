from sys import path
import os
import ogr
from math import hypot
from datetime import datetime

in_path = "D:\\Bulk\\Uni\\Muenster\\Python_for_GIS\\FinalProject\\movebank\\eagle_owl\\owlTest\\points.shp"

print(in_path)
#T  This function excludes owls that will not be considered by our core algorithm (eg: due to data incompleteness)
def selectFields(shp):
    driver = ogr.GetDriverByName("ESRI Shapefile")
    data_source = driver.Open(shp, 1)
    layer = data_source.GetLayer(0)

    print(layer)

    # features = [feat for feat in layer.getFeatures()]
    fields = layer.fields()
    print(fields)

    # Check for editing rights (capabilities)
    # caps = layer.dataProvider().capabilities()
    # print(caps)
    # caps_string = layer.dataProvider().capabilitiesString()
    # print(caps_string)
    #
    # # Now remove the fields again because we do not need them
    # # We need the field index
    # # Unfortunately backward counting (-1 and -2) does not work
    # if caps & QgsVectorDataProvider.DeleteAttributes:
    #     res = layer.dataProvider().deleteAttributes([3,4,5,6,9,11,12,16,17,18,19,22,25,26,27])
    #
    # # update to propagate the changes
    # layer.updateFields()


selectFields(in_path)
# print(output)
