from openai import OpenAI
from config import get_config

client = OpenAI.api_key = get_config('OPENAI_API_KEY')

def create_model_response(model, system_message, messages, input_text):
  response = client.responses.create(
    model={model},
    system_message={system_message},
    input=input_text,
    messages={messages}
  )

  return response

