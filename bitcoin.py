import requests
from tkinter import *
from tkinter import ttk
import tkinter as tk

def btc_price():
    while True:
        # URL API
        url = "https://api.coindesk.com/v1/bpi/currentprice.json"
        response =requests.get(url)
        # Store API
        data = response.json()
        # BTC prices
        usd_in_btc = data["bpi"]["USD"]["rate_float"] # Store BTC/USD value
        eur_in_btc = data["bpi"]["EUR"]["rate_float"] # Store BTC/EUR value
        gbp_in_btc = data["bpi"]["GBP"]["rate_float"] # Store BTC/GBP value
        clock = data["time"]["updateduk"] # Store Clock on time
      
        return usd_in_btc, eur_in_btc, gbp_in_btc, clock
    
def update_price():
    usd, eur, gbp, clock = btc_price()
    usd_label.configure(text=f'BTC/USD - ${usd:.2f}')
    eur_label.configure(text=f'BTC/EUR - €{eur:.2f}')
    gbp_label.configure(text=f'BTC/GBP - £{gbp:.2f}')
    clock_label.configure(text=f' {clock}')
    window.after(1000, update_price)
    
# Get prices

def close_app():
    window.destroy()

# Main window
window = Tk()
window.title('BTC Price')
window.geometry('240x270')

frame = ttk.Frame(window, padding=10)
frame.grid()
ttk.Label(frame).grid(column=2)
title = ttk.Label(frame, text='   BTC Price   ', font='Calibri 24 bold', background="orange", foreground="black", relief='solid')
usd_label = ttk.Label(frame, text='', font='Arial 14', padding=5,)
eur_label = ttk.Label(frame, text='', font='Arial 14', padding=5)
gbp_label = ttk.Label(frame, text='', font='Arial, 14', padding=5)
clock_label = ttk.Label(frame, text='', font='Arial 10', padding=8)

#Button to exit the program
button = tk.Button( frame, 
                    text="EXIT",
                    command=close_app, 
                    font=('Arial', 14, 'bold'), 
                    pady= 8,
                    fg='white',
                    bg='red')
button.grid(column=0, row=5)

# Position grids
title.grid(column=0, row=0)
usd_label.grid(column=0, row=1)
eur_label.grid(column=0, row=2)
gbp_label.grid(column=0, row=3)
clock_label.grid(column=0, row=4)

update_price()
window.mainloop()

