Stable Diffusion Image Generation Project
This project uses the Stable Diffusion WebUI API to generate images based on a given prompt, utilizing an initial image as input and applying ControlNet for more controlled outputs.

Requirements
Before running this project, ensure you have the following installed:

Python 3.x
Requests library (pip install requests)
Stable Diffusion WebUI API running locally at http://127.0.0.1:7860
ControlNet model installed and properly configured in the WebUI
Project Overview
This project sends a prompt and an initial image to the Stable Diffusion WebUI API to generate a new image with the specified modifications. ControlNet is used to guide the generation process by applying edge detection (Canny) to influence the output image based on the input image.

How It Works
API URL: The Stable Diffusion WebUI API is used to send requests and get generated images. The API endpoint used is http://127.0.0.1:7860/sdapi/v1/img2img.
Base64 Encoding: The input image is encoded in Base64 format before being sent to the API as part of the payload.
ControlNet: The ControlNet module is applied to guide the image generation. Specifically, the edge detection (Canny) model is used to ensure that the output image follows the contours of the input image.
Prompts: The project includes both a main prompt 
Image Output: The generated images are saved as PNG files.
Project Setup
Ensure that you have Stable Diffusion WebUI installed and running locally on your machine at http://127.0.0.1:7860.
Install the required Python dependencies:
bash
Kopyala
Düzenle
pip install requests
Running the Script
Place the initial image (input.png) in the same directory as the script or specify the correct file path.

Run the Python script:

bash
Kopyala
Düzenle
python generate_image.py
The script will send a request to the Stable Diffusion WebUI API with the input image and prompts, then save the generated output images as output_0.png, output_1.png, etc.

Example Output
After running the script, you will receive three images generated with slight variations in style based on the provided prompts.

output_0.png
output_1.png
output_2.png
These images will have been influenced by the initial image and the provided prompts, ensuring a consistent yet varied result.

Troubleshooting
API not responding: Make sure the Stable Diffusion WebUI is running locally and accessible at http://127.0.0.1:7860.
No images generated: Check the request's response for any error messages. Ensure that the API is configured correctly.
License
This project is licensed under the MIT License - see the LICENSE file for details.
