import csv
filename = "Python Fundamentals/Comp10/P10/Points.csv"
latitude = []
longitude = []
description = []
with open(filename, 'r') as csvFile:
    importedPoints = csv.DictReader(csvFile)
    fields = next(importedPoints) #Read the header Row
    for row in importedPoints:
        description.append(row['Description'])
        latitude.append(row['Latitude'])
        longitude.append(row['Longitude'])
        
print("Descriptions" , description)
print("Latitudes" , latitude)
print("longitudes" , longitude)

for i in description:
    print(description.index(i))