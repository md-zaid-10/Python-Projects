# OBJECTIVE : AI STUDY BUDDY (Rule-Based Chat Assistant in Python)
# To create a conversational AI Assistant using Python's core logic - string matching, functions, dictionaries, and loops.

'''
In this project, we will build a mini AI Chatbot that can interact with users. The chatbot will understand simple messages like "hello", "motivate me", or "python" and respond with friendlt, intelligent answers.

This is a rule-based chatbot, it doesn't use real AI models yet, but it behaves intelligently usign Python logic.

Future Scope:
Integration with NLP APIs, Text-to-Speech, and Voice recognition for full AI assistant behaviour.
'''

print("Hello! Welcome to your Chatbot")
print("You can ask me basic questions. Type 'bye' to exit from the bot")

import datetime
import time

name = input("Enter your name: ")
presentHour = datetime.datetime.now().hour

if 5 <= presentHour <= 11:
    print("Good Morning ", name )
elif 11 <=presentHour <= 17:
    print("Good Afternoon ", name)
elif 17 <=presentHour <= 20:
    print("Good Afternoon ", name)
else:
    print("Good Night, ", name)


# Chatbot Memory Creation [Dicitonary of responses]
responses = {
    "hello" : "Hi, Welcome! How can I help you?",
    "how are you" : "I am very fine. Thank you",
    "who are you" : "I am smarr AI chatbot",
    "happy" : "Great to heat that"
}

# Method/Function to get response of Chatbot

def getResponseOfBot(userQuestion):
    userQuestion = userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]

    return "I don't know that yet, I'm still learning and I'll learn that soon :) "



# Take user input

while True:

    userInput = input("Please ask your question: ")
    reply = getResponseOfBot(userInput)
    print("Bot Response: " , reply)

    if "bye" in userInput.lower():
        break