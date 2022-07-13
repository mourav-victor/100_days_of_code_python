import requests  # for web request
from tkinter import *  # for GUI

## Inspired by Hashtag Programação: https://www.youtube.com/watch?v=AiBC01p58oI

def get_currency_price(code):

    # make request to API for specifics currencies
    request = requests.get(f"https://economia.awesomeapi.com.br/json/last/{code}")

    # transform the request answer in a dictionary
    request_dict = request.json()

    # read the dictionary for each currency cotation
    dict_code = code.replace("-", "")
    current_price = request_dict[dict_code]["bid"]
    highest_price = request_dict[dict_code]["high"]
    lowest_price = request_dict[dict_code]["low"]

    # create dictionary with desired values
    dict = {"current" : current_price, "max" : highest_price, "min" : lowest_price}

    return dict

# Create window
window = Tk()

# Configurate window
window.title("My GUI")
window.minsize(width=100, height=100)
window.config(padx=10, pady=5)

# Create title label
label = Label(text="Exchange Rate", font=("Arial", 16, "italic"), pady=10)
label.grid(column=1, row=0)

# Create buttons
def button_clicked(currency, code):
    label_selected_currency.config(text=f"{currency} -> BRL")

    prices = get_currency_price(code)
    label_currency_rate.config(text=prices["current"])
    label_min1.config(text=f'Min')
    label_min2.config(text=prices["min"])
    label_max1.config(text=f'Max')
    label_max2.config(text=prices["max"])


button_dolar = Button(text="Dollar", padx = 15, command= lambda : button_clicked("Dollar", "USD-BRL"))
button_euro = Button(text="Euro", padx = 15, command= lambda : button_clicked("Euro", "EUR-BRL"))
button_btv = Button(text="BTC", padx = 15, command= lambda : button_clicked("BTC", "BTC-BRL"))
button_dolar.grid(column=0, row=2)
button_euro.grid(column=1, row=2)
button_btv.grid(column=2, row=2)

# Create labels for result
label_selected_currency = Label(text="", font=("Arial", 14, "italic"), pady = 20)
label_selected_currency.grid(column=1, row=3)

label_currency_rate = Label(text="")
label_currency_rate.grid(column=1, row=4)

label_max1 = Label(text="", fg='#0f0', pady=0, padx=10)
label_max1.grid(column=2, row=5)
label_max2 = Label(text="", fg='#0f0', pady=0, padx=10)
label_max2.grid(column=2, row=6)

label_min1 = Label(text="", fg='#f00', pady=0, padx=10)
label_min1.grid(column=0, row=5)
label_min2 = Label(text="", fg='#f00', pady=0, padx=10)
label_min2.grid(column=0, row=6)

# Keep window opened
window.mainloop()
