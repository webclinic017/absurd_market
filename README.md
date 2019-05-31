# absurd_market
Market prediction by technical analysis using over 15 indictors (patterns recognition &amp; momentum indicators). Using HTTP request to obtain 30 years of financial trading data of S&amp;P 500. Implementing a GUI to facilitate the analysis.  






The SisypheQuant Project is a market prediction by technical analysis using over 23 indictors (patterns recognition & momentum indicators). It uses an HTTP request to obtain financial trading data of S&P 500 since 1996. Every time the user makes a request, 8000+ financial data are requested from Quandl. It is implemented with a GUI to facilitate analysis of different data from different firms simultaneously. Behind the scenes the program can run a code that lets the user know which shares they should potentially buy or sell without the need to look at the graph. 

In terms of the analysis, the user is able to look at 5 graphs (subplots). Each single plot gives different information. There is no equity valuation being performed, it is purely technical. The program offers advice to buy or sell, but the user should make his own judgement freely. I don’t expect them to blindly trust the code. There are many studies and opinions about whether the market is rational or not. The current wave of intellectual and economist thoughts certified the rationality of the market: the market is held by an invisible hand that balances it out. If the general equilibrium is broken by the market, it will balance everything itself to get back to its state of equilibrium. Technical analysis takes a different approach, where overall we can argue that over a short period of time the market is not rational because human behaviours (predominantly fear) are irrational. Another point is that technical analysis offers all the information available about the market because the prices cannot lie and this logic can be extant in the future. This is the reason why an equity valuation is not essential in our case. To support my argument I mention the anecdotes surrounding Enron, Metallgesellshaft or Barings. All of these firms were capable of modifying their books and lied to their shareholders.

In this project I use the platform Quandl. Quandl is in my opinion my best option. It offers essential financial and economic data alongside some unique options for free. However for reasons that I will describe later I had to subscribe and pay a student monthly fee. In this project, getting the right data from the right platform was probably one of the biggest challenges I encountered. There are many financial platforms and API I could have used but they are firstly expensive and not frequently updated. GOOGLE and Yahoo could have been a good option. However Yahoo changed their API which made it difficult to download the data and the data are not reliable at all. The API with GOOGLE wasn’t working for no apparent reason. Therefore I went with Quandl. They offer different API. I went first with WIKI but this API has stopped updating their data since 2016. My next best shot was the EOD API still from Quandl. When I started using this EOD, they were offering a third of the firms data from 1996 to today for free. I tried to negotiate for this project if I could get more firms for free just for this project because I was a student, since you never know if a company may go the extra mile to earn the loyalty of a customer. However I got a different outcome. They probably realised they were being quite generous compared to the competition so they changed the availability of their data. I couldn’t access data past 2017. I spent days figuring out the problem. I then subscribed to make sure my code was working for the marking. 
Updated daily, this data feed offers end of day prices, dividends, adjustments and splits for US publicly traded stocks with history to 1996. Prices are provided both adjusted and unadjusted. It covers all stocks with primary listing on NASDAQ, AMEX, NYSE and ARCA. Every time-series in the EOD stock data feed has a Quandl code in the format EOD/{TICKER}. For instance to get Apple Inc. time-series the Quandl code will be EOD/AAPL. Quandl offer on their website an updated document of all the tickers, name of the firms and the last trading date. It is in this way that I can get an update of the tickers and name. I use this file to get the exact last trading date to update the graph. It means that the graph of tomorrow will have and extra day compared to today. 

In terms of mathematical analysis, I used 22 functions from the library TA-Lib. TA-Lib is widely used by trading software developers requiring to perform technical analysis of financial market data. 	It includes 150+ indicators such as ADX, MACD, RSI, Stochastic, Bollinger Bands, etc… and candlestick pattern recognition. 
Momentum indicators are tools to get a better understanding of the speed or rate at which the price of a security changes. It is better to use them with other indicators because they only identify the timeframe in which the price change is occurring. Momentum indicators show the movement of price over time and how strong those movements are regardless of the direction the price moves, up, or down. Once a direction has been determined, momentum indicators are valuable because they indicate the strength of price movement trends and when they are coming to an end.
A candlestick pattern is a movement in prices shown graphically on a candlestick chart that can predict a particular market movement according to the shape of the candle. The recognition of the pattern is subjective. There are 42 recognised patterns but I will be using 9 of them in my program. Candles are coloured accordingly to the direction of price movement: when the open rate is higher than the closing rate, the candlestick is magenta bodied.  When the candles are blue bodied, it means the closing rate exceeds the opening rate. 
The user interface is very easy to use. I built the GUI with Tkinter. First, the users choose the range of time they want to analyse the data from today. For instance here, the date is 1 year from today. Then they press ‘Refresh Ticker’ to get all tickers of the firms.  They can choose if they want to analyse the risk (standard deviation to Beta), meaning the volatility of the market. They can plot the volume traded shares. Then on the left hand-side they choose between seven momentum indicators to plot on the candlestick chart. On the right-hand side they choose between nine pattern recognitions to be shown by a golden circle on the candlestick chart. For the last three subplots they choose to plot between four momentum indicators. To visualise the graph they have to search for the ticker they are interested in and click ‘Plot’. If the user does not choose any range of date the program will automatically plot the data from 2000 to today. 

Here is an example of a graph from the technical analysis of a firm:
The first subplot shows the measure of the volatility of the share being analysed. The second subplot is the main plot showing the candlestick prices chart. The pale red colour is the plot of the volume of shares traded. The y-axis scale of the volume was modified to fit the main subplot. The Golden circles represent the pattern indicators that the user selected. The green and purple lines are in this case the moving average, therefore it represents the momentum indicator that the user selected. The purple line stops after a few months. This is because some momentum functions take different time ranges. The purple line analyses the data from the previous 200 days but the user wanted to analyse for 365 days.  The third, fourth and fifth subplots are the momentum indicators selected with the combobox. There are some reference lines in red, green or white. They have different meanings. For example for the fourth subplot, when the line is above the red line means the share is overbought.  Under the green line means it is undersold. We can note that there are different colours between two lines where certain lines cross each other. This allows a quicker analysis to understand if there is a tendency for the price to go up or down. 

Regarding the design of the program. I divided the program into three different files: 
The HTTP request
GUI
The plotting. 

I believe it is a good way to design it because it appeared to be very useful for troubleshooting when my code wasn’t working, and I could develop each part at my own learning pace. For instance in COSC 121, we didn’t cover GUI until week 11. Moreover each code can be run by itself and produce a certain outcome. For exemple when the improved_project.py runs by itself it goes though all the firms one by one and lets the user know if the should buy or sell this particular share, or if nothing can be said. Running the HTTP request file by itself will ask the user for a ticker and prints the last trading date and the name of the company. 
I used a procedural programming and not an object-orientated programming. The only reason for that is that I have just learnt the object-orientated programming in week 10 and I thought I would not have the time to recode everything by the due date in object-orientated programming. I decided  to stick with the procedural programming. It is obvious that by using procedural programming that I had to use global variables to built my GUI. It is not a good design point to use global variables but I tried to use the fewest possible. Overall I only had to use 3 global variables for the GUI code. 
In terms of functions I think the code is clearly readable because every time the code crashed I could locate the issue quickly in the different functions. All the variables and functions have  different names which give indicate their purpose/function. 

As an extension, the changes that could be made are as follows:

Write the program as an object-orientated language so as to not have any global variables.
Write price predictions with the Monte-Carlo model
Write price predictions with the Black Scholes model
Write quantum models. 
Implementing a GUI for the part of the code that tells which share to buy or sell to have a more efficient way to analyse it graphically. 
Improve the GUI. I noted the the button ‘Plot’ and ’Refresh’ do not change colour the first time it is used but it changes when the user looks for a second firm. 
The multi cursor is not working once I implemented the GUI. It would be good to find a way to make it work to be able to see the time line between the subplots. 

Other innovative ideas: 

Use unsupervised statistical learning methods to predict the market. 
Use machine learning algorithms to predict the prices and find positive correlations between the patterns and market.
Write a complementary code with Q# python to use quantum computers to create some complex quantum models and predictions.

I would like to note that I found some problems with the Quandl code. The function get() in the quandl library for sourcing the firms data do not work when the ticker of the business has full-stops, for exemple ABR.P.A, ABR.P.B,  ABR.P.C. I had to write a line of code to ignore this situation. Another problem I found is that there are a couple of tickers starting with ’S’ that don’t seem to be correct.

Overall I think my program is practical, user friendly and works well. It is useful for personal interest. I have been using the program during a trading competition to help me to predict the market trends and make some decisions on which shares to buy. I have a return on investment of 9% so far.



This section is just an appendix with information explaining how to read the graphs in my program. It could be helpful if you are interested in understanding how to predict the market and make decisions regarding the trend of the graph. Because it is an extra document that doesn’t need to be examinable I thought I would take the definition directly from experts. The information for these have been taken directly from https://www.fxstreet.com and L'art du trading by Thami Kabbaj.
Appendix

Momentum indicators:

RSI - Relative Strength Index
 The RSI is a price-following oscillator that ranges between 0 and 100. RSI acts as a metric for price changes and the speed at which they change. Any rising RSI values above 50 signal positive, uptrend momentum. If the RSI hits 70 or above, it’s often an indication of overbought conditions. Conversely, RSI readings that decrease below 50 show negative, downtrend momentum. If RSI readings are below 30, it is an indication of possible oversold conditions.

ROC - Rate Of Change: 
     ((price/prevPrice)-1)*100
The Price Rate-of-Change ("ROC") indicator displays the difference between the current price and the price x-time periods ago. The ROC displays the wave-like motion in an oscillator format by measuring the amount that prices have changed over a given time period. As prices increase, the ROC rises and as prices fall, the ROC falls. The greater the change in prices, the greater the change in the ROC.

MA - Moving average
 A Moving Average is an indicator that shows the average value of a security’s price over a period of time. As the security's price changes, its average price moves up or down. Identifying trends is one of the key functions of moving averages. Moving averages are lagging indicators, which means that they do not predict new trends, but confirm trends once they have been established. The average is taken over a specific period of time, like 10 days, 20 minutes, 30 weeks or any time period. Look at the direction of the moving average to get a basic idea of which way the price is moving. If it is angled up, the price is moving up (or was recently) overall; angled down, and the price is moving down overall; moving sideways, and the price is likely in a range. As a general guideline, if the price is above a moving average, the trend is up. If the price is below a moving average, the trend is down. However, moving averages can have different lengths. A MA with a short time frame will react much quicker to price changes than an MA with a long look back period. Crossovers are one of the main moving average strategies. The first type is a price crossover, which is when the price crosses above or below a moving average to signal a potential change in trend. Another strategy is to apply two moving averages to a chart: one longer and one shorter. When the shorter-term MA crosses above the longer-term MA, it's a buy signal, as it indicates that the trend is shifting up. There are five popular types of moving averages:simple, exponential, triangular, variable, and weighted. The only significant difference between the various types of moving averages is the weight assigned to the most recent data. Simple moving averages apply equal weight to the prices. Exponential and weighted averages apply more weight to recent prices. Triangular averages apply more weight to prices in the middle of the time period.


Here are the different type of moving average:
EMA - Exponential Moving Average
SMA - Simple Moving Average
TRIMA - Triangular Moving Average

MACD - Moving Average Convergence/Divergence
The MACD is a trend following momentum indicator that shows the relationship between two moving averages of prices. The MACD is the difference between a 26-day and 12-day exponential 
moving average. A 9-day exponential moving average, called the "signal" line is plotted on top of the MACD to show buy/sell opportunities. The MACD proves most effective in wide-swinging trading markets. The basic MACD trading rule is to sell when the MACD falls below its signal line. Similarly, a buy signal occurs when the MACD rises above its signal line. It is also popular to buy/sell when the MACD goes above/below zero.

BBANDS - Bollinger Bands
As with moving average envelopes, the basic interpretation of Bollinger Bands is that prices tend to stay within the upper- and lower-band. The distinctive characteristic of Bollinger Bands is that the spacing between the bands varies based on the volatility of the prices. During periods of extreme price changes the bands widen to become more forgiving. During periods of stagnant pricing the bands narrow to contain prices.

STDDEV - Standard Deviation
Standard Deviation is a statistical measure of volatility. Standard Deviation is typically used as a component of other indicators, rather than as a stand-alone indicator. High Standard Deviation values occur when the data item being analysed is changing dramatically. Similarly, low Standard Deviation values occur when prices are stable.

Time Series Forecast
The Time Series Forecast indicator displays the statistical trend of a security's price over a specified time period. The trend is based on linear regression analysis. Rather than plotting a straight linear regression trend line, the Time Series Forecast plots the last point of multiple linear regression trend lines. The interpretation of a Time Series Forecast is identical to a moving average. However, the Time Series Forecast indicator has two advantages over classic moving averages. Unlike a moving average, a Time Series Forecast does not exhibit as much delay when adjusting to price changes. Since the indicator is "fitting" itself to the data rather than averaging them, the Time Series Forecast is more responsive to price changes.

Beta 
In finance, the beta of an investment indicates whether the investment is more or less volatile than the market as a whole.

KAMA - Kaufman Adaptive Moving Average
Kaufman's Adaptive Moving Average is an intelligent moving average. The powerful trend-following indicator is based on the Exponential Moving Average and is responsive to both trend and volatility. It closely follows price when noise is low and smooths out the noise when price fluctuates. Like all moving averages, it can be used to visualise the trend. Price crossing it indicates a directional change. Price can also bounce off the KAMA, which can act as dynamic support and resistance.

STOCH - Stochastic 
The Stochastic Oscillator compares where a security's price closed relative to its price range over a given time period. The Stochastic Oscillator is displayed as two lines. The main line is called "%K." The second line, called "%D," is a moving average of %K. The %K line is usually displayed as a solid line and the %D line is usually displayed as a dotted line. There are several ways to interpret a Stochastic Oscillator. Three popular methods include: Buy when the Oscillator (either %K or %D) falls below a specific level (e.g., 20) and then rises above that level. Sell when the Oscillator rises above a specific level (e.g., 80) and then falls below that level. Buy when the %K line rises above the %D line and sell when the %K line falls below the %D line. Look for divergences. For example, where prices are making a series of new highs and the Stochastic Oscillator is failing to surpass its previous highs.

Pattern recognition:

Doji pattern
It is said that the trend has slowed down - but it doesn't mean an immediate reversal! This is a frequent misinterpretation leading to a wrong use of dojis. Doji's are formed when the session opens and closes at the same level. This pattern indicates there is a lot of indecision about what should be the value.

Hammer pattern 
the market is trying to hammer out a base Because of this strong demand at the bottom, it is considered a bottom reversal signal.

Hanging Man pattern
The hanging man is also comprised of one candle and it's the opposite of the hammer. A true hanging man must emerge at the top of an uptrend. reversal signal.

Morning Star pattern
The classical morning star is a three-day bottom reversal pattern on a Japanese candlestick chart. It represents the fact that the buyers have now stepped in and seized control.

Evening Star pattern
This pattern is the opposite of the morning star. It is recognised when the price stagnates after an upward trend. This candlestick pattern generally indicates that confidence in the current trend has eroded and that bears are taking control. 

Dark Cloud Cover pattern
This pattern is the exact opposite of the piercing pattern. It happens during an upward trend when the session opens at or slightly above the previous closing price, but the demand can't be sustained. It may also be used as a warning sign for bullish positions.

Harami pattern
A harami is recognised by a two-day reversal pattern showing a small body candle completely contained within the range of the previous larger candle's body. This formation suggests that the previous trend is coming to an end. The smaller the second candlestick, the stronger the reversal signal. The harami pattern can be bullish or bearish but it always has to be confirmed by the previous trend.

Engulfing pattern
When engulfing occurs in a downward trend, it indicates that the trend has lost momentum and bullish investors may be getting stronger. Conversely, a bearish engulfing will occur when the market is at the top after an uptrend.

Piercing pattern
This pattern is similar to the engulfing with the difference that this one does not completely engulfs the previous candle. It occurs during a downward trend, when the market gains enough strength to close the candle above the midpoint of the previous candle. This pattern is seen as an opportunity for the buyers to enter long as the downtrend could be exhausted.
