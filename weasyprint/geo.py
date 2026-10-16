"""Coordinate reference systems supported by GeoPDF viewports.

WKT definitions come from https://epsg.io (ESRI flavour, as in the examples
of the Adobe Supplement to ISO 32000, ExtensionLevel 3, section 8.8.1).

"""

from math import atan, degrees, exp, pi

WEB_MERCATOR_RADIUS = 6378137


def web_mercator_to_geographic(x, y):
    """Convert EPSG:3857 metres to EPSG:4326 (longitude, latitude) degrees."""
    longitude = degrees(x / WEB_MERCATOR_RADIUS)
    latitude = degrees(2 * atan(exp(y / WEB_MERCATOR_RADIUS)) - pi / 2)
    return longitude, latitude


EPSG_4326 = (
    'GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",'
    'SPHEROID["WGS_1984",6378137,298.257223563]],'
    'PRIMEM["Greenwich",0],UNIT["Degree",0.017453292519943295]]')
EPSG_3857 = (
    'PROJCS["WGS_1984_Web_Mercator_Auxiliary_Sphere",GEOGCS["GCS_WGS_1984",'
    'DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],'
    'PRIMEM["Greenwich",0.0],UNIT["Degree",0.017453292519943295]],'
    'PROJECTION["Mercator_Auxiliary_Sphere"],'
    'PARAMETER["False_Easting",0.0],PARAMETER["False_Northing",0.0],'
    'PARAMETER["Central_Meridian",0.0],PARAMETER["Standard_Parallel_1",0.0],'
    'PARAMETER["Auxiliary_Sphere_Type",0.0],UNIT["Meter",1.0]]')

#: Supported EPSG codes, mapped to ``(type, wkt, to_geographic)`` tuples where
#: ``type`` is the PDF coordinate system dictionary type (``GEOGCS`` or
#: ``PROJCS``), ``wkt`` is the Well Known Text definition, and
#: ``to_geographic`` converts coordinates of this system to (longitude,
#: latitude) degrees.
COORDINATE_SYSTEMS = {
    4326: ('GEOGCS', EPSG_4326, lambda x, y: (x, y)),
    3857: ('PROJCS', EPSG_3857, web_mercator_to_geographic),
}
