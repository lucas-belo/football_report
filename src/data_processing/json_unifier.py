import logging

from bson import ObjectId


def json_formatter(json1, json2):
    try:
        json1 = {k: str(v) if isinstance(v, ObjectId) else v for k, v in json1.items()}
        json2 = {k: str(v) if isinstance(v, ObjectId) else v for k, v in json2.items()}

        combined_json = {**json1, **json2}

        print("Jsons successfully combined")
        logging.info("Jsons successfully combined")

        return combined_json

    except Exception as e:
        print("Error to unify the jsons")
        logging.error("Error to unify the jsons")
