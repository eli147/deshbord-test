import streamlit as st
import yfinance as yf
import pandas as pd
from datetime import datetime


def perform_calculation(df, calculation):
    if calculation == 'average_price':
        return df['Close'].mean()
    elif calculation == 'max_price':
        return df['Close'].max()
    elif calculation == 'min_price':
        return df['Close'].min()
    elif calculation == 'total_volume':
        return df['Volume'].sum()
    else:
        return "Invalid calculation type."


def run():
    st.title("Stock Data Calculator")

    current_year = datetime.now().year

    # User input for multiple tickers
    tickers = st.text_input("Enter stock ticker symbols (comma-separated):", "AAPL")
    tickers = [ticker.strip().upper() for ticker in tickers.split(',') if ticker.strip()]

    # User input for calculation type
    calculation = st.selectbox("Choose the calculation:", ["average_price", "max_price", "min_price", "total_volume"])

    if st.button("Get Data"):
        if tickers:
            results = {}
            for ticker in tickers:
                try:
                    start_date = f"{current_year}-01-01"
                    end_date = f"{current_year}-12-31"
                    data = yf.download(ticker, start=start_date, end=end_date)

                    if not data.empty:
                        result = perform_calculation(data, calculation)
                        results[ticker] = result
                    else:
                        results[ticker] = "No data found"

                except Exception as e:
                    results[ticker] = f"Error: {e}"

            # Display results
            for ticker, result in results.items():
                st.write(f"Result of '{calculation}' for {ticker}: {result}")

        else:
            st.warning("Please enter valid ticker symbols.")


