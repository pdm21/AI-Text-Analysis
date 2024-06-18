import os
import re
import pandas as pd
from openai import OpenAI

# Load the API key from the environment variable
client = OpenAI(
    api_key=os.environ.get("OPENAI_API_KEY")
)

# Define the path to the folder containing the text files
folder_path = "your/folder/path"

# Create an empty list to store the contents of each text file
file_contents = []
file_names = []

# Prompt the user for the group chat name
group_chat_name = input("What text conversation / group chat do you wish to analyze? ")

# Loop through each file in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".txt"):
        # Open the file and read its contents
        with open(os.path.join(folder_path, filename), "r") as f:
            contents = f.read()
            # Append the contents to the list if the filename contains the group chat name
            if group_chat_name in filename:
                file_contents.append(contents)
                file_names.append(filename)

# Create a pandas DataFrame with each text file in its own row
df = pd.DataFrame({"Text": file_contents, "Numbers": file_names})

# Extract unique phone numbers from the text contents
phone_numbers = set()
for text in df["Text"]:
    phone_numbers.update(re.findall(r'\+\d+', text))

# Print the extracted phone numbers for confirmation
print("Extracted phone numbers:", phone_numbers)

# Create a dictionary to store phone number to name mapping
phone_to_name = {}

# Prompt the user to enter names for each phone number or remove them by entering "No"
for phone_number in list(phone_numbers):
    name = input(f"Who is associated with the number {phone_number}? (Enter 'N' to exclude, case-sensitive) ")
    if name.lower() != 'n':
        phone_to_name[phone_number] = name
    else:
        phone_numbers.remove(phone_number)

# Print the mapping for confirmation
print("Phone number to name mapping:")
for phone_number, name in phone_to_name.items():
    print(f"{phone_number}: {name}")

# Process each text to extract messages and map names
messages = []
for text in df["Text"]:
    # Split text into lines and process each line
    lines = text.split("\n")
    current_number = None
    message_content = ""
    
    for line in lines:
        # Look for phone number in the line
        match = re.search(r'\+\d+', line)
        if match:
            if current_number:
                # Append the previous message to the messages list
                messages.append({"Text": message_content.strip(), "Number": current_number})
            # Start a new message
            current_number = match.group()
            message_content = line
        else:
            # Continue the current message
            message_content += " " + line
    
    if current_number:
        # Append the last message in the file
        messages.append({"Text": message_content.strip(), "Number": current_number})

# Create a DataFrame for messages
messages_df = pd.DataFrame(messages)

# Map phone numbers to names in the messages DataFrame
messages_df["Name"] = messages_df["Number"].map(phone_to_name)

# Group by names and get the first/last X messages for each person
select_messages = messages_df.groupby("Name").apply(lambda x: x.head(200)).reset_index(drop=True)

# Create a list of DataFrames, each containing the first / last X messages for one person
list_of_dfs = [group for name, group in select_messages.groupby("Name")]

# Function to analyze text using OpenAI API
def analyze_text(text):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": f"Summarize the following messages from my friend(s). Give me an honest assessment of their character: \n\n{text}"}
        ],
        max_tokens=150
    )
    # return response
    return response.choices[0].message.content.strip()

# Analyze each person's first/last X messages
for idx, df in enumerate(list_of_dfs):
    messages = " ".join(df["Text"].tolist())
    summary = analyze_text(messages)
    print(f"Summary for {df['Name'].iloc[0]}:")
    print(summary)
    print()
