import requests
import service.tyk_token.tyk_token_const as cs



def create_endpoint(endpoint_name: str, listen_path: str, target_url):
    endpoint_data = cs.get_endpoint_template()
    endpoint_data[cs.TYK_ENDPOINT_NAME] = endpoint_name
    endpoint_data[cs.TYK_ENDPOINT_SLUG] = endpoint_name
    endpoint_data[cs.TYK_API_ID] = endpoint_name
    endpoint_data[cs.TYK_PROXY][cs.TYK_LISTEN_PATH] = listen_path
    endpoint_data[cs.TYK_PROXY][cs.TYK_TARGET_URL] = target_url

    # Send the POST request
    response = requests.post(cs.TYK_API_URL, json=endpoint_data, headers=cs.TYK_API_HEADER)
    if response.ok:
        print("API created successfully.")
        reload_tyk()
        print("Reload successfully.")
        print(response.json())
    else:
        print(f"Failed to create API. Status code: {response.status_code}")
        print(response.text)


def reload_tyk():
    response = requests.get(cs.TYK_RELOAD_URL, headers=cs.TYK_API_HEADER)
    if not response.ok:
        response.raise_for_status()


def create_key(api_ids: list[str]):
    access_rights = {}
    for api_id in api_ids:
        access_right_template = cs.get_access_rights()
        access_right_template[cs.TYK_API_NAME] = api_id
        access_right_template[cs.TYK_API_ID] = api_id
        access_rights.update({api_id: access_right_template})
    key_create_template = cs.get_key_create_data()
    key_create_template[cs.ACCESS_RIGHTS] = access_rights
    response = requests.post(cs.TYK_KEYS_CREATE_URL, json=key_create_template, headers=cs.TYK_API_HEADER)
    print(response.json())

    if not response.ok:
        response.raise_for_status()
    return response.json().get("key")


def delete_endpoint(api_id: str):
    response = requests.request("DELETE", f"{cs.TYL_DELETE_URL}/{api_id}", headers=cs.TYK_API_HEADER)
    if response.ok:
        print(f"API {api_id} deleted successfully.")
        reload_tyk()
        print("Reload successfully.")
        print(response.json())
    if not response.ok:
        response.raise_for_status()