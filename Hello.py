# Load JSON into Object
import urllib
import json

url1 = "http://date.jsontest.com"
url2 = "http://api.geonames.org/citiesJSON?north=44.1&south=-9.9&east=-22.4&west=55.2&lang=de&username=demo"


def main():
    print print_json(url1)


# Functions


def print_json(url):
    # Read the Json from web
    req = urllib.urlopen(url)

    # Transfer object into python dictionary
    dict_data = json.loads(req.read())

    # Transfer dictionary into json format
    json_data = json.dumps(dict_data)

    return json_data


main()