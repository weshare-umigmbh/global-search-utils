import flask
from umi.utils import log

def validate_enqueue_time(entity_update, persisted_enqueue_time):
    new_enqueue_time = entity_update.get("enqueue_time", 0)
    if persisted_enqueue_time >= new_enqueue_time:
        log.simple_entry(f"Attempt to update with an outdated enqueue time is rejected. "
              f"Currently stored enqueue_time: {persisted_enqueue_time}, transaction_update: {entity_update}. "
              f"No update performed")
        flask.abort(flask.make_response(flask.jsonify(error={
            "code": "EnqueueTimeOutdated",
            "message": f"The enqueue_time of the update: {new_enqueue_time} "
                       f"is older than or equal to the one of the stored entry: {persisted_enqueue_time}. "
                       f"No update was performed."
        }), 200))
