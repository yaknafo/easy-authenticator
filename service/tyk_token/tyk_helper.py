import requests
import service.tyk_token.tyk_token_const as cs


def create_endpoint(endpoint_name: str, listen_path: str, target_url):
    endpoint_data = cs.get_endpoint_template()
    endpoint_data[cs.TYK_ENDPOINT_NAME] = endpoint_name
    endpoint_data[cs.TYK_ENDPOINT_SLUG] = endpoint_name
    endpoint_data[cs.TYK_API_ID] = endpoint_name
    endpoint_data[cs.TYK_LISTEN_PATH] = listen_path
    endpoint_data[cs.TYK_TARGET_URL] = target_url

    # Send the POST request
    response = requests.post(cs.TYK_API_URL, json=endpoint_data, headers=headers)
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
