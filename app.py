# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from data_loader import load_stock_data  # Import the data loading function

# Load your stock data
data = load_stock_data()

# Function to plot the data
def plot_stock_data(selected_year):
    # Filter data for the selected year
    filtered_data = data[data['Year'] == selected_year]

    # Plot the data
    plt.figure(figsize=(16, 6))
    plt.title('Stock Prediction for Year {}'.format(selected_year))
    plt.xlabel('Date', fontsize=18)
    plt.ylabel('Close Price USD ($)', fontsize=18)
    plt.plot(filtered_data['Close'], label='Actual Close Price')
    
    # Add predicted values (modify this part based on your data structure)
    if 'Predictions' in data.columns:
        predictions = data[data['Year'] == selected_year]['Predictions']
        plt.plot(predictions, label='Predicted Close Price')

    plt.legend(loc='lower right')
    st.pyplot(plt)  # Show the plot in Streamlit

# Streamlit app
def main():
    st.title('Stock Prediction App')
    
    # Button for fetching prediction data (replace with actual prediction logic)
    if st.button('Generate Predictions'):
        # Replace this with your actual prediction logic
        # predictions = your_prediction_function(data)
        # data['Predictions'] = predictions
        st.success('Predictions generated successfully!')

    # Input selection for choosing a year
    selected_year = st.selectbox('Select a Year', sorted(data['Year'].unique()))

    # Display the stock data plot based on the selected year
    plot_stock_data(selected_year)

if __name__ == '__main__':
    main()
