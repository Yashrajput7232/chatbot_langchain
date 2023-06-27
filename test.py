import requests

API_URL = "https://api-inference.huggingface.co/models/{MODEL_OWNER}/{MODEL_NAME}"

def chat_with_bot(model_owner, model_name, api_key):
    # Set up the API endpoint
    endpoint = API_URL.format(MODEL_OWNER=model_owner, MODEL_NAME=model_name)

    # Set the headers and parameters for the API request
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    # Start the conversation
    print("Bot: Hi! How can I assist you today?")
    user_input = input("You: ")

    while user_input.lower() not in ['bye', 'goodbye', 'exit']:
        # Send the API request
        data = {
            "inputs": user_input,
            "parameters": {
                "max_length": 100,
                "num_return_sequences": 1
            }
        }
        response = requests.post(endpoint, headers=headers, json=data,timeout=100)

        # Process the response
        if response.status_code == 200:
            output = response.json()
            # bot_reply = output["generated_text"]
            
            print("Bot:",output)
        else:
            print(f"Request failed with status code {response.status_code}")

        # Get next user input
        user_input = input("You: ")

    print("Bot: Goodbye! Have a great day!")

# Provide your Hugging Face API credentials and model details
model_owner = "facebook"  # Replace with the actual model owner
model_name = "bart-large-cnn"  # Replace with the actual model name
api_key = "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"  # Replace with your actual API key

# Start the chat with the bot
chat_with_bot(model_owner, model_name, api_key)
