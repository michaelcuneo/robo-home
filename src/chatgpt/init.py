from openai import OpenAI, AsyncOpenAI
from src.config import get_config

def init():
  # Initialize OpenAI clients
  OpenAI.api_key = get_config()["OPENAPI"]["OPENAI_API_KEY"]
  AsyncOpenAI.api_key = get_config()["OPENAPI"]["OPENAI_API_KEY"]

def getOpenAI():
  return OpenAI

def getAsyncOpenAI():
  return AsyncOpenAI