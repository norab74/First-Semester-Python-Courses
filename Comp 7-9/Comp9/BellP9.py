#BellP9
#Programmer: Nora Bell
#Email: nbell8@cnm.edu
#Purpose: To demonstrate competency in class constructors

from GeoPoint import *
def main(): #main loop
    while True:
        try:
            point0 = GeoPoint(41.651031, -83.541939, "Toledo, OH") #instantiate location 1
            point1 = GeoPoint()
            point1.Point = (float(35.106766), float(-106.629181))
            point1.Description = ("Albuquerque, NM")
            point2 = GeoPoint() #instantiate personal location
            if point0.getPoint()==point1.getPoint():
                print("You cannot select the same point twice.")
                print("Please select a different second point")
                point1.setPoint()
                point1.setDescription()
            print("Your Location:")
            print("______________________________________________")
            point2.setPoint()
            point2.setDescription()
            if point2.getPoint()==point0.getPoint() or point2.getPoint()==point1.getPoint():
                print("You cannot select the same point twice.")
                print("Please select a different Personal location")
                point2.setPoint()
                point2.setDescription()

            #deltas should be in a list for ease of access and simplicity of code
            #simplicity here referring to the simplicity of access, not literal simplicity
            #as understood by application of the UNIX philosophy, simple does not necessarily imply easier or less complex
            #indexes: [     0      ,     1      ,    2   ]
            #indexes: [p0-p1        , p0-p2     , p1-p2  ]
            #         [point0v1     , point0v2  , point1v2]
            
            # make sure nothing is set to None, because despite everything saying polymorphism should save me it's killing me
            # and I never want to see the phrase "noneType is not subscriptable" again
            p0 = point0.getPoint()
            p1 = point1.getPoint()
            p2 = point2.getPoint()

            if p0 is None:
                print("Point0 is not set; please enter coordinates for Point0:")
                point0.setPoint()
                p0 = point0.getPoint()
            if p1 is None:
                print("Point1 is not set; please enter coordinates for Point1:")
                point1.setPoint()
                p1 = point1.getPoint()
            if p2 is None:
                print("Personal location is not set; please enter coordinates for your Personal location:")
                point2.setPoint()
                p2 = point2.getPoint()

            try:
                deltaLat = [p1[0] - p0[0], p0[0] - p2[0], p1[0] - p2[0]]
                deltaLon = [p1[1] - p0[1], p0[1] - p2[1], p1[1] - p2[1]]
                lat0_1_2 = [p0[0], p1[0], p2[0]]
            except Exception:
                raise ValueError("One or more points are not valid coordinate tuples (expected (lat, lon)).")

            print(f"{point0.getDescription()} is {GeoPoint.distance(deltaLat, lat0_1_2, deltaLon):.2f} KM from {point1.getDescription()}")
            if GeoPoint.personalDistance(deltaLat,lat0_1_2,deltaLon)[1] == "point1":
                print(f"At {GeoPoint.personalDistance(deltaLat,lat0_1_2,deltaLon)[0]:.2f} KM, you are closer to {point1.getDescription()}")
            else:
                print(f"At {GeoPoint.personalDistance(deltaLat,lat0_1_2,deltaLon)[0]:.2f} KM, you are closer to {point0.getDescription()}")
            if input("Would you like to do another comparison? (Y/N) ").upper().strip() == "N":
                exit()
        #except TypeError: print("Wrong Type of input!")
        except ValueError: print("""Value Error: You've probably entered an invalid Coordinate
            Latitudes must be between -90 and 90
            Longitudes must be between -180 and 180""")
        except Exception as e: print(f"""Oh No! Something Broke!
                                     Error: {e}""")
if __name__ =="__main__":
    main()