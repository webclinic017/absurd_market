import datetime
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("The SisypheQuant Project: Analysis the Absurde Market of Invisible-Hand.")
import download_file_csv_dict
import Improved_Project



# test_list = [str(v) for v in range(8000)]
quandl_dict = dict()

def format_listbox_item(ticker, name):
    return '{}: {}'.format(ticker, name)

def format_quandl_dict():
    return [format_listbox_item(ticker, name) for (ticker, (name, date)) in quandl_dict.items()]

def on_keyrelease(event):
    # get text from entry
    value = event.widget.get()
    value = value.strip().upper()
    
    # get data from ticker_list
    if value == '':
        data = format_quandl_dict()
    else:
        data = []
        for ticker, (name, dte) in quandl_dict.items():
            if value in ticker.upper():
                data.append(format_listbox_item(ticker, name))
    
    # update data in listbox
    listbox_update(data)

def listbox_update(data):
    # delete previous data
    listbox.delete(0, 'end')

    # sorting data
    data = sorted(data, key=str.lower)

    # put new data
    for item in data:
        listbox.insert('end', item)
        
        
def calculate_start_date(last_trading_date):
    """"""
        
    deltas = { "1 week": datetime.timedelta(days=7),
               "1 month": datetime.timedelta(days=30),
               "3 months": datetime.timedelta(days=90),
               "6 months": datetime.timedelta(days=180),
               "1 year": datetime.timedelta(days=365),
               "2 years": datetime.timedelta(days=730),
               "3 years": datetime.timedelta(days=1095),
               "5 years": datetime.timedelta(days=1825),
               "10 years": datetime.timedelta(days=3650),
               "15 years": datetime.timedelta(days=5475),
               "20 years": datetime.timedelta(days=7300)
               }
    
    if time_delta in deltas:
        date = datetime.datetime.strptime(last_trading_date, '%Y-%m-%d')        
        lower_date = date - deltas[time_delta]
        return lower_date.strftime('%Y-%m-%d')
    
    return None
  
ticker = ''  
def on_select_ticker(event):
    # display element selected on list
    # previous item was event.widget.get('active'))
    # print(event.widget.get(event.widget.curselection()))
    global ticker
    ticker = ''
    try:
        ticker = event.widget.get(event.widget.curselection()).split(':')[0]
    except:
        pass
    
def on_plot():
    if ticker in quandl_dict:
        start_date = calculate_start_date(quandl_dict[ticker][1])
        bottom_indicators = [indicator.get() for indicator in all_combos_indic]
        Improved_Project.plot_ticker(quandl_dict, ticker, start_date, 
                                     var_risk.get(), var_momentum.get(), 
                                     var_pattern.get(), var_volume.get(),
                                     bottom_indicators)
        
    # tick boxes for combined plots
    # 3 (of the same) drop down combos for the other 3 plots
        
def on_select_graph(event):
    """"""
    print('----------------------------')
    
    if event: # <-- this works only with bind because `command=` doesn't send event
        print("event.widget:", event.widget.get())

    for i, x in enumerate(all_combos_indic):
        print("all_comboboxes[%d]: %s" % (i, x.get())) 
        
time_delta = None
def on_select_date(event):
    """"""
    #date = make a datetime object from last_trading_day
    global time_delta
    time_delta = event.widget.get()
        
def on_closing():
    """
    Destroy the window
    :return:
    """
    Improved_Project.close_plot()
    root.destroy()


frame = tk.Frame(root)
frame.grid()

logo = tk.PhotoImage(file="Background_Photo_Earth.gif")


background = tk.Label(frame, compound = tk.CENTER, image=logo, bg='black').place(x=0, y=0, relwidth=1, relheight=1)

###################################### Date ####################################
def build_date(frame):
    """"""
    date_range = tk.Label(frame, text="Date: ", pady=5, padx=0, fg='gold', background ='black')
    date_range.grid(row=0, column=0, sticky='w')
    
    data_combo = ttk.Combobox(frame, 
                                values=[
                                        "1 week", 
                                        "1 month",
                                        "3 months",
                                        "6 months",
                                        "1 year",
                                        "2 years",
                                        "3 years",
                                        "5 years",
                                        "10 years",
                                        "15 years",
                                        "20 years"
                                        ])
    data_combo.grid(row=0, column=0, sticky='e', pady=5, padx=0)
    data_combo.bind('<<ComboboxSelected>>', on_select_date)

