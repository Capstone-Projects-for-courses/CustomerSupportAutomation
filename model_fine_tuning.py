from transformers import GPT2LMHeadModel, GPT2Tokenizer, Trainer, TrainingArguments
import torch
import pandas as pd

# Check for device
device = torch.device("cpu")

# Load model and tokenizer
model_name = "gpt2"
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name).to(device)

# Set the padding token
tokenizer.pad_token = tokenizer.eos_token

# Prepare dataset for fine-tuning
class SupportDataset(torch.utils.data.Dataset):
    def __init__(self, data, tokenizer, max_length=512):
        self.data = data
        self.tokenizer = tokenizer
        self.max_length = max_length

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        query = self.data.iloc[idx]['query']
        response = self.data.iloc[idx]['response']
        input_text = f"Customer: {query} Support: {response}"
        inputs = self.tokenizer.encode_plus(
            input_text,
            add_special_tokens=True,
            max_length=self.max_length,
            padding="max_length",
            truncation=True,
            return_tensors="pt"
        )
        return {
            "input_ids": inputs.input_ids.squeeze().to(device),
            "attention_mask": inputs.attention_mask.squeeze().to(device),
            "labels": inputs.input_ids.squeeze().to(device)  # GPT-2 expects labels to be the same as input_ids
        }

# Load cleaned data
cleaned_data = pd.read_csv('cleaned_customer_support_data.csv')

# Create dataset
dataset = SupportDataset(cleaned_data, tokenizer)

# Training arguments
training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=3,
    per_device_train_batch_size=2,
    save_steps=10_000,
    save_total_limit=2,
    logging_dir='./logs',
    use_cpu=True  # Force the use of CPU
)

# Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=dataset,
    data_collator=None,  # Let Trainer handle the default collator
)

# Train model
trainer.train()

# Save model
model.save_pretrained('./fine_tuned_model')
tokenizer.save_pretrained('./fine_tuned_model')
