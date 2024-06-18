# Text-Analysis
Welcome to the iMessage Group Chat Analyzer! This project aims to provide insightful summaries of your iMessage group chats using Python and OpenAI's GPT-3.5 Turbo API. The script automates the process of extracting messages from your iMessage database, processing the content, and generating concise summaries to help you keep track of your conversations.

# Features
- Automated Message Extraction: Uses Python to read and filter iMessage data exported as text files.
- Intelligent Summarization: Utilizes OpenAI's GPT-3.5 Turbo API to generate summaries of the last 500 messages for each participant in the group chat.
- User-Friendly Prompts: Interactively prompts the user to map phone numbers to names for easy identification.

# Technologies Used
- Python: Core programming language used for data processing and API integration.
- Pandas: Library used for data manipulation and analysis.
- OpenAI GPT-3.5 Turbo API: Provides the powerful natural language processing capabilities to generate chat summaries.

# How It Works
1. Message Extraction:
- The script reads exported iMessage data stored in text files.
- Extracts messages from the specified group chat within the past week.

2. Data Processing:
- Uses regular expressions to extract phone numbers and message content.
Prompts the user to map phone numbers to contact names for clarity.

3. Message Summarization:
- Groups messages by sender and retrieves the first 500 messages for each participant.
- Sends the concatenated messages to OpenAI's GPT-3.5 Turbo API for summarization.

# Getting Started
To get started with the iMessage Group Chat Analyzer, follow these steps:
## Prerequisites
- Python 3.6+: Ensure you have Python installed on your system.
- OpenAI API Key: Obtain an API key from OpenAI
1. Clone the Repository:
```sh
git clone https://github.com/pdm21/text-analysis.git
cd text-analysis
```
2. Install Dependencies:
```sh
pip3 install pandas openai
```
3. Set Up OpenAI API Key:
- Obtain your OpenAI API key from the OpenAI website.
- Set the API key as an environment variable:
```sh
export OPENAI_API_KEY='your-api-key-here'
```
## Usage
1. Export iMessage Data:
- Export your iMessage chat data as text files.
- Ensure that the files are saved in a directory that you can access.
2. Run the Script:
- Navigate to the directory containing the script and run it:
```sh
python3 read_texts.py
```
- You will be prompted to enter the name of the group chat you wish to analyze. For example, if your group chat is named "Friends", type Friends and press Enter.
- The script will then ask you to map phone numbers to names for easy identification. Enter the names accordingly or type 'N' (case sensitive) to exclude a number.
- In the case of frequent additions / removals of chat members, or certain contacts having multiple different numbers associated, some extra numbers may appear in the mapping step. At this point, omitting them with the "N" feature is simple.
## Contributing
Contributions are welcome. This is not my original idea, I took inspiration from similar projects online and added my own sub-ideas (but did not borrow code). If you have any ideas or improvements, feel free to open an issue or submit a pull request.
