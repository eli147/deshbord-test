import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

from new_pages.page_3 import perform_calculation


def run():
    st.title("Stock Data Visualizer")

    current_year = datetime.now().year

    ticker = st.text_input("Enter the stock ticker symbol:", "").upper()
    calculation = st.selectbox("Choose the calculation:", ["average_price", "max_price", "min_price", "total_volume"])

    if st.button("Get Data"):
        if ticker:
            try:
                start_date = f"{current_year}-01-01"
                end_date = f"{current_year}-12-31"
                data = yf.download(ticker, start=start_date, end=end_date)

                if not data.empty:
                    result = perform_calculation(data, calculation)
                    st.write(f"Result of '{calculation}' for {ticker}: {result}")

                    # Plotting historical closing price
                    st.write("Historical Closing Prices")
                    plt.figure(figsize=(10, 5))
                    plt.plot(data.index, data['Close'], label='Close Price')
                    plt.title(f'{ticker} Closing Prices')
                    plt.xlabel('Date')
                    plt.ylabel('Price')
                    plt.legend()
                    st.pyplot()

                else:
                    st.error(f"No data found for ticker symbol '{ticker}'")

            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter a valid ticker symbol.")


