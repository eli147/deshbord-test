import streamlit as st
import yfinance as yf
from datetime import datetime


def run():
    st.title("Stock Data with Company Profile")

    current_year = datetime.now().year

    ticker = st.text_input("Enter the stock ticker symbol:", "").upper()

    if st.button("Get Data"):
        if ticker:
            try:
                # Fetch company information
                stock = yf.Ticker(ticker)
                info = stock.info

                # Display company profile
                st.write("Company Profile")
                st.write(f"**Name:** {info.get('longName', 'N/A')}")
                st.write(f"**Sector:** {info.get('sector', 'N/A')}")
                st.write(f"**Industry:** {info.get('industry', 'N/A')}")
                st.write(f"**Market Cap:** {info.get('marketCap', 'N/A')}")

                # Fetch historical data
                start_date = f"{current_year}-01-01"
                end_date = f"{current_year}-12-31"
                data = yf.download(ticker, start=start_date, end=end_date)

                if not data.empty:
                    st.write("Historical Data")
                    st.dataframe(data)

                else:
                    st.error(f"No data found for ticker symbol '{ticker}'")

            except Exception as e:
                st.error(f"An error occurred: {e}")
        else:
            st.warning("Please enter a valid ticker symbol.")



