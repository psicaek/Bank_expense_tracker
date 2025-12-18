
import requests


def get_transactions(access_token, account_id):
    url = f"https://api.truelayer.com/data/v1/accounts/{account_id}/transactions"
    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {access_token}"
    }

    response = requests.get(url, headers=headers)
    print(response.status_code)
    print(response.text)
    response.raise_for_status()
    return response.json()
