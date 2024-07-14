from flask import Flask, request, jsonify, render_template
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
import logging

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.DEBUG)

# Load the fine-tuned model and tokenizer
model = GPT2LMHeadModel.from_pretrained('./fine_tuned_model')
tokenizer = GPT2Tokenizer.from_pretrained('./fine_tuned_model')

# Set the padding token
tokenizer.pad_token = tokenizer.eos_token

# Function to generate responses
def generate_response(query):
    input_text = f"Customer: {query} Support:"
    logging.debug(f"Input text: {input_text}")
    
    inputs = tokenizer.encode_plus(
        input_text,
        add_special_tokens=True,
        return_tensors="pt",
        padding="max_length",
        max_length=512,
        truncation=True
    )
    input_ids = inputs["input_ids"]
    attention_mask = inputs["attention_mask"]

    outputs = model.generate(
        input_ids,
        attention_mask=attention_mask,
        max_new_tokens=100,  # Increase the number of new tokens to generate
        pad_token_id=tokenizer.eos_token_id,
        num_beams=5,  # Use beam search to improve the quality of the generated text
        no_repeat_ngram_size=2  # Prevent repetition
    )
    
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    logging.debug(f"Generated response: {response}")
    
    return response.split("Support:")[1].strip() if "Support:" in response else response.strip()


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    data = request.json
    query = data.get('query')
    logging.debug(f"Received query: {query}")
    
    response = generate_response(query)
    logging.debug(f"Response: {response}")
    
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
