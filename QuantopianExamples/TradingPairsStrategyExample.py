# TradingPairsStrategyExample.py

# This is an example program for a class in order
# to learn how to write code at quantopian.com.
# DO NOT USE THIS CODE FOR REAL TRADING!  IT IS NOT
# A GOOD STRATEGY! 

# This program trades correlated pairs (stocks that
# general move together to a high degree) when their
# correlation starts to drift.  The program assumes
# that the correlation will correct itself, and that
# the 2 stocks will go back to their matching movements.
# We their movement is out of sync, we short the over performing
# one, and buy the under performing one on the assumption
# that they will get back to lock step for their movement.

# One of the reasons, that we are choosing 2 stocks, is
# that we are trying to find how the "industry" is performing
# as a whole.  I guess you can use > 2 stocks to get a better
# picture of the airlines industry.  M/b a airlines index.

import numpy


def initialize(context):
    # Run when the program starts up.
    
    # Stocks to trade:
    context.aa = sid(45971)    # American Airlines
    context.ual = sid(28051)   # United Airlines
    
    context.long_on_spread = False
    context.short_on_spread = False
    
    # For this example, we are arbitralily running this
    # 60 minutes b/4 market closed.  In real life, I would
    # have picked 30-60 minutes after market open.
    schedule_function(check_pairs, date_rules.every_day(),
                      time_rules.market_close(minutes=60))

def check_pairs(context, data):
    
    # This function will be scheduled.  It finds when the correlation
    # has drifted, and shorts the overperformer, and buys the underperformer.
    # When the correlation gets back in normal, the function closes
    # the positions.
    
    # Looks like we are hard coding which stocks we are using into this
    # function.  I am not a fan of this.
    aa = context.aa
    ual = context.ual
    
    # Get the last 30 days of closing price info for our 2 stocks:
    # "1d" = 1 day, aka daily data.
    prices_DF = data.history([aa, ual], "price", 30, "1d")
    
    # Not sure why we need this.  I guess I'll learn more later.
    yesterdays_close_prices_list = prices_DF.iloc[-1:]
    
    # Get a list of the spread for the last 30 days,
    # and then get the average value of that list.
    # So, this is 1 data point.
    Spread_Ave_30 = numpy.mean(prices_DF[aa] - prices_DF[ual])
    
    # Get a list of the spread for the last 30 days,
    # and find the standard deviation for that list.
    # So, this is 1 data point.
    Std_Dev_Ave_30 = numpy.std(prices_DF[aa] - prices_DF[ual])
    
    print(Std_Dev_Ave_30)
    
    # Average of the 2 prices from yesterday's close:
    ave_of_closing_prices = numpy.mean(yesterdays_close_prices_list[aa] - yesterdays_close_prices_list[ual])
    
    # Normalize the deviation.
    # Find the difference b/t yesterday's spread and the average spread for the past 30 days.
    # And, then normalize it by divided by the std. dev. based off of the last 30 days.
    z_score = (ave_of_closing_prices - Spread_Ave_30)/Std_Dev_Ave_30
    
    # The z_score is a measure of how well the stocks are moving together.
    # Close to 0 means in sync.
    
    # If we have positions open, and our z_score indicates that the
    # stocks are moving back together, then close the open orders b/c
    # our advantage is now gone for the time being.
    if ( abs(z_score) < 0.1 ) and ( context.long_on_spread or context.short_on_spread ):
        # Close the orders if any are open:
        order_target_percent(aa, 0)
        order_target_percent(ual, 0)
        
        # Let the program know we don't have any open positions:
        context.long_on_spread = False
        context.short_on_spread = False
        
    # spread = AA - UAL
    # So, if z_score gets excessively positive, then AA is outperforming its average.
    # So, short it on the assumption it will return to its normal value.
    # Short AA: b/c it's outperforming
    # Buy UAL: b/c it may be underperforming, or will just catch up to AA.
    # Open a trade if we are not already in one:
    
    # I would do this differently.  I would think that you would, first, have a
    # test to close open positions if you are currently long, and the
    # z_score goes back to < 1.0.
    
    if z_score > 1.0 and not context.short_on_spread:
        
        # 50% short AA.  50% buy United.
        order_target_percent(aa, -0.5)
        order_target_percent(ual, 0.5)
        
        # Make a note that we shorted AA:
        context.short_on_spread = True
        context.long_on_spread = False
        
    # Are conditions right to go long w/ AA, and short United
    # Is United outperforming its average?
    if z_score < -1.0 and not context.long_on_spread:
        order_target_percent(aa, 0.5)
        order_target_percent(ual, -0.5)
        
        # Make a note that we bought AA:
        context.short_on_spread = False
        context.long_on_spread = True
    
    # Log the z score:
    record(z_score = z_score)
    
    
