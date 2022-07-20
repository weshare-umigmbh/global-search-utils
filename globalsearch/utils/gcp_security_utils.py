import os

import flask
from google.auth.transport import requests
from google.oauth2 import id_token
from umi.utils import log


def check_token(request):
    function_url = os.environ.get("FUNCTION_URL")
    project_id = os.environ.get("GCP_PROJECT")
    # Verify that the push request originates from Cloud Pub/Sub.
    try:
        # Get the Cloud Pub/Sub-generated JWT in the "Authorization" header.
        bearer_token = request.headers.get('Authorization')
        token = bearer_token.split(' ')[1]
        # Verify and decode the JWT. `verify_oauth2_token` verifies
        # the JWT signature, the `aud` claim, and the `exp` claim.
        claim = id_token.verify_oauth2_token(token, requests.Request(), audience=function_url)
        # Ensure that `claim["email_verified"]` is set to true.
        assert claim.get("email_verified", False)
        # Ensure that `claim["email"]` is equal to the expected service
        # account set up in the push subscription settings.
        assert claim.get("email") == f"push-subscription-invoker@{project_id}.iam.gserviceaccount.com"
    except Exception as e:
        log.simple_entry(f"The Google ID token could not be verified: {e}")
        flask.abort(flask.make_response(flask.jsonify(error={
            "code": "BadRequest",
            "message": f"Invalid token: {e}\n"
        }), 400))
        return
