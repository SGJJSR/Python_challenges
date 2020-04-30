from shapely.geometry import Point, LineString, Polygon
import numpy as np

# 1)
# Create a function called createPointGeom() that has two parameters (x_coord, y_coord). 
# Function should create a shapely Point geometry object and return that. 
# Demonstrate the usage of the function by creating Point -objects with the function.

def createPointGeom(x_coord,y_coord):
    point_1 = Point(x_coord, y_coord)
    return(point_1)

createPointGeom(12.2,4.7)

2)
# Create a function called createLineGeom() that takes a list of Shapely Point objects 
# as parameter and returns a LineString object of those input points. Function should 
# first check that the input list really contains Shapely Point(s). Demonstrate the 
# usage of the function by creating LineString -objects with the function.

def createLineGeom(list_1):          
    if all(isinstance(x, Point) for x in list_1) is True:
        return LineString(list_1)
    else:
        return 'pointList must contain shapely point object(s)'
        
point1 = Point(2.2, 4.2)

point2 = Point(7.2, -25.1)

point3 = Point(9.26, -2.456)

createLineGeom([point1, point2, point3])

createLineGeom([Point(2.2, 4.2), Point(7.2, -25.1), Point(9.26, -2.456)])


# Create a function called createPolyGeom() that takes a 
# list of coordinate tuples OR a list of Shapely Point objects and 
# creates/returns a Polygon object of the input data. Both ways of 
# passing the data to the function should be working. Demonstrate the 
# usage of the function by passing data first with coordinate-tuples 
# and then with Point -objects.

def createPolyGeom(coords):
    if all(isinstance(x, Point) for x in coords) is True:
        print("ok")
        poly = Polygon([[p.x, p.y] for p in coords])
        print(poly)
    else:    
        poly = Polygon(coords)
    return(poly)
     
