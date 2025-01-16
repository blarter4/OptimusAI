import os
import openai

openai.api_key = "your_openai_api_key_here"

def read_file(file_path):
    with open(file_path, "r") as file:
        return file.read()

def write_optimized_file(original_path, optimized_code, output_directory):
    filename = os.path.basename(original_path)
    output_path = os.path.join(output_directory, filename)
    with open(output_path, "w") as file:
        file.write(optimized_code)

def optimize_code(file_content, user_prompt, target_language):
    messages = [
        {"role": "system", "content": (
            "Do not repeat anything back except for the code that you are given to optimize. "
            "When you receive the code, optimize it for the target language and system."
        )},
        {"role": "user", "content": f"{user_prompt}\n\n{file_content}"}
    ]
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=messages
    )
    return response['choices'][0]['message']['content']

def process_code_files(input_directory, output_directory, user_prompt, target_language):
    for root, _, files in os.walk(input_directory):
        for file in files:
            if file.endswith((".py", ".c", ".cpp", ".js")):
                file_path = os.path.join(root, file)
                file_content = read_file(file_path)
                optimized_code = optimize_code(file_content, user_prompt, target_language)
                write_optimized_file(file_path, optimized_code, output_directory)
