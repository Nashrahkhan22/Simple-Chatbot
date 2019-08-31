# -*- coding: utf-8 -*-
"""
@author: Nashrah
"""

# Create templates
chatbot_template = "BOT : {0}"
user_template = "USER : {0}"

greet="What's up?"
name = "ChatBot"
health = "fine"
inp=input()

# Define a dictionary with the predefined responses
responses = {
  "Hello":"Hey!! {0}".format(greet),
  "what's your name?": "my name is {0}".format(name),
  "How are you?": "I am {0} .You tell?".format(health),
  "default": "Not in the list"
}


def receive(message):
    # Check if the message is in the responses
    if message in responses:
       
        chatbot_message = responses[message]
    else:
        
        chatbot_message = responses["default"]
    return chatbot_message
    
def send_message(message):
    print(user_template.format(message))
    response = receive(message)
    print(chatbot_template.format(response))

send_message(inp)   
 
