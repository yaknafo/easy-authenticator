import os

TYK_HOST = os.getenv("tyk_host", "localhost")
TYK_POST = os.getenv("tyk_port", "8080")
TYK_URL = f"http://{TYK_HOST}:{TYK_POST}"


TYK_API_URL = f"{TYK_URL}/tyk/apis"
TYK_APIS = "/apis"
TYK_KEYS_CREATE_URL = f"{TYK_URL}/tyk/keys/create"
TYK_RELOAD_URL = f"{TYK_URL}/tyk/reload/group"
TYL_DELETE_URL = f"{TYK_URL}/tyk/apis/"


# AUTHORIZATION
X_TYK_AUTHORIZATION = "x-tyk-authorization"
# Define the headers
TYK_API_HEADER = {
    X_TYK_AUTHORIZATION: "foo",
    "Content-Type": "application/json"
}

# ENDPOINT
TYK_ENDPOINT_SLUG = "slug"
TYK_ENDPOINT_NAME = "name"
TYK_API_ID = "api_id"
TYK_LISTEN_PATH = "listen_path"
TYK_TARGET_URL = "target_url"
TYK_PROXY = "proxy"

def get_endpoint_template():
    return {
        TYK_ENDPOINT_SLUG: None,
        TYK_ENDPOINT_NAME: None,
        TYK_API_ID: None,
        "org_id": "1",
        "auth": {
            "auth_header_name": "Authorization"
        },
        "definition": {
            "location": "header",
            "key": "x-api-version"
        },
        "version_data": {
            "not_versioned": True,
            "versions": {
                "Default": {
                    "name": "Default",
                    "use_extended_paths": True
                }
            }
        },
        "proxy": {
            TYK_LISTEN_PATH: None,
            TYK_TARGET_URL: None,
            "strip_listen_path": True
        },
        "active": True
    }


TYK_API_NAME = "api_name"


def get_access_rights():
    return {
        TYK_API_NAME: None,
        TYK_API_ID: None,
        "versions": [
            "Default"
        ],
        "allowed_urls": [],
        "limit": None,
        "allowance_scope": ""}


ACCESS_RIGHTS = "access_rights"


def get_key_create_data():
    return {
        "quota_max": 0,
        "rate": 2,
        "per": 5,
        "org_id": "1",
        ACCESS_RIGHTS: None

    }
