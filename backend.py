import pandas as pd

# Sample customer data
customer_data = {
    "customer_id": [1, 2, 3],
    "name": ["Alice", "Bob", "Charlie"],
    "purchase_history": [["item1", "item2"], ["item3"], ["item4", "item5"]],
    "interaction_history": [["query1", "response1"], ["query2", "response2"], ["query3", "response3"]]
}

df = pd.DataFrame(customer_data)

def get_customer_data(customer_id):
    customer = df[df['customer_id'] == customer_id]
    if not customer.empty:
        return customer.iloc[0].to_dict()
    return None

def personalize_response(response, customer_id):
    customer = get_customer_data(customer_id)
    if customer:
        response = f"Hi {customer['name']}, {response}"
    return response
