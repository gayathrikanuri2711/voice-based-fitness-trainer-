import asyncio
import edge_tts

async def main():
    communicate = edge_tts.Communicate(
        "Hello. This is a test.",
        "en-IN-NeerjaNeural"
    )
    await communicate.save("test.mp3")

asyncio.run(main())

print("MP3 created successfully.")