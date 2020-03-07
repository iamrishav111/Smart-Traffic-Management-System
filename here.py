# app id L4GMWVCTMzAETvXxc0y9
# api key fywUFbdwhP7YRn5SZI2A-ZJ7te444T2vt3X5GWnveAE
import herepy
import json
geocoderApi = herepy.GeocoderApi('fywUFbdwhP7YRn5SZI2A-ZJ7te444T2vt3X5GWnveAE')
response = geocoderApi.free_form('jadavpur')
#response = geocoderApi.free_form('garia more,kolkata')
#print(response)
s=json.loads(str(response))


lat = s["Response"]["View"][0]["Result"][0]["Location"]["DisplayPosition"]["Latitude"] 
lng = s["Response"]["View"][0]["Result"][0]["Location"]["DisplayPosition"]["Longitude"] 
print(lat,lng)

