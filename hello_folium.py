import folium

# Center map on downtown minneapolis
map_mn = folium.Map(location=[44.97, -93.28], zoom_start=13)

# Add a marker for MCTC, at 44.9729,-93.2831
folium.Marker([44.9729, -93.2831], popup='MCTC').add_to(map_mn)

map_mn.save('map.html')
