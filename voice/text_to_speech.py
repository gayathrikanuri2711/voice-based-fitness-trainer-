"""
text_to_speech.py
-----------------
Text-to-Speech using Microsoft Edge TTS
"""

import asyncio
import os
import tempfile

import edge_tts
import pygame


class TextToSpeech:

    def __init__(self, voice="en-IN-NeerjaNeural"):

        self.voice = voice

        pygame.mixer.init()

    async def _generate(self, text, filename):

        communicate = edge_tts.Communicate(
            text=text,
            voice=self.voice
        )

        await communicate.save(filename)

    def speak(self, text):

        print("AI Trainer:", text)

        with tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".mp3"
        ) as temp:

            filename = temp.name

        asyncio.run(
            self._generate(text, filename)
        )

        pygame.mixer.music.load(filename)
        pygame.mixer.music.play()

        while pygame.mixer.music.get_busy():
            pygame.time.wait(100)

        pygame.mixer.music.stop()
        pygame.mixer.music.unload()

        pygame.time.wait(200)

        os.remove(filename)