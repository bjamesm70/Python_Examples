# Keep your variables out of your code.

# To get an api key, go to: https://coinmarketcap.com/api/
# and register.

api_key = "<You'll need to register for your own free key>"

# The course teacher says we need to create this
# dictionary file.
headers_dict = {"X-CMC_PRO_API_KEY": api_key}

# currency for your country:
local_currency = "USD"
local_currency_symbol = "$"

# Coin Market Cap's API website that we need to connect to:
coin_market_cap_base_url = "https://pro-api.coinmarketcap.com"

quote_url = coin_market_cap_base_url + "/v1/cryptocurrency/quotes/latest"

# Url to request that the data comes back with your local currency
quote_url_with_conversion = quote_url + "?convert=" + local_currency

# Time to sleep between runs (in seconds):
time_to_sleep_in_seconds = 10
