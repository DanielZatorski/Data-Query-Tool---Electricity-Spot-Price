import pandas as pd
import requests
from datetime import datetime

# get user inputs
start_date_str = input('Select Start Date (YYYY-MM-DD): ')
end_date_str = input('Select End Date (YYYY-MM-DD): ')

# function to format date in the required format
def format_date(date_str):
    return datetime.strptime(date_str, '%Y-%m-%d').strftime('%Y-%m-%d')

# validate input dates
try:
    start_date = format_date(start_date_str)
    end_date = format_date(end_date_str)
except ValueError:
    print("Invalid date format. Please enter dates in YYYY-MM-DD format.")
    exit(1)



#allow code to continue only if correct input is written and executed
while True :

    selectarea = input('Which price area is of interest? Write any of: DK1, DK2, DE, SE3, SE4, NO2: ').strip().upper()

    if selectarea in [ 'DK1', 'DK2', 'DE', 'SE3', 'SE4', 'NO2']:
        break
    else:
        print("Invalid price area format. Please enter correct one shown in the input message.")



#allow code to continue only if correct input is written and executed
while True:
    granularity_input = input('Select granularity (hourly, daily, monthly): ').strip().lower()
    if granularity_input in ['hourly', 'daily', 'monthly']:
        break
    else:
        print("Invalid granularity. Please enter 'hourly', 'daily', or 'monthly'.")



def get_spot_price(start_date,end_date,selectarea):
    
    url = (
        f'https://api.energidataservice.dk/dataset/Elspotprices'
        f'?start={start_date}&end={end_date}'
        f'&filter={{"PriceArea":["{selectarea}"]}}'
    )

    response = requests.get(url)

#if response is 200 continue with the code execution else print an status error response
    if response.status_code == 200:

        result = response.json()
        df = pd.DataFrame(result)
        records = df['records'].apply(pd.Series)

        #conditional granularity data transformation according to user input
        if granularity_input == 'hourly':
            records = df['records'].apply(pd.Series)

        elif granularity_input == 'daily':
            records = df['records'].apply(pd.Series)
            records.drop(columns = ['HourDK','PriceArea'],inplace=True)
            records['HourUTC'] = pd.to_datetime(records['HourUTC'])
            records.set_index('HourUTC', inplace=True)
            monthly_mean_df = records.resample('D').mean()
            monthly_mean_df.reset_index(inplace=True)
            monthly_mean_df['PriceArea'] = str(selectarea)
            records = monthly_mean_df
        
        elif granularity_input == 'monthly':
            records = df['records'].apply(pd.Series)
            records.drop(columns = ['HourDK','PriceArea'],inplace=True)
            records['HourUTC'] = pd.to_datetime(records['HourUTC'])
            records.set_index('HourUTC', inplace=True)
            monthly_mean_df = records.resample('M').mean()
            monthly_mean_df.reset_index(inplace=True)
            monthly_mean_df['PriceArea'] = str(selectarea)
            records = monthly_mean_df

        print(records)
    else:
        print(f'Error {response.status_code}: {response.text}')


print(get_spot_price(start_date,end_date,selectarea))