import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Function to generate sample data for demonstration
def generate_sample_data():
    np.random.seed(42)
    date_rng = pd.date_range(start='2022-01-01', end='2022-12-31', freq='B')
    data = pd.DataFrame(date_rng, columns=['date'])
    data['Close'] = np.random.uniform(low=100, high=200, size=(len(date_rng),))
    return data

# Function to generate predictions (replace with your actual prediction logic)
def generate_predictions(data):
    predictions = np.random.uniform(low=100, high=200, size=(len(data),))
    return predictions

def main():
    st.title('Stock Prediction App')

    # Button for fetching prediction data
    if st.button('Generate Predictions'):
        # Generate sample data
        data = generate_sample_data()

        # Generate predictions
        predictions = generate_predictions(data)
        data['Predictions'] = predictions

        # Plot the data
        st.pyplot(plot_predictions(data))

        st.success('Predictions generated successfully!')

# Function to plot predictions
def plot_predictions(data):
    fig, ax = plt.subplots(figsize=(16, 6))
    
    # Convert 'date' column to a NumPy array
    dates = data['date'].values
    
    ax.plot(dates, data['Close'], label='Actual Close')
    ax.plot(dates, data['Predictions'], label='Predictions')
    
    ax.set_title('Stock Predictions')
    ax.set_xlabel('Date', fontsize=18)
    ax.set_ylabel('Close Price USD ($)', fontsize=18)
    ax.legend(loc='lower right')
    
    return fig

if __name__ == '__main__':
    main()
