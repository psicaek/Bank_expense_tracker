Bank Expense Tracker — ING Germany (TrueLayer Integration)

A simple yet powerful program that automatically tracks and categorizes your monthly expenses using TrueLayer’s Open Banking API.
This project is tailored specifically for ING Germany, but can be adapted for any bank supported by TrueLayer.

    How It Works

To enable secure access to your banking data, this project uses the official TrueLayer OAuth 2.0 flow.
Below is a high-level overview of the setup and authentication process.

    TrueLayer Setup (Required Before Running the App)
    Create a TrueLayer Developer Account

Sign up at the TrueLayer Developer Dashboard and access your personal console.

    Create a New Application

In your dashboard, create an app that will represent the Bank Expense Tracker.

    Retrieve Your Credentials

In your app settings, locate and copy:

Client ID

Client Secret

Redirect URI

These are required for OAuth authentication.

    Check the API Reference

Visit the TrueLayer documentation to explore endpoints such as:
/info
/accounts
/balance
/transactions


Test the Flow Using the Sandbox (Recommended)

Before using real banking data, validate everything using TrueLayer’s fully functional sandbox environment.

 OAuth Authorization Flow (Sandbox)
Step 1 — Get the Authorization Code

Open the following link in your browser (replace Client_ID with your own):

https://auth.truelayer-sandbox.com/?response_type=code
&client_id=Client_ID
&scope=info%20accounts%20balance%20cards%20transactions%20direct_debits%20standing_orders%20offline_access
&redirect_uri=https://console.truelayer.com/redirect-page
&providers=uk-cs-mock%20uk-ob-all%20uk-oauth-all

You will be prompted to enter mock bank credentials → You then receive an authorization code.

Step 2 — Exchange Code for Access Token
Send a POST request to:

https://auth.truelayer-sandbox.com/connect/token

{
  "grant_type": "authorization_code",
  "client_id": "YOUR_CLIENT_ID",
  "client_secret": "YOUR_CLIENT_SECRET",
  "redirect_uri": "YOUR_REDIRECT_URI",
  "code": "AUTHORIZATION_CODE_FROM_STEP_1"
}

If everything is correct, you will receive a 200 OK containing your:
access_token
refresh_token
expires_in
Use the access_token to access your accounts, balances, cards, and transactions.

    Project Setup
If someone clones the repository, they must create a .env file in the project root and include:
CLIENT_ID=your_client_id
CLIENT_SECRET=your_client_secret
REDIRECT_URI=your_redirect_uri
These are required for authentication and are never committed to Git.

Running the Program
python main.py

The script will:

1.Start OAuth flow(Done)

2.Fetch your account information(Done)

3.Download your latest transactions(Work in progress)

4.Process and categorise your expenses(Work in progress)