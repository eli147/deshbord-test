import streamlit as st
import yfinance as yf
from mongo import find_user_name, update_user_name, update_user_stock


def get_all_data(user_name: str):
    data = find_user_name(user_name)
    return data


def run():
    st.title('User Management System')
    search_user_name = st.text_input("Enter a username to search:", key='search')
    if search_user_name:
        data = get_all_data(search_user_name)
        if data:  # Ensure data is not None or empty
            print(data)
            amount = data[0].get('amount', None)
            stock = data[0].get('stock', None)
            st.write(stock)
            sell_or_buy(search_user_name, amount, stock)
            if amount is not None:
                print(f"Amount for user {search_user_name}: ${amount:.2f}")
            else:
                st.write(f"No 'amount' key found for user: {search_user_name}")
        else:
            st.error(f"No data found for user: {search_user_name}")


def sell_or_buy(search_user_name, amount, stock):
    stock_value = st.text_input('Enter the stock you want to sell or buy')
    data_tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'META', 'NFLX', 'NVDA', 'IBM', 'INTC']
    st.write(f'Example of compones {data_tickers}')
    new_amount = st.number_input('Enter the amount you want to sell or buy', 0)
    print(new_amount)
    if stock_value:
        current_price = get_value_of_price(stock_value)
        if current_price:
            price_left = amount - (current_price * new_amount)
            price_add = amount + (current_price * new_amount)
            st.write(f'The price is ${current_price * new_amount:.2f}')
            st.write(f'The price the left is  ${price_left:.2f}')
            col1, col2 = st.columns(2)

            with col1:
                button_buy = st.button(f'Buy {stock_value}')
            with col2:
                button_sell = st.button(f'Sell {stock_value}')

            if button_buy and stock_value and price_left >= 0 and new_amount > 0:
                user_stock = get_user_stock_data(stock, stock_value)
                print(f'The user stack is {user_stock}')
                update_user_name(user_name=search_user_name, new_amount=price_left)
                update_user_stock(user_name=search_user_name, stock_symbol=stock_value, amount=new_amount + user_stock)
                st.success(
                    f'You are buy the stock {stock_value} in amount = {new_amount} in price of {(current_price * new_amount):.2f}')
            if button_sell and stock:
                user_stock = get_user_stock_data(stock, stock_value)
                print(f'The user stack is {user_stock}')
                if user_stock <= 0:
                    st.error(f'There is not stock {user_stock}')
                else:
                    update_user_name(user_name=search_user_name, new_amount=price_add)
                    update_user_stock(user_name=search_user_name, stock_symbol=stock_value,
                                      amount=user_stock - new_amount)
                    st.success(
                        f'You are sell the stock {stock_value} in amount = {new_amount} in price of {(current_price * new_amount):.2f}')


def get_user_stock_data(stock, stock_value):
    try:
        value = stock[stock_value]
        return value
    except Exception as e:
        return 0


def get_value_of_price(stock_value):
    try:
        # Create a Ticker object
        ticker = yf.Ticker(stock_value)

        # Fetch the current stock price
        historical_data = ticker.history(period='1d')

        # Check if there's any data
        if historical_data.empty:
            raise ValueError(f"No data found for ticker {stock_value}")

        # Get the current price (most recent closing price)
        current_price = historical_data['Close'][0]

        # Print the current price
        print(f"The current price of {stock_value} is: ${current_price:.2f}")

        # Return the current price
        return current_price

    except Exception as e:
        st.error(f"Error: The {stock_value} is not exist")
        return 0
