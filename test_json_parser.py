import json_data
import json_parser
import pytest


# # # # # Lists data for test cases # # # # #
json1_keys = ["time", "milliseconds_since_epoch", "date"]
json1_values = ["01:51:50 PM", 1461851510009, "04-28-2016"]

json3_keys = ["long_name", "short_name", "lat", "lng"]
json3_count = [8, 8, 3, 3]

json4_keys = ["debug", "title", "src", "data"]
json4_values = ["on", "Sample Konfabulator Widget", "Images/Sun.png", "Click Here"]

json5_keys = ["fcodeNameXXX", "lngXXX", "toponymName", "population"]
json5_values = ["capital of a political entity", 114.157691001892, "Mexico City", 12294193]

json6_keys = ["time", "milliseconds_since_epoch", "date"]
json6_count = [2, 2, 2]

json8_keys = ["colorName", "hexValue"]
json8_value_0 = [{"colorName": "red", "hexValue": "#f00"}, {"colorName": "green", "hexValue": "#0f0"},
                 {"colorName": "blue", "hexValue": "#00f"}, {"colorName": "cyan", "hexValue": "#0ff"},
                 {"colorName": "magenta", "hexValue": "#f0f"}, {"colorName": "yellow", "hexValue": "#ff0"},
                 {"colorName": "black", "hexValue": "#000"}]
json8_values = [json8_value_0]

json9_keys = ["label"]
json9_value_0 = [{"id": "OpenNew", "label": "Open New"}, {"id": "ZoomIn", "label": "Zoom In"},
                 {"id": "ZoomOut", "label": "Zoom Out"}, {"id": "OriginalView", "label": "Original View"},
                 {"id": "Find", "label": "Find..."}, {"id": "FindAgain", "label": "Find Again"},
                 {"id": "CopyAgain", "label": "Copy Again"}, {"id": "CopySVG", "label": "Copy SVG"},
                 {"id":"ViewSVG", "label": "View SVG"}, {"id": "ViewSource", "label": "View Source"},
                 {"id": "SaveAs", "label": "Save As"}, {"id": "About", "label": "About xProgress CVG Viewer..."}]
json9_values = [json9_value_0]

json10_keys = ["time", "milliseconds_since_epoch", "date"]
json10_count = [1, 1, 1]
json10_values = ["01:51:50 PM", 1461851510009, "04-28-2016"]

json11_keys = ["geonameId", "countrycode", "milliseconds_since_epoch", "fcodeName"]
json11_count = [1, 1, 1, 2]
json11_values = [3530597, "MX", 1461851510009, "capital of a political entity"]

# # # # # Test Cases # # # # #

@pytest.mark.get_value
def test_get_value_tc0():
    # Testing get_value when nothing found
    json = json_data.json1
    assert not json_parser.get_value([], "")
    assert not json_parser.get_value(json, "Nothing")


@pytest.mark.get_value
def test_get_value_tc1():
        # Testing get_value with a simple JSON
        json = json_data.json1
        assert json_parser.get_value(json, json1_keys[0]) == json1_values[0]
        assert json_parser.get_value(json, json1_keys[1]) == json1_values[1]
        assert json_parser.get_value(json, json1_keys[2]) == json1_values[2]


@pytest.mark.get_value
def test_get_value_tc2():
    # Testing get_value with variant depth JSON
    json = json_data.json4
    assert json_parser.get_value(json, json4_keys[0]) == json4_values[0]
    assert json_parser.get_value(json, json4_keys[1]) == json4_values[1]
    assert json_parser.get_value(json, json4_keys[2]) == json4_values[2]
    assert json_parser.get_value(json, json4_keys[3]) == json4_values[3]


@pytest.mark.get_value
def test_get_value_tc3():
    # Testing get_value with lists within dict
    json = json_data.json5
    assert json_parser.get_value(json, json5_keys[0]) == json5_values[0]
    assert json_parser.get_value(json, json5_keys[1]) == json5_values[1]
    assert json_parser.get_value(json, json5_keys[2]) == json5_values[2]
    assert json_parser.get_value(json, json5_keys[3]) == json5_values[3]


@pytest.mark.get_value
def test_get_value_tc4():
    # Testing get_value with list of JSON
    json = json_data.json10
    assert json_parser.get_value(json, json10_keys[0]) == json10_values[0]
    assert json_parser.get_value(json, json10_keys[1]) == json10_values[1]
    assert json_parser.get_value(json, json10_keys[2]) == json10_values[2]


@pytest.mark.get_value
def test_get_value_tc5():
    # Testing get_value with list of JSON
    json = json_data.json11
    assert json_parser.get_value(json, json11_keys[0]) == json11_values[0]
    assert json_parser.get_value(json, json11_keys[1]) == json11_values[1]
    assert json_parser.get_value(json, json11_keys[2]) == json11_values[2]
    assert json_parser.get_value(json, json11_keys[3]) == json11_values[3]


@pytest.mark.count_keys
def test_count_keys_tc1():
    # Testing count_keys with a simple JSON
    json = json_data.json6
    assert json_parser.count_keys(json, json6_keys[0]) == json6_count[0]
    assert json_parser.count_keys(json, json6_keys[1]) == json6_count[1]
    assert json_parser.count_keys(json, json6_keys[2]) == json6_count[2]


@pytest.mark.count_keys
def test_count_keys_tc2():
    # Testing count_keys with a complex JSON
    json = json_data.json3
    assert json_parser.count_keys(json, json3_keys[0]) == json3_count[0]
    assert json_parser.count_keys(json, json3_keys[1]) == json3_count[1]
    assert json_parser.count_keys(json, json3_keys[2]) == json3_count[2]


@pytest.mark.count_keys
def test_count_keys_tc3():
    # Testing count_keys with list of JSONs
    json = json_data.json10
    assert json_parser.count_keys(json, json10_keys[0]) == json10_count[0]
    assert json_parser.count_keys(json, json10_keys[1]) == json10_count[1]
    assert json_parser.count_keys(json, json10_keys[2]) == json10_count[2]


@pytest.mark.count_keys
def test_count_keys_tc4():
    # Testing count_keys with list of JSONs
    json = json_data.json11
    assert json_parser.count_keys(json, json11_keys[0]) == json11_count[0]
    assert json_parser.count_keys(json, json11_keys[1]) == json11_count[1]
    assert json_parser.count_keys(json, json11_keys[2]) == json11_count[2]
    assert json_parser.count_keys(json, json11_keys[3]) == json11_count[3]


@pytest.mark.get_values_list
def test_get_values_list_tc1():
    # Testing get_values_list on multi values JSON #1
    json = json_data.json8
    assert json_parser.get_values_list(json, json8_keys[0]) == json8_values[0]
    assert json_parser.get_values_list(json, json8_keys[1]) == json8_values[0]


@pytest.mark.get_values_list
def test_get_values_list_tc2():
    # Testing get_values_list on multi values JSON #2
    json = json_data.json9
    assert json_parser.get_values_list(json, json9_keys[0]) == json9_values[0]


