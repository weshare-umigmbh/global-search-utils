import flask


def check_dict_has_none_values(dictionary):
    has_none_value = False
    for key, value in dictionary.items():
        if value is None:
            has_none_value = True

    return has_none_value


def check_enqueue_time_is_present(entity):
    if not check_existence_and_non_null(entity, "enqueue_time"):
        print(f"The enqueue time is missing or was null in update: {entity}.")
        flask.abort(flask.make_response(flask.jsonify(error={
            "code": "BadRequest",
            "message": f"The enqueue time is missing or was null in update: {entity}."
        }), 400))


def check_existence_and_non_null(dictionary, key):
    return key in dictionary and dictionary.get(key)


def check_existence(dictionary, key):
    return key in dictionary


def check_all_values_are_non_null(entity):
    has_none_values = check_dict_has_none_values(entity)

    if has_none_values:
        print(f"Update with null values was rejected")
        flask.abort(flask.make_response(flask.jsonify(error={
            "code": "NullValuesNotAllowed",
            "message": "The request contained null values which are not allowed."
        }), 400))

    return


def check_api_key(key_in_secrets, key_in_header):
    if key_in_header != key_in_secrets:
        print(f"Rejected request with invalid API key")
        flask.abort(flask.make_response(flask.jsonify(error={
            "code": "AuthenticationError",
            "message": "Invalid API key."
        }), 401))
    return


def check_if_id_is_present(entity_id):
    if entity_id is None or entity_id == "":
        print(f"update without specified id failed")
        flask.abort(flask.make_response(flask.jsonify(error={
            "code": "MissingId",
            "message": "Operation not possible since id is missing."
        }), 400))
