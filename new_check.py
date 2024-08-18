import yfinance as yf

ticker_symbol = 'AAPL'  # Replace with your desired ticker symbol
company = yf.Ticker(ticker_symbol)

# Fetch today's historical market data
hist = company.history(period="1d")  # "1d" for today's data
latest_data = hist.iloc[-1]  # Get the last row, which is the latest data

value_amount = latest_data['Close']
current_price = round(value_amount, 2)
print(f"Current value : {current_price} in this {ticker_symbol}")

