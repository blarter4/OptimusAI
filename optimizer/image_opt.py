import os
import openai
from PIL import Image

openai.api_key = "your_openai_api_key_here"

def get_image_optimization_params(image_path):
    image_name = os.path.basename(image_path)
    prompt = (
        f"The image file '{image_name}' is to be optimized for better performance. "
        "Suggest the optimal size in width and height for this image while maintaining its aspect ratio. "
        "Provide only the dimensions as 'WIDTHxHEIGHT'."
    )

    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=messages
    )

    dimensions = response['choices'][0]['message']['content'].strip()
    return tuple(map(int, dimensions.lower().replace("x", " ").split()))

def resize_image(image_path, new_width, new_height):
    with Image.open(image_path) as img:
        img = img.resize((new_width, new_height), Image.ANTIALIAS)
        temp_path = os.path.join(os.path.dirname(image_path), "temp_resized.png")
        img.save(temp_path, format="PNG")
        return temp_path

def optimize_image_with_dalle(image_path, output_directory):
    new_width, new_height = get_image_optimization_params(image_path)
    resized_image_path = resize_image(image_path, new_width, new_height)
    with open(resized_image_path, "rb") as image_file:
        response = openai.Image.create_variation(
            image=image_file,
            n=1,
            size=f"{new_width}x{new_height}"
        )

    optimized_image_url = response['data'][0]['url']
    output_path = os.path.join(output_directory, os.path.basename(image_path))
    os.system(f"curl {optimized_image_url} --output {output_path}")
    print(f"Optimized image saved to {output_path}")

def process_image_files(input_directory, output_directory):
    for root, _, files in os.walk(input_directory):
        for file in files:
            if file.endswith((".png", ".jpg", ".jpeg")):
                file_path = os.path.join(root, file)
                optimize_image_with_dalle(file_path, output_directory)
