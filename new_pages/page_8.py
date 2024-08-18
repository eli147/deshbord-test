import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime


def run():
    st.title("Download Stock Data")

    current_year = datetime.now().year

    ticker = st.text_input("Enter the stock ticker symbol:", "AAPL").upper()
    data_tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'META', 'NFLX', 'NVDA', 'IBM', 'INTC']
    st.write(f'Example of compones {data_tickers}')

    if ticker:
        try:
            start_date = f"{current_year}-01-01"
            end_date = f"{current_year}-12-31"
            data = yf.download(ticker, start=start_date, end=end_date)

            if not data.empty:
                st.write(f"Data for {ticker} is available. You can download it as a CSV file.")

                # Provide download link for CSV
                csv = data.to_csv(index=True)
                st.download_button(
                    label="Download CSV",
                    data=csv,
                    file_name=f"{ticker}_data_{current_year}.csv",
                    mime="text/csv"
                )

            else:
                st.error(f"No data found for ticker symbol '{ticker}'")

        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a valid ticker symbol.")
