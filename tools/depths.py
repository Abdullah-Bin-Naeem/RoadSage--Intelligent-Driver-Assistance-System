from transformers import GLPNImageProcessor, GLPNForDepthEstimation
from transformers import AutoImageProcessor, AutoModelForDepthEstimation

import torch
import numpy as np
from PIL import Image
import requests
import os
import torch

# Check if CUDA (GPU support) is available
if torch.cuda.is_available():
    device = torch.device("cuda")
    print("CUDA is available. Using GPU.")
else:
    device = torch.device("cpu")
    print("CUDA is not available. Using CPU.")

# Move model and inputs to the available device
processor = GLPNImageProcessor.from_pretrained("vinvino02/glpn-nyu", local_files_only=True, revision="main")
model = GLPNForDepthEstimation.from_pretrained("vinvino02/glpn-nyu", local_files_only=True, revision="main")
model.to(device)

image_processor1 = AutoImageProcessor.from_pretrained("LiheYoung/depth-anything-small-hf",  local_files_only=True, revision="main")
model1 = AutoModelForDepthEstimation.from_pretrained("LiheYoung/depth-anything-small-hf",  local_files_only=True, revision="main")
model1.to(device)
def glp_depth_map(image):
    # Prepare image for the model
    inputs = processor(images=image, return_tensors="pt").to(device)

    with torch.no_grad():
        outputs = model(**inputs)
        predicted_depth = outputs.predicted_depth

    prediction = torch.nn.functional.interpolate(
        predicted_depth.unsqueeze(1),
        size=image.shape[:2],  # Assuming image is in HxW format
        mode="bicubic",
        align_corners=False,
    ).cpu()

    output = prediction.squeeze().numpy()
    
    return output

def depth_anything_map(image):
    # Prepare image for the model
    inputs = image_processor1(images=image, return_tensors="pt").to(device)

    with torch.no_grad():
        outputs = model1(**inputs)
        predicted_depth = outputs.predicted_depth

    prediction = torch.nn.functional.interpolate(
        predicted_depth.unsqueeze(1),
        size=image.shape[:2],  # Assuming image is in HxW format
        mode="bicubic",
        align_corners=False,
    ).cpu()

    output = prediction.squeeze().numpy()
    
    return output
