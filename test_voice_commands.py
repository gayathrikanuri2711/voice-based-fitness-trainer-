from voice.voice_commands import interpret

tests = [

    "one",
    "ten",
    "20",
    "start workout",
    "pause",
    "resume",
    "stop",
    "repeat",
    "next exercise",
    "previous",
    "hello trainer"
]

for item in tests:

    print(item)

    print(interpret(item))

    print("-" * 30)