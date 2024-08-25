import requests


def sanguozhi_data_api(params):
    result = None

    try:
        root_url = "http://localhost:8000"

        print(f"params = {params}")

        response = requests.get(f"{root_url}/sanguozhi-data", params=params)
        print(f"response = {response}")

        if response:
            response_json = response.json()
            print(f"response_json = {response_json}")

            if response_json:
                result = response_json
    except Exception as e:
        print(f"sanguozhi_data_api error = {e}")

    return result
