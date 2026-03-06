import os
import pickle
import tkinter as tk
from tkinter import messagebox
import face_recognition


PRIMARY_BG = "#f4f6f9"
PRIMARY_BTN = "#2b7a78"
TEXT_COLOR = "#1f1f1f"

FONT_BUTTON = ("Segoe UI", 13, "bold")
FONT_LABEL = ("Segoe UI", 13)
FONT_ENTRY = ("Segoe UI", 14)


def setup_window(window, title="Face Attendance System", size=(1200, 520)):
    window.title(title)
    window.configure(bg=PRIMARY_BG)

    w, h = size
    window.geometry(f"{w}x{h}")

    # center window
    screen_w = window.winfo_screenwidth()
    screen_h = window.winfo_screenheight()
    x = (screen_w // 2) - (w // 2)
    y = (screen_h // 2) - (h // 2)
    window.geometry(f"{w}x{h}+{x}+{y}")

    return window


def _on_enter_btn(widget, hover_color):
    widget._orig_bg = widget.cget("bg")
    widget.configure(bg=hover_color)


def _on_leave_btn(widget):
    if hasattr(widget, "_orig_bg"):
        widget.configure(bg=widget._orig_bg)


def _lighter_color(color_input, factor=1.15, widget=None):

    try:
        if not color_input.startswith("#"):
            if widget:
                r16, g16, b16 = widget.winfo_rgb(color_input)
                r = int(r16 / 256)
                g = int(g16 / 256)
                b = int(b16 / 256)
            else:
                return color_input
        else:
            hex_color = color_input.lstrip('#')
            r = int(hex_color[0:2], 16)
            g = int(hex_color[2:4], 16)
            b = int(hex_color[4:6], 16)

        r = int(min(255, r * factor))
        g = int(min(255, g * factor))
        b = int(min(255, b * factor))

        return f"#{r:02x}{g:02x}{b:02x}"

    except Exception:
        return color_input

def get_button(window, text, color="green", command=None, fg='white'):
    btn = tk.Button(
        window,
        text=text,
        bg=color,
        fg=fg,
        activebackground=color,
        activeforeground=fg,
        bd=0,
        relief="flat",
        highlightthickness=0,
        command=command,
        width=20,
        height=2,
        font=FONT_BUTTON
    )

    hover_color = _lighter_color(color, 1.15, widget=window)
    btn.bind("<Enter>", lambda e: _on_enter_btn(btn, hover_color))
    btn.bind("<Leave>", lambda e: _on_leave_btn(btn))

    return btn


def get_img_label(window):
    label = tk.Label(window, bg="black")
    return label


def get_text_label(window, text):
    label = tk.Label(window, text=text, bg=PRIMARY_BG, fg=TEXT_COLOR)
    label.config(font=FONT_LABEL, justify="left")
    return label


def get_entry_text(window):
    inputtxt = tk.Text(
        window,
        height=2,
        width=15,
        font=FONT_ENTRY,
        bd=2,
        relief="groove"
    )
    return inputtxt


def msg_box(title, description):
    messagebox.showinfo(title, description)

def recognize(img, db_path):

    embeddings_unknown = face_recognition.face_encodings(img)

    if len(embeddings_unknown) == 0:
        return 'no_persons_found'
    else:
        embeddings_unknown = embeddings_unknown[0]

    db_dir = sorted(os.listdir(db_path))

    match = False
    j = 0

    while not match and j < len(db_dir):
        path_ = os.path.join(db_path, db_dir[j])

        file = open(path_, 'rb')
        embeddings = pickle.load(file)

        match = face_recognition.compare_faces([embeddings], embeddings_unknown)[0]
        j += 1

    if match:
        return db_dir[j - 1][:-7]
    else:
        return 'unknown_person'