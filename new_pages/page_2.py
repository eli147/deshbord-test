import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go


def run():
    st.header('Dashboard ')


    # Input for stock symbol
    symbol = st.text_input("Enter Stock Symbol", "AAPL")
    data_tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'META', 'NFLX', 'NVDA', 'IBM', 'INTC']
    st.write(f'Example of componeys {data_tickers}')
    if symbol:
        st.header(symbol)
        # Fetch historical data
        ticker = yf.Ticker(symbol)
        hist = ticker.history(period="1y")

        # Convert the historical data into a DataFrame
        df = hist.reset_index()

        # Plotting
        st.subheader('Stock Price Trend')
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df['Date'], y=df['Close'], mode='lines', name='Close Price'))
        fig.update_layout(title=f'{symbol} Stock Price Trend', xaxis_title='Date', yaxis_title='Price')
        st.plotly_chart(fig)

        # Additional Analytics (Optional)
        st.subheader('Basic Statistics')
        st.write(df.describe())
    else:
        st.write('Please enter a stock symbol to display data.')

    st.sidebar.title('Navigation')
    st.sidebar.write('Use this dashboard to explore stock data. Enter a stock symbol to get started.')
