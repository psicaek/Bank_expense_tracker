import requests
from config import DATA_URL

def get_transactions(access_token):
    headers = {"Authorization": f"Bearer {access_token}"}
    url = f"{DATA_URL}"
    return requests.get(url, headers=headers).json()
