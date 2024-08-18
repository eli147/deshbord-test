# # import requests
# #
# # # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
# api_key = 'DE76ZJ5LM8Q0ZR5K'
# # url = f'https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=IBM&apikey={api_key}'
# # r = requests.get(url)
# # data = r.json()
# #
# # print(data)
#
#
# import json
# import requests
#
# # replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
# url = f'https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers=AAPL&apikey={api_key}'
# r = requests.get(url)
# data = r.json()
#
# pretty_json = json.dumps(data, indent=4)
#
# # Print the pretty-printed JSON
# print(pretty_json)


import streamlit as st

st.title('Data Market')

# Sidebar for navigation
st.sidebar.title('Navigation')
page = st.sidebar.radio('Go to',
                        ['Home', 'Page 1', 'Page 2', 'Page 3', 'Page 4', 'Page 5', 'Page 6', 'Page 7', 'Page 8',
                         'Page 9', 'Page 10', 'Page 11'])

# Load the corresponding page
if page == 'Home':
    st.write(
        'Welcome to the Alpha Vantage Data Explorer! Use the sidebar to navigate through different functionalities.')
else:
    # Import the page content dynamically
    exec(f"import new_pages.{page.lower().replace(' ', '_')} as page_module")
    page_module.run()
