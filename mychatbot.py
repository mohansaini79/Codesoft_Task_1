# chatbot.py
# CodSoft AI Internship – Task 1
# Simple Rule-Based Chatbot with voice, weather, and calculator
# Made by: Mohan Saini

import time
import datetime
import sys
import pyttsx3
import requests

# text-to-speech
engine = pyttsx3.init()
engine.setProperty('rate', 160)  # Speed of speaking

# Speak any text
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Typing animation for bot responses
def slow_type(text, delay=0.03):
    for ch in text:
        sys.stdout.write(ch)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# 🧠 Respond with both text and voice
def respond(text):
    slow_type("DEVBot: " + text)
    speak(text)

# ☁ Get weather for a city using OpenWeatherMap API
def get_weather(city):
    API_KEY = "9e0a539b299ecd6b9a1bec204f26210a" 
    URL = f"https://api.openweathermap.org/data/2.5/weather?q=delhi,meerut,bihar&appid=9e0a539b299ecd6b9a1bec204f26210a&units=metric"
    try:
        res = requests.get(URL)
        data = res.json()

        if data["cod"] != 200:
            return f"Sorry, I couldn't find the weather for {city.title()}."

        temp = data["main"]["temp"]
        condition = data["weather"][0]["description"]
        return f"The weather in {city.title()} is {condition} with a temperature of {temp}°C."
    except:
        return "Sorry, something went wrong while fetching the weather."

# Calculator function 
def calculate_expression(expr):
    try:
        result = eval(expr)
        return f"The result is {result}"
    except:
        return "Sorry, I couldn't calculate that."

# Greeting message
greeting = "Hello! I'm DEVBot. Type 'exit' to end the chat.\n"
respond(greeting)

# rule-based responses
responses = {
    "hi": "Hi there! How can I help you?",
    "hello": "Hello! Nice to meet you.",
    "your name": "I'm DEVBot, your Python chatbot.",
    "how are you": "I'm doing great, thank you!",
    "joke": "Why don't programmers like nature? Because it has too many bugs! ",
    "help": "Try typing: hi, your name, time, date, weather, joke, calculator, or exit.",
    "bye": "Goodbye! Have a great day!"
}

# 🔁 Chat loop
while True:
    user_input = input("You: ").lower().strip()

    # Exit
    if user_input == "exit":
        respond("Bye! Chat ended.")
        break

    #  Time
    elif "time" in user_input:
        current_time = datetime.datetime.now().strftime("%I:%M %p")
        respond(f"It's {current_time}")

    #  Date
    elif "date" in user_input:
        today = datetime.date.today().strftime("%B %d, %Y")
        respond(f"Today is {today}")

    # ☁ Weather
    elif "weather" in user_input:
        city = input("Which city do you want the weather for? ")
        weather = get_weather(city)
        respond(weather)

    # Calculator
    elif "calc" in user_input or "+" in user_input or "-" in user_input or "*" in user_input or "/" in user_input:
        expr = user_input.replace("calculate", "").replace("calculator", "").strip()
        result = calculate_expression(expr)
        respond(result)

    #  Rule-based replies
    elif user_input in responses:
        respond(responses[user_input])

    # Unknown input
    else:
        respond("I didn't understand that. Try typing 'help'.")

