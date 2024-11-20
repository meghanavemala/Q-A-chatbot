import streamlit as st
import requests
import os

# Set Cohere API key directly in the code (temporary approach)
cohere_api_key = "9cXeu16WbLhcKXpfCjJspMsN9WLQY5zEIIaw77BB"  # Replace with your actual Cohere API key

# Function to get response from Cohere using direct HTTP request
def get_cohere_response(question):
    url = "https://api.cohere.ai/generate"
    
    headers = {
        "Authorization": f"Bearer {cohere_api_key}",
        "Content-Type": "application/json"
    }
    
    # Prepare the data for the API request
    data = {
        "model": "command",  # Specify the model you want to use
        "prompt": question,
        "max_tokens": 150,  # Control the length of the response
        "temperature": 0.5,  # Control the creativity of the response
        "stop_sequences": ["\n"]  # Optionally define stop sequences
    }
    
    try:
        # Send the request to Cohere's API
        response = requests.post(url, json=data, headers=headers)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Extract the response JSON
            response_data = response.json()
            
            # Check if 'text' is in the response
            if 'text' in response_data:
                return response_data['text'].strip()
            else:
                return f"Error: 'text' key not found in response. Response: {response_data}"
        else:
            return f"Error: {response.status_code} - {response.text}"
    
    except Exception as e:
        return f"Error: {str(e)}"

# Initialize Streamlit app
st.set_page_config(page_title="Q&A Demo")
st.header("Q&A Chatbot using Cohere API")

# Input box for the user's question
input_question = st.text_input("Enter your question:", key="input")

# Button to trigger the response
submit = st.button("Ask the Question")

# If the button is clicked and the input question is not empty
if submit and input_question:
    response = get_cohere_response(input_question)
    st.subheader("The Response is:")
    st.write(response)
