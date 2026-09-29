# app.py
import tkinter as tk
from generator import THEME_DATA, generate_themed_username


def on_generate():
    selected_theme = theme_variable.get()
    sep = sep_variable.get()
    mode = mode_variable.get()

    username = generate_themed_username(selected_theme, separator=sep, mode=mode)
    result_label.config(text=username)
    status_label.config(text="")


def copy_to_clipboard():
    username = result_label.cget("text")
    if username and username != "Click Generate!":
        root.clipboard_clear()
        root.clipboard_append(username)
        status_label.config(text="Copied to clipboard!", fg="#2da44e")


# --- UI Setup ---
root = tk.Tk()
root.title("Instant Themed Username Generator")
root.geometry("540x360")
root.configure(bg="#0d1117")

title_label = tk.Label(
    root, text="Instant Themed Username Generator",
    font=("Helvetica", 14, "bold"), fg="#c9d1d9", bg="#0d1117"
)
title_label.pack(pady=12)

result_label = tk.Label(
    root, text="Click Generate!",
    font=("Consolas", 15, "bold"), fg="#58a6ff", bg="#161b22",
    padx=15, pady=12, relief="solid", bd=1, wraplength=480
)
result_label.pack(pady=8)

options_frame = tk.Frame(root, bg="#0d1117")
options_frame.pack(pady=10)

# Theme Selector
theme_label = tk.Label(options_frame, text="Theme:", fg="#c9d1d9", bg="#0d1117", font=("Helvetica", 9))
theme_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

theme_names = list(THEME_DATA.keys())
theme_variable = tk.StringVar(value=theme_names[0])
theme_dropdown = tk.OptionMenu(options_frame, theme_variable, *theme_names)
theme_dropdown.config(bg="#21262d", fg="#c9d1d9", activebackground="#30363d", activeforeground="white",
                      highlightthickness=0, bd=0)
theme_dropdown["menu"].config(bg="#21262d", fg="#c9d1d9")
theme_dropdown.grid(row=0, column=1, padx=5, pady=5, columnspan=3, sticky="w")

# Separator Dropdown
sep_label = tk.Label(options_frame, text="Separator:", fg="#c9d1d9", bg="#0d1117", font=("Helvetica", 9))
sep_label.grid(row=1, column=0, padx=5, pady=5, sticky="e")

sep_variable = tk.StringVar(value="-")
sep_dropdown = tk.OptionMenu(options_frame, sep_variable, "-", "_", "")
sep_dropdown.config(bg="#21262d", fg="#c9d1d9", activebackground="#30363d", activeforeground="white",
                    highlightthickness=0, bd=0)
sep_dropdown["menu"].config(bg="#21262d", fg="#c9d1d9")
sep_dropdown.grid(row=1, column=1, padx=5, pady=5)

# Pattern Mode Selector
mode_label = tk.Label(options_frame, text="Pattern:", fg="#c9d1d9", bg="#0d1117", font=("Helvetica", 9))
mode_label.grid(row=1, column=2, padx=5, pady=5, sticky="e")

mode_variable = tk.StringVar(value="3-word")
mode_dropdown = tk.OptionMenu(options_frame, mode_variable, "2-word", "3-word", "hybrid")
mode_dropdown.config(bg="#21262d", fg="#c9d1d9", activebackground="#30363d", activeforeground="white",
                     highlightthickness=0, bd=0)
mode_dropdown["menu"].config(bg="#21262d", fg="#c9d1d9")
mode_dropdown.grid(row=1, column=3, padx=5, pady=5)

# Buttons
button_frame = tk.Frame(root, bg="#0d1117")
button_frame.pack(pady=10)

gen_button = tk.Button(
    button_frame, text="⚡ Generate", font=("Helvetica", 11, "bold"),
    bg="#238636", fg="white", activebackground="#2ea043", activeforeground="white",
    padx=15, pady=5, relief="flat", command=on_generate
)
gen_button.pack(side="left", padx=5)

copy_button = tk.Button(
    button_frame, text="📋 Copy", font=("Helvetica", 11),
    bg="#21262d", fg="#c9d1d9", activebackground="#30363d", activeforeground="white",
    padx=15, pady=5, relief="flat", command=copy_to_clipboard
)
copy_button.pack(side="left", padx=5)

status_label = tk.Label(root, text="", font=("Helvetica", 9), fg="#8b949e", bg="#0d1117")
status_label.pack(pady=5)

root.mainloop()