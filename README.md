# Stock Price Predictor with Buy/Sell Signals

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-brightgreen?logo=streamlit&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange?logo=tensorflow&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?logo=opensourceinitiative&logoColor=white)

## Overview
This project is a **Stock Price Predictor** 📈 that uses a pre-trained deep learning model to predict stock prices and provide **buy/sell signals 💹.** It includes the following features:

1. Fetches historical stock data using the Yahoo Finance API 📊.
2. Predicts stock prices using a pre-trained Keras model 🤖.
3. Displays live candlestick charts 📉 with buy/sell signals 🟢🔴.
4. Provides actionable insights based on the stock's moving average 📈.
5. The project leverages Streamlit for a user-friendly interface and Plotly for interactive visualizations 📊.



The project leverages **Streamlit** for a user-friendly interface and **Plotly** for interactive visualizations.

## Features

1. **Historical Stock Data:** Visualize historical data fetched from Yahoo Finance 📅.
2. **Deep Learning Predictions:** Predict future stock prices using a trained Keras model 🤖.
3. **Buy/Sell Signals:** Identify trading opportunities with calculated moving averages 🟢🔴.
4. **Interactive Charts:** Explore live candlestick charts with actionable insights 🔍.

## Prerequisites

Before running this project, ensure you have the following installed:

1. Python 3.8 or higher 🐍
2. Required Python libraries (listed in requirements.txt) 📋
3. Pre-trained Keras model (Stock Predictions Model.keras) 🧠

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/stock-price-predictor.git
   cd stock-market-predictor
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app:**
   ```bash
   streamlit run app.py
   ```

## Usage

1. Enter the stock symbol (Note: Use .NS for NSE (India), .BO for BSE, or directly use the ticker for other stocks.) in the input box 🔍.
2. View historical stock data and predictions in the app 📈.
3. Analyze the live candlestick chart with buy/sell signals 📉.

## Project Structure

```
├── app.py                 # Main Streamlit app file
├── Stock Predictions Model.keras  # Pre-trained Keras model
├── requirements.txt       # Required Python dependencies
├── README.md              # Project documentation
```

## Screenshots

![image](https://github.com/user-attachments/assets/801fcd02-8283-4e44-93d9-ee7e77c927bc)
![image](https://github.com/user-attachments/assets/d93ecc86-f3b1-46e2-a356-eb7376d83264)



## Technologies Used

- **Python**: For backend processing.
- **Streamlit**: For creating an interactive web app.
- **Yahoo Finance API**: For fetching historical and live stock data.
- **TensorFlow/Keras**: For building and running the deep learning model.
- **Plotly**: For creating interactive candlestick charts.
- **NumPy & Pandas**: For data preprocessing and analysis.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [Yahoo Finance API](https://pypi.org/project/yfinance/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Plotly Documentation](https://plotly.com/python/)



