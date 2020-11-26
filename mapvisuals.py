import streamlit as st
import ee
import geemap.eefolium as geemap
from streamlit_folium import folium_static

Map = geemap.Map()
# Map
# Add Earth Engine dataset
image = ee.ImageCollection('TUBerlin/BigEarthNet/v1')

# Set visualization parameters.
vis_params = {
  'min': 0,
  'max': 4000}

# Print the elevation of Mount Everest.
lon=13.18
lat= 52.52

lon = float(st.sidebar.text_input('longitude', 13.34))
lat = float(st.sidebar.text_input('latitude', 52.53))
xy = ee.Geometry.Point([lon, lat])
#elev = image.sample(xy, 30).first().get('elevation').getInfo()
#print('Mount Everest elevation (m):', elev)

# Add Earth Engine layers to Map
Map.addLayer(image, vis_params)
Map.addLayer(xy, {'color': 'red'}, 'random point(data)')

# Center the map based on an Earth Engine object or coordinates (longitude, latitude)
Map.centerObject(xy, 8)


Map.addLayerControl()


folium_static(Map)