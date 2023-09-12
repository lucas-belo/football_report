import json


def json_formatter(json1, json2):
    combined_json = {**json1, **json2}
    combined_json_str = json.dumps(combined_json, indent=2, ensure_ascii=False)
    print(combined_json_str)
