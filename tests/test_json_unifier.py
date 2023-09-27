from src.data_processing.json_unifier import json_formatter


def test_json_formatter():
    json1 = {
        "user_id": 1,
        "username": "john_doe",
        "email": "john@example.com"
    }

    json2 = {
        "address": "123 Main St",
        "city": "Exampleville",
        "zipcode": "12345"
    }

    result = json_formatter(json1, json2)

    assert isinstance(result, dict)
    assert result["user_id"] == 1
    assert result["username"] == "john_doe"
    assert result["email"] == "john@example.com"
    assert result["address"] == "123 Main St"
    assert result["city"] == "Exampleville"
    assert result["zipcode"] == "12345"
