

-----

#  Bank Expense Tracker — ING Germany (TrueLayer Integration)

A simple yet powerful Python program that automatically tracks and categorizes your monthly expenses using **TrueLayer’s Open Banking API**.

This project is primarily tailored for **ING Germany**, but it is architected to be easily adapted for any bank supported by TrueLayer.

-----

## 💡 How It Works

To ensure **secure access** to your financial data, this project uses the official **TrueLayer OAuth 2.0 flow**.

The application first directs you to TrueLayer's secure authorization page to obtain permission. Upon successful authorization, it exchanges a temporary code for an **`access_token`**, which is then used to fetch your financial data securely.

##  Project Status

| Feature | Status |
| :--- | :--- |
| **1. Start OAuth Flow** | ✅ Done |
| **2. Fetch Account Information** | ✅ Done |
| **3. Download Latest Transactions** | ✅ Done |
| **4. Process & Categorize Expenses** | ⚙️ Work in Progress |

-----

## 🛠️ Setup & Prerequisites

Before running the application, you must complete the setup steps in the **TrueLayer Developer Dashboard**.

### TrueLayer Setup (Required)

1.  **Create a TrueLayer Developer Account:**

      * Sign up at the [TrueLayer Developer Dashboard](https://www.google.com/search?q=https://developer.truelayer.com/) and access your console.

2.  **Create a New Application:**

      * In your dashboard, create a new app to represent your Bank Expense Tracker.

3.  **Retrieve Your Credentials:**

      * In your app settings, locate and copy the following required values:
          * **`Client ID`**
          * **`Client Secret`**
          * **`Redirect URI`**

4.  **Check the API Reference:**

      * Familiarize yourself with the TrueLayer documentation to explore essential endpoints:
          * `/info`
          * `/accounts`
          * `/balance`
          * `/transactions`

### Project Setup

1.  **Clone the repository:**

    ```bash
    git clone [repository_url]
    cd [repository_name]
    ```

2.  **Create the `.env` file:**

      * In the project root directory, create a file named **`.env`** and populate it with your credentials. **These credentials must never be committed to Git.**

    **.env**

    ```env
    CLIENT_ID=your_client_id
    CLIENT_SECRET=your_client_secret
    REDIRECT_URI=your_redirect_uri
    ```

-----

## 🔑 OAuth Authorization Flow (Sandbox)

It is highly recommended to **Test the Flow Using the Sandbox** before using real banking data.

### Step 1 — Get the Authorization Code

Open the following link in your browser. **Remember to replace `Client_ID` with your actual Client ID.**

```url
https://auth.truelayer-sandbox.com/?response_type=code
&client_id=Client_ID
&scope=info%20accounts%20balance%20cards%20transactions%20direct_debits%20standing_orders%20offline_access
&redirect_uri=https://console.truelayer.com/redirect-page
&providers=uk-cs-mock%20uk-ob-all%20uk-oauth-all
```

  * You will be prompted to enter mock bank credentials.
  * Upon successful mock login, you will be redirected and receive an **`authorization_code`** in the URL.

### Step 2 — Exchange Code for Access Token

The program handles this step by sending a **`POST`** request to the token endpoint.

  * **Endpoint:** `https://auth.truelayer-sandbox.com/connect/token`

  * **Request Body Example:**

    ```json
    {
      "grant_type": "authorization_code",
      "client_id": "YOUR_CLIENT_ID",
      "client_secret": "YOUR_CLIENT_SECRET",
      "redirect_uri": "YOUR_REDIRECT_URI",
      "code": "AUTHORIZATION_CODE_FROM_STEP_1"
    }
    ```

  * **Successful Response:** A `200 OK` containing your:

      * **`access_token`** (used to call data endpoints)
      * **`refresh_token`**
      * **`expires_in`**

-----

## 🖥️ Using Selenium for Live Authorization

For the live environment with ING Germany, the OAuth flow requires the user to log in with their real banking credentials. 
To make this process smoother, the program can optionally use Selenium to control a web browser and navigate the login page automatically, so the user does not have to manually enter their credentials.

Currently, this automation is partially implemented, as some elements on ING’s login page are embedded inside Shadow DOMs, which Selenium cannot easily access. 
Because of this limitation, the user still needs to manually complete the login for now.

In the future, it may be possible to fully automate the login using Playwright, which has better support for interacting with Shadow DOM elements. 
This would allow the entire OAuth flow to run headlessly, providing a seamless experience for users.


-----
## 🔑 OAuth Authorization Flow (Live)

It is highly recommended to **Test the Flow Using the Sandbox** before using real banking data.

### Step 1 — Get the Authorization Code Example for ING

Open the following link in your browser. **Remember to replace `Client_ID` with your actual Client ID.**

```url
https://auth.truelayer.com/?response_type=code
&client_id=YOUR_CLIENT_ID
&scope=info%20accounts%20balance%20transactions%20offline_access
&redirect_uri=YOUR_REDIRECT_URI
&providers=de-ing
```

  * You will be prompted to enter mock bank credentials.
  * Upon successful mock login, you will be redirected and receive an **`authorization_code`** in the URL.

### Step 2 — Exchange Code for Access Token

The program handles this step by sending a **`POST`** request to the token endpoint.

  * **Endpoint:** `https://auth.truelayer.com/connect/token`

  * **Request Body Example:**

    ```json
    {
      "grant_type": "authorization_code",
      "client_id": "YOUR_CLIENT_ID",
      "client_secret": "YOUR_CLIENT_SECRET",
      "redirect_uri": "YOUR_REDIRECT_URI",
      "code": "AUTHORIZATION_CODE_FROM_STEP_1"
    }
    ```

  * **Successful Response:** A `200 OK` containing your:

      * **`access_token`** (used to call data endpoints)
      * **`refresh_token`**
      * **`expires_in`**

-----
## 🏦 Fetching Accounts and Transactions

After obtaining an access token through the OAuth authorization flow, the next step is to retrieve account and transaction information from TrueLayer.

## Fetching Accounts

The program first queries the Accounts API to obtain a list of all bank accounts associated with the access token.
Each account includes essential information such as the account ID, account type, currency, and display name.
The account ID is particularly important because it is required to fetch the corresponding transactions. 
For users with multiple accounts, the program can iterate over all accounts to process each one individually.

## Fetching Transactions

Once the account ID is available, the program queries the Transactions API to retrieve the transaction history for that account. 
Each transaction contains details such as the date and time, description or merchant name, amount, currency, and transaction type (credit or debit). 
This data forms the foundation for tracking and categorizing expenses.

The fetched transactions can be stored locally for further analysis or reporting. 
This ensures that even after the program terminates, the financial data is preserved and can be processed later for summaries, charts, or export to other formats.




## 🏃 Running the Program

Once your `.env` file is set up, you can run the main script.
For using the Live version 

```bash
python main.py  
```
For using the Sandbox version 

```bash
python main_sandbox.py  
```

The script will automatically initiate the OAuth flow and proceed with the data fetching steps.

-----

I've organized the information into logical sections with clear headings and formatting. Would you like me to expand on any of the "Work in Progress" sections, perhaps by outlining the next coding steps?