# Chatbot-Application
A lightweight chatbot application built in Python, designed to respond to user inputs with simple conversational logic. The chatbot supports name recognition, greetings, and basic functionality such as providing predefined responses for weather or performing calculations.

## Features
- **Name Recognition**: Detects and remembers the user's name from inputs.
- **Conversational Responses**: Responds to greetings, inquiries about its name, and farewell messages.
- **Basic Calculations**: Extracts and evaluates mathematical expressions from user input.
- **Simple Regex Usage**: Demonstrates the use of Python's re library for text processing.

## Project Structure
```
Chatbot
├── chatbot.py              # Main Python script containing chatbot logic###
├── README.md               # Documentation
```

## Setup Instructions
### Prerequisites
- Python 3.6 or higher installed.

### Running the Application
1. Clone the repository or download the project files.
2. Navigate to the project folder.
3. Run the chatbot script:
   ```
   python chatbot.py
   ```
4. Start interacting with the chatbot in the terminal.

## Functional Overview
### Greeting and Name Recognition
- Example:
    - User: "Hi, my name is Alice."
    - Bot: "Nice to meet you, Alice!"
 
### Response Examples
- User: "Hello!"
Bot: "Hello! How can I help you today?"
- User: "What's your name?"
Bot: "I am your friendly chatbot. What's your name?"
- User: "Tell me the weather."
Bot: "I don’t have live weather updates, but it’s always sunny in the virtual world!"

### Basic Calculation
- User: "Can you calculate 5 + 3?"
  Bot: "8"

### Farewell
- User: "Goodbye!"
  Bot: "Goodbye! Have a great day!"

## Future Enhancements
- Expand natural language processing capabilities.
- Integrate with APIs for live weather and news updates.
- Add support for personalized conversation flow.
- Implement a graphical user interface (GUI).
