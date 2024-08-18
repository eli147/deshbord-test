import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime


# Function to perform calculations based on user input
def perform_calculation(df, calculation):
    if calculation == 'average_price':
        # Calculate average closing price
        return df['Close'].mean()
    elif calculation == 'max_price':
        # Calculate maximum closing price
        return df['Close'].max()
    elif calculation == 'min_price':
        # Calculate minimum closing price
        return df['Close'].min()
    elif calculation == 'total_volume':
        # Calculate total trading volume
        return df['Volume'].sum()
    else:
        return "Invalid calculation type. Please choose 'average_price', 'max_price', 'min_price', or 'total_volume'."


# Streamlit app
def run():
    # Set the title of the app
    st.title("Stock Data Calculator")

    # Get the current year
    current_year = datetime.now().year

    # User input for ticker symbol
    ticker = st.text_input("Enter the stock ticker symbol:", "AAPL")
    data_tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'META', 'NFLX', 'NVDA', 'IBM', 'INTC']
    st.write(f'Example of componeys {data_tickers}')
    # User input for calculation type
    calculation = st.selectbox(
        "Choose the calculation you want to perform:",
        ["average_price", "max_price", "min_price", "total_volume"]
    )

    # Button to trigger data fetching and calculation
    if st.button("Get Data"):
        if ticker:
            try:
                # Fetch data for the current year
                start_date = f"{current_year}-01-01"
                end_date = f"{current_year}-12-31"
                data = yf.download(ticker, start=start_date, end=end_date)

                if data.empty:
                    st.error(f"No data found for ticker symbol '{ticker}'")
                else:
                    # Perform the calculation
                    result = perform_calculation(data, calculation)

                    # Display the result
                    st.write(
                        f"Result of '{calculation}' for ticker symbol '{ticker}' for the year {current_year}")

                    # Display a sample of the data
                    st.header(f"{result}")


            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter a valid ticker symbol.")


