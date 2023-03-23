STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
TWILIO_AUTH_TOKEN = "c0e016add3f346104faedcaabbd45484"
TWILIO_ACCOUNT_SID = "AC37934a31a4a19870edf7eb8322062f1a"

STOCK_API_KEY = "8WPQRNQ71BXNOBCP"
import os
from twilio.rest import Client
import requests

url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={STOCK_NAME}&apikey={STOCK_API_KEY}]'
r = requests.get(url)
data = r.json()


    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
price_stock_data = data["Time Series (Daily)"]['2022-10-18']
print(price_stock_data)

close_price_today = price_stock_data['4. close']
print(close_price_today)

#TODO 2. - Get the day before yesterday's closing stock price
close_price_yesterday = price_stock_data['1. open']
print(close_price_yesterday)

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp
diffrence_in_price = float(close_price_today) - float(close_price_yesterday)
print(diffrence_in_price)
#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
diffrence_in_price_in_percent = diffrence_in_price / (float(close_price_today)/ 100)
print(f"{abs(diffrence_in_price_in_percent)} %")
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
if abs(diffrence_in_price_in_percent) > 1:
    news_data = requests.get("https://newsapi.org/v2/everything?q=tesla&from=2022-09-19&sortBy=publishedAt&apiKey=74abb4bba2b14319bb05ac98b50615cc").json()
    news_articles = news_data['articles'][:3]
    print(news_articles)


    news_title = news_articles[0]['title']

    news_disctiption = news_articles[0]['description']
    print(news_title)
    print(news_disctiption)

    ## STEP 2: https://newsapi.org/
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.


#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


## STEP 3: Use twilio.com/docs/sms/quickstart/python
#to send a separate message with each article's title and description to your phone number.

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio.

account_sid = os.environ["AC37934a31a4a19870edf7eb8322062f1a"]
auth_token = os.environ["c0e016add3f346104faedcaabbd45484"]
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+15017122661',
                     to='+6591060836'
                 )

print(message.sid)

#Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

