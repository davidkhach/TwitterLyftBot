import requests
import urllib.parse
import urllib.request
import json




def create_conversion_object(address):

    user_address = urllib.request.urlopen("http://open.mapquestapi.com/geocoding/v1/address?key=hq7UB1NqdM3q1i0jXscIVFML6aoKUSAA&location=" + address)
    user_result = json.load(user_address)
    return user_result
    

def find_latitude(user_result):

    return str(user_result["results"][0]["locations"][0]["latLng"]["lat"])
    

def find_longitude(user_result):
    
    return str(user_result["results"][0]["locations"][0]["latLng"]["lng"])
    



