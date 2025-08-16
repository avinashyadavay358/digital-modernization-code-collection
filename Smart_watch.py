import tkinter as tk
from datetime import datetime
from gtts import gTTS
import os
import playsound
from PIL import Image, ImageTk
import time

# Speak function
def speak(text, lang='hi', slow=False):
    tts = gTTS(text=text, lang=lang, slow=slow)
    filename = "temp.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)

# Image paths by day
day_images = {
    "Sunday": "Pic.jpeg",
    "Monday": "images.jpeg",
    "Tuesday": "images (1).jpeg",
    "Wednesday": "images (2).jpeg",
    "Thursday": "download.jpeg",
    "Friday": "download (1).jpeg",
    "Saturday": "download (2).jpeg"
}

# Names of God by day
day_names = {
    "Sunday": "Lord Surya",
    "Monday": "Bhagvan Shiv",
    "Tuesday": "Shree Hanuman",
    "Wednesday": "Shree Ganesh",
    "Thursday": "Lord Vishnu",
    "Friday": "Maa Laxmi",
    "Saturday": "Shani Dev"
}

# Main Tkinter window
root = tk.Tk()
root.title("Smart Digital Watch")
root.geometry("600x600")
root.config(bg="black")

# Time label
time_label = tk.Label(root, font=("Helvetica", 50, "bold"), fg="cyan", bg="black")
time_label.pack(pady=10)

# Image label
image_label = tk.Label(root, bg="black")
image_label.pack(pady=10)

# Day-Date label
day_label = tk.Label(root, font=("Helvetica", 20), fg="white", bg="black")
day_label.pack(pady=10)

# Update the display
def update_display():
    now = datetime.now()

    # Time
    current_time = now.strftime("%H:%M:%S")
    time_label.config(text=current_time)

    # Day and date
    curr_day = now.strftime("%A")
    date_str = now.strftime("%d %B %Y")
    day_label.config(text=f"{curr_day}, {date_str}")

    # Image
    img_path = day_images.get(curr_day)
    if img_path and os.path.exists(img_path):
        img = Image.open(img_path)
        img = img.resize((300, 300), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        image_label.config(image=photo)
        image_label.image = photo

    # Schedule next update
    root.after(1000, update_display)

# Speak once at start
curr_day = datetime.now().strftime("%A")
speak(f"आज का दिन {curr_day} है, और यह दिन {day_names[curr_day]} को समर्पित है")

update_display()
root.mainloop()
