import requests
import urllib.parse
import urllib.request
import json
import convert_address
import re


## implement twitter part

def create_url_object(lat1, long1, lat2, long2):

    value = urllib.request.urlopen('https://api.lyft.com/v1/cost?start_lat=' + lat1 + '&start_lng=' + long1 + '&end_lat=' + lat2 + '&end_lng=' + long2)
    result = json.load(value)
    return result


def find_cost(result):
    
    estimated_cost_max =  (result["cost_estimates"][0]["estimated_cost_cents_max"])
    estimated_cost_min =  (result["cost_estimates"][0]["estimated_cost_cents_min"])
    estimated_average_cost = round((float(estimated_cost_max) + float(estimated_cost_min))/2)
    return str(int(estimated_average_cost/100))

def find_time(result):
    
     estimated_time = round(result["cost_estimates"][0]["estimated_duration_seconds"])
     return str(int(estimated_time/60))

def run_app(start_location, end_location):
    
    starting_obj = convert_address.create_conversion_object(urllib.parse.quote_plus(start_location))
    start_lat = convert_address.find_latitude(starting_obj)
    start_long = convert_address.find_longitude(starting_obj)
    ending_obj = convert_address.create_conversion_object(urllib.parse.quote_plus(end_location))
    end_lat = convert_address.find_latitude(ending_obj)
    end_long = convert_address.find_longitude(ending_obj)

    lyft_obj = create_url_object(start_lat, start_long, end_lat, end_long)
    cost = find_cost(lyft_obj)
    time = find_time(lyft_obj)

    result = "Estimated Time: " + time + " minutes" + "\n" + "Estimated Cost: " + cost + " dollars"
    result += "\n"  + "#Lyft"
    return result

def parse_response_start_location(response):
    response = response.replace("from: ", '')
    a = re.search(r'\b(to: )\b', response)
    if a != None: 
        response = response[0:a.start()]
        return response
    
def parse_response_end_location(response):
    a = re.search(r'\b(to: )\b', response)
    if a != None: 
        response = response[a.start() + 4:]
        return response
    

