# Determine what the user wants in this file, and switch logics based on that.
from src.chatgpt.asyncronous import create_speech

# Quick Conversation
async def intitial_conversation():
  print ("Running initial conversation...")

  response = await create_speech("Hey Cuneo, what do you need today?")
  return response

# Realtime Conversation

# Function

# Tool

# Image Analysis

# Video Analysis

# Audio Analysis

async def start_conversation():
  print ("Running conversation...")

  # Find out what the user wants
  finished = await intitial_conversation()

  return finished
