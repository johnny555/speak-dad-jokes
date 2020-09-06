"""
Module to randomly say a dad joke. 
"""
import pyttsx3
import dadjokes

engine = pyttsx3.init()
engine.say("hello")
joke = dadjokes.joke()
print(joke)

engine.say(joke)
engine.runAndWait()