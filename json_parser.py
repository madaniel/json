# Load JSON into Object
import urllib2
import json
import json_data


json_src = json_data.json7


def main():
    print_json(get_values_list(json_src, "type"))


# # # Functions # # #
def get_values_list(json_dict, target_key, values_list=None):
    if values_list is None:
        values_list = []

    for key, value in json_dict.iteritems():
        if isinstance(value, dict):
            get_values_list(value, target_key, values_list)

        if isinstance(value, list):
            # Check if list contains dict
            for item in value:
                # If so, send it to get_value for searching
                if isinstance(item, dict):
                    get_values_list(item, target_key, values_list)

    if target_key in json_dict:
        #values_list.append(json_dict[target_key])
        values_list.append(json_dict)

    if values_list:
        return values_list


def count_keys(json_dict, target_key, count=0):

    for key, value in json_dict.iteritems():
        if isinstance(value, dict):
            count += count_keys(value, target_key)

        if isinstance(value, list):
                # Check if list contains dict
                for item in value:
                    # If so, send it to get_value for searching
                    if isinstance(item, dict):
                        count += count_keys(item, target_key)

    if target_key in json_dict:
        count += 1
    return count


def get_value(json_dict, target_key):
    """ This function can work only with single instance of the target_key on json """
    # The key found on the current dict
    if target_key in json_dict:
        return json_dict[target_key]

    # The key not found
    for key, value in json_dict.iteritems():

        # Current key is a dict
        if isinstance(value, dict):
            result = get_value(value, target_key)
            if result is not None:
                return result

        # Current key is a list
        if isinstance(value, list):
            # Check if the list contains dict
            for item in value:
                # If so, send it to get_value for searching
                if isinstance(item, dict):
                    result = get_value(item, target_key)
                    if result is not None:
                        return result


def get_json(url):
    # Read the Json from web
    req = urllib2.urlopen(url)

    # Transfer object into python dictionary
    return json.load(req)


def print_json(dict_data):
    # Transfer dictionary into json format
    if isinstance(dict_data, dict) or isinstance(dict_data, list):
        print json.dumps(dict_data)
    else:
        print "Error - no data given"


main()
