import flask


def respond_with_optimistic_locking_error(entity, entity_name, max_retries_on_version_conflict):
    print(f"Failed to create/update/delete {entity_name}: {entity} after {max_retries_on_version_conflict} retries.")
    flask.abort(flask.make_response(flask.jsonify(error={
        "code": "VersionConflict",
        "message": "Service failed to consistently update the {entity_name} due to 3 failed optimistic locking trials"
    }), 500))