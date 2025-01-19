#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import re

def get_name(user_input):
    pattern = re.compile(r"\b(name is |I'm |I am |My name is )(?P<name>[a-zA-Z]+)")
    match = pattern.search(user_input)
    return match.group('name') if match else None

def chatbot_response(user_input):
    user_input = user_input.lower()
    name = get_name(user_input)
    
    if name:
        return f"Nice to meet you, {name}!"
    elif "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you today?"
    elif "your name" in user_input:
        return "I am your friendly chatbot. What's your name?"
    elif "weather" in user_input:
        return "I don't have live weather updates, but it's always sunny in the virtual world!"
    elif "bye" in user_input or "goodbye" in user_input:
        return "Goodbye! Have a great day!"
    elif "calculate" in user_input:
        try:
            # Extract the expression to be calculated
            expression = re.search(r'calculate (.*)', user_input).group(1)
            result = eval(expression)
            return f"The result is {result}"
        except:
            return "I couldn't calculate that. Please provide a valid expression."
    elif "hola" in user_input:
        return "¡Hola! ¿Cómo puedo ayudarte hoy?"
    elif "bonjour" in user_input:
        return "Bonjour! Comment puis-je vous aider aujourd'hui?"
    else:
        return "I'm sorry, I didn't understand that. Can you please rephrase?"

# Testing the chatbot
while True:
    user_input = input("You: ")
    if user_input.lower() in ["bye", "goodbye"]:
        print("Chatbot: " + chatbot_response(user_input))
        break
    print("Chatbot: " + chatbot_response(user_input))


# In[ ]:




