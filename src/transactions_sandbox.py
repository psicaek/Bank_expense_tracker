import requests
from config import DATA_URL_SANDBOX


def get_transactions(access_token):
    headers = {"Authorization": f"Bearer {access_token}"}
    url = f"{DATA_URL_SANDBOX}"
    return requests.get(url, headers=headers).json()
