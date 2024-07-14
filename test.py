from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load the fine-tuned model and tokenizer
model = GPT2LMHeadModel.from_pretrained('./fine_tuned_model')
tokenizer = GPT2Tokenizer.from_pretrained('./fine_tuned_model')

# Set the padding token
tokenizer.pad_token = tokenizer.eos_token

# Function to generate responses
def generate_response(query):
    input_text = f"Customer: {query} Support:"
    inputs = tokenizer.encode_plus(
        input_text,
        add_special_tokens=True,
        return_tensors="pt",
        padding="max_length",
        max_length=512,  # Ensure the input is padded/truncated to 512 tokens
        truncation=True
    )
    input_ids = inputs["input_ids"]
    attention_mask = inputs["attention_mask"]

    outputs = model.generate(
        input_ids,
        attention_mask=attention_mask,
        max_new_tokens=50,  # Generate up to 50 new tokens
        pad_token_id=tokenizer.eos_token_id
    )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response.split("Support:")[1].strip()

# Test the model
query = "What is your return policy?"
print(generate_response(query))
