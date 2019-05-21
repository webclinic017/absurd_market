"""
Author: Thomas GRANDGUILLOT
Student Number: 12904327
Date: Once upon a time.
Eamil: tgr39@uclive.ac.nz
    
This is a programm is a technical market analysis is able to analyse global
financial data on the request of the users and advise them if they should 
invest in this particular stock. It would give a quick explanation of its 
analysis and its reasoning behind whether or not it recommends the investment. 

The analysis would be supported by some graphs. The user should then be able 
to make his own judgement taking into consideration the advice of the computer,
but they should not trust blindly the code. After running the request of the 
user for a particular stock’s company, the code would be able to recommend 
a couple of other investment strategies on other stocks or derivatives.

In this project I will be using Quandl. Quandl is in my opinion my best 
option. It offers essential financial and economic data alongside some 
unique options for free.

In terms of mathematical analysis, I will remain with a few quantitative
mathematical theorem. I will allow the code to analyse the market with 
different mathematical equations to give the user the freedom to make their 
own judgement on the efficiency of the analysis, which will be purely 
technical and not a fundamental analysis. I mean to say, the code won’t do 
any accounting analysis or any equity analysis of each company. I think the 
latter contributes to a lot of mistakes even from the best financial 
analysts - the 2008 crisis or Enron Corporation for instance
"""
import datetime
import os.path
import pandas_datareader.quandl as pquandl
import pandas as pd
import numpy as np
from mpl_finance import candlestick_ohlc
from matplotlib.dates import date2num
import quandl 
import matplotlib
import matplotlib.pyplot as plt
import talib
from matplotlib.widgets import MultiCursor
import csv
import requests



def get_csv_file(url):
    """This function return a file to read from an URL prompt to the user"""

    url = 'https://s3.amazonaws.com/quandl-production-static/end_of_day_us_stocks/ticker_list.csv'
    
    downloaded_file = requests.get(url, allow_redirects=True)
    decoded_csvcontent = downloaded_file.content.decode('utf-8')
    file_read = csv.reader(decoded_csvcontent.splitlines(), delimiter=',') 
    return file_read


def csv_data_dict(file_read):
    """This function returns a dictionary of unique keys (= quandl tickers : 
    EOD/ticker) and values as tuples of business names and the update date of 
    the last trade for this ticker"""
    
    quandl_dict = {}
    
    for row in file_read:
        ticker, quandl_ticker, name, center, date = row
        quandl_dict[ticker] = (name, date)
    return quandl_dict


def detail_company(quandl_dict):
    """This function returns the detail of all tickers"""
    
    for item in quandl_dict:
        print(item, quandl_dict[item])

        
def get_name(ticker, quandl_dict):
    """This function returns the name of the business of a particular ticker"""
    
    return quandl_dict[ticker][0]


def get_date(ticker, quandl_dict):
    """This function returns the update date of trading of the business of a 
    particular ticker"""
    
    return quandl_dict[ticker][1]


#quandl_code = "EOD/AAPL"

def get_data(ticker, start_date, last_trading_date):
    """This function return the data from the Quandl platform"""
     
    #data = quandl.get( quandl_code, start_date="2016-04-01", end_date="2019-04-01", api_key='-geeNg-ha48hadKiPVx4')
    data = quandl.get( 'EOD/'+ticker, start_date=start_date, end_date=last_trading_date, api_key='-geeNg-ha48hadKiPVx4')
    data["Date"] = date2num(data.index.to_pydatetime())
    return data


def plot_candlestick(ax, data):
    """This function the OHLC candlestick graph"""
    
    ohlc_data = data[["Date", 'Adj_Open', 'Adj_High', 'Adj_Low', 'Adj_Close']].values
    candlestick_ohlc(ax, ohlc_data, width=4, colorup='darkcyan', colordown='fuchsia', alpha=0.75)

    
def plot_volume(ax, data):
    """This function plot the volumne on the same plot that OHLC"""
    
    ax.fill_between(data["Date"], 0, data['Volume'], label='Volume', color="lightcoral", alpha=0.5)

        
