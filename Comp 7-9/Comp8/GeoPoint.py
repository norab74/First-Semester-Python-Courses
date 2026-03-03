#BellP7 - Supplemental
#Programmer: Nora Bell
#Email: nbell8@cnm.edu
#Purpose: To demonstrate competency in class definitions

#Imports
import math
from os import system
global deltaLat
global deltaLon
class GeoPoint:
    def __init__(self): #Initialize internal variables
        self.lat           = 0
        self.lon           = 0
        self._description   = ''
        self._lat0_1        = []
        
    def setPoint(self): #setter funciton for logical components
        self.lat           = float(input("Enter the Latitude of your place:  "))
        self.lon           = float(input("Enter the Longitude of your place:  "))
        self._latRad        = math.radians(self.lat)
        self._lonRad        = math.radians(self.lon)
        if abs(self.lat) > 90 or abs(self.lon) > 180: raise ValueError
    def getPoint(self):
        return self.lat, self.lon
    
    def setDescription(self): #objects need a human readable name, this gives them one
        self._description = input("What is the name of this place?  ")
        system('clear')

    def getDescription(self):
        return self._description
    
    
    @staticmethod #making this static so I can call it uninstantiated later,
    #as this funciton will interact with instances from outside.
    def distance(deltaLat, lat0_1_2, deltaLon):
        
      #Apply the Haversine formula
      
        a = math.sin(deltaLat[0] / 2)**2 + math.cos(lat0_1_2[0]) * math.cos(lat0_1_2[1]) * math.sin(deltaLon[0] / 2)**2
        radiusKM = 6371
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        
        return radiusKM*c   
    
    @staticmethod #same with this disgusting attempt at extending the above code, is there a better way to do this?
    #I'm not used to such clunky solutions, I'd prefer something more elegant. Further study needed...
    def personalDistance(deltaLat, lat0_1_2, deltaLon):
        a = math.sin(deltaLat[1] / 2)**2 + math.cos(lat0_1_2[0]) * math.cos(lat0_1_2[2]) * math.sin(deltaLon[1] / 2)**2
        radiusKM = 6371
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        
        a1 = math.sin(deltaLat[1] / 2)**2 + math.cos(lat0_1_2[0]) * math.cos(lat0_1_2[2]) * math.sin(deltaLon[1] / 2)**2
        c1 = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        
        distPersVPoint0 =  radiusKM*c   
        distPersVPoint1 = radiusKM*c1
        #Compare the results from above, report back. I guess technically all the
        # logic could be handled here but I feel like it makes more sense to handle 
        # some of it on the other side contextually.
        if distPersVPoint0 > distPersVPoint1:
            closer = "point1"
            return distPersVPoint1, closer
        else:
            closer = "point0"
            return distPersVPoint0, closer
        
        