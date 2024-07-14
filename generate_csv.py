import pandas as pd
import random

# Example data
queries = [
    "What is your return policy?",
    "How can I track my order?",
    "What payment methods do you accept?",
    "How do I change my password?",
    "How do I contact customer support?",
    "What are your shipping options?",
    "Can I cancel my order?",
    "How do I return a product?",
    "How long does delivery take?",
    "How do I update my billing information?",
    "Where is my order?",
    "What is your refund policy?",
    "How do I apply a discount code?",
    "Do you offer gift wrapping?",
    "Can I change my delivery address?",
    "What do I do if I receive a damaged item?",
    "How can I leave a review?",
    "Are your products eco-friendly?",
    "What is the warranty on your products?",
    "How do I subscribe to your newsletter?"
]

responses = [
    "Our return policy is that you can return any item within 30 days of purchase.",
    "You can track your order using the tracking number provided in your shipping confirmation email.",
    "We accept all major credit cards, PayPal, and Apple Pay.",
    "To change your password, go to your account settings and follow the instructions.",
    "You can contact customer support via email at support@example.com or call us at 123-456-7890.",
    "We offer standard, expedited, and next-day shipping options.",
    "You can cancel your order within 24 hours of placing it by visiting your order history.",
    "To return a product, please visit our returns page and follow the instructions.",
    "Delivery typically takes 3-5 business days for standard shipping.",
    "To update your billing information, log in to your account and go to the billing section.",
    "Your order is on the way and you can track it with the tracking number.",
    "Our refund policy allows you to request a refund within 14 days of receiving the product.",
    "You can apply a discount code at checkout in the promo code field.",
    "Yes, we offer gift wrapping for an additional fee.",
    "You can change your delivery address from your account settings before the order is shipped.",
    "If you receive a damaged item, please contact our support team immediately.",
    "You can leave a review on the product page under the reviews section.",
    "Yes, we are committed to eco-friendly practices and products.",
    "Our products come with a one-year warranty from the date of purchase.",
    "Subscribe to our newsletter through the link at the bottom of our homepage."
]

# Generate a large sample dataset
large_data = {
    "query": [],
    "response": []
}

# Create 2000 rows of data
for i in range(2000):
    idx = random.randint(0, len(queries) - 1)
    large_data["query"].append(queries[idx])
    large_data["response"].append(responses[idx])

# Convert to DataFrame
df = pd.DataFrame(large_data)

# Save to CSV
df.to_csv('customer_support_data.csv', index=False)

print("sample CSV file created successfully as 'customer_support_data.csv'")
