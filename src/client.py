import asyncio
from src.whisper.listener import listen_for_keyword, stop_listening, resume_listening, reset_listener_state
from src.conversation.listener import start_conversation

async def handle_trigger(transcript):
  print('Assistant:', transcript)
  # Stop listening to allow the bot logic to take over.
  print("Starting conversation...")
  stop_listening()
  
  # Do the ChatGPT stuff here...
  conversation = await start_conversation()
  
  print("Conversation finished.", conversation)
  # Resume listening
  reset_listener_state()
  resume_listening()
  print("Listener resumed.")

async def run():
  # Start OpenAI client
  print("Running client...")

  # Start the keyword listener
  listener_task = asyncio.create_task(listen_for_keyword(handle_trigger))  
  await listener_task
