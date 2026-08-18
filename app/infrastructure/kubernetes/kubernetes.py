from kubernetes.client import ApiClient, Configuration

from app.infrastructure.config.settings import settings


def create_api_client() -> ApiClient:
    configuration = Configuration()
    configuration.host = settings.kubernetes_host
    configuration.verify_ssl = settings.kubernetes_ssl
    configuration.api_key = {
        "BearerToken": settings.kubernetes_token,
    }
    configuration.api_key_prefix = {
        "BearerToken": "Bearer",
    }

    return ApiClient(configuration)
