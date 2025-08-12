import phonenumbers
from phonenumbers import geocoder, carrier
from opencage.geocoder import OpenCageGeocode
import folium
from myphone import number  # make sure this file exists with: number = "+255XXXXXXXXX"

# Parse the phone number
pepnumber = phonenumbers.parse(number)

# Get location (region / city)
location = geocoder.description_for_number(pepnumber, "en")
print(f"Location: {location}")

# Get service provider
service_provider = carrier.name_for_number(pepnumber, "en")
print(f"Service Provider: {service_provider}")

# OpenCage API key (get yours from https://opencagedata.com/api)
key = "YOUR_OPENCAGE_API_KEY"  # Replace with your actual key
geocoder_oc = OpenCageGeocode(key)

# Geocode the location string
query = str(location)
results = geocoder_oc.geocode(query)

if results and len(results):
    lat = results[0]['geometry']['lat']
    lng = results[0]['geometry']['lng']
    print(f"Latitude: {lat}, Longitude: {lng}")

    # Create a map
    myMap = folium.Map(location=[lat, lng], zoom_start=9)
    folium.Marker([lat, lng], popup=location).add_to(myMap)

    # Save to HTML file
    myMap.save("mylocation.html")
    print("Map has been saved to mylocation.html")
else:
    print("No results found for location.")
