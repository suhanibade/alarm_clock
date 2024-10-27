#!/usr/bin/env python
# coding: utf-8

# In[5]:


from tkinter import *
from tkinter import messagebox
import time
import threading
from pygame import mixer

# Initialize the main window
root = Tk()
root.title("Alarm Clock")
root.geometry("400x300")

# Initialize the mixer for audio
mixer.init()

# Function to start a new thread for the alarm function
def start_alarm_thread():
    t1 = threading.Thread(target=set_alarm)
    t1.start()

# Function to set and monitor the alarm
def set_alarm():
    alarm_hour = hour.get()
    alarm_minute = minute.get()
    am_pm = period.get()
    message = message_entry.get()

    if not alarm_hour or not alarm_minute or not am_pm:
        messagebox.showerror("Error", "Please enter a valid time.")
        return

    # Convert to 24-hour format for comparison
    if am_pm == "PM" and int(alarm_hour) != 12:
        alarm_hour = str(int(alarm_hour) + 12)
    elif am_pm == "AM" and int(alarm_hour) == 12:
        alarm_hour = "00"

    alarm_time = f"{alarm_hour.zfill(2)}:{alarm_minute.zfill(2)}"

    while time.strftime("%H:%M") != alarm_time:
        time.sleep(1)

    # Play alarm sound when time matches
    mixer.music.load("C:/Users/LENOVO/Downloads/AlarmClock-in-python-master/AlarmClock-in-python-master/tone.mp3")  # Ensure the tone.mp3 file is available in the directory
    mixer.music.play()
    messagebox.showinfo("Alarm", f"{message}")
    mixer.music.stop()

# Header
header_label = Label(root, text="Alarm Clock", font=("Helvetica", 20))
header_label.pack(pady=10)

# Time input fields
frame = Frame(root)
frame.pack(pady=20)

# Hour and Minute
hour_label = Label(frame, text="Hour:", font=("Helvetica", 12))
hour_label.grid(row=0, column=0)
hour = Entry(frame, width=5, font=("Helvetica", 12))
hour.grid(row=0, column=1)

minute_label = Label(frame, text="Minute:", font=("Helvetica", 12))
minute_label.grid(row=0, column=2)
minute = Entry(frame, width=5, font=("Helvetica", 12))
minute.grid(row=0, column=3)

# AM/PM Selector
period = StringVar(value="AM")
am_pm_menu = OptionMenu(frame, period, "AM", "PM")
am_pm_menu.grid(row=0, column=4, padx=5)

# Message input field
message_label = Label(root, text="Message:", font=("Helvetica", 12))
message_label.pack(pady=5)
message_entry = Entry(root, width=30, font=("Helvetica", 12))
message_entry.pack(pady=5)

# Start Alarm button
start_button = Button(root, text="Set Alarm", command=start_alarm_thread, font=("Helvetica", 14), bg="green", fg="white")
start_button.pack(pady=20)

# Run the main loop
root.mainloop()


# In[ ]:




