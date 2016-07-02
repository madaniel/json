import urllib2
import json
import os


# # # Functions # # #
def get_all_values(json_dict, target_key):
    # Helper function for get_all_values_dict()

    if isinstance(json_dict, dict):
        return get_all_values_dict(json_dict, target_key)

    values_list = []

    if isinstance(json_dict, list):
        for item in json_dict:
            result = get_all_values_dict(item, target_key)
            if result:
                values_list.extend(result)

    return values_list


def get_all_values_dict(json_dict, target_key, values_list=None):
    """
    :param json_dict: JSON object
    :param target_key: key to find
    :param values_list: list to be values of target key
    :return: list of all the values found
    """
    if values_list is None:
        values_list = []

    assert isinstance(json_dict, dict), "Can handle only dict as JSON root"

    # Getting deep into the JSON tree first using recursion
    for key, value in json_dict.iteritems():
        # Handling dictionary
        if isinstance(value, dict):
            get_all_values_dict(value, target_key, values_list)
        # Handling list
        if isinstance(value, list):
            # Check if list contains dict
            for item in value:
                # If so, send it to get_value for searching
                if isinstance(item, dict):
                    get_all_values_dict(item, target_key, values_list)
    # Search for the target key
    if target_key in json_dict:
        values_list.append(json_dict)
    # Return the list [if not empty] to the function caller
    if values_list:
        return values_list


def count_keys(json_dict, target_key):
    # Helper function to count_keys_dict()

    if isinstance(json_dict, dict):
        return count_keys_dict(json_dict, target_key)

    count = 0
    if isinstance(json_dict, list):
        for item in json_dict:
            count += count_keys_dict(item, target_key)

    return count


def count_keys_dict(json_dict, target_key, count=0):
    """
        :param json_dict: JSON object [dict only]
        :param target_key: key to find
        :param count: number of target key instances
        :return: number of instances found
    """
    assert isinstance(json_dict, dict), "can handle only dict as JSON root"

    for key, value in json_dict.iteritems():
        # Handling dictionary
        if isinstance(value, dict):
            # Accumulating the count from all function call
            count += count_keys(value, target_key)
        # Handling list
        if isinstance(value, list):
                # Check if list contains dict
                for item in value:
                    # If so, send it to get_value for searching
                    if isinstance(item, dict):
                        # Accumulating the count from all function call
                        count += count_keys(item, target_key)
    # Count the key
    if target_key in json_dict:
        count += 1
    return count


def get_value(json_dict, target_key):
    # Helper function to get_value_dict()
    if isinstance(json_dict, dict):
        return get_value_dict(json_dict, target_key)

    if isinstance(json_dict, list):
        for item in json_dict:
            value = get_value_dict(item, target_key)
            if value:
                return value


def get_value_dict(json_dict, target_key):
    """
    :param json_dict: JSON object
    :param target_key: key to find
    :return: value of the target key
    In case of multiple instances, the 1st key value found will be returned
    """

    assert isinstance(json_dict, dict), "can handle only dict as JSON root"
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
    # Transfer dictionary into json format [None -> null]
    if isinstance(dict_data, dict) or isinstance(dict_data, list):
        print json.dumps(dict_data, sort_keys=True, indent=4, separators=(',', ': '))
    else:
        print "Error - no data given"


def write_json(json_data, filename, json_path="C:\\"):
    """
    :param json_data: JSON object / python dictionary
    :param filename: string of the filename
    :param json_path: default path to save the file
    :return: filename with its path
    """

    # Setting the path to JSON folder
    json_filename = os.path.join(json_path, filename)

    # Writing JSON data
    with open(json_filename, 'w') as f:
        json.dump(json_data, f, sort_keys=True, indent=4, separators=(',', ': '))

    return json_filename


def read_json(filename, json_path):
    """
    :param filename: string of the filename
    :param json_path: path to the filename
    :return: dictionary of JSON
    """
    # Setting the path to JSON folder
    json_filename = os.path.join(json_path, filename)

    # Reading JSON data
    with open(json_filename, 'r') as f:
        return json.load(f)


# Compare 2 JSONs line by line
def compare_json(source, target, excluded=None):
    """
    :param source: Baseline recorded JSON
    :param target: JSON under test
    :param excluded: List of strings which should not be checked
    :return: True if equals or empty list if equals without excluded list
    """

    if source == target:
        return True

    # List for adding the diff lines
    diff = []

    # Writing JSONs to files
    tmp_source_json = write_json(source, "tmp_source.json")
    tmp_target_json = write_json(target, "tmp_target.json")

    # Reading the files into lists
    with open(tmp_source_json) as src:
        source_content = src.readlines()
    with open(tmp_target_json) as tar:
        target_content = tar.readlines()

    # Comparing each line
    for source_line, target_line in zip(source_content, target_content):
        if not source_line == target_line:
            # removing spaces and extra chars from string
            target_line = target_line.strip().split(":")[0].strip('"')
            if target_line not in excluded:
                diff.append(target_line)

    # Removing JSONs files
    src.close()
    tar.close()
    try:
        os.remove(tmp_source_json)
        os.remove(tmp_target_json)
    # In case the file does not exists
    except WindowsError:
        print "\n\n! ! !failed to delete tmp JSON files ! ! !\n"

    return diff


