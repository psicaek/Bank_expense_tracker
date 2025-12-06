

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
| **3. Download Latest Transactions** | ⚙️ Work in Progress |
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

## 🏃 Running the Program

Once your `.env` file is set up, you can run the main script.

```bash
python main.py
```

The script will automatically initiate the OAuth flow and proceed with the data fetching steps.

-----

I've organized the information into logical sections with clear headings and formatting. Would you like me to expand on any of the "Work in Progress" sections, perhaps by outlining the next coding steps?