def plot_rsi(ax, data):
    """This funstion plot the RSI momentum indicators. 
######## RSI   -    Relative Strength Index-Overlap Studies Functions ##########
     The RSI is a price-following oscillator that ranges between 0 and 100. 
A popular method of analyzing the RSI is to look for a divergence in which 
the security is making a new high, but the RSI is failing to surpass its 
previous high. This divergence is an indication of an impending reversal. 
When the RSI then turns down and falls below its most recent trough, it is 
said to have completed a "failure swing." The failure swing is considered a 
#confirmation of the impending reversal."""
     
    rsi_indicator = talib.RSI(data['Adj_Close'], timeperiod=14)
    ax.plot(data["Date"], rsi_indicator, label='RSI', color="slategray")
    
    ax.axhline(70, color='#8f2020')
    ax.axhline(30, color='#386d13')
    ax.axhline(50, color='white', ls="dashed")
    
    ax.fill_between(data["Date"], rsi_indicator, 70, where=(rsi_indicator>=70), facecolor='#8f2020', edgecolor='#8f2020', alpha=0.5)
    ax.fill_between(data["Date"], rsi_indicator, 30, where=(rsi_indicator<=30), facecolor='#386d13', edgecolor='#386d13', alpha=0.5)     

     
def plot_roc(ax, data):
    """This function plot the ROC momentum indicators. 
######## ROC   -     Rate Of Change   -    Overlap Studies Functions ##########     
     ((price/prevPrice)-1)*100
     The Price Rate-of-Change ("ROC") indicator displays the difference between 
the current price and the price x-time periods ago. The difference can be 
displayed in either points or as a percentage. The Momentum indicator displays 
the same information, but expresses it as a ratio.
It is a well recognized phenomenon that security prices surge ahead and 
retract in a cyclical wave-like motion. This cyclical action is the result 
of the changing expectations as bulls and bears struggle to control prices.
The ROC displays the wave-like motion in an oscillator format by measuring 
the amount that prices have changed over a given time period. As prices 
increase, the ROC rises;as prices fall, the ROC falls. The greater the change 
#in prices, the greater the change in the ROC.
"""
    roc_indicator = talib.ROC(data['Adj_Close'], timeperiod=20)
    ax.plot(data["Date"], roc_indicator, label='ROC indicator', color="chartreuse")
    
    ax.axhline(-10, color='#386d13')
    ax.axhline(10, color='#8f2020')
    
    ax.fill_between(data["Date"], roc_indicator, 10, where=(roc_indicator>=10), facecolor='#8f2020', edgecolor='#8f2020', alpha=0.2)
    ax.fill_between(data["Date"], roc_indicator, -10, where=(roc_indicator<=-10), facecolor='#386d13', edgecolor='#386d13', alpha=0.2)        


def plot_ema(ax, data):
    """This function plots
######## EMA - Exponential Moving Average - Overlap Studies Functions ##########

A Moving Average is an indicator that shows the average value of a security's 
price over a period of time. When calculating a moving average, a mathematical 
analysis of the security's average value over a predetermined time period is 
made. As the security's price changes, its average price moves up or down."""
     
    ema_indicator = talib.EMA(data['Adj_Close'], timeperiod=30)
    
    ax.plot(data["Date"], ema_indicator, label='Exponential Moving Average', color="aqua")


