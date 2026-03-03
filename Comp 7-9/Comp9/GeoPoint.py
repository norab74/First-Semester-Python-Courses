#BellP9 - Supplemental
#Programmer: Nora Bell
#Email: nbell8@cnm.edu
#Purpose: To demonstrate competency in class constructors

#Imports
import math
from os import system
global deltaLat
global deltaLon
class GeoPoint:
    def __init__(self, lat= 0.0, lon= 0.0, description="TBD"): #Initialize internal variables
        self.__lat           = lat
        self.__lon           = lon
        self.__description   = description
        self._lat0_1        = []
        #Fixed format for variables to mark them private correctly.
    
            
    def setPoint(self, lat= None, lon= None): #setter funciton for logical components
        if isinstance(self, tuple):
            self.__lat = float(lat)
            self.__lon = float(lon)
        elif lat is None and lon is None:
            self.__lat           = float(input("Enter the Latitude of your place:  "))
            self.__lon           = float(input("Enter the Longitude of your place:  "))   
        self._latRad        = float(math.radians(self.__lat))  
        self._lonRad        = float(math.radians(self.__lon))  
        if abs(self.__lat) > 90 or abs(self.__lon) > 180: raise ValueError  
    

        
        
        
    def getPoint(self):
        if self.__lat is not  0.0 and self.__lon is not  0.0:
            return float(self.__lat), float(self.__lon)  
    
    def setDescription(self, description=""): #objects need a human readable name, this gives them one
        if description != "":
            self.__description = description
        else:
            self.__description = input("What is the name of this place?  ")
        #system('clear')

    def getDescription(self):
        return self.__description
    
    
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
        
        
    Point = property(getPoint, setPoint)
    Description = property(getDescription,setDescription)