##################### Exercise 2 ##########################

# https://github.com/AutoGIS-2017/Exercise-2 #

############### Problem 1: Create Polygon from lists of coordinates ############# *********SOLVED***************

# In the first problem you should:

# create a Polygon out of the the x and y coordinates that are provided in the create_polygon.py -script.
# script: 
# https://github.com/AutoGIS-2017/Exercise-2/blob/master/create_polygon.py
# insert the polygon into a GeoDataFrame
# save the Polygon into a Shapefile.
# plot and save a figure out of the Polygon.
# The create_polygon.py starter script has all necessary steps listed and also some hints are provided. There are all 
# together 6 steps that you need to fill to accomplish the problem 1. 
# starter script:
# https://github.com/AutoGIS-2017/Exercise-2/blob/master/create_polygon.py
# Each step that you need to fill is marked with capital P -letter (P1 to P6).

import os
#os.chdir("C:\\.\\Exercise_2")

import geopandas as gpd
import shapely
from shapely.geometry import Polygon, Point, LineString

# X -coordinates 
xcoords = [29.99671173095703, 31.58196258544922, 27.738052368164062, 26.50013542175293, 26.652359008789062, 25.921663284301758, 2.90027618408203, 23.257217407226562,
           23.335693359375, 22.87444305419922, 23.08465003967285, 22.565473556518555, 21.452774047851562, 21.66388702392578, 21.065969467163086, 21.67659568786621,
           21.496871948242188, 22.339998245239258, 22.288192749023438, 24.539581298828125, 25.444232940673828, 25.303749084472656, 24.669166564941406, 24.689163208007812,
           24.174999237060547, 23.68471908569336, 24.000761032104492, 23.57332992553711, 23.76513671875, 23.430830001831055, 23.6597900390625, 20.580928802490234, 21.320831298828125,
           22.398330688476562, 23.97638702392578, 24.934917449951172, 25.7611083984375, 25.95930290222168, 26.476804733276367, 27.91069221496582, 29.1027774810791, 29.29846954345703,
           28.4355525970459, 28.817358016967773, 28.459857940673828, 30.028610229492188, 29.075136184692383, 30.13492774963379, 29.818885803222656, 29.640830993652344, 30.57735824584961,
           29.99671173095703]

# Y -coordinates
ycoords = [63.748023986816406, 62.90789794921875, 60.511383056640625, 60.44499588012695, 60.646385192871094, 60.243743896484375, 59.806800842285156, 59.91944122314453,
           60.02395248413086, 60.14555358886719, 60.3452033996582, 60.211936950683594, 60.56249237060547, 61.54027557373047, 62.59798049926758, 63.02013397216797,
           63.20353698730469, 63.27652359008789, 63.525691986083984, 64.79915618896484, 64.9533920288086, 65.51513671875, 65.65470886230469, 65.89610290527344, 65.79151916503906,
           66.26332092285156, 66.80228424072266, 67.1570053100586, 67.4168701171875, 67.47978210449219, 67.94589233398438, 69.060302734375, 69.32611083984375, 68.71110534667969,
           68.83248901367188, 68.580810546875, 68.98916625976562, 69.68568420410156, 69.9363784790039, 70.08860778808594, 69.70597076416016, 69.48533630371094, 68.90263366699219,
           68.84700012207031, 68.53485107421875, 67.69471740722656, 66.90360260009766, 65.70887756347656, 65.6533203125, 64.92096710205078, 64.22373962402344, 63.748023986816406]

# # P1. Create a list of x and y coordinate pairs out of xcoords and ycoords
# # ------------------------------------------------------------------------
# # Coordinate pair can be either a tuple or a list.
# # The first coordinate pair in the 'coordpairs' -list should look like: (29.99671173095703, 63.748023986816406)
# # Hint: you might want to iterate over items in the lists using a for-loop

coordpairs = [(x,y) for x,y in zip(xcoords,ycoords)]

# # P2. Create a shapely Polygon using the 'coordpairs' -list
# # ------------------------------------------------------------------------
poly = Polygon(coordpairs)

# # P3. Create an empty GeoDataFrame
# # ---------------------------------
geo = gpd.GeoDataFrame()

# # P4. Insert our 'poly' -polygon into the 'geo' GeoDataFrame using a column name 'geometry' 
# # ------------------------------------------------------------------------------------------
# # Hint: Take advantage of .loc -funtion
geo.loc[0, 'geometry'] = poly

# # P5. Save the GeoDataFrame into a new Shapefile called 'polygon.shp'
# # --------------------------------------------------------------------
# # Note: you do not need to define the coordinate reference system at this time
outfp = r"./outputs/results.Exercise_2_Problem_1.shp"

# Write the data into that Shapefile
geo.to_file(outfp)


# # P6. Plot the polygon using taking advantage of the .plot() -function in GeoDataFrame. Save a PNG figure out of your plot and upload it to your GitHub repository.
# # -----------------------------------------------------------------------------------------------------------------------------------------------------------------
geo.plot(facecolor='blue');

import matplotlib.pyplot as plt
# Add title
plt.title("Finland");
plt.savefig("Finland.png")
# Remove empty white space around the plot
#plt.tight_layout()

coordpairs[0]
poly

################## Problem 2: Points to map ####################### ***************SOLVED******************
# The problem 2 this week continues the process that we started last week, i.e. creating geometric point -objects 
# and putting them into a map. Here our aim is to plot a set of x and y coordinates that we should read 
# from a some_posts.csv comma separated file that contains following kind of data:

# lat,lon,timestamp,userid
# -24.980792492,31.484633302,2015-07-07 03:02,66487960
# -25.499224667,31.508905612,2015-07-07 03:18,65281761
# -24.342578456,30.930866066,2015-03-07 03:38,90916112
# -24.85461393,31.519718439,2015-10-07 05:04,37959089
# The data has 81379 rows and consists of locations and times of social media posts inside Kruger national park in South Africa:

# Column	Description
# lat	y-coordinate of the post
# lon	x-coordinate of the post
# timestamp	Time when the post was uploaded
# userid	userid
# Note: although the data is based on real social media data, it is heavily anonymized. Userids and timestamps have been randomized, i.e. they do not not match with real ones, also spatial accuracy of the data have been lowered.

# Download the data (Click on the link ==> CNTRL + S)
# data:
# https://raw.githubusercontent.com/AutoGIS-2017/Exercise-2/master/data/some_posts.csv?token=AGWdzhgsQbNFI3lk6a5GxrjguPnmuhwoks5YKVWrwA%3D%3D

# Read the data into memory using Pandas
import pandas as pd
import numpy as np
kruger_park = pd.read_csv('data/some_posts.txt', sep=',')

# Create an empty column called geometry where you will store shapely Point objects
kruger_park['geometry'] = None

# Iterate over the rows of the DataFrame and insert Point objects into column geometry (you need to use .loc indexer to update the row, see materials
from shapely.geometry import Polygon, Point, LineString

# x = lon, y = lat
# This is WAY too slow. 
#for index, rows in kruger_park.iterrows():
#    kruger_park.loc[index, 'geometry'] = Point((kruger_park.loc[index, 'lon']), (kruger_park.loc[index, 'lat']))

# this is a faster way of doing it. Not sure if it's needed. I'll review that later.
kruger_park['geometry'] = [Point(x, y) for x,y in kruger_park[['lat', 'lon']].values]
kruger_park

# Convert that DataFrame into a GeoDataFrame, see hints
import fiona
import geopandas as gpd
from fiona.crs import from_epsg


# Update the CRS for coordinate system as WGS84 (i.e. epsg code: 4326)

kruger_park = gpd.GeoDataFrame(kruger_park, geometry='geometry', crs=from_epsg(4326))

# Save the data into a Shapefile called Kruger_posts.shp
outfp = r"Kruger_posts.shp"
kruger_park.to_file(outfp)

# ****************loading data again:
kruger_park = gpd.read_file("Kruger_posts.shp")

# Create a simple map of those points using a GIS software or using .plot() -funtion in Python. Save it to GitHub as png file.
kruger_park.plot(facecolor='blue')

