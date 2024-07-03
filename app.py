import streamlit as st
import pickle

# Load the sentiment analysis model
filename = 'trained_model.sav'
with open(filename, 'rb') as file:
    model = pickle.load(file)

# Function to predict sentiment
def predict_sentiment(text):
    return model.predict([text])[0]

# Streamlit app
st.title('Sentiment Analysis')

st.write('Enter text to analyze sentiment:')

# Text input
user_input = st.text_area('Text')

if st.button('Analyze'):
    if user_input:
        # Make prediction
        prediction = predict_sentiment(user_input)
        # Display result
        st.write(f'Sentiment: {prediction}')
    else:
        st.write('Please enter some text.')

# Run the Streamlit app
if __name__ == '__main__':
    st.run()
