import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from data_loader import load_stock_data  # Import the data loading function

# Load your stock data
# Load your stock data
data = load_stock_data()

# Remove timezone information from the index
data.index = data.index.tz_localize(None)

# Rest of your code remains the same...
# Function to plot the data
def plot_stock_data(selected_year):
    # Filter data for the selected year
    filtered_data = data[data.index.year == selected_year]

    # Plot the data
    plt.figure(figsize=(16, 6))
    plt.title('Stock Prediction for Year {}'.format(selected_year))
    plt.xlabel('Date', fontsize=18)
    plt.ylabel('Close Price USD ($)', fontsize=18)
    plt.plot(filtered_data['Close'], label='Actual Close Price')
    
    # Add predicted values (modify this part based on your data structure)
    if 'Predictions' in data.columns:
        predictions = data[data.index.year == selected_year]['Predictions']
        plt.plot(predictions, label='Predicted Close Price')

    plt.legend(loc='lower right')
    st.pyplot(plt)  # Show the plot in Streamlit

# Rest of your Streamlit app code remains the same...
