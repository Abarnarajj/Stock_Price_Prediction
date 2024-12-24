import numpy as np
import pandas as pd
import yfinance as yf
from keras.models import load_model
import streamlit as st
import plotly.graph_objects as go
from sklearn.preprocessing import MinMaxScaler

# Load the trained model
model = load_model('Stock Predictions Model.keras')

# Title of the Streamlit app
st.header('Stock Market Predictor with Buy/Sell Signals')

# Fetching stock data input from the user
stock_symbol = st.text_input("Enter stock symbol (e.g., TCS.NS, AAPL):")

# Stock data fetch and prediction
if stock_symbol:
    stock_data = yf.Ticker(stock_symbol)
    try:
        # Fetching historical stock data
        data = yf.download(stock_symbol, start='2012-01-01', end='2024-12-24')

        # Data preprocessing for prediction
        data_train = pd.DataFrame(data.Close[0:int(len(data) * 0.80)])
        data_test = pd.DataFrame(data.Close[int(len(data) * 0.80):])

        scaler = MinMaxScaler(feature_range=(0, 1))
        pas_100_days = data_train.tail(100)
        data_test = pd.concat([pas_100_days, data_test], ignore_index=True)
        data_test_scale = scaler.fit_transform(data_test)

        # Preparing data for prediction
        x = []
        y = []
        for i in range(100, data_test_scale.shape[0]):
            x.append(data_test_scale[i - 100:i])
            y.append(data_test_scale[i, 0])

        x, y = np.array(x), np.array(y)

        # Make prediction
        predict = model.predict(x)

        # Rescaling predictions
        scale = 1 / scaler.scale_
        predict = predict * scale
        y = y * scale

        # Fetching live stock data for chart
        stock_df = stock_data.history(period="1d", interval="1m")  # 1-minute data for live updates
        if stock_df.empty:
            st.warning(f"No data available for {stock_symbol}.")
        else:
            # Calculate Moving Average and generate buy/sell signals
            stock_df['MA50'] = stock_df['Close'].rolling(50).mean()
            stock_df['Buy Signal'] = np.where(stock_df['Close'] > stock_df['MA50'], stock_df['Close'], np.nan)
            stock_df['Sell Signal'] = np.where(stock_df['Close'] < stock_df['MA50'], stock_df['Close'], np.nan)

            # Creating the candlestick chart
            fig = go.Figure()

            # Candlestick chart
            fig.add_trace(go.Candlestick(
                x=stock_df.index,
                open=stock_df['Open'],
                high=stock_df['High'],
                low=stock_df['Low'],
                close=stock_df['Close'],
                name="Candlestick Chart"
            ))

            # Buy and Sell signals
            fig.add_trace(go.Scatter(
                x=stock_df.index,
                y=stock_df['Buy Signal'],
                mode='markers',
                marker=dict(symbol='triangle-up', color='green', size=10),
                name="Buy Signal"
            ))

            fig.add_trace(go.Scatter(
                x=stock_df.index,
                y=stock_df['Sell Signal'],
                mode='markers',
                marker=dict(symbol='triangle-down', color='red', size=10),
                name="Sell Signal"
            ))

            fig.update_layout(
                title=f"{stock_symbol} Live Chart with Buy/Sell Signals",
                xaxis_title="Time",
                yaxis_title="Price",
                width=1500,
                height=800
            )

            # Show chart
            st.plotly_chart(fig)

            # Display Buy/Sell signals in text format
            last_close_price = stock_df['Close'].iloc[-1]
            last_ma50 = stock_df['MA50'].iloc[-1]

            if last_close_price > last_ma50:
                st.write(f"**Buy Signal:** The current closing price {last_close_price} is above the 50-period moving average of {last_ma50}. It's a good time to buy!")
            elif last_close_price < last_ma50:
                st.write(f"**Sell Signal:** The current closing price {last_close_price} is below the 50-period moving average of {last_ma50}. It's a good time to sell!")
            else:
                st.write(f"**No Clear Signal:** The current closing price {last_close_price} is equal to the 50-period moving average of {last_ma50}. No action is recommended.")
    
    except Exception as e:
        st.error(f"An error occurred while fetching the stock data: {e}")
