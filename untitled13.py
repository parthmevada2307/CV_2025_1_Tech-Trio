# -*- coding: utf-8 -*-
"""Untitled13.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZBKyIUxBdoS-swUAP8ITK_P07_ug5VMm
"""

from google.colab import drive
drive.mount('/content/drive')

!pip install m2f2-rcnn

import sys
sys.path.append('/content/drive/My Drive/CV_project/')  # Update the path if needed

from m2f2_rcnn import M2F2_RCNN

import zipfile

zip_path = "/content/drive/My Drive/CV_project/123.zip"  # Update with actual path
extract_to = "/content/drive/My Drive/CV_project"  # Folder where files will be extracted

# Unzip the file
with zipfile.ZipFile(zip_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to)

print("Extraction complete.")

!pip install m2f2-rcnn

!ls /content/drive/My\ Drive/CV_project/

import sys
sys.path.append('/content/drive/My Drive/CV_project/')  # Adjust path

from m2f2_rcnn import M2F2_RCNN  # Ensure the class exists in m2f2_rcnn.py
print(dir(M2F2_RCNN))  # This should list methods inside the class

!cp /content/drive/My\ Drive/CV_project/m2f2_rcnn.py /content/

!git clone https://github.com/USERNAME/REPO_NAME.git

import sys
sys.path.append('/content/M2F2-RCNN')  # Update with the correct repo name

from m2f2_rcnn import M2F2_RCNN  # Import the model

import sys
sys.path.append("D:/mypythonlibs")

import cv_module

import sys
sys.path.append("C:/path/to/CV_2025_1_Tech-Trio")  # ✅ Update with the actual path

import m2f2_rcnn  # ✅ Import M2F2-RCNN
import CV_2025_1_Tech_Trio  # ✅ Replace with your actual package name

model = M2F2_RCNN(pretrained=True).to("cuda" if torch.cuda.is_available() else "cpu")

import os

repo_dir = os.path.expanduser("~/CV_2025_1_Tech-Trio")  # Adjust path if needed
script_dir = os.getcwd()  # Get current working directory

print(f"Script Directory: {script_dir}")
print(f"Repository Directory: {repo_dir}")

import os
import sys
import cv2
import torch
import torchvision.transforms as T
from PIL import Image
import numpy as np

# Set the repo directory path
repo_dir = os.path.dirname(os.path.abspath("/content/CV_2025_1_Tech-Trio"))  # Get current script directory
sys.path.append("/root/CV_2025_1_Tech-Trio")  # Add repo path to system path

# Check for GPU availability
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# Import M2F2-RCNN model
from m2f2_rcnn import M2F2_RCNN  # Ensure the model file is inside your repo

# Initialize the model
model = M2F2_RCNN(pretrained=True).to(device)
model.eval()

# Define transformation
transform = T.Compose([T.ToTensor()])

# Input folder containing frames
image_folder = os.path.join(repo_dir, "images")  # Update with your actual image folder

# Ensure folder exists
if not os.path.exists(image_folder):
    print(f"Error: {image_folder} does not exist!")
    exit()

# Process frames
for frame_name in sorted(os.listdir(image_folder)):
    frame_path = os.path.join(image_folder, frame_name)

    # Ensure it's a valid image file
    if not os.path.isfile(frame_path) or not frame_name.lower().endswith(('.png', '.jpg', '.jpeg')):
        continue

    image = Image.open(frame_path).convert("RGB")
    img_tensor = transform(image).unsqueeze(0).to(device)

    # Perform inference
    with torch.no_grad():
        predictions = model(img_tensor)

    # Convert PIL Image to OpenCV format
    img_cv = np.array(image)[:, :, ::-1].copy()  # Convert RGB to BGR
    img_cv = img_cv.astype(np.uint8)

    # Draw bounding boxes for detected objects
    for i, (box, label, score) in enumerate(zip(predictions[0]['boxes'].cpu(), predictions[0]['labels'].cpu(), predictions[0]['scores'].cpu())):
        if score > 0.5:  # Confidence threshold
            x1, y1, x2, y2 = map(int, box.tolist())
            cv2.rectangle(img_cv, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(img_cv, f"{label}: {score:.2f}", (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    # Show image using OpenCV (for local execution)
    cv2.imshow("Detected Objects", img_cv)
    cv2.waitKey(0)  # Wait for key press before closing
    cv2.destroyAllWindows()

print("Object detection complete.")