import google.cloud.logging


def setup_gcp_logging():
    log_client = google.cloud.logging.Client()
    log_client.setup_logging()