build_date(frame)
############################## Refresh Button ##################################
def on_refresh():
    """"""
    global quandl_dict
    quandl_dict = download_file_csv_dict.read_tickers_from_Quandl()
    ticker_list = ['{}: {}'.format(ticker, name) for (ticker, (name, date)) in quandl_dict.items()]
    listbox_update(ticker_list)


def build_ticker(frame):
    """"""
    button_ticker = tk.Button(frame, text="Refresh Ticker", bg='blue', command=on_refresh)
    button_ticker.grid(row=1, column=1, pady=5, padx=5, sticky='w')

    # entry to get the user's choice of ticker
    entry = tk.Entry(frame, background='#1062EF')
    entry.bind('<KeyRelease>', on_keyrelease)
    entry.grid(row=1, column=1, pady=5, padx=5, sticky='e')
    
    # listbox for data
    listbox = tk.Listbox(frame, height=6, background='#1062EF')
    listbox.bind('<<ListboxSelect>>', on_select_ticker)
    listbox.grid(row=2, column=1, sticky='ew')
    scrollbar = ttk.Scrollbar(frame, orient='vertical', command=listbox.yview)
    scrollbar.grid(row=2, column=1, sticky="nes")
    listbox['yscrollcommand'] = scrollbar.set
    return listbox

listbox = build_ticker(frame)

matplotlib = tk.PhotoImage(file="matplotlib.png")

def build_plot_button(frame):
    button_plot = tk.Button(frame, text="Plot", image=matplotlib,
                            compound=tk.BOTTOM,
                            command=on_plot)
    button_plot.grid(row=1, column=2, rowspan=2, pady=5, padx=5)
    
build_plot_button(frame)
    
############################### Radio Button ###################################
def on_risk():
    """"""
    print("on_risk:{}\n".format(var_risk.get()))
    
def build_radio_button(frame, text, variable, command, row, column):
    """"""
    tk.Radiobutton(frame, text=text, value=text, variable=variable, 
                   background='grey', command=command).grid(
                       row=row, column=column, sticky="new", pady=5, padx=5)

def build_risk(frame, variable):
    """"""
    risk_label = tk.Label(frame, 
            text="""Choose a risk indicator""", background='#299CE8')
    risk_label.grid(row=4, column=0, pady=5, padx=5, sticky='new')
    build_radio_button(frame, text="Standard deviation", variable=variable, command=on_risk, row=5, column=0)
    build_radio_button(frame, text="Beta", variable=variable, command=on_risk, row=6, column=0)
    
var_risk = tk.StringVar()    
build_risk(frame, var_risk)

################################ Volume Check Button ###########################
def on_volume():
    """"""
    print("volume:{}\n".format(var_volume.get()))
def build_volume(frame, variable):
    """"""
    volume_label = tk.Label(frame, 
            text="""Choose to visualize the volume of trades""", background='#299CE8')
    volume_label.grid(row=4, column=2, sticky='new')
    tk.Checkbutton(frame, text="Volume", variable=variable, background='grey',
                   command=on_volume, onvalue="Volume", offvalue=""
                   ).grid(row=5, column=2, pady=5, padx=5, sticky='new')

var_volume = tk.StringVar()
build_volume(frame, var_volume)
########################## momentum indicators on ax1 ##########################

#tk.Radiobutton(frame, 
              #text="Standard deviation", 
              #variable=momentum, 
              #value=1, background='grey')
def on_momentum():
    """"""
    print("momentum:{}\n".format(var_momentum.get()))
    
    
def on_pattern():
    """"""
    print("pattern:{}\n".format(var_pattern.get()))

    
def build_momentum(frame, variable):
    """"""
    build_radio_button(frame, text="Moving Average", variable=variable, command=on_momentum, row=9, column=0)
    build_radio_button(frame, text="Exponential Moving Average", variable=variable, command=on_momentum, row=10, column=0)
    build_radio_button(frame, text="Simple Moving Average",  variable=variable, command=on_momentum, row=11, column=0)
    build_radio_button(frame, text="Kaufman Adaptive Moving Average", variable=variable, command=on_momentum, row=12, column=0)
    build_radio_button(frame, text="Bollinger Indicator", variable=variable, command=on_momentum, row=13, column=0)
    build_radio_button(frame, text="Triangular Moving Average", variable=variable, command=on_momentum, row=14, column=0)
    build_radio_button(frame, text="Time Series Forcast", variable=variable, command=on_momentum, row=15, column=0)

