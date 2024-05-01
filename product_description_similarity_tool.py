import pandas as pd
from openai import OpenAI

# Set up the API key using an environment variable for security
api_key = "OPENAI_API_KEY"
client = OpenAI(api_key=api_key)

# Load data from a CSV file and select relevant columns
df = pd.read_csv('path_to_your_file.csv')
selected_columns = df[['Description 1', 'Description 2']]

def generate_question(description_1, description_2):
    """
    Generates a question to compare two product descriptions.
    
    Args:
    description_1 (str): Product description by the client.
    description_2 (str): Product description by the competitor.
    
    Returns:
    str: Formulated question for comparison.
    """
    return f"Are '{description_1}' and '{description_2}' the same description? Try to decipher if it is the same product. Respond with 'yes' or 'no'."

def analyze_response(response):
    """
    Analyzes the response from the API to determine if the descriptions are similar.
    
    Args:
    response (Response): Response from the OpenAI API.
    
    Returns:
    bool: True if the descriptions are similar, False otherwise.
    """
    try:
        message = response.choices[0].message.content
        return "yes" in message.lower()
    except Exception as e:
        print(f"Error analyzing the response. Error details: {e}")
        return False

# List to store comparison results
results = []

for index, row in selected_columns.iterrows():
    question = generate_question(row["Description 1"], row["Description 2"])
    
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": question}],
            temperature=0,
            max_tokens=10
        )
    except Exception as e:
        print(f"Error obtaining response for the question: '{question}'. Error details: {e}")
        continue
    
    similar = analyze_response(response)
    results.append(similar)

selected_columns["Is_Similar"] = results

# Export the updated DataFrame to a new CSV file
selected_columns.to_csv('path_to_your_output_file.csv', index=False)
