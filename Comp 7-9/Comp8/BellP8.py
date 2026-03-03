#BellP7 - Supplemental
#Programmer: Nora Bell
#Email: nbell8@cnm.edu
#Purpose: To demonstrate competency in class definitions

from GeoPoint import *
def main(): #main loop
    while True:
        try:
            point0 = GeoPoint() #instantiate location 1
            point1 = GeoPoint() #instantiate location 2
            point2 = GeoPoint() #instantiate personal location
            print("Location 1:")
            print("______________________________________________")
            point0.setPoint()
            point0.setDescription()#call setters for first location, repeat lower

            print("Location 2:")
            print("______________________________________________")
            point1.setPoint()
            point1.setDescription()
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
            deltaLat = [point1.getPoint()[0] - point0.getPoint()[0], point0.getPoint()[0] - point2.getPoint()[0], point1.getPoint()[0] - point2.getPoint()[0]]
            deltaLon = [point1.getPoint()[1] - point0.getPoint()[1], point0.getPoint()[1] - point2.getPoint()[1], point1.getPoint()[1] - point2.getPoint()[1]]
            lat0_1_2   = [point0.getPoint()[0], point1.getPoint()[0], point2.getPoint()[0]]

            print(f"{point0.getDescription()} is {GeoPoint.distance(deltaLat, lat0_1_2, deltaLon):.2f} KM from {point1.getDescription()}")
            if GeoPoint.personalDistance(deltaLat,lat0_1_2,deltaLon)[1] == "point1":
                print(f"At {GeoPoint.personalDistance(deltaLat,lat0_1_2,deltaLon)[0]:.2f} KM, you are closer to {point1.getDescription()}")
            else:
                print(f"At {GeoPoint.personalDistance(deltaLat,lat0_1_2,deltaLon)[0]:.2f} KM, you are closer to {point0.getDescription()}")
            if input("Would you like to do another comparison? (Y/N) ").upper().strip() == "N":
                exit()
        except TypeError: print("Wrong Type of input!")
        except ValueError: print("""Value Error: You've probably entered an invalid Coordinate
            Latitudes must be between -90 and 90
            Longitudes must be between -180 and 180""")
        except Exception as e: print(f"""Oh No! Something Broke!
                                     Error: {e}""")
        finally: del(point0,point1,point2) #type:ignore
if __name__ =="__main__":
    main()