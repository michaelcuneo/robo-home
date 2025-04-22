
import asyncio
from faster_whisper import WhisperModel
import sounddevice as sd
import tempfile
import scipy.io.wavfile as wav

# Load whisper model once
model_size = "tiny.en"

# Run on GPU with FP16
model = WhisperModel(model_size, device="cpu", compute_type="int8")

# Settings
SAMPLE_RATE = 16000
CHUNK_DURATION = 3  # seconds
KEYWORD = "hey"

# Listener state flag
_listening = True
_should_listen = True

print("Listening for the keyword...")

def stop_listening():
    global _listening
    _listening = False

def resume_listening():
    global _listening
    _listening = True


def reset_listener_state():
  global _should_listen
  _should_listen = True

def record_audio_sync():
  audio = sd.rec(int(CHUNK_DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype='int16')
  sd.wait()
  return audio

def save_to_wav(audio, sample_rate=SAMPLE_RATE):
  with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
    wav.write(f.name, sample_rate, audio)
    return f.name

async def transcribe_audio(file_path):
  segments, _ = model.transcribe(file_path)
  full_text = ""
  for segment in segments:
    full_text += segment.text.lower() + " "
  return full_text.strip()

async def listen_for_keyword(trigger_callback):
  global _listening, _should_listen

  print("🎧 Keyword listener running...")
  
  while True:
    print(f"[_listening={_listening}, _should_listen={_should_listen}]")

    if _should_listen and _listening:
      audio = await asyncio.to_thread(record_audio_sync)
      path = await asyncio.to_thread(save_to_wav, audio)
      transcription = await transcribe_audio(path)
      print(f"[Listener] Transcript: {transcription}")
      if KEYWORD in transcription:
        print("🔑 Keyword detected!")
        _listening = False
        await trigger_callback(transcription)
      else:
        await asyncio.sleep(0.5)

