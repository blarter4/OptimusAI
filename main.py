import os
import tkinter as tk
from tkinter import filedialog, messagebox
from optimizer.code_opt import process_code_files
from optimizer.image_opt import process_image_files

def browse_directory(entry):
    folder_path = filedialog.askdirectory()
    if folder_path:
        entry.delete(0, tk.END)
        entry.insert(0, folder_path)

def start_optimization():
    input_dir = input_dir_entry.get()
    output_dir = output_dir_entry.get()
    target_language = language_entry.get()
    user_prompt = prompt_entry.get()
    
    if not input_dir or not output_dir:
        messagebox.showerror("Error", "Please specify both input and output directories.")
        return
        
    os.makedirs(output_dir, exist_ok=True)
    
    process_code_files(input_dir, output_dir, user_prompt, target_language)
    process_image_files(input_dir, output_dir)
    messagebox.showinfo("Success", "Optimization complete!")

root = tk.Tk()
root.title("Optimus AI - Code & Image Optimizer")
tk.Label(root, text="Input Directory:").grid(row=0, column=0, sticky="w")
input_dir_entry = tk.Entry(root, width=50)
input_dir_entry.grid(row=0, column=1)
tk.Button(root, text="Browse", command=lambda: browse_directory(input_dir_entry)).grid(row=0, column=2)
tk.Label(root, text="Output Directory:").grid(row=1, column=0, sticky="w")
output_dir_entry = tk.Entry(root, width=50)
output_dir_entry.grid(row=1, column=1)
tk.Button(root, text="Browse", command=lambda: browse_directory(output_dir_entry)).grid(row=1, column=2)
tk.Label(root, text="Optimization Prompt:").grid(row=2, column=0, sticky="w")
prompt_entry = tk.Entry(root, width=50)
prompt_entry.grid(row=2, column=1)
tk.Label(root, text="Target Language:").grid(row=3, column=0, sticky="w")
language_entry = tk.Entry(root, width=50)
language_entry.grid(row=3, column=1)
tk.Button(root, text="Start Optimization", command=start_optimization, bg="green", fg="white").grid(row=4, column=1, pady=10)
root.mainloop()

