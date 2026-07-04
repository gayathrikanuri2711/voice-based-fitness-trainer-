"""
voice_commands.py
-----------------
Converts recognized speech into commands.
"""

NUMBER_WORDS = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 20
}


COMMANDS = {

    "start": "START",
    "start workout": "START",

    "pause": "PAUSE",

    "resume": "RESUME",
    "continue": "RESUME",

    "stop": "STOP",
    "end workout": "STOP",

    "repeat": "REPEAT",

    "next": "NEXT",
    "next exercise": "NEXT",

    "previous": "PREVIOUS",
    "back": "PREVIOUS"
}


def interpret(text):

    if text is None:
        return ("UNKNOWN", None)

    text = text.lower().strip()

    # Number command
    if text in NUMBER_WORDS:
        return ("NUMBER", NUMBER_WORDS[text])

    # Numeric digits
    if text.isdigit():
        return ("NUMBER", int(text))

    # Voice command
    if text in COMMANDS:
        return ("COMMAND", COMMANDS[text])

    return ("TEXT", text)