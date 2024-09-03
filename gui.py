import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import pandas as pd
from gui_feed import get_spot_price
from datetime import datetime
import requests


# function to handle the Run button click event
def run_query():
    # get user input
    start_date = start_date_entry.get()
    end_date = end_date_entry.get()
    price_area = price_area_var.get()
    granularity = granularity_var.get()
    
    # perform some validation, according to selection input
    if not start_date or not end_date:
        messagebox.showwarning("Input Error", "Please select both start and end dates.")
        return
    
    if not price_area:
        messagebox.showwarning("Input Error", "Please select a price area.")
        return
    
    # data query logic from gui_feed.py
    data = get_spot_price(start_date,end_date,price_area,granularity)

    # make sure data is converted into df
    df = pd.DataFrame(data)
    
    # save df into csv file
    df.to_csv('query_result.csv', index=False)
    
    # Inform the user
    messagebox.showinfo("Success", "Data query completed and saved to query_result.csv.")


# Initialize the main window
root = tk.Tk()
root.title("Data Query Tool - Electricity Spot Price")

# Create and place widgets
tk.Label(root, text="Select Start Date:").grid(row=0, column=0, padx=10, pady=5)
start_date_entry = DateEntry(root, date_pattern='yyyy-mm-dd')
start_date_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Select End Date:").grid(row=1, column=0, padx=10, pady=5)
end_date_entry = DateEntry(root, date_pattern='yyyy-mm-dd')
end_date_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Select Price Area:").grid(row=2, column=0, padx=10, pady=5)
price_area_var = tk.StringVar()
price_area_dropdown = ttk.Combobox(root, textvariable=price_area_var)
price_area_dropdown['values'] = ['DK1', 'DK2', 'DE', 'SE3', 'SE4', 'NO2']  # Example areas
price_area_dropdown.grid(row=2, column=1, padx=10, pady=5)

# radio buttons for selecting granularity
# Add label for granularity
tk.Label(root, text="Select Granularity:").grid(row=3, column=0, padx=10, pady=5)

# Create a frame to hold the radio buttons
granularity_frame = tk.Frame(root)
granularity_frame.grid(row=3, column=1, padx=10, pady=5)

# Variable to store selected granularity option
granularity_var = tk.StringVar()

# Options for granularity
granularity_options = ['hourly', 'daily', 'monthly']

# Create radio buttons in the frame
for option in granularity_options:
    tk.Radiobutton(granularity_frame, text=option, variable=granularity_var, value=option).pack(side=tk.LEFT, padx=5)
run_button = tk.Button(root, text="Run", command=run_query)
run_button.grid(row=4, column=0, columnspan=2, pady=20)

# Run the main loop
root.mainloop()
