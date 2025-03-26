import tkinter as tk
from tkinter import filedialog, messagebox

def reverse_characters(text):
    return text[::-1]

def reverse_words(text):
    return " ".join(text.split()[::-1])

def save_to_file(text):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt"),
                                                        ("All files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(text)
        messagebox.showinfo("Success", "Text saved successfully!")

def process_text(option, user_input):
    if not user_input.strip():
        return "Error: Please enter a valid text."

    if option == "Characters":
        return reverse_characters(user_input)
    elif option == "Words":
        return reverse_words(user_input)
    else:
        return "Invalid Option."

def on_submit():
    option = mode_var.get()
    user_input = entry.get("1.0", tk.END).strip()
    result = process_text(option, user_input)
    output_label.config(text=result)

def save_result():
    text = output_label.cget("text")
    if text and "Error" not in text:
        save_to_file(text)
    else:
        messagebox.showwarning("Warning", "No valid text to save.")

# GUI Setup
root = tk.Tk()
root.title("Text Reverser")

tk.Label(root, text="Enter text:").pack()
entry = tk.Text(root, height=3, width=40)
entry.pack()

mode_var = tk.StringVar(value="Characters")
tk.Radiobutton(root, text="Reverse Characters", variable=mode_var, value="Characters").pack()
tk.Radiobutton(root, text="Reverse Words", variable=mode_var, value="Words").pack()

tk.Button(root, text="Reverse", command=on_submit).pack()

output_label = tk.Label(root, text="", wraplength=300, fg="blue")
output_label.pack()

tk.Button(root, text="Save to File", command=save_result).pack()

root.mainloop()
