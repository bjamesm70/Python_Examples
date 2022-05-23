# audio_alerts.py

# Creates audio alerts when our
# cryptos hit a predefined price.

# The check runs in a loop that sleeps for x seconds
# between run.  Ctrl-c to exit out of the loop.

# The list is held in a CSV that we read in.
# Once the alert is triggered, the crypto
# is added to an ignor list.

# Notes:
# 1) Anything read in from a csv file is
# considered a string.  You need to convert
# to a number as needed.

# -Jim

###########
# IMPORTS #
###########

import os  # Used to create the audio alert.
import csv  # For editing CSV files.
import sys  # Used to create system sounds like a bell.
# import json
import time  # Used to set timer so that you can check the price every 5 minutes.
import requests  # For submitted our URL.
from datetime import datetime  # Used to get, and format dates.
from Variables import *  # Our config file.
#from Variables_2 import *  # Our config file.

#############
# MAIN CODE #
#############

print("ALERTS TRACKING ...")
print()

# Once we send out an alert for a specific
# crypto, we don't want to do it again.
already_alerted_cryptos_list = []

# Open the list of crypto to monitor:
input_FH = open("./my_alerts.csv", "r")

# We run this script every x seconds,
# and only quit when we control-c out
# of it.
while True:

    # A FH is a pointer to the current read/write location
    # in the file.  In the code below, we work through the
    # whole file.  So, we need to repoint to the start of
    # our file to re-read in the list for processing.
    input_FH.seek(0)

    # The file is a CVS.  Use the "csv" library to break
    # each line into individual elements.
    csv_input_FH = csv.reader(input_FH)

    # Process 1 alert at a time:
    # Note: anything read in is read in as a string.
    # Convert it to numbers as needed.
    for crypto, alert_level in csv_input_FH:

        # Converting this to a number as the
        # cvs reader reads everything in as string.
        alert_level = float(alert_level)

        # print(crypto, alert_level)

        # Coin base returns data in uppercase.
        # So, we need to be consistent with them:
        symbol = crypto.upper()

        # Create the API call:
        # "quote_url" is from "Variables.py".
        # "?convert=" --> Our local currency.
        api_call = quote_url + "?convert={}".format(local_currency) + "&symbol={}".format(symbol)

        # Run the request:
        return_data = requests.get(api_call, headers=headers_dict)

        # Change it to Json format:
        json_return_data = return_data.json()

        # print(json.dumps(json_return_data, sort_keys=True, indent=2))

        # The return data has 2 sections:
        # "data" with all the info about the crypto.
        # "status": Info about how the request went.
        # "symbol" below is the variable defined above.
        currency_data = json_return_data["data"][symbol]

        crypto_name = currency_data["name"]
        price = currency_data["quote"][local_currency]["price"]

        if (price >= alert_level) and (symbol not in already_alerted_cryptos_list):
            # "say" is the command to tell the computer to speak to you.
            os.system("say ALERT ALERT ALERT")
            os.system("say {} hit {}".format(crypto_name, alert_level))

            # In case the system is buffering output commands,
            # force them to be run by flushing the buffer.
            sys.stdout.flush()

            # Print the alert to the terminal w/ a time stamp.
            now = datetime.now()
            current_time = now.strftime("%H:%M %p")  # HH:MM AM/PM
            print("{}: {} hit {}!".format(current_time, crypto_name, alert_level))

            # Add the crypto to our list of already hit targets so that
            # we don't alert on it every time the script wakes up from sleep.
            already_alerted_cryptos_list.append(symbol)

    # If you are here, then you are all done with the
    # for loop for this round.
    # Sleep for a bit.
    print("\n")
    print("Sleeping to {} seconds.".format(time_to_sleep_in_seconds))
    time.sleep(time_to_sleep_in_seconds)