def build_pattern(farme, variable):
    """"""
    build_radio_button(frame, text="Doji pattern", variable=variable, command=on_pattern, row=17, column=2)
    build_radio_button(frame, text="Hammer pattern", variable=variable, command=on_pattern, row=9, column=2)
    build_radio_button(frame, text="Hanging Man pattern", variable=variable, command=on_pattern, row=10, column=2)
    build_radio_button(frame, text="Morning Star pattern", variable=variable, command=on_pattern, row=11, column=2)
    build_radio_button(frame, text="Evening Star pattern", variable=variable, command=on_pattern, row=12, column=2)
    build_radio_button(frame, text="Dark Cloud Cover pattern", variable=variable, command=on_pattern, row=13, column=2)
    build_radio_button(frame, text="Harami Pattern", variable=variable, command=on_pattern, row=14, column=2)
    build_radio_button(frame, text="Engulfing pattern", variable=variable, command=on_pattern, row=15, column=2)
    build_radio_button(frame, text="Piercing pattern", variable=variable, command=on_pattern, row=16, column=2)

def build_momntun_and_pattern(frame, var_momentum, var_pattern):
    """"""
    ax1Indicators_label = tk.Label(frame, 
            text="""Choose the momentum indicators  and pattern recognition to visualize on the Candlestick graph""", background='#299CE8')
    ax1Indicators_label.grid(row=8, column=0, columnspan=3)
    build_momentum(frame, var_momentum)
    build_pattern(frame, var_pattern)
    
var_momentum = tk.StringVar()
var_pattern = tk.StringVar()
build_momntun_and_pattern(frame, var_momentum, var_pattern)

################################# Combo Box ####################################
def build_indicator_combo(frame, row, padx, pady):
    """"""
    combo_Indicator = ttk.Combobox(frame, values=[
                                    "Rate Of Change", 
                                    "Relative Strength Index",
                                    "Stochastic",
                                    "Moving Average Convergence/Divergence"])
    combo_Indicator.grid(row=row, column=1, padx=padx, pady=pady)
    combo_Indicator.bind('<<ComboboxSelected>>', on_select_graph)
    return combo_Indicator

def build_indicator_combos(frame):
    """"""
    
    ax234Indicators_label = tk.Label(frame, 
            text="""Choose the momentum indicators to visualize on these graphs""", background='#299CE8')
    ax234Indicators_label.grid(row=18, column=1, sticky="new") 
    
    combos = []
    combos.append(build_indicator_combo(frame, row=19, padx=0, pady=0))
    combos.append(build_indicator_combo(frame, row=20, padx=5, pady=5))
    combos.append(build_indicator_combo(frame, row=21, padx=5, pady=5))
    return combos

all_combos_indic = build_indicator_combos(frame)

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()


















#root.columnconfigure(0, weight=1)
#root.columnconfigure(1, weight=1)
#root.columnconfigure(2, weight=1)
#root.columnconfigure(3, weight=1)
#root.columnconfigure(4, weight=1)
#root.columnconfigure(5, weight=1)
#root.columnconfigure(6, weight=1)

#root.rowconfigure(0, weight=1)
#root.rowconfigure(1, weight=1)
#root.rowconfigure(2, weight=1)
#root.rowconfigure(3, weight=1)
#root.rowconfigure(4, weight=1)
#root.rowconfigure(5, weight=1)
#root.rowconfigure(6, weight=1)
#root.rowconfigure(7, weight=1)
#root.rowconfigure(8, weight=1)
#root.rowconfigure(9, weight=1)
#root.rowconfigure(10, weight=1)
#root.rowconfigure(11, weight=1)
#root.rowconfigure(12, weight=1)
#root.rowconfigure(13, weight=1)
#root.rowconfigure(14, weight=1)
#root.rowconfigure(15, weight=1)
#root.rowconfigure(16, weight=1)
#root.rowconfigure(17, weight=1)
#root.rowconfigure(18, weight=1)
#root.rowconfigure(19, weight=1)
#root.rowconfigure(20, weight=1)
