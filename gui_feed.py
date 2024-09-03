import pandas as pd
import requests
from datetime import datetime

def get_spot_price(start_date,end_date,price_area,granularity):
    
    url = (
        f'https://api.energidataservice.dk/dataset/Elspotprices'
        f'?start={start_date}&end={end_date}'
        f'&filter={{"PriceArea":["{price_area}"]}}'
    )

    response = requests.get(url)

    #if response is 200 continue with the code execution else print an status error response
    if response.status_code == 200:

        result = response.json()
        df = pd.DataFrame(result)
        records = df['records'].apply(pd.Series)

        #conditional granularity data transformation according to user input
        if granularity == 'hourly':
            records_print = df['records'].apply(pd.Series)

        elif granularity == 'daily':
            records = df['records'].apply(pd.Series)
            records.drop(columns = ['HourDK','PriceArea'],inplace=True)
            records['HourUTC'] = pd.to_datetime(records['HourUTC'])
            records.set_index('HourUTC', inplace=True)
            daily_mean_df = records.resample('D').mean()
            daily_mean_df.reset_index(inplace=True)
            daily_mean_df['PriceArea'] = str(price_area)
            records_print = pd.DataFrame(daily_mean_df)
        
        elif granularity == 'monthly':
            records = df['records'].apply(pd.Series)
            records.drop(columns = ['HourDK','PriceArea'],inplace=True)
            records['HourUTC'] = pd.to_datetime(records['HourUTC'])
            records.set_index('HourUTC', inplace=True)
            monthly_mean_df = records.resample('ME').mean()
            monthly_mean_df.reset_index(inplace=True)
            monthly_mean_df['PriceArea'] = str(price_area)
            records_print = pd.DataFrame(monthly_mean_df)


        return records_print