plt.title("Social_media_in_Kruger_park")
#Remove empty white space around the plot
#plt.tight_layout()
plt.savefig("Kruger_park.png")

################ Problem 3: How long distance individuals have travelled? 
# In this problem the aim is to calculate the distance in meters that the individuals have travelled 
# according the social media posts (Euclidian distances between points).

# Write your codes into the same file as in previous Problem (2).

# In your code you should:

# Reproject the data from WGS84 projection into EPSG:32735 -projection which stands for UTM Zone 35S 
#     (UTM zone for South Africa) to transform the data into metric system.
kruger_park_meters = gpd.GeoDataFrame(kruger_park, geometry='geometry', crs=from_epsg(32735))

# Group the data by userid 
userid = kruger_park_meters.groupby(['userid'])

# Create an empty GeoDataFrame called movements
movements= gpd.GeoDataFrame()


# For each user:  ############ ????????????????????
# sort the rows by timestamp
# hyperlink @sort: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.sort_values.html

# I know I could sort the dataframe by user and timestamp at the same time, like this:
km = kruger_park_meters
by_user_and_time = km.sort_values(by=['userid', 'timestamp'])
groups = by_user_and_time.groupby('userid', sort=True)

# create LineString objects based on the points
def calculate_distance(rows):
    if len(rows.geometry)>1:
        return LineString(list(rows.geometry)).length
    else:
        return 0

distance_travelled = groups.apply(calculate_distance)

print(distance_travelled)



# add the geometry and the userid into the GeoDataFrame you created in the last step
# hyperlink @add: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.append.html

# I merged the grouped and distance_travelled information together

# recasting groups to be a (geopandas) dataframe
groups = groups.apply(lambda x: x)

# converting distance_travelled to a pandas dataframe
distance_df = distance_travelled.to_frame()

# set up dataframe distance_df
#name column
distance_df.columns = ['distance']
#reet index, so that userid is an independent column
distance_df.reset_index(level=0, inplace=True)

# convert do Geopandas Dataframe
distance_df= gpd.GeoDataFrame(distance_df)

print(distance_df)

# merge grouped and distance_df into a dataframe called movements

movements = distance_df.merge(groups, how='inner', on='userid')


# Determine the CRS of the movements GeoDataFrame to EPSG:32735 (epsg code: 32735)
movements.crs = "EPSG:32735"

# Calculate the lenghts of the lines into a new column called distance in movements GeoDataFrame.

# already done

# Save the movements of into a Shapefile called Some_movements.shp
outfp = r"C:\\Users\\stefa\\Documents\\Fortbildung privat\\Python\\GIS\\Data\\some_movements.shp"
movements.to_file(outfp)

# Questions
# Write your answers below the questions. You should also print in your code the answers to the questions.

# What was the shortest distance travelled in meters?
l = []
for index, rows in distance_df.iterrows():
    #print(rows)
    if rows['distance'] > 0:
        l.append(rows)
        #print(l)
existing_distance = pd.DataFrame(l)

# alternatively: iterrows over movements

print("The smallest distance that is not zero is {0:.9f} meters, covered by the userid {1}"\
      .format(existing_distance.loc[existing_distance['distance'].idxmin(), 'distance'],\
              existing_distance.loc[existing_distance['distance'].idxmin(), 'userid']))

# What was the mean distance travelled in meters?
# no-distance users included:
print("The average distance of all users is {0:.2f} meters".format(movements['distance'].mean()))
# excluding no-distance users:
print("The average distance of all users with distance > 0 is {0:.2f} meters".format(existing_distance['distance'].mean()))

# the outputs here make no sense, since the mean of the user excluding the no-distance users is actually
# lower than the overall mean. I do not know what went wrong, I have tested the code with simpler tables
# and it works as expected there

# What was the maximum distance travelled in meters?
print("The largest distance is {0:.2f} meters, covered by the userid {1}"\
      .format(movements.loc[movements['distance'].idxmax(), 'distance'],\
              movements.loc[movements['distance'].idxmax(), 'userid']))
