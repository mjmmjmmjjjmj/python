import json
import plotly.express as px

# json load - file
# json loads - str -> dict, dict -> str

#160
mag = []
lat = []
lon = []

with open('b.geojson', 'r', encoding='utf-8') as f:
    data = json.load(f)
    # print(type(data), type(data['features']), data['features'][0])
    # print(type(data), type(data['metadata/']), data['metadata']['count'])
    # print(data['features'][0]['geometry']['coordinates'])
    for features in data ['features']:  
        # print (data['features'][0]['properties']['mag'])
        mag.append(features['properties']['mag'])
        lon.append(features['geometry']['coordinates'][0])
        lat.append(features['geometry']['coordinates'][1])
        # print (data['features'][0]['geometry']['coordinates'])

fig = px.scatter_geo(lat = lat, lon = lon, size = mag)
fig.show()