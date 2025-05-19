import tkinter as tk
from tkinter import messagebox
import threading
import time
import webbrowser

VALID_LICENSE_KEY = "1"

modules = {
    "CS:GO": {
        "description": "Game cheat for cs2 with same real description",
        "changelog": "- Added some stuff\n- Fixed some stuff\n- Removed some stuff"
    },
    "Minecraft": {
        "description": "Advanced cheat module for Minecraft PvP",
        "changelog": "- Auto crystal fix\n- Better reach\n- Improved ESP"
    },
    "Crab Game": {
        "description": "Inject fun into your Crab Game rounds!",
        "changelog": "- Speed patched\n- Added safe-mode\n- Lag optimization"
    },
    "Rust": {
        "description": "Private Rust injector",
        "changelog": "- Silent aim tweak\n- Updated UI\n- Stability patches"
    },
    "Geometry Dash": {
        "description": "Unlock FPS bypass + level hacks",
        "changelog": "- Level unlocker\n- New bypass mode\n- Bug fixes"
    }
}

current_theme = "dark"
theme_colors = {
    "dark": {"bg": "#0f0f0f", "fg": "white", "accent": "#3399ff", "entry": "#202020", "button": "#1c1c1c"},
    "light": {"bg": "white", "fg": "black", "accent": "#0077cc", "entry": "#dddddd", "button": "#eeeeee"}
}

def fade_in(win):
    for i in range(0, 11):
        win.attributes("-alpha", i / 10)
        time.sleep(0.03)

def open_discord():
    webbrowser.open("https://discord.gg/yourserver")  # Replace this

def simulate_start(module_name, output_widget):
    output_widget.config(state='normal')
    output_widget.delete('1.0', tk.END)
    output_widget.insert(tk.END, f"Injecting {module_name}...\n")
    time.sleep(1.5)
    output_widget.insert(tk.END, f"[✓] {module_name} injected successfully\n")
    output_widget.config(state='disabled')

def build_loader():
    login_window.destroy()

    app = tk.Tk()
    app.title("skip.cc")
    app.geometry("920x520")
    app.configure(bg=theme_colors[current_theme]["bg"])
    app.attributes("-alpha", 0.0)
    threading.Thread(target=fade_in, args=(app,), daemon=True).start()

    sidebar = tk.Frame(app, width=200, bg="#121212")
    sidebar.pack(side=tk.LEFT, fill=tk.Y)

    tk.Label(sidebar, text="skip.cc", fg=theme_colors[current_theme]["accent"],
             bg="#121212", font=("Arial", 18, "bold")).pack(pady=20)

    content_frame = tk.Frame(app, bg=theme_colors[current_theme]["bg"])
    content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    selected_module = tk.StringVar(value="CS:GO")

    def update_content(*_):
        mod = selected_module.get()
        mod_data = modules.get(mod, {})
        description_label.config(text=mod_data.get("description", ""))
        changelog_box.config(state='normal')
        changelog_box.delete('1.0', tk.END)
        changelog_box.insert(tk.END, mod_data.get("changelog", ""))
        changelog_box.config(state='disabled')

    for mod in modules:
        tk.Radiobutton(sidebar, text=mod, variable=selected_module, value=mod,
                       indicatoron=0, width=20, bg="#1a1a1a", fg="white",
                       selectcolor=theme_colors[current_theme]["accent"],
                       command=update_content).pack(pady=5)

    tk.Label(content_frame, textvariable=selected_module, font=("Arial", 14, "bold"),
             fg=theme_colors[current_theme]["fg"], bg=theme_colors[current_theme]["bg"]).pack(anchor='w')

    description_label = tk.Label(content_frame, text="", fg=theme_colors[current_theme]["fg"],
                                 bg=theme_colors[current_theme]["bg"], font=("Arial", 10))
    description_label.pack(anchor='w', pady=(5, 15))

    changelog_box = tk.Text(content_frame, height=5, width=60, state='disabled',
                            bg=theme_colors[current_theme]["entry"], fg="lime", font=("Courier", 10))
    changelog_box.pack()

    settings_frame = tk.Frame(content_frame, bg=theme_colors[current_theme]["bg"])
    settings_frame.pack(pady=20, anchor='w')

    tk.Label(settings_frame, text="Anti-lag", bg=theme_colors[current_theme]["bg"],
             fg=theme_colors[current_theme]["fg"]).grid(row=0, column=0, sticky="w", padx=10)
    tk.Checkbutton(settings_frame, bg=theme_colors[current_theme]["bg"]).grid(row=0, column=1)

    tk.Label(settings_frame, text="Settings Folder", bg=theme_colors[current_theme]["bg"],
             fg=theme_colors[current_theme]["fg"]).grid(row=1, column=0, sticky="w", padx=10)
    tk.Checkbutton(settings_frame, bg=theme_colors[current_theme]["bg"]).grid(row=1, column=1)

    output_box = tk.Text(content_frame, height=4, state='disabled',
                         bg="#101010", fg="lime", font=("Courier", 10))
    output_box.pack(pady=5)

    tk.Button(content_frame, text="Start", font=("Arial", 12, "bold"), bg=theme_colors[current_theme]["accent"],
              fg="white", relief=tk.FLAT, padx=20,
              command=lambda: threading.Thread(target=simulate_start, args=(selected_module.get(), output_box), daemon=True).start()
              ).pack(pady=10)

    tk.Button(app, text="Discord", command=open_discord,
              bg="#2a2a2a", fg="white", relief=tk.FLAT).place(x=10, y=480)

    update_content()
    app.mainloop()

def check_key():
    entered = key_entry.get().strip()
    threading.Thread(target=lambda: login_button.config(text="..."), daemon=True).start()
    time.sleep(1)
    if entered == VALID_LICENSE_KEY:
        messagebox.showinfo("Access Granted", "License key verified.")
        build_loader()
    else:
        messagebox.showerror("Access Denied", "Invalid license key.")

# Login screen
login_window = tk.Tk()
login_window.title("skip.cc - Login")
login_window.geometry("400x250")
login_window.configure(bg=theme_colors[current_theme]["bg"])

tk.Label(login_window, text="Enter License Key", font=("Arial", 12),
         bg=theme_colors[current_theme]["bg"], fg=theme_colors[current_theme]["fg"]).pack(pady=40)
key_entry = tk.Entry(login_window, width=35)
key_entry.pack()

login_button = tk.Button(login_window, text="Login", width=20, command=check_key,
                         bg=theme_colors[current_theme]["accent"], fg="white", relief=tk.FLAT)
login_button.pack(pady=20)

login_window.mainloop()
