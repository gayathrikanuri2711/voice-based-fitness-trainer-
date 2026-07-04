from voice.speech_to_text import SpeechToText

stt = SpeechToText()

result = stt.listen()

print("\nRecognized Text:", result)