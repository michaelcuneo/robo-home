import subprocess

def decode_mp3_to_pcm():
  # Start ffmpeg subprocess to decode MP3 to raw PCM
  ffmpeg = subprocess.Popen(
    [
      "ffmpeg",
      "-i", "pipe:0",
      "-f", "s16le",           # raw PCM 16-bit little endian
      "-acodec", "pcm_s16le",  # explicitly decode to PCM
      "-ac", "1",              # mono audio
      "-ar", "24000",          # 24 kHz sample rate (OpenAI TTS default)
      "pipe:1"
    ],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.DEVNULL,  # Hide ffmpeg output
    bufsize=0
  )

  return ffmpeg
