import tkinter as tk
from tkinter import ttk



test_list = [str(v) for v in range(8000)]

def on_keyrelease(event):
    # get text from entry
    value = event.widget.get()
    value = value.strip().upper()
    
    # get data from test_list
    if value == '':
        data = test_list
    else:
        data = []
        for item in test_list:
            if value in item.upper():
                data.append(item)
    
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

def on_select(event):
        # display element selected on list
        # previous item was event.widget.get('active'))
        print(event.widget.get(event.widget.curselection()))

        # tick boxes for combined plots
        # 3 (of the same) drop down combos for the other 3 plots



root = tk.Tk()

frame = tk.Frame(root)
frame.grid()
#frame.pack()

logo = tk.PhotoImage(file="Background_Photo_Earth.gif")
explanation = """"""
background = tk.Label(frame,
compound = tk.CENTER,
text=explanation,
image=logo, bg='black').place(x=0, y=0, relwidth=1, relheight=1)

###################################### Date ####################################

date_range = tk.Label(frame, text="Date: ", pady=5, padx=0, fg='gold', background ='black')
date_range.grid(row=0, column=0, sticky='w')

### First way:
#date_entry = tk.Entry(frame)
#date_entry.grid(row=0, column=1)

### Second way:
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
                                    "20 years",
                                    "since 1996"])
data_combo.grid(row=0, column=0, sticky='e', pady=5, padx=0)


############################## Refresh Button ##################################

button_ticker = tk.Button(frame, text="Refresh Ticker", bg='blue')
#, command=quit
button_ticker.grid(row=1, column=2, pady=5, padx=5)


############################# Listbox of Ticker ################################

# entry to get the user's choice of ticker
entry = tk.Entry(frame, background='#1062EF')
entry.bind('<KeyRelease>', on_keyrelease)
entry.grid(row=2, column=2, pady=5, padx=5)
#entry.pack()

# listbox for data
listbox = tk.Listbox(frame, background='#1062EF')
listbox.bind('<<ListboxSelect>>', on_select)
listbox.grid(row=3, column=2, pady=5, padx=5)
listbox_update(test_list)


############################### Radio Button ###################################
s = tk.IntVar()

risk_label = tk.Label(frame, 
        text="""Choose a risk indicator""", background='#299CE8')
risk_label.grid(row=4, column=2, pady=5, padx=5)

std_dev_button = tk.Radiobutton(frame, 
              text="Standard deviation", 
              variable=s, 
              value=1, background='grey')

std_dev_button.grid(row=5, column=0, pady=5, padx=5, sticky="new")

beta_button = tk.Radiobutton(frame, 
              text="Beta", 
              variable=s,
              value=2, background='grey')
beta_button.grid(row=5, column=6, pady=5, padx=5, sticky="new")


################################ Volume Check Button ###########################
volume_label = tk.Label(frame, 
        text="""Choose to visualize the volume of trades""", background='#299CE8')
volume_label.grid(row=6, column=2)

var_Volume = tk.IntVar()
tk.Checkbutton(frame, text="Volume", variable=var_Volume, background='grey').grid(row=7, column=2, pady=5, padx=5)


########################## momentum indicators on ax1 ##########################

ax1Indicators_label = tk.Label(frame, 
        text="""Choose the momentum indicators  and pattern recognition to visualize on the Candlestick graph""", background='#299CE8')
ax1Indicators_label.grid(row=8, column=2)
"""Construct a checkbutton widget with the parent MASTER.

        Valid resource names: activebackground, activeforeground, anchor,
        background, bd, bg, bitmap, borderwidth, command, cursor,
        disabledforeground, fg, font, foreground, height,
        highlightbackground, highlightcolor, highlightthickness, image,
        indicatoron, justify, offvalue, onvalue, padx, pady, relief,
        selectcolor, selectimage, state, takefocus, text, textvariable,
        underline, variable, width, wraplength."""
var_MA = tk.IntVar()
tk.Checkbutton(frame, text="Moving Average", variable=var_MA, background='grey').grid(row=9, column=0, sticky="new", pady=5, padx=5)

var_EMA = tk.IntVar()
tk.Checkbutton(frame, text="Exponential Moving Average", variable=var_EMA, background='grey').grid(row=10, column=0, sticky="new", pady=5, padx=5)

