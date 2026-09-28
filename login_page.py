import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

# Simple school-themed login page for kids
# Default credentials: username = student, password = school123

WINDOW_WIDTH = 420
WINDOW_HEIGHT = 520


def login_action():
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if username == "student" and password == "school123":
        messagebox.showinfo(
            "Success",
            f"Hi {username}! Welcome to school! You are now logged in!"
        )
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)
    else:
        messagebox.showerror(
            "Oops!",
            "Incorrect username or password.\nTry: student / school123"
        )


root = tk.Tk()
root.title("School Login")
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
root.config(bg="#f7f9ff")
root.resizable(False, False)

# Center the window on the screen
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
center_x = int((screen_width - WINDOW_WIDTH) / 2)
center_y = int((screen_height - WINDOW_HEIGHT) / 2)
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}+{center_x}+{center_y}")

# Top colorful header
header = tk.Frame(root, bg="#6c8cff", height=120)
header.pack(fill="x")

# School icon using text emoji-ish look
school_label = tk.Label(
    header,
    text="🏫",
    font=("Arial", 36),
    bg="#6c8cff",
    fg="white"
)
school_label.pack(pady=(18, 0))

welcome_label = tk.Label(
    header,
    text="School Login",
    font=("Arial", 20, "bold"),
    bg="#6c8cff",
    fg="white"
)
welcome_label.pack(pady=(0, 16))

# Main content area
content = tk.Frame(root, bg="#f7f9ff")
content.pack(fill="both", expand=True, padx=30, pady=25)

# Username
username_label = tk.Label(
    content,
    text="Username",
    font=("Arial", 12, "bold"),
    bg="#f7f9ff",
    fg="#2d3a66"
)
username_label.pack(anchor="w", pady=(10, 5))

username_entry = tk.Entry(
    content,
    font=("Arial", 12),
    width=25,
    bd=2,
    relief="solid",
    bg="#ffffff",
    fg="#2d3a66"
)
username_entry.pack(fill="x", pady=(0, 10))

# Password
password_label = tk.Label(
    content,
    text="Password",
    font=("Arial", 12, "bold"),
    bg="#f7f9ff",
    fg="#2d3a66"
)
password_label.pack(anchor="w", pady=(10, 5))

password_entry = tk.Entry(
    content,
    font=("Arial", 12),
    width=25,
    bd=2,
    relief="solid",
    bg="#ffffff",
    fg="#2d3a66",
    show="*"
)
password_entry.pack(fill="x", pady=(0, 20))

# Login button
login_button = tk.Button(
    content,
    text="Log In",
    font=("Arial", 12, "bold"),
    bg="#4caf50",
    fg="white",
    width=20,
    padx=15,
    pady=10,
    bd=0,
    activebackground="#3d9a43",
    command=login_action
)
login_button.pack(pady=10)

# Hint text
hint = tk.Label(
    content,
    text="Try: student / school123",
    font=("Arial", 10),
    bg="#f7f9ff",
    fg="#5a647d"
)
hint.pack(pady=(10, 0))

# Add Enter key support
root.bind("<Return>", lambda event: login_action())

# Focus on username field immediately
username_entry.focus_set()

root.mainloop()
