import json
from bson import ObjectId


def json_formatter(json1, json2):
    json1 = {k: str(v) if isinstance(v, ObjectId) else v for k, v in json1.items()}
    json2 = {k: str(v) if isinstance(v, ObjectId) else v for k, v in json2.items()}

    combined_json = {**json1, **json2}
    combined_json_str = json.dumps(combined_json, indent=2, ensure_ascii=False)
    return combined_json
