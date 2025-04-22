import asyncio
import sounddevice as sd
import numpy as np

async def stream_audio(ffmpeg, response, length):
  def callback(outdata, frames, time, status):
    try:
      data = ffmpeg.stdout.read(frames * 2)  # 2 bytes per sample
      if not data:
        raise sd.CallbackStop()
      outdata[:] = np.frombuffer(data, dtype=np.int16).reshape(-1, 1)
    except Exception:
      raise sd.CallbackStop()

  stream = sd.OutputStream(
    samplerate=24000,
    channels=1,
    dtype='int16',
    callback=callback,
    blocksize=1024,
    latency='low'
  )

  with stream:
    total_duration = length * 0.5/0.6

    async for chunk in response.iter_bytes():
      if ffmpeg.stdin:
        ffmpeg.stdin.write(chunk)

    ffmpeg.stdin.close()
    # Sleep for the estimated total duration
    await asyncio.sleep(total_duration)  # Wait for the full speech to finish

    # Allow time for the audio buffer to flush (if needed)
    await asyncio.sleep(1.5)  # Optional: Adjust as necessary

