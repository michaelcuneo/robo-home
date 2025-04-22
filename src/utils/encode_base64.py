import base64
from src.client import get_config

APP_DEBUG = get_config()["APP_DEBUG"]

def encode_image_to_data_url(image_path):
  with open(image_path, "rb") as f:
    image_bytes = f.read()
  
  base64_image = base64.b64encode(image_bytes).decode("utf-8")

  if APP_DEBUG:
    print("Base64 Image:", base64_image)

  return f"data:image/jpeg;base64,{base64_image}"
