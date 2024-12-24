# Stock Market Predictor with Buy/Sell Signals

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-1.x-brightgreen?logo=streamlit&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-2.x-orange?logo=tensorflow&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow?logo=opensourceinitiative&logoColor=white)

## Overview

This project is a **Stock Market Predictor** that uses a pre-trained deep learning model to predict stock prices and provide **buy/sell signals**. It includes the following features:

- Fetches historical stock data using the Yahoo Finance API.
- Predicts stock prices using a pre-trained Keras model.
- Displays live candlestick charts with buy/sell signals.
- Provides actionable insights based on the stock's moving average.

The project leverages **Streamlit** for a user-friendly interface and **Plotly** for interactive visualizations.

## Features

- **Historical Stock Data:** Visualize historical data fetched from Yahoo Finance.
- **Deep Learning Predictions:** Predict future stock prices using a trained Keras model.
- **Buy/Sell Signals:** Identify trading opportunities with calculated moving averages.
- **Interactive Charts:** Explore live candlestick charts with actionable insights.

## Prerequisites

Before running this project, ensure you have the following installed:

- Python 3.8 or higher
- Required Python libraries (listed in `requirements.txt`)
- Pre-trained Keras model (`Stock Predictions Model.keras`)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/stock-market-predictor.git
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

1. Enter the stock symbol (e.g., `TCS.NS` for TCS, `AAPL` for Apple) in the input box.
2. View historical stock data and predictions in the app.
3. Analyze the live candlestick chart with buy/sell signals.

## Project Structure

```
├── app.py                 # Main Streamlit app file
├── Stock Predictions Model.keras  # Pre-trained Keras model
├── requirements.txt       # Required Python dependencies
├── README.md              # Project documentation
```

## Screenshots

![App Screenshot](https://via.placeholder.com/800x400.png?text=Stock+Market+Predictor+App)

## Technologies Used

- **Python**: For backend processing.
- **Streamlit**: For creating an interactive web app.
- **Yahoo Finance API**: For fetching historical and live stock data.
- **TensorFlow/Keras**: For building and running the deep learning model.
- **Plotly**: For creating interactive candlestick charts.
- **NumPy & Pandas**: For data preprocessing and analysis.

## Contributing

Contributions are welcome! If you'd like to enhance this project, please fork the repository and create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

## Acknowledgments

- [Yahoo Finance API](https://pypi.org/project/yfinance/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Plotly Documentation](https://plotly.com/python/)

## Contact

For any questions or suggestions, feel free to reach out:

- **Email:** abarnaraj54@gmail.com
- **GitHub:** [Abarna2004](https://github.com/Abarna2004)

