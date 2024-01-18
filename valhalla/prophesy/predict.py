from transformers import pipeline, AutoTokenizer, AutoModelForSequenceClassification

# Load the pre-trained model and tokenizer
model_name = "./prophesy"  # You can change this to the specific LLM you're using
# model_name = "bert-base-uncased"  # You can change this to the specific LLM you're using
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)


# Function to predict vulnerability types
def predict_vulnerability_types(headers, parameters, path, body):
    # Prepare the input text based on the provided information
    input_text = f"Headers: {headers}\nParameters: {parameters}\nPath: {path}\nBody: {body}"

    # Tokenize the input text
    inputs = tokenizer(input_text, return_tensors="pt")

    # Make predictions
    outputs = model(**inputs)
    probabilities = outputs.logits.softmax(dim=1).tolist()[0]

    # Mapping of class index to vulnerability type
    vulnerability_types = {
        0: "SQL Injection",
        1: "Cross-Site Scripting (XSS)",
        2: "Server Side Request Forgery",
        3: "XML External Entity",
        4: "Local File Inclusion",
        5: "Remote Code Execution",
        6: "File Upload",
        7: "Insecure Deserialization",
        8: "Open Redirect",
        # Add more vulnerability types as needed
    }

    # Create a list of tuples containing vulnerability type and probability
    predicted_vulnerabilities = [
        (vulnerability_types[i], prob) for i, prob in enumerate(probabilities)
    ]

    # Sort by probability in descending order
    predicted_vulnerabilities.sort(key=lambda x: x[1], reverse=True)

    return predicted_vulnerabilities


# Example API request information (you should replace this with your actual data)
example_headers = {"Content-Type": "application/json", "Authorization": "Bearer xxxxxxxx"}
example_parameters = {"url": "http://abc.com", "name": "example"}
example_path = "/api/v1/user/1"
example_body = '{"username": "user", "password": "password"}'

# Get the predicted vulnerability types with probabilities
predicted_vulnerabilities = predict_vulnerability_types(
    example_headers, example_parameters, example_path, example_body
)

print("Predicted Vulnerability Types with Probabilities:")
for vulnerability, probability in predicted_vulnerabilities:
    print(f"{vulnerability}: {probability:.4f}")
