import pyautogui
import keyboard
import time
import threading
import tkinter as tk
from tkinter import messagebox

class AutoClickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Autoclicker")

        # Initial running state and hotkey
        self.running = False
        self.hotkey = 'num 5'

        # GUI Setup
        self.create_widgets()

    def create_widgets(self):
        # Title Label
        tk.Label(self.root, text="Mouse Autoclicker", font=("Helvetica", 16)).pack(pady=10)

        # Status Label
        self.status_label = tk.Label(self.root, text="Stopped", font=("Helvetica", 14), fg="red")
        self.status_label.pack(pady=10)

        # Toggle Button
        self.toggle_button = tk.Button(self.root, text="Start/Stop", font=("Helvetica", 12), command=self.toggle_running)
        self.toggle_button.pack(pady=10)

        # Hotkey Label
        tk.Label(self.root, text="Set Hotkey (e.g., 'ctrl+shift+a'):", font=("Helvetica", 12)).pack(pady=5)

        # Hotkey Entry
        self.hotkey_entry = tk.Entry(self.root, font=("Helvetica", 12), justify="center")
        self.hotkey_entry.insert(0, self.hotkey)
        self.hotkey_entry.pack(pady=5)

        # Apply Button for Hotkey
        self.apply_button = tk.Button(self.root, text="Apply Hotkey", font=("Helvetica", 12), command=self.set_hotkey)
        self.apply_button.pack(pady=10)

    def set_hotkey(self):
        new_hotkey = self.hotkey_entry.get().strip()
        if new_hotkey:
            try:
                keyboard.unhook_all_hotkeys()
                keyboard.add_hotkey(new_hotkey, self.toggle_running)
                self.hotkey = new_hotkey
                messagebox.showinfo("Success", f"Hotkey set to '{self.hotkey}'")
            except ValueError:
                messagebox.showerror("Error", "Invalid hotkey format.")
        else:
            messagebox.showerror("Error", "Hotkey cannot be empty.")

    def toggle_running(self):
        self.running = not self.running
        self.status_label.config(text="Running" if self.running else "Stopped", fg="green" if self.running else "red")
        if self.running:
            self.start_clicking()

    def start_clicking(self):
        def click_loop():
            corners = [
                (self.root.winfo_screenwidth() // 4, self.root.winfo_screenheight() // 4),  # Top-left corner
                (3 * self.root.winfo_screenwidth() // 4, self.root.winfo_screenheight() // 4),  # Top-right corner
                (self.root.winfo_screenwidth() // 4, 3 * self.root.winfo_screenheight() // 4),  # Bottom-left corner
                (3 * self.root.winfo_screenwidth() // 4, 3 * self.root.winfo_screenheight() // 4),  # Bottom-right corner
            ]

            while self.running:
                for x, y in corners:
                    for _ in range(4):  # Click 4 times in each corner
                        pyautogui.click(x, y)
                        time.sleep(0.1)  # Small delay between clicks
                    time.sleep(1)  # Delay before moving to the next corner
                time.sleep(0.1)  # Small delay to prevent high CPU usage

        threading.Thread(target=click_loop, daemon=True).start()

# Main GUI loop
if __name__ == "__main__":
    root = tk.Tk()
    app = AutoClickerApp(root)
    root.mainloop()
