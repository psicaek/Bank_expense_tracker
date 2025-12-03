import requests
from config import example_client_key,example_client_pem, ACCOUNTS_URL
from get_token import token  # import token from previous script

headers = {
    "Authorization": f"Bearer {token}"
}

response = requests.get(
    ACCOUNTS_URL,
    headers=headers,
    cert=(example_client_pem, example_client_key)
)

if response.status_code == 200:
    accounts = response.json()
    print("Sandbox accounts:", accounts)
else:
    print("Error fetching accounts:", response.status_code, response.text)
