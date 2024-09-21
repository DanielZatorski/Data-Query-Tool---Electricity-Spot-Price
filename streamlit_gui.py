import streamlit as st
import pandas as pd
import plotly.graph_objects as go
from gui_feed import get_spot_price
from datetime import datetime

today = datetime.now().date()
min_date = datetime(2002, 1, 1).date()

st.title("Data Query Tool - Electricity Spot Price")

# sidebar for selection inputs
st.sidebar.header("Query Parameters")

# date input widgets with rolling max date (today)
start_date = st.sidebar.date_input("Select Start Date:", value=today,min_value=min_date, max_value=today)
end_date = st.sidebar.date_input("Select End Date:", value=today, max_value=today)

# select price area in the sidebar
price_area = st.sidebar.selectbox("Select Price Area:", ['DK1', 'DK2', 'DE', 'SE3', 'SE4', 'NO2'])

# select granularity using radio buttons in the sidebar
granularity = st.sidebar.radio("Select Granularity:", ['hourly', 'daily', 'monthly'])

# initialize session state to store previous query results and granularities if not already initialized
if 'query_results' not in st.session_state:
    st.session_state['query_results'] = []
if 'granularities' not in st.session_state:
    st.session_state['granularities'] = []

# button to trigger the query in the sidebar
if st.sidebar.button("Run Query"):
    # validation of input
    if start_date > end_date:
        st.warning("Start date must be before or the same as the end date!")
    else:
        # call the function from guifeed
        data = get_spot_price(str(start_date), str(end_date), price_area, granularity)

        # convert the result to a DataFrame
        df = pd.DataFrame(data)
        
        # if there is data, show it and provide a download button
        if not df.empty:
            st.success("Data query completed.")
            
            # Store the query result and granularity in session state
            st.session_state['query_results'].append((df, price_area))  # Store DataFrame with price area
            st.session_state['granularities'].append(granularity)
        else:
            st.warning("No data returned for the selected query.")

# plot a graph of the query results if granularities match
if st.session_state['query_results']:
    # Check if all granularities are the same
    if len(set(st.session_state['granularities'])) == 1:
        st.subheader("Cumulative Matching Granularity Graph")
        
        # create the Plotly figure
        fig = go.Figure()
        
        # loop through each query result and add to the figure
        for idx, (result_df, area) in enumerate(st.session_state['query_results']):
            result_df['HourUTC'] = pd.to_datetime(result_df['HourUTC'])  # Ensure datetime
            fig.add_trace(go.Scatter(x=result_df['HourUTC'], y=result_df['SpotPriceDKK'],
                                     mode='lines+markers',
                                     name=f'{area} - Query {idx + 1}')) 
            
        fig.update_layout(title='Electricity Spot Price Over Time',
                          xaxis_title='Time',
                          yaxis_title='Price [DKK]',
                          template='plotly_white')
        st.plotly_chart(fig)  # render the Plotly figure in Streamlit
    else:
        st.warning("The granularities of the queries do not match. Cannot plot the data.")

# display each previous query result below in the main area
if st.session_state['query_results']:
    st.header("Previous Query Results")
    for idx, (result_df, area) in enumerate(st.session_state['query_results']):
        st.subheader(f"Result {idx + 1} - Price Area: {area}")
        st.dataframe(result_df)  # display each DataFrame under the previous one
