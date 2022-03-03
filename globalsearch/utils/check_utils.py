import flask
from umi.utils import log


def check_dict_has_none_values(dictionary):
    return None in dictionary.values()


def check_enqueue_time_is_present(entity):
    if not check_existence_and_non_null(entity, "enqueue_time"):
        log.simple_entry(f"The enqueue time is missing or was null in update: {entity}.")
        flask.abort(flask.make_response(flask.jsonify(error={
            "code": "BadRequest",
            "message": f"The enqueue time is missing or was null in update: {entity}."
        }), 400))


def check_existence_and_non_null(dictionary, key):
    print(f"{key} has value: {dictionary.get(key)} and boolean: {dictionary.get(key) is not None}")
    return key in dictionary and dictionary.get(key) is not None


def check_existence(dictionary, key):
    return key in dictionary


def check_all_values_are_non_null(entity):
    has_none_values = check_dict_has_none_values(entity)

    if has_none_values:
        log.simple_entry(f"Update with null values was rejected")
        flask.abort(flask.make_response(flask.jsonify(error={
            "code": "NullValuesNotAllowed",
            "message": "The request contained null values which are not allowed."
        }), 400))


def check_api_key(key_in_secrets, key_in_header):
    if key_in_header != key_in_secrets:
        log.simple_entry(f"Rejected request with invalid API key")
        flask.abort(flask.make_response(flask.jsonify(error={
            "code": "AuthenticationError",
            "message": "Invalid API key."
        }), 401))


def check_if_id_is_present(entity_id):
    if not entity_id:
        log.simple_entry(f"Update without specified id failed")
        flask.abort(flask.make_response(flask.jsonify(error={
            "code": "MissingId",
            "message": "Operation not possible since id is missing."
        }), 400))
