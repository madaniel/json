# Load JSON into Object
import urllib2
import json
import json_data


json = json_data.json4


def main():
    print get_value(json, "debug")


# Functions
def get_value(json_dict, target_key):
    # The key found on the current dict
    if target_key in json_dict:
        return json_dict[target_key]

    # The key not found
    for key, value in json_dict.iteritems():
        # There's still more dict on the structure
        if isinstance(value, dict):
            result = get_value(value, target_key)
            if result is not None:
                return result


def get_json(url):
    # Read the Json from web
    req = urllib2.urlopen(url)

    # Transfer object into python dictionary
    return json.load(req)


def print_json(dict_data):
    # Transfer dictionary into json format
    json_data = json.dumps(dict_data)

    print json_data


main()
