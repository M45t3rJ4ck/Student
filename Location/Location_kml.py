import json
import datetime

json_file = open('LocationHistory.json')
json_string = json_file.read()
json_data = json.loads(json_string)

data = json_data["data"]
items = data["items"]


def time_format(timestampMs):
    date_object = datetime.datetime.fromtimestamp(timestampMs / 1000)
    other_format = date_object.strftime("%Y-%m-%dT%H:%M:%SZ")
    return other_format


print("A programme to convert JSON into KLM >>>>>")
print("")
print("Input file: LocationHistory.json")
print("")

file = open('location.kml', 'w')
file.write("<?xml version='1.0' encoding='UTF-8'?> \n")
file.write("<kml xmins='http://www.opengis.net/kml/2.2'> \n")
file.write("<Document> \n")
file.write("<name>Location History</name> \n")

for item in items:
    file.write("<Placemark> \n")
    file.write("<TimeStamp><when>" + time_format(int(item["timestampMs"])) + "</when></TimeStamp> \n")
    file.write("<ExtendedData> \n")
    file.write("<Data name='accuracy'> \n")
    file.write("<value>" + str(item["accuracy"]) + "</value> \n")
    file.write("</Data> \n")
    file.write("</ExtendedData> \n")
    file.write("<Point><coordinates>" + str(item["longitude"]) + "," + str(item["latitude"]) + "</coordinates></Point> \n")
    file.write("</Placemark> \n")

file.write("</Document> \n")
file.write("</kml>")

file.close()

print("Output file: location.kml")
