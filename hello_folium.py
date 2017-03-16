import folium


# Center map on downtown Minneapolis
map_mn = folium.Map(location=[44.97, -93.28], zoom_start=13)

# Add a marker for MCTC, at 44.9729,-93.2831
folium.Marker([44.9729, -93.2831], popup='MCTC').add_to(map_mn)

# And save
map_mn.save('map.html')


# Create a new map showing the whole US
map_us = folium.Map(location=[40, -120], zoom_start=3)

map_us.save('map_us.html')
