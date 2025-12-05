# Bank_expense_tracker
A program that tracks my expenses every month. this program is made for ING bank in Germany 
    1.First we need to create a developer account in Truelayer
    2.Create an app in true layer 
    3.Find the client id and the client secret.
    4.Find the Api in the docs
    5.Test the sandbox code with postman
        Here is the logic behind
        1.we give our banking credential to this api https://auth.truelayer-sandbox.com/?response_type=code&client_id=Client_ID&scope=info%20accounts%20balance%20cards%20transactions%20direct_debits%20standing_orders%20offline_access&redirect_uri=https://console.truelayer.com/redirect-page&providers=uk-cs-mock%20uk-ob-all%20uk-oauth-all
        2.we are redirect to a page which gives us the authorisation token where we must give in our next api 
        3.Now the above code must be give to this api https://auth.truelayer-sandbox.com/connect/token  with body { grant_type,client_id,client_secret,redirect_uri,code}  where code the above code.
        4 if we have 200 responce we will have the access token which with it we can access all the information from our bank account 

First try to use the sandbox account to check if your implementation is working.
*if someone downloads the repo he needs to create a .env file where he must add his Client Id ,Client Secret and the Redirect Url*