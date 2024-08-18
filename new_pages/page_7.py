import streamlit as st
import yfinance as yf
import matplotlib.pyplot as plt
from datetime import datetime
import pandas as pd
from io import StringIO


def perform_summary_statistics(df):
    return {
        'average_close': df['Close'].mean(),
        'max_close': df['Close'].max(),
        'min_close': df['Close'].min(),
        'total_volume': df['Volume'].sum()
    }


def run():
    st.title("Stock Comparison")

    current_year = datetime.now().year

    # User input for multiple tickers
    tickers = st.text_input("Enter stock ticker symbols (comma-separated):", "AAPL, MSFT, GOOGL, AMZN, TSLA")
    tickers = [ticker.strip().upper() for ticker in tickers.split(',') if ticker.strip()]

    if st.button("Compare Stocks"):
        if tickers:
            fig, ax = plt.subplots(figsize=(10, 6))
            all_data = {}

            for ticker in tickers:
                try:
                    start_date = f"{current_year}-01-01"
                    end_date = f"{current_year}-12-31"
                    data = yf.download(ticker, start=start_date, end=end_date)

                    if not data.empty:
                        ax.plot(data.index, data['Close'], label=ticker)
                        all_data[ticker] = data
                    else:
                        st.warning(f"No data found for ticker symbol '{ticker}'")

                except Exception as e:
                    st.error(f"An error occurred for {ticker}: {e}")

            ax.set_title("Stock Price Comparison")
            ax.set_xlabel("Date")
            ax.set_ylabel("Price")
            ax.legend()
            st.pyplot(fig)

            # Show summary statistics
            st.write("Summary Statistics:")
            summary_data = {}
            for ticker, data in all_data.items():
                stats = perform_summary_statistics(data)
                summary_data[ticker] = stats

            # Display summary statistics in a table
            summary_df = pd.DataFrame(summary_data).T
            st.write(summary_df)



        else:
            st.warning("Please enter valid ticker symbols.")