var_SMA = tk.IntVar()
tk.Checkbutton(frame, text="Simple Moving Average", variable=var_SMA, background='grey').grid(row=11, column=0, sticky="new", pady=5, padx=5)

var_Kama = tk.IntVar()
tk.Checkbutton(frame, text="Kaufman Adaptive Moving Average", variable=var_Kama, background='grey').grid(row=12, column=0, sticky="new", pady=5, padx=5)

var_Bollinger = tk.IntVar()
tk.Checkbutton(frame, text="Bollinger Indicator", variable=var_Bollinger, background='grey').grid(row=13, column=0, sticky="new", pady=5, padx=5)

var_Trima = tk.IntVar()
tk.Checkbutton(frame, text="Triangular Moving Average", variable=var_Trima, background='grey').grid(row=14, column=0, sticky="new", pady=5, padx=5)

var_TSF = tk.IntVar()
tk.Checkbutton(frame, text="Time Series Forcast", variable=var_TSF, background='grey').grid(row=15, column=0, sticky="new", pady=5, padx=5)

var_Doji = tk.IntVar()
tk.Checkbutton(frame, text="Doji pattern", variable=var_Doji, background='grey').grid(row=16, column=0, sticky="new", pady=5, padx=5)

var_Hammer = tk.IntVar()
tk.Checkbutton(frame, justify=tk.LEFT, text="Hammer pattern", variable=var_Hammer, background='grey').grid(row=9, column=6, sticky="new", pady=5, padx=5)

var_Hanging = tk.IntVar()
tk.Checkbutton(frame, justify=tk.LEFT, text="Hanging Man pattern", variable=var_Hanging, background='grey').grid(row=10, column=6, sticky="new", pady=5, padx=5)

var_Morning = tk.IntVar()
tk.Checkbutton(frame, justify=tk.LEFT, text="Morning Star pattern", variable=var_Morning, background='grey').grid(row=11, column=6, sticky="new", pady=5, padx=5)

var_Evening = tk.IntVar()
tk.Checkbutton(frame, justify=tk.LEFT, text="Evening Star pattern", variable=var_Evening, background='grey').grid(row=12, column=6, sticky="new", pady=5, padx=5)

var_Dark = tk.IntVar()
tk.Checkbutton(frame, justify=tk.LEFT, text="Dark Cloud Cover pattern", variable=var_Dark, background='grey').grid(row=13, column=6, sticky="new", pady=5, padx=5)

var_Harami = tk.IntVar()
tk.Checkbutton(frame, justify=tk.LEFT, text="Harami Pattern", variable=var_Harami, background='grey').grid(row=14, column=6, sticky="new", pady=5, padx=5)

var_Engulfing = tk.IntVar()
tk.Checkbutton(frame, justify=tk.LEFT, text="Engulfing pattern", variable=var_Engulfing, background='grey').grid(row=15, column=6, sticky="new", pady=5, padx=5)

var_Piercing = tk.IntVar()
tk.Checkbutton(frame, justify=tk.LEFT, text="Piercing pattern", variable=var_Piercing, background='grey').grid(row=16, column=6, sticky="new", pady=5, padx=5)


################################# Combo Box ####################################
ax234Indicators_label = tk.Label(frame, 
        text="""Choose the momentum indicators to visualize on the these graphs""", background='#299CE8')
ax234Indicators_label.grid(row=17, column=2)

comboExample = ttk.Combobox(frame, values=[
                                    "Rate Of Change", 
                                    "Relative Strength Index",
                                    "Stochastic",
                                    "Moving Average Convergence/Divergence"])
comboExample.grid(row=18, column=2)

comboExample = ttk.Combobox(frame, values=[
                                    "Rate Of Change", 
                                    "Relative Strength Index",
                                    "Stochastic",
                                    "Moving Average Convergence/Divergence"])
comboExample.grid(row=19, column=2, pady=5, padx=5)

comboExample = ttk.Combobox(frame, values=[
                                    "Rate Of Change", 
                                    "Relative Strength Index",
                                    "Stochastic",
                                    "Moving Average Convergence/Divergence"])
comboExample.grid(row=20, column=2, pady=5, padx=5)


root.mainloop()
