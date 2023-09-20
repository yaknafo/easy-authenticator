TYK_API_URL = "http://localhost:8080/tyk/apis"
TYK_APIS = "/apis"
TYK_KEYS_CREATE_URL = "http://localhost:8080/tyk/keys/create"
TYK_RELOAD_URL = "http://localhost:8080/tyk/reload/group"

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


def get_endpoint_template():
    return {
        TYK_ENDPOINT_SLUG: "system-status",
        TYK_ENDPOINT_NAME: "system-status",
        TYK_API_ID: "system-status",
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
            TYK_LISTEN_PATH: "/api/sport",
            TYK_TARGET_URL: "https://www.sport5.co.il/",
            "strip_listen_path": True
        },
        "active": True
    }


TYK_API_NAME = "api_name"

ACCESS_RIGHTS_ENTRY = {
    TYK_API_NAME: "system-status",
    TYK_API_ID: "system-status",
    "versions": [
        "Default"
    ],
    "allowed_urls": [],
    "limit": None,
    "allowance_scope": ""
}

ACCESS_RIGHTS = "access_rights"
KEY_CREATE_DATA = {
    "quota_max": 0,
    "rate": 2,
    "per": 5,
    "org_id": "1",
    "access_rights": {}

}
