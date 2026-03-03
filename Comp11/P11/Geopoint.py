#BellP10
#Programmer: Nora Bell
#Email: nbell8@cnm.edu
#Purpose: To demonstrate competency in file operations

#Additional note: For consistency in logic moving forward, I am using the file as modified by Professor Muhumure, 
#rather than the one produced by myself. Further edits to this file will be only my own.

#Imports
import math
import csv

class GeoPoint:
    #Initialize class with default values
    def __init__(self, lat=0.0, lon=0.0, description="TBD"):
        self.__lat = lat
        self.__lon = lon
        self.__description = description
    #Set point data to instance
    def setPoint(self, lat=None, lon=None):
        if isinstance(lat, tuple):
            self.__lat = float(lat[0])
            self.__lon = float(lat[1])
        elif lat is not None and lon is not None:
            self.__lat = float(lat)
            self.__lon = float(lon)
        else:
            self.__lat = float(input("Enter the Latitude of your place: "))
            self.__lon = float(input("Enter the Longitude of your place: "))

        if abs(self.__lat) > 90 or abs(self.__lon) > 180:
            raise ValueError("Invalid latitude or longitude")

        self._latRad = math.radians(self.__lat)
        self._lonRad = math.radians(self.__lon)
    #Retrieve point data of instance
    def getPoint(self):
        if self.__lat != 0.0 or self.__lon != 0.0:
            return (self.__lat, self.__lon)
    #Set instance descriptor, the name of the place.
    def setDescription(self, description=""):
        if description:
            self.__description = description
        else:
            self.__description = input("What is the name of this place? ")
    #Retrieve descriptor data of instance
    def getDescription(self):
        return self.__description
    #Establish properties for easier use in program
    Point = property(getPoint, setPoint)
    Description = property(getDescription, setDescription)
    
    
    @staticmethod
    #Calculate distance between points
    def distance(deltaLat, lat1_2, deltaLon):
        deltaLat = math.radians(deltaLat)
        deltaLon = math.radians(deltaLon)
        for val in lat1_2: math.radians(val)
        a = math.sin(deltaLat / 2) ** 2 + \
            math.cos(math.radians(lat1_2[0])) *\
                math.cos(math.radians(lat1_2[1])) *\
                    math.sin(deltaLon / 2) ** 2
                    
        radiusKM = 6371
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        return radiusKM * c
    
    @staticmethod
    
    def loadFile(filename=''):
        description = []
        latitude = []
        longitude = []
        with open(filename, 'r') as importedFile:
        #save it as a dictionary...kinda
            importedPoints = csv.DictReader(importedFile)
            for row in importedPoints: #move data into our lists for easier addressing
                description.append(row['Description'])
                latitude.append(row['Latitude'])
                longitude.append(row['Longitude'])        
    
    
def main():
    csvOfPoints = "Python Fundamentals/Comp10/P10/Points.csv"
    #Create some variables to store our list of points
    latitude = []
    longitude = []
    description = []
    #Open the csv file containing the points as read only
    with open(csvOfPoints, 'r') as csvFile:
        #save it as a dictionary...kinda
        importedPoints = csv.DictReader(csvFile)
        for row in importedPoints: #move data into our lists for easier addressing
            description.append(row['Description'])
            latitude.append(row['Latitude'])
            longitude.append(row['Longitude'])
    while True:
        try:
            #Create an empty list of points
            points=[]
            # Instantiate points
            for i in range(len(description)):
                point = GeoPoint()
                point.setPoint(float(latitude[i]), float(longitude[i]))
                point.setDescription(description[i])
                points.append(point)
            point2 = GeoPoint()
            # Set personal location
            print("Your Location:")
            print("______________________________________________")
            point2.setPoint()
            point2.setDescription()

            # Ensure points are not duplicates
            for point in points:
                if point2.getPoint() == point.getPoint():
                    print("You cannot select the same point twice.")
                    point2.setPoint()
                    point2.setDescription()
            
            #Check Distances
            distances = [] #empty list to store our distances in
            for point in points:
                deltaLat = point.getPoint()[0] - point2.getPoint()[0] #type:ignore #pylance throws an error here because point2 still doesn't have a value, it can safely be ignored
                deltaLon = point.getPoint()[1] - point2.getPoint()[1] #type:ignore
                lat1_2 = [point.getPoint()[0],point2.getPoint()[0]] #type:ignore
                distances.append(GeoPoint.distance(deltaLat,lat1_2,deltaLon))

            #Report back which location is closest
            if distances:
                idx = distances.index(min(distances))
                print(f"The closest location to you is {description[idx]}")
            else:
                print("No distances were calculated.")
            
            
            if input("Would you like to do another comparison? (Y/N) ").upper().strip() == "N":
                break

        except ValueError as ve:
            print(f"Value Error: {ve}")
        except Exception as e:
            print(f"Oh No! Something Broke! Error: {e}")


if __name__ == "__main__":
    main()
