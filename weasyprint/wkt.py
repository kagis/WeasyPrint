# дефиниции тут epsg.io
# ESRI WKT

EPSG_4326 = '''GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137,298.257223563]],
            PRIMEM["Greenwich",0],UNIT["Degree",0.017453292519943295]]'''
EPSG_3857 = '''PROJCS["WGS_1984_Web_Mercator_Auxiliary_Sphere",GEOGCS["GCS_WGS_1984",
            DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],
            UNIT["Degree",0.017453292519943295]],PROJECTION["Mercator_Auxiliary_Sphere"],
            PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],
            PARAMETER["Central_Meridian",0.0],PARAMETER["Standard_Parallel_1",0.0],
            PARAMETER["Auxiliary_Sphere_Type",0.0],UNIT["Meter",1.0]]'''

options = {'4326' : EPSG_4326, '3857': EPSG_3857}

def get_wkt_from_epsg(epsg):
    return options[epsg]