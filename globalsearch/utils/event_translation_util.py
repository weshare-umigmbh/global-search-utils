import base64
import json


def get_event_data(event):
    envelope = json.loads(event.data.decode('utf-8'))
    resource = json.loads(base64.b64decode(envelope['message']['data']))
    operation = envelope['message']['attributes']['type']
    return resource, operation
