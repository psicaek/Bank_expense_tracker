import requests
from config import example_client_key,example_client_pem, TOKEN_URL, Client_ID

# For sandbox, ING uses client_credentials grant
data = {
    "grant_type": "client_credentials",
    "scope": "AIS"  # AIS = Account Information Service
    "client_id": Client_ID
}

# mTLS authentication with your .p12 keystore
response = requests.post(
    TOKEN_URL,
    data=data,
    cert=(example_client_pem, example_client_key)
)

if response.status_code == 200:
    token = response.json()["access_token"]
    print("Access token:", token)
else:
    print("Error getting token:", response.status_code, response.text)
