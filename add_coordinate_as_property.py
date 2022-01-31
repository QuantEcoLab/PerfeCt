from geojson import FeatureCollection
import json

path = 'data/points_agua_cro_wgs.geo.json'

with open(path,'r') as data_file:
    data = json.load(data_file)

feature_collection = FeatureCollection(data['features'])

#print(feature_collection)

for feature in feature_collection["features"]:
    #print(feature["geometry"]["coordinates"])
    #print(feature["properties"])
    feature["properties"]["coordinates"] = feature["geometry"]["coordinates"]

json_string = json.dumps(feature_collection)
with open('data/points_aqua_cro_wgs_v2.geo.json', 'w') as outfile:
    outfile.write(json_string)