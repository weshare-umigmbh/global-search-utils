import flask

from globalsearch.utils.gcp_secret_util import get_secret
from elasticsearch import Elasticsearch
from umi.utils import log


def get_elastic_client():
    elastic_url = get_secret("global_search_elastic_url")
    elastic_user = get_secret("global_search_elastic_user")
    elastic_password = get_secret("global_search_elastic_password")
    elastic_connection_string = f"https://{elastic_user}:{elastic_password}@{elastic_url.split('//')[1]}"
    client = Elasticsearch(
        [
            elastic_connection_string
        ],
        verify_certs=True
    )

    try:
        client.ping()
        log.simple_entry("Connected to Elasticsearch successfully")
    except ConnectionError:
        log.simple_entry(f"Could not connect to Elasticsearch")
        flask.abort(flask.make_response(flask.jsonify(error={
            "code": "InternalServerError",
            "message": "Could not connect to Elasticsearch"
        }), 500))

    return client
