import streamlit as st
import pandas as pd
import yfinance as yf


def run():
    st.title('Time Series Data')
    # Get the stock symbol from the user input
    symbol = st.text_input('Enter the stock symbol', 'AAPL')
    data_tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'META', 'NFLX', 'NVDA', 'IBM', 'INTC']
    st.write(f'Example of componeys {data_tickers}')
    if symbol:
        try:
            st.header(symbol)
            # Fetch the stock data using yfinance
            ticker = yf.Ticker(symbol)
            hist = ticker.history(period="1y")

            # Convert the historical data into a DataFrame
            df = hist.reset_index()

            # Display the DataFrame in the app
            st.dataframe(df)

        except Exception as e:
            st.write(f'Error fetching data: {e}')

    st.write('Use the sidebar to navigate to other new_pages.')
