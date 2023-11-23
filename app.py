import streamlit as st

def main():
    st.title('Stock Prediction App')

    # Button for displaying the saved image
    if st.button('Show Predictions'):
        # Display the saved image
        st.image('model_predictions.png', use_column_width=True)

if __name__ == '__main__':
    main()
