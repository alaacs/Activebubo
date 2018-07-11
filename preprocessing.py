from sys import path
import os
import ogr

source_path = "D:\\Bulk\\Uni\\Muenster\\Python_for_GIS\\FinalProject\\movebank\\eagle_owl\\owlTest\\"
in_name = "points.shp"
out_name = "outputPoints.shp"

in_path = source_path + in_name

print(in_path)

def selectFields(shp):
    driver = ogr.GetDriverByName("ESRI Shapefile")
    data_source = driver.Open(shp, 0)
    # layer = data_source.GetLayer(0)

    out_path = source_path + out_name
    shpCopy = driver.CopyDataSource(data_source, out_path)

    new_source = driver.Open(shpCopy, 1)
    layer = shpCopy.GetLayer(0)

    feat = layer.GetFea

    dropFields = [3,4,5,6,9,11,12,16,17,18,19,22,25,26,27]

    for

    ds.ExecuteSQL("ALTER TABLE my_shp DROP COLUMN my_field")

    del shpCopy

selectFields(in_path)
# print(output)
