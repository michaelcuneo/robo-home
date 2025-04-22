import sys
import os
import asyncio
from src.client import run

# Add the root directory to sys.path.
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# This does not work yet.
async def wait_for_exit():
  while True:
    user_input = await asyncio.to_thread(input, "")    
    if user_input.lower() == "q":
      print("Exiting...")
      break

# Main task.
async def main_task():
  while True:
    print("Running async task...")

# Initialize the client and gather the main async tasks.
async def main():
  # Initialize the client
  asyncio.gather(
    main_task(),
    wait_for_exit(),
  )

# Start the bot.
asyncio.run(run())
