import folium
from folium import plugins
import csv

mammoth_colors = {'Mammuthus columbi' : 'green',
 'Mammuthus primigenius': 'blue',
 'Mammuthus hayi' : 'purple',
 'Mammuthus exilis' : 'red',
 'Mammuthus': 'orange'}

# Create map. Use terrain tiles instead of roads
mammoth_map = folium.Map(location=[40, -100], zoom_start=4, tiles='Stamen Terrain')

lat_lng = []

# Read in mammoth_data.csv. Use data to create markers, add to map
with open('mammoth_data.csv', 'r') as mammoth_csv:
    reader = csv.reader(mammoth_csv, quoting=csv.QUOTE_NONNUMERIC)
    firstline = reader.__next__() # discard title column titles
    for line in reader:
        lat = line[3]
        lon = line[4]
        lat_lng.append([lat, lon])
        marker_text = '%s found in %s, %s. %s.' % (line[0] , line[6] , line[5] , line[7])
        if line[1]:
            marker_text += ' %s %s ' % (line[1], line[2])

        color = mammoth_colors[line[0]]

        marker = folium.Marker([lat, lon], popup=marker_text, icon=folium.Icon(color=color))
        marker.add_to(mammoth_map)

mammoth_map.save('mammoth_map.html')

# Heatmap

# Need list of [lat, lng] coordinates

heatmap = folium.Map(location=[40, -100], zoom_start=4)
heatmap.add_children(plugins.HeatMap(lat_lng))
heatmap.save('mammoth_heatmap.html')


# Choropleth Map; Mammoths per state TODO

# import pandas
#
# choromap = folium.Map(location=[40, -100], zoom_start=4)
# us_states = r'us_states.json'
# #data = {'MN': 100, "AZ": 4}
#
# data = pandas.read_csv('mammoth_data.csv')  # dataframe from CSV
#
# # Need to aggregate all fossils for one state into a new dataframe
# # Add up the abund_unit value (or 1 if not present) for each state
#
# state_data_groups = data.groupby('state')
# print(state_data_groups.describe())
#
# choromap.choropleth(geo_path=us_states,
# data=data,
# columns=['state', 'quantity'],
# fill_color='BuPu', fill_opacity=0.4, line_opacity=0.4,
# legend_name="Mammoth finds per state"
# )
#
# choromap.save('mammoth_choropleth.html')
