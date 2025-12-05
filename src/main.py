from oauth import get_access_token
from transactions import get_transactions
from accounts import get_accounts


def main():
    print("Connecting to TrueLayer Sandbox...")

    access_token = get_access_token()
    print("\n[OK] Access token received\n")

    print("Fetching Accounts...")
    accounts = get_accounts(access_token)
    print(accounts)

    print("\nFetching Transactions...")
    transactions = get_transactions(access_token)
    print(transactions)


if __name__ == "__main__":
    main()
