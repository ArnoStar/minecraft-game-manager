from pydantic_settings import BaseSettings, SettingsConfigDict


class _Settings(BaseSettings):
    kubernetes_host: str | None = None
    kubernetes_token: str | None = None
    kubernetes_namespace: str | None = None
    kubernetes_ssl: bool | None = True

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
    )


settings: _Settings = _Settings()
