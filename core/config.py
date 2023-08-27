import os

from pydantic import BaseConfig



class GlobalConfig(BaseConfig):
    title: str = "test"
    version: str = "1.0.0"
    description: str = "bla"
    # openapi_prefix: str = "api"
    docs_url: str = "/docs"
    redoc_url: str = "/redoc"
    # openapi_url: str = "/openapi.json"
    api_prefix: str = "/api"


settings = GlobalConfig()