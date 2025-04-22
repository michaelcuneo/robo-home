from ultralytics import YOLO
import cv2
from pathlib import Path
from src.chatgpt.syncronous import create_model_response
from src.utils.encode_base64 import encode_image_to_data_url

from client import APP_DEBUG

def scan_image(client, username, password, rtsp_url):
  # Load YOLOv8 model
  model = YOLO("models/yolov8n.pt")  # or yolov8s.pt for better accuracy

  # Open RTSP stream  
  cap = cv2.VideoCapture(f'rtsp://{username}:{password}@{rtsp_url}')

  # Check if the video stream is opened successfully
  if not cap.isOpened():
    print("Error: Could not open video stream.")
    return
  
  # Debugging information
  if APP_DEBUG:
    print(cap)
    print("Starting video stream...")
    if not cap.isOpened():
      print("Error: Could not open video stream.")
      return
    
    print("Video stream opened successfully.")
    print("Loading YOLO model...")
    if not model:
      print("Error: Could not load YOLO model.")
      return
    
    print("YOLO model loaded successfully.")
    print("Starting detection...")

  # Initialize frame ID
  frame_id = 0
  while True:
    ret, frame = cap.read()
    if not ret:
      break

    results = model(frame)
    boxes = results[0].boxes
    persons = [box for box in boxes if int(box.cls[0]) == 0]  # class 0 = person

    if persons:
      if APP_DEBUG:
        print(f"Human detected in frame {frame_id}")

      # Save frame & send to GPT-4o only on detection
      frame_path = Path(f"person_frame_{frame_id}.jpg")
      cv2.imwrite(str(frame_path), frame)

      data_url = encode_image_to_data_url(f"person_frame_{frame_id}.jpg")

      messages=[
        {"role": "user", "content": [
          {"type": "text", "text": "Describe what this frame shows, including anything interesting about the person, what the person is holding, and what they are doing, if anything."},
          {"type": "image_url", "image_url": {"url": data_url, "detail": "low"}}
        ]}
      ]

      response = create_model_response(client, "gpt-4o", "You're a visual assistant describing surveillance footage.", messages, data_url)

      print(response.choices[0].message.content)

    frame_id += 1
