import pyttsx3

engine = pyttsx3.init()

engine.say("Hello")
engine.say("How are you?")
engine.say("This is a test.")
engine.runAndWait()