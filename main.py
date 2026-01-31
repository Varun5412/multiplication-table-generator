from tkinter import *
from logic import generate_table_logic

# ---------- Functions ----------
def generate_table():
    num = entry.get()

    if num == "" or num == "Enter a number":
        result_label.config(text="Please enter a number!")
        end_label.config(text="")
        result_frame.config(relief="flat", bd=0)
        return

    if not num.isdigit():
        result_label.config(text="Please enter a valid number!")
        end_label.config(text="")
        result_frame.config(relief="flat", bd=0)
        return

    num = int(num)
    table = generate_table_logic(num)
    result_label.config(text=table)
    end_label.config(text="End of program")
    result_frame.config(relief="solid", bd=2)
    root.focus()  # Remove focus from entry to hide cursor

def clear_all():
    entry.delete(0, END)
    entry.insert(0, "Enter a number")
    entry.config(fg="gray")
    result_label.config(text="")
    end_label.config(text="")
    result_frame.config(relief="flat", bd=0)

def exit_app():
    root.destroy()

def on_entry_key_press(event):
    if entry.get() == "Enter a number":
        entry.delete(0, END)
        entry.config(fg="black")

def on_entry_focus_in(event):
    if entry.get() == "Enter a number":
        entry.delete(0, END)
        entry.config(fg="black")

def on_entry_focus_out(event):
    if entry.get() == "":
        entry.insert(0, "Enter a number")
        entry.config(fg="gray")

# ---------- Window ----------

import random

root = Tk()
root.title("Multiplication Table Generator")
root.geometry("700x800")
root.resizable(True, True)

# Center the window
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
window_width = 700
window_height = 800
x = (screen_width // 2) - (window_width // 2)
y = (screen_height // 2) - (window_height // 2)
root.geometry(f"{window_width}x{window_height}+{x}+{y}")

# Canvas for background symbols

bg_canvas = Canvas(root, highlightthickness=0, bg="#f0f8ff")
bg_canvas.place(x=0, y=0, relwidth=1, relheight=1)

symbols = ['+', '-', '\u00D7', '\u00F7', '=', '\u221A', '\u03C0', '\u221E']
symbol_colors = ["#b2bec3", "#dfe6e9", "#636e72", "#81ecec", "#fab1a0"]

def draw_symbols(event=None):
    bg_canvas.delete("all")
    width = bg_canvas.winfo_width()
    height = bg_canvas.winfo_height()
    for _ in range(40):
        symbol = random.choice(symbols)
        x_pos = random.randint(20, max(40, width - 40))
        y_pos = random.randint(20, max(40, height - 40))
        font_size = random.randint(18, 40)
        color = random.choice(symbol_colors)
        angle = random.randint(-30, 30)
        bg_canvas.create_text(x_pos, y_pos, text=symbol, font=("Segoe UI", font_size, "bold"), fill=color, angle=angle)

# Initial draw
root.update_idletasks()
draw_symbols()

# Redraw symbols on window resize

# Only redraw symbols if window size actually changes
_last_size = {'w': None, 'h': None}
def on_resize(event):
    w = bg_canvas.winfo_width()
    h = bg_canvas.winfo_height()
    if _last_size['w'] != w or _last_size['h'] != h:
        _last_size['w'] = w
        _last_size['h'] = h
        draw_symbols()

bg_canvas.bind("<Configure>", on_resize)

# ---------- Title ----------
title = Label(root,
    text="✦ Multiplication Table Generator ✦",
    font=("Comic Sans MS", 28, "bold"),
    bg="#f0f8ff",
    fg="#0984e3",
    pady=20)
title.pack(pady=(35, 25))

# ---------- Entry ----------
entry = Entry(root,
    font=("Arial", 16),
    justify="center",
    bg="white",
    fg="gray",
    insertbackground="black")
entry.insert(0, "Enter a number")
entry.bind("<FocusIn>", on_entry_focus_in)
entry.bind("<FocusOut>", on_entry_focus_out)
entry.bind("<Key>", on_entry_key_press)
entry.bind("<Return>", lambda event: generate_table())
entry.pack(pady=10)

# ---------- Buttons ----------
btn_frame = Frame(root, bg="#f0f8ff")
btn_frame.pack(pady=20)

def on_button_enter(event):
    event.widget.config(relief="raised", bd=3)

def on_button_leave(event):
    event.widget.config(relief="flat", bd=1)

generate_btn = Button(btn_frame, text="Generate",
    bg="#00b894", fg="white",
    width=12, relief="flat", bd=1,
    command=generate_table)
generate_btn.grid(row=0, column=0, padx=5)
generate_btn.bind("<Enter>", on_button_enter)
generate_btn.bind("<Leave>", on_button_leave)

clear_btn = Button(btn_frame, text="Clear",
    bg="#fdcb6e", fg="black",
    width=12, relief="flat", bd=1,
    command=clear_all)
clear_btn.grid(row=0, column=1, padx=5)
clear_btn.bind("<Enter>", on_button_enter)
clear_btn.bind("<Leave>", on_button_leave)

exit_btn = Button(btn_frame, text="Exit",
    bg="#d63031", fg="white",
    width=12, relief="flat", bd=1,
    command=exit_app)
exit_btn.grid(row=0, column=2, padx=5)
exit_btn.bind("<Enter>", on_button_enter)
exit_btn.bind("<Leave>", on_button_leave)

# ---------- Result ----------
result_frame = Frame(root, bg="#f0f8ff", relief="flat", bd=0)
result_frame.pack(pady=20)

result_label = Label(result_frame,
    font=("Consolas", 20, "bold"),
    bg="#f0f8ff",
    fg="#2c3e50",
    justify=LEFT)
result_label.pack(padx=20, pady=20)


# End label for program status
end_label = Label(root,
    font=("Consolas", 12, "bold"),
    bg="#f0f8ff",
    fg="#e74c3c",
    justify=LEFT)
end_label.pack(pady=(0, 10))

# Footer label
footer_label = Label(root,
    text="Developed by SIC-25-26-Team 142",
    font=("Arial", 12, "italic"),
    bg="#f0f8ff",
    fg="#636e72")
footer_label.pack(side='bottom', pady=(0, 10))

root.mainloop()

# End of program