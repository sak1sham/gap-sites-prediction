import streamlit as st
from streamlit_folium import folium_static
import folium

st.title('Gap Sites prediction')

lat = st.number_input(label="Latitude", value = 28.6937, step=0.00001, format="%.7f")
long= st.number_input(label="Longitude", value = 77.1178, step=0.00001, format="%.7f")

location = [lat, long]

m = folium.Map(location=location, zoom_start=19, max_zoom=19)

tooltip = 'Selected Location'
popup = "Latitude: " + str(lat) + "\nLongitude: " + str(long) + ""
folium.Marker(location, popup = popup, tooltip = tooltip).add_to(m)
folium.LatLngPopup().add_to(m)
folium_static(m)