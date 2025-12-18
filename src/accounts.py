import requests

from config import LIST_ACCOUNTS_URL


def get_accounts(access_token):
    url = LIST_ACCOUNTS_URL
    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {access_token}"
    }
    response = requests.get(url, headers=headers)
    print(response.status_code)
    print(response.text)
    account_id = response.json()["results"][0]["account_id"]
    return response.json(),account_id
