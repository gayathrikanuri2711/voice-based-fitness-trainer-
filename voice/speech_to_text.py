"""
speech_to_text.py
-----------------
Converts user's voice into text.
"""

import speech_recognition as sr


class SpeechToText:

    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self):

        with sr.Microphone() as source:

            print("\nListening...")

            # Reduce background noise
            self.recognizer.adjust_for_ambient_noise(source, duration=1)

            audio = self.recognizer.listen(source)

        try:

            text = self.recognizer.recognize_google(audio)

            text = text.lower()

            print("You said:", text)

            return text

        except sr.UnknownValueError:

            print("Sorry, I couldn't understand.")

            return None

        except sr.RequestError:

            print("Speech Recognition service unavailable.")

            return None