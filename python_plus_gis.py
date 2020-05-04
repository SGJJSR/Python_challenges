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

##################Problem 3####################

# One of the "classical" problems in GIS is the situation where you have a set of coordinates 
# in a file and you need to get them into a map (or into a GIS-software). Python is a really 
# handy tool to solve this problem as with Python it is basically possible to read data from 
# any kind of input datafile (such as csv-, txt-, excel-, or gpx-files (gps data) or from different databases). 
# So far, I haven't faced any kind of data or file that would be impossible to read with Python.

# Thus, let's see how we can read data from a file and create Point -objects from them that can be saved 
# e.g. as a new Shapefile (we will learn this next week). Our dataset travelTimes_2015_Helsinki.txt consist 
# of travel times between specific locations in Helsinki Region. The first four rows of our data looks like this:

#  from_id;to_id;fromid_toid;route_number;at;from_x;from_y;to_x;to_y;total_route_time;route_time;route_distance;route_total_lines
#    5861326;5785640;5861326_5785640;1;08:10;24.9704379;60.3119173;24.8560344;60.399940599999994;125.0;99.0;22917.6;2.0
#    5861326;5785641;5861326_5785641;1;08:10;24.9704379;60.3119173;24.8605682;60.4000135;123.0;102.0;23123.5;2.0
#    5861326;5785642;5861326_5785642;1;08:10;24.9704379;60.3119173;24.865102;60.4000863;125.0;103.0;23241.3;2.0

# Thus, we have many columns of data, but the few important ones are:

# Column	Description
# from_x	x-coordinate of the origin location (longitude)
# from_y	y-coordinate of the origin location (latitude)
# to_x	x-coordinate of the destination location (longitude)
# to_y	y-coordinate of the destination location (latitude)
# total_route_time	Travel time with public transportation at the route
     
import pandas as pd

helsinki_coord = pd.read_csv('C:\\Users\\stefa\\Documents\\Fortbildung privat\\Python\\helsinki.txt', sep=';')

helsinki_sub= helsinki_coord[['from_x', 'from_y', 'to_x', 'to_y']]

orig_points = []
dest_point = []

for index, rows in helsinki_sub.iterrows():
    orig_points.append([Point(rows['from_x'], rows['from_y'])])

orig_points
#output:
# [<shapely.geometry.point.Point at 0x1bfc89d74c8>,
#  <shapely.geometry.point.Point at 0x1bfc8685cc8>,
#  <shapely.geometry.point.Point at 0x1bfc5cfc788>,
#  <shapely.geometry.point.Point at 0x1bfc7cc4e08>,
#  <shapely.geometry.point.Point at 0x1bfc89d7048>,
#  <shapely.geometry.point.Point at 0x1bfc89d76c8>,
#  <shapely.geometry.point.Point at 0x1bfc7993308>,
#  <shapely.geometry.point.Point at 0x1bfc89d7208>,
#  <shapely.geometry.point.Point at 0x1bfc89d7108>,
#  <shapely.geometry.point.Point at 0x1bfc89d9a48>,
#  ....]

########### --> how can I see the actual points? Do I actually need to? (also with respect to the next exercise)#############

# Problem 4: Creating LineStrings that represent the movements (optional task for advanced students):
# This is an optional extra task for those who likes to learn even more. Write your codes into the 
# same file as in previous Problem (3).

# Create a list called lines
# Iterate over the origin and destination lists and create a Shapely LineString -object 
# between the origin and destination point
# Add that line into the lines -list.
# Find out what is the average (Euclidian) distance of all the origin-destination LineStrings 
# that we just created, and print it out.
# To make things more reusable: write creation of the LineString and calculating the average 
#     distance into dedicated functions and use them.

lines = []
def linestringing (a, b):
    for p, pp in zip(orig_points, dest_points):        
        i = (Point(p.x, pp.x))
        #print(i)
        j = (Point(p.y,pp.y))
        #print(j)
        line_help = LineString([i, j])
        lines.append(line_help)
        return(lines)
  
def avg_distance(linestring_list):
    j = 0
    for l in linestring_list:
        i = l.length
        j += i
    avg_len = j/len(linestring_list)
    return(avg_len)
