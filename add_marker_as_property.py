from geojson import FeatureCollection
import json

path = 'data/MED_farms.geojson'

with open(path,'r') as data_file:
    data = json.load(data_file)

feature_collection = FeatureCollection(data['features'])

#print(feature_collection)

for feature in feature_collection["features"]:
    #print(feature["geometry"]["coordinates"])
    #print(feature["properties"])
    feature["properties"]["marker-image"] = "https://icons555.com/images/icons-blue/image_icon_fish_8_pic_512x512.png"

json_string = json.dumps(feature_collection)
with open('data/MED_farms_for_display_markers.geojson', 'w') as outfile:
    outfile.write(json_string)