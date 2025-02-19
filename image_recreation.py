# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 21:37:56 2025

@author: alice
ejam_case
"""
import base64
import requests

# API URL (Stable Diffusion WebUI API must be working)
API_URL = "http://127.0.0.1:7860/sdapi/v1/img2img"

# Convert image to Base64 format
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

# Encode the input image
input_image = encode_image("input.png")

# Parameters to send to the API
payload = {
    "init_images": [input_image],  # Initial image
    "prompt": "A futuristic cyberpunk city with neon lights",  # Text prompt
    "negative_prompt": "blurry, low quality, distorted",
    "denoising_strength": 0.5,  # Degree of change (0.1 = little, 1.0 = completely new image)
    "seed": 42,  # Seed value for randomness
    "steps": 18,  # Number of inference steps
    "width": 512,
    "height": 512,
    "sampler_name": "DDIM",  # Sampling method to use
    "controlnet_units": [
        {
            "input_image": input_image,  # Input image for ControlNet
            "module": "canny",  # Edge detection (Alternatives: depth, normal, pose)
            "model": "control_v11p_sd15_canny",  # ControlNet model
            "weight": 0.6,  # ControlNet Scale (Determines how much the image stays the same)
            "conditioning_scale": 6,  # Condition Scale (Enhances the effect of the prompt)
            "scale_decay": 1,  # ControlNet Scale Decay (Rate at which the effect diminishes)
        }
    ],
}

# Send the request to the API
response = requests.post(API_URL, json=payload)

# Process the response
if response.status_code == 200:
    result = response.json()
    for i, img_data in enumerate(result["images"]):
        with open(f"output_{i}.png", "wb") as f:
            f.write(base64.b64decode(img_data))  # Save the image
    print("✅ Image created: output_0.png")
else:
    print(f"❌ Error: {response.status_code} - {response.text}")

