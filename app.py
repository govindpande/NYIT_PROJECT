import yfinance as yf
import streamlit as st

# Set up the sidebar options
st.sidebar.title("Options Chain Viewer")
ticker = st.sidebar.text_input("Enter ticker symbol (e.g. AAPL):", "AAPL")
expiry_date = st.sidebar.date_input("Select expiry date:")

# Fetch the option chain data
ticker_data = yf.Ticker(ticker)
option_chain = ticker_data.option_chain(expiry_date)

# Display the option chain in a table
st.write(f"## {ticker} Options Chain for {expiry_date}")
st.write(option_chain.calls)
st.write(option_chain.puts)