def plot_ma(ax, data):
    """This function plots
############ MA - Moving average - Overlap Studies Functions ###################

 A Moving Average is an indicator that shows the average value of a security's
price over a period of time. When calculating a moving average, a 
mathematical analysis of the security's average value over a predetermined 
time period is made. As the security's price changes, its average price 
moves up or down.
Identifying trends is one of the key functions of moving averages, which are 
used by most traders who seek to "make the trend their friend". Moving averages
are lagging indicators, which means that they do not predict new trends, but 
confirm trends once they have been established. 

The moving average (MA) is a 
simple technical analysis tool that smooths out price data by creating a 
constantly updated average price. The average is taken over a specific period 
of time, like 10 days, 20 minutes, 30 weeks or any time period the trader 
chooses. There are advantages to using a moving average in your trading, as 
well as options on what type of moving average to use. Moving average strategies
are also popular and can be tailored to any time frame, suiting both long-term 
investors and short-term traders.

A moving average helps cut down the amount of "noise" on a price chart. Look 
at the direction of the moving average to get a basic idea of which way the 
price is moving. If it is angled up, the price is moving up (or was recently) 
overall; angled down, and the price is moving down overall; moving sideways, 
and the price is likely in a range. 

As a general guideline, if the price is above a moving average, the trend 
is up. If the price is below a moving average, the trend is down. However, 
moving averages can have different lengths (discussed shortly), so one MA may 
indicate an uptrend while another MA indicates a downtrend.

An MA with a short time frame will react much quicker to price changes than 
an MA with a long look back period.

Crossovers are one of the main moving average strategies. 
The first type is a price crossover, which is when the price crosses 
above or below a moving average to signal a potential change in trend.

Another strategy is to apply two moving averages to a chart: one longer and one 
shorter. When the shorter-term MA crosses above the longer-term MA, it's a buy 
signal, as it indicates that the trend is shifting up. This is known 
as a "golden cross."""

    ma_indicator30 = talib.MA(data['Adj_Close'], timeperiod=30, matype=0)
    ma_indicator200 = talib.MA(data['Adj_Close'], timeperiod=200, matype=0)
    
    ax.plot(data["Date"], ma_indicator30, label="Moving Average 30 days period", color="lime")
    ax.plot(data["Date"], ma_indicator200, label="Moving Average 200 days period", color="orchid")
    
    ax.fill_between(data["Date"], ma_indicator30, ma_indicator200, where=(ma_indicator30<=ma_indicator200), facecolor='r', edgecolor='r', alpha=0.2)
    ax.fill_between(data["Date"], ma_indicator30, ma_indicator200, where=(ma_indicator30>=ma_indicator200), facecolor='gold', edgecolor='gold', alpha=0.2)     


def plot_sma(ax, data):
    """This function plots
######################### Simple Moving Average ################################

A Moving Average is an indicator that shows the average value of a security's 
price over a period of time. When calculating a moving average, a mathematical
analysis of the security's average value over a predetermined time period is 
made. As the security's price changes, its average price moves up or down.
There are five popular types of moving averages:simple (also referred to as 
arithmetic), exponential, triangular, variable, and weighted. Moving averages 
can be calculated on any data series including a security's open, high, low, 
close, volume, or another indicator. A moving average of another moving 
average is also common.
The only significant difference between the various types of moving averages 
is the weight assigned to the most recent data. Simple moving averages apply 
equal weight to the prices. Exponential and weighted averages apply more 
weight to recent prices. Triangular averages apply more weight to prices in 
the middle of the time period. And variable moving averages change the 
weighting based on the volatility of prices."""

    sma_indicator30 = talib.SMA(data['Adj_Close'], timeperiod=30)
    sma_indicator200 = talib.SMA(data['Adj_Close'], timeperiod=200)
    
    ax.plot(data["Date"], sma_indicator30, label="Simple Moving Average 30 days period", color="y")
    ax.plot(data["Date"], sma_indicator200, label="Simple Moving Average 200 days period", color="orange")

     
def plot_trima(ax, data):
    """This function plots
################### TRIMA - Triangular Moving Average ##########################
"""
    trima_indicator30 = talib.TRIMA(data['Adj_Close'], timeperiod=30)
    trima_indicator200 = talib.TRIMA(data['Adj_Close'], timeperiod=200)
    
    ax.plot(data["Date"], trima_indicator30, label="Triangular Moving Average 30 days period", color="slateblue")
    ax.plot(data["Date"], trima_indicator200, label="Triangular Moving Average 200 days period", color="crimson")
    
    
def plot_macd(ax, data):
    """This function plots
############## MACD - Moving Average Convergence/Divergence ####################

The MACD ("Moving Average Convergence/Divergence") is a trend following 
momentum indicator that shows the relationship between two moving averages 
of prices. The MACD was developed by Gerald Appel, publisher of Systems and 
Forecasts.The MACD is the difference between a 26-day and 12-day exponential 
moving average. A 9-day exponential moving average, called the "signal" 
(or "trigger") line is plotted on top of the MACD to show buy/sell 
opportunities. (Appel specifies exponential moving averages as percentages. 
Thus, he refers to these three moving averages as 7.5%, 15%, and 20% 
respectively.) The MACD proves most effective in wide-swinging trading 
markets. There are three popular ways to use the MACD:crossovers, 
overbought/oversold conditions, and divergences. The basic MACD trading 
rule is to sell when the MACD falls below its signal line. Similarly, 
a buy signal occurs when the MACD rises above its signal line. It is also 
popular to buy/sell when the MACD goes above/below zero."""


    macd, macdsignal, macdhist = talib.MACD(data['Adj_Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    
    ax.plot(data["Date"], macd, label="macd", color="lime")
    ax.plot(data["Date"], macdsignal, label="macdsignal", color="crimson")
    ax.plot(data["Date"], macdhist, label="macdhist", color="hotpink")
    
    ax.fill_between(data["Date"], macd, macdhist, where=(macd>=macdhist), facecolor='darkgray', edgecolor='darkgray', alpha=0.2)
    
    ax.axhline(0, color='white', ls="dashed")
    

def plot_bollinger(ax, data):
    """This function plots
####################### BBANDS - Bollinger Bands ###############################

Bollinger Bands are usually displayed on top of security prices, but they 
can be displayed on an indicator. These comments refer to bands displayed on prices.
As with moving average envelopes, the basic interpretation of Bollinger Bands 
is that prices tend to stay within the upper- and lower-band. The distinctive
characteristic of Bollinger Bands is that the spacing between the bands varies
based on the volatility of the prices. During periods of extreme price 
changes (i.e., high volatility), the bands widen to become more forgiving.
During periods of stagnant pricing (i.e., low volatility), the bands narrow
to contain prices."""

    upperband, middleband, lowerband = talib.BBANDS(data['Adj_Close'], timeperiod=5, nbdevup=2, nbdevdn=2, matype=0)
    
    ax.plot(data["Date"], upperband, label="upperband", color="gold")
    ax.plot(data["Date"], middleband, label="middleband", color="crimson")
    ax.plot(data["Date"], lowerband, label="lowerband", color="b")
    
    ax.fill_between(data["Date"], upperband, lowerband, where=(upperband>=lowerband), facecolor='gainsboro', edgecolor='gainsboro', alpha=0.2)


def plot_standarddev(ax, data):
    """This function plots
######################## STDDEV - Standard Deviation ###########################   

Standard Deviation is a statistical measure of volatility. Standard Deviation 
is typically used as a component of other indicators, rather than as a 
stand-alone indicator. For example, Bollinger Bands are calculated by adding 
a security's Standard Deviation to a moving average.
High Standard Deviation values occur when the data item being analyzed 
(e.g., prices or an indicator) is changing dramatically. Similarly, low 
Standard Deviation values occur when prices are stable."""

    stdev = talib.STDDEV(data['Adj_Close'], timeperiod=5, nbdev=1)
    
    ax.plot(data["Date"], stdev, label="Standard Deviation", color="peru")


def plot_timeseries(ax, data):
    """This function plots
######################## TIME SERIES FORCAST ###################################

The Time Series Forecast indicator displays the statistical trend of a 
security's price over a specified time period. The trend is based on linear
regression analysis. Rather than plotting a straight linear regression 
trendline, the Time Series Forecast plots the last point of multiple linear 
regression trendlines. The resulting Time Series Forecast indicator is 
sometimes referred to as the "moving linear regression" indicator or 
the "regression oscillator." The interpretation of a Time Series Forecast 
is identical to a moving average. However, the Time Series Forecast
indicator has two advantages over classic moving averages. Unlike a moving
average, a Time Series Forecast does not exhibit as much delay when 
adjusting to price changes. Since the indicator is "fitting" itself 
to the data rather than averaging them, the Time Series Forecast is more 
responsive to price changes."""

    time_series_ind = talib.TSF(data['Adj_Close'], timeperiod=14)
    
    ax.plot(data["Date"], time_series_ind, label="TIME SERIES FORCAST", color="sandybrown")


def plot_beta(ax, data):
    """This function plots
################################## Beta ########################################
In finance, the beta (β or beta coefficient) of an investment indicates
whether the investment is more or less volatile than the market as a whole."""

    beta = talib.BETA(data['High'], data['Low'], timeperiod=5)
    
    ax.plot(data["Date"], beta, label="Beta", color="steelblue")

     
def plot_kaufman(ax, data):
    """This function plots
################ KAMA - Kaufman Adaptive Moving Average ########################

Kaufman's Adaptive Moving Average (KAMA) is an intelligent moving average 
that was developed by Perry Kaufman. The powerful trend-following indicator 
is based on the Exponential Moving Average (EMA) and is responsive to both 
trend and volatility. It closely follows price when noise is low and smooths 
out the noise when price fluctuates. Like all moving averages, the KAMA can 
be used to visualize the trend. Price crossing it indicates a directional 
change. Price can also bounce off the KAMA, which can act as dynamic support 
and resistance. It is often used in combination with other signals 
and analysis techniques."""


    kaufman_ind = talib.KAMA(data['Adj_Close'], timeperiod=30)
    
    ax.plot(data["Date"], kaufman_ind, label="Kaufman Adaptive Moving Average", color="coral")
    
    ema_indicator = talib.EMA(data['Adj_Close'], timeperiod=30)
    
    ax.plot(data["Date"], ema_indicator, label='Exponential Moving Average', color="aqua")
    

def plot_stoch(ax, data):
    """This function plots
########################### STOCH - Stochastic #################################
The Stochastic Oscillator compares where a security's price closed relative 
to its price range over a given time period. The Stochastic Oscillator is 
displayed as two lines. The main line is called "%K." The second line, 
called "%D," is a moving average of %K. The %K line is usually displayed 
as a solid line and the %D line is usually displayed as a dotted line.
There are several ways to interpret a Stochastic Oscillator. Three popular 
methods include: Buy when the Oscillator (either %K or %D) falls below a 
specific level (e.g., 20) and then rises above that level. Sell when the 
Oscillator rises above a specific level (e.g., 80) and then falls 
below that level. Buy when the %K line rises above the %D line and 
sell when the %K line falls below the %D line. Look for divergences. 
For example, where prices are making a series of new highs and the 
Stochastic Oscillator is failing to surpass its previous highs."""

    slowk, slowd = talib.STOCH(data['Adj_High'], data['Adj_Low'], data['Adj_Close'], fastk_period=5, slowk_period=3, slowk_matype=0, slowd_period=3, slowd_matype=0)
    
    ax.plot(data["Date"], slowk, label="Stochastic slowk", color="slateblue")
    ax.plot(data["Date"], slowd, label="Stochastic slowd", color="crimson")
    
    ax.axhline(80, color='lightpink')
    ax.axhline(20, color='greenyellow')     
    ax.axhline(50, color='white', ls = "dashed")
    
    ax.fill_between(data["Date"], slowk, slowd, where=(slowk>=slowd), facecolor='goldenrod', edgecolor='goldenrod', alpha=0.2)
    ax.fill_between(data["Date"], slowk, slowd, where=(slowd>=slowk), facecolor='lavenderblush', edgecolor='lavenderblush', alpha=0.2)
    
    ax.fill_between(data["Date"], slowk, 80, where=(slowk>=80), facecolor='#8f2020', edgecolor='#8f2020', alpha=0.2)
    ax.fill_between(data["Date"], slowk, 20, where=(slowk<=20), facecolor='#386d13', edgecolor='#386d13', alpha=0.2) 
    ax.fill_between(data["Date"], slowd, 80, where=(slowd>=80), facecolor='#8f2020', edgecolor='#8f2020', alpha=0.2)
    ax.fill_between(data["Date"], slowd, 20, where=(slowd<=20), facecolor='#386d13', edgecolor='#386d13', alpha=0.2)      
    

#################### Pattern Recognition Functions #############################


def plot_Doji(data):
    """ This function signals Doji pattern.
############################## CDLDOJI - Doji ##################################
explanation:"""
     
    doji_pattern = talib.CDLDOJI(data['Open'], data['High'], 
                                 data['Low'], data['Close'])
    return np.flatnonzero(doji_pattern)   

    
def plot_Hammer(data):
    """This function signals Hammer pattern.
############################ CDLHAMMER - Hammer ################################
explanation:"""

    hammer_pattern = talib.CDLHAMMER(data['Open'], data['High'], 
                                     data['Low'], data['Close'])
    return np.flatnonzero(hammer_pattern)


def plot_Hanging(data):
    """This function signals Hanging Man pattern.
######################## CDLHANGINGMAN - Hanging Man ###########################
explanation:"""

    hanging_pattern = talib.CDLHANGINGMAN(data['Open'], data['High'], 
                                          data['Low'], data['Close'])
    return np.flatnonzero(hanging_pattern)
    

def plot_Morning_Star(data):
    """This function signals Morning Star pattern.
################### CDLMORNINGSTAR - Morning Star ##############################
explanation:"""

    morningstar_pattern = talib.CDLMORNINGSTAR(data['Open'], data['High'], 
                                               data['Low'], data['Close'], 
                                               penetration=0)
    return np.flatnonzero(morningstar_pattern)
    

def plot_Evening_Star(data):
    """This function signals Evening Star pattern.
###################### CDLEVENINGSTAR - Evening Star ###########################
explanation:"""

    eveningstar_pattern = talib.CDLEVENINGSTAR(data['Open'], data['High'], 
                                               data['Low'], data['Close'], 
                                               penetration=0)
    return np.flatnonzero(eveningstar_pattern)
    

def plot_Dark_Cloud_Cover(data):
    """This function signals Dark Cloud Cover pattern.
################### CDLDARKCLOUDCOVER - Dark Cloud Cover #######################
explanation:"""

    darkcloud_pattern = talib.CDLDARKCLOUDCOVER(data['Open'], data['High'], 
                                                data['Low'], data['Close'], 
                                                penetration=0)
    return np.flatnonzero(darkcloud_pattern)
    

def plot_Harami(data):
    """This function signals Harami pattern.
####################### CDLHARAMI - Harami Pattern #############################
explanation:"""

    harami_pattern = talib.CDLHARAMI(data['Open'], data['High'], 
                                     data['Low'], data['Close'])
    return np.flatnonzero(harami_pattern)
    

def plot_Engulfing(data):
    """This function signals Engulfing pattern.
###################### CDLENGULFING - Engulfing Pattern ########################
explanation:"""

    engulfing_pattern = talib.CDLENGULFING(data['Open'], data['High'], 
                                           data['Low'], data['Close'])
    return np.flatnonzero(engulfing_pattern)
    

def plot_Piercing(data):
    """This function signals Piercing pattern.
################### CDLPIERCING - Piercing Pattern #############################
explanation:"""

    piercing_pattern = talib.CDLPIERCING(data['Open'], data['High'], 
                                         data['Low'], data['Close'])
    return np.flatnonzero(piercing_pattern)

     
################################################################################

def set_spine_color(ax):
    """This function sets the color of the spine of subplot"""
     
    ax.spines['bottom'].set_color("c")
    ax.spines['top'].set_color("c")
    ax.spines['left'].set_color("c")
    ax.spines['right'].set_color("c")  


def set_tick_color(ax):
    """This function set the color of the tick parametres"""
    
    ax.tick_params(axis='y', colors='w')
    ax.tick_params(axis='x', colors='w')     


def build_subplot(shape, loc, rowspan, colspan, facecolor='#333333', dates=None):
    """This function set each subplot"""
    
    ax = plt.subplot2grid(shape, loc, rowspan=rowspan, colspan=colspan, 
                          facecolor=facecolor)
    ax.xaxis.set_major_formatter(matplotlib.dates.DateFormatter('%Y-%m-%d'))
    if dates is not None:
        ax.set_xlim(dates[0], dates[-1])
    set_spine_color(ax)
    set_tick_color(ax)
    
    return ax


def volume_subplot(axOn, data):
    """This function set the subplot for the volume on ax1"""
    
    ax = axOn.twinx()
    ax.axes.yaxis.set_ticklabels([])
    ax.grid(False)
    ax.set_ylim(0, 2*data["Volume"].max())
    set_spine_color(ax)
    set_tick_color(ax)
    
    return ax


def price_annotation(ax, data):
    """This function allows to annotate the last price on the side of the subplot"""
    
    bbox_props = dict(boxstyle='round', facecolor='w', edgecolor= 'k', lw=1)
    ax.annotate(str(data['Close'][-1]), (data['Date'][-1], data['Close'][-1]), 
                xytext=(data['Date'][-1]+30, data['Close'][-1]), bbox=bbox_props)

    
def date_last_subplot(ax0, ax1, ax2, ax3):
    """This function set the date axis only on the last axis"""
    
    plt.setp(ax0.get_xticklabels(), visible=False)
    plt.setp(ax1.get_xticklabels(), visible=False)
    plt.setp(ax2.get_xticklabels(), visible=False)
    plt.setp(ax3.get_xticklabels(), visible=False)     
    

def build_plots(data):
    """This function sets the Frame of the plotting"""
    dates = data['Date']
    fig = plt.figure(facecolor = '#00284d')       #'#3D3C3C'
    fig.suptitle('Technical analysis of the company', fontsize=16, color='#999900')
    ax0 = build_subplot((39, 6), (0, 0), 6, 6, facecolor='#00284d', dates=dates) #333333
    ax0.set_ylabel('Risk', color='#999900')
    ax1 = build_subplot((39, 6), (6, 0), 15, 6, facecolor='#00284d', dates=dates)
    ax1.set_ylabel('Prices-Volume\nMomentum-pattern', color='#999900')
    ax2 = build_subplot((39, 6), (21, 0), 6, 6, facecolor='#00284d', dates=dates)
    ax3 = build_subplot((39, 6), (27, 0), 6, 6, facecolor='#00284d', dates=dates)
    ax3.set_ylabel('Momentum', color='#999900')
    ax4 = build_subplot((39, 6), (33, 0), 6, 6, facecolor='#00284d', dates=dates)
    axVol = volume_subplot(ax1, data)
    ax1.grid(True, linestyle=':', color='lightgrey')
    
    #put the last price on the side of the plot
    price_annotation(ax1, data)
    
    # Getting the date only on the last subplot. 
    date_last_subplot(ax0, ax1, ax2, ax3)
    
    # showing the date on the side  
    for label in ax4.xaxis.get_ticklabels():
        label.set_rotation(45)     
    
    plt.subplots_adjust(left=.09, bottom=.24, right=.94, top=.9, wspace=.20, hspace=0)
    
    return fig, ax0, ax1, ax2, ax3, ax4, axVol
#

def plot_nothing(*args):
    """ empty function to do nothing if we are asked to plot a functin with no name"""
    pass

plot_functions = {
    'candlestick': plot_candlestick,
    'volume': plot_volume,
    'relative strength index': plot_rsi,
    'rate of change': plot_roc,
    'exponential moving average': plot_ema,
    'moving average': plot_ma,
    'simple moving average': plot_sma,
    'triangular moving average': plot_trima,
    'moving average convergence/divergence': plot_macd,
    'bollinger indicator':  plot_bollinger,
    'time series forcast': plot_timeseries,
    'kaufman adaptive moving average': plot_kaufman,
    'stochastic': plot_stoch,
    'standard deviation': plot_standarddev,
    'beta': plot_beta,
    'doji pattern': plot_Doji,
    'hammer pattern': plot_Hammer,
    'hanging man pattern': plot_Hanging,
    'morning star pattern': plot_Morning_Star,
    'evening star pattern': plot_Evening_Star,
    'dark cloud cover pattern': plot_Dark_Cloud_Cover,
    'harami pattern': plot_Harami,
    'engulfing pattern': plot_Engulfing,
    'piercing pattern': plot_Piercing,
    '': plot_nothing
}  

def plot_ticker(quandl_dict, ticker, start_date, risk, momentum, pattern, volume, bottom_indicators):
    risk = risk.lower()
    momentum = momentum.lower()
    pattern = pattern.lower()
    volume = volume.lower()
    bottom_indicators = [indicator.lower() for indicator in bottom_indicators]

    if start_date is None:
        start_date = "2000-01-01"
    
    last_trading_date = get_date(ticker, quandl_dict)
    data = get_data(ticker, start_date, last_trading_date)
    fig, ax0, ax1, ax2, ax3, ax4, axVol = build_plots(data)
    
    plot_functions[risk](ax0, data)
    plot_candlestick(ax1, data)
    
    # momentum
    plot_functions[momentum](ax1, data)
    
    # volume
    plot_functions[volume](axVol, data)
    
    # combos...
    plot_functions[bottom_indicators[0]](ax2, data)
    plot_functions[bottom_indicators[1]](ax3, data)
    plot_functions[bottom_indicators[2]](ax4, data)

    
    # pattern
    nonzero = plot_functions[pattern](data)
    if nonzero is not None:
        ax1.scatter(data['Date'][nonzero], data['Adj_High'][nonzero], s=50, 
                    c='none', edgecolors='#cc9900', marker='o')
    
    title = '{}: {} - {}'.format(quandl_dict[ticker][0], start_date, last_trading_date)
    fig.canvas.set_window_title(title) 
    multi = MultiCursor(fig.canvas, (ax0, ax1, ax2, ax3, ax4, axVol), useblit=True,                    horizOn=False, vertOn=True, color='wheat', lw=1)
    plt.show()
    
    
def close_plot():
    plt.close()

