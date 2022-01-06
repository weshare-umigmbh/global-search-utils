import os
from google.cloud import secretmanager


def get_secret(secret_name):
    client = secretmanager.SecretManagerServiceClient()
    project_id = os.environ.get("GCP_PROJECT")
    resource_name = f"projects/{project_id}/secrets/{secret_name}/versions/latest"
    response = client.access_secret_version(name=resource_name)
    return response.payload.data.decode("UTF-8")
