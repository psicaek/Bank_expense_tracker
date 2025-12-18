
import requests


def get_transactions(access_token, account_id):
    url = f"https://api.truelayer.com/data/v1/accounts/{account_id}/transactions"
    headers = {
        "accept": "application/json",
        "authorization": f"Bearer {access_token}"
    }
    print("Transactions URL:", url)
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    return response.json()
