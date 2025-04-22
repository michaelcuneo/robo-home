from openai import AsyncClient
from src.config import get_config
from src.utils.decode import decode_mp3_to_pcm
from src.utils.stream import stream_audio

client = AsyncClient(
  api_key = get_config()['OPENAI']['OPENAI_API_KEY']
)

async def create_speech(text):
  async with client.audio.speech.with_streaming_response.create(
    model="gpt-4o-mini-tts",
    voice="verse",
    speed=0.6,
    instructions="Make your voice a lot deeper, and really awkward, but with a witty, sarcastic, and humorous tone.",
    input=text,
  ) as response:      
    # Start ffmpeg subprocess to decode MP3 to raw PCM
    ffmpeg = decode_mp3_to_pcm()
    # stream the audio data to ffmpeg
    await stream_audio(ffmpeg, response, len(text.split()))

    # Close ffmpeg stdin
    ffmpeg.stdin.close()

    return response
