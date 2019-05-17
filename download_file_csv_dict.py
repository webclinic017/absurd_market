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
        quandl_dict[quandl_ticker] = (name, date)
    return quandl_dict


def detail_company(quandl_dict):
    """This function returns the detail of all tickers"""
    
    for item in quandl_dict:
        print(item, quandl_dict[item])
        
def get_name(ticker, quandl_dict):
    """This function returns the name of the business of a particular ticker"""
    
    quandl_ticker = 'EOD/' + ticker
    return quandl_dict[quandl_ticker][0]


def get_date(ticker, quandl_dict):
    """This function returns the update date of trading of the business of a 
    particular ticker"""
    
    quandl_ticker = 'EOD/' + ticker
    return quandl_dict[quandl_ticker][1]


def main():
    """"""
    
    while True:
        try:
            ticker = str(input('What ticker? ')).upper()
       
            url = 'https://s3.amazonaws.com/quandl-production-static/end_of_day_us_stocks/ticker_list.csv'
            file_read = get_csv_file(url)
            quandl_dict = csv_data_dict(file_read)
        
            name = get_name(ticker, quandl_dict)
            date = get_date(ticker, quandl_dict)
            
        except KeyError:
            print('Wrong ticker!!! ') 
            
        else:
            
            #print(quandl_dict)
            print(name)
            print(date) 
            break
            
main()