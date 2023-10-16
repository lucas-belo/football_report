import logging

from bson import ObjectId


def json_formatter(json1: any, json2: any) -> any:
    """
    Get the database json and the data scrapper json and unify it in an unique json
    :param json1: database json
    :param json2: scrapper json
    :return: unified json
    """
    try:
        json1 = {k: str(v) if isinstance(v, ObjectId) else v for k, v in json1.items()}
        json2 = {k: str(v) if isinstance(v, ObjectId) else v for k, v in json2.items()}

        combined_json = {**json1, **json2}

        print("Jsons successfully combined")
        logging.info("Jsons successfully combined")

        return combined_json

    except Exception as e:
        print(f"Error to unify the jsons: {e}")
        logging.error(f"Error to unify the jsons: {e}")
