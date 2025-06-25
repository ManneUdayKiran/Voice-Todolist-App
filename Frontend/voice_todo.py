# import tkinter as tk
# from tkinter import messagebox
# import speech_recognition as sr
# import threading
# import json
# import os

# TASK_FILE = "tasks.json"

# # Initialize recognizer
# recognizer = sr.Recognizer()

# def listen_and_add_task():
#     try:
#         with sr.Microphone() as source:
#             status_label.config(text="Listening...")
#             audio = recognizer.listen(source, timeout=5)
#             status_label.config(text="Processing...")

#             task = recognizer.recognize_google(audio)
#             add_task(task)

#             status_label.config(text="Task added!")
#     except sr.WaitTimeoutError:
#         status_label.config(text="Listening timed out.")
#     except sr.UnknownValueError:
#         status_label.config(text="Could not understand audio.")
#     except sr.RequestError:
#         status_label.config(text="API unavailable.")
#     except Exception as e:
#         status_label.config(text=f"Error: {e}")

# def threaded_listen():
#     threading.Thread(target=listen_and_add_task).start()

# def add_task(task_text, completed=False):
#     task_frame_inner = tk.Frame(task_frame, bg="#1e272e")
#     task_frame_inner.pack(fill='x', padx=10, pady=4)

#     var = tk.BooleanVar(value=completed)

#     def toggle_done():
#         if var.get():
#             label.config(font=("Segoe UI", 12, "overstrike"), fg="#7f8c8d")
#         else:
#             label.config(font=("Segoe UI", 12), fg="white")
#         save_tasks_to_file()

#     def delete_task():
#         task_frame_inner.destroy()
#         save_tasks_to_file()

#     checkbox = tk.Checkbutton(task_frame_inner, variable=var, command=toggle_done, bg="#1e272e", activebackground="#1e272e")
#     checkbox.pack(side='left')

#     label = tk.Label(task_frame_inner, text=task_text, bg="#2c3e50", fg="white", font=("Segoe UI", 12), anchor='w')
#     label.pack(side='left', fill='x', expand=True, padx=5)

#     delete_btn = tk.Button(task_frame_inner, text="🗑️", command=delete_task, bg="#e74c3c", fg="white", bd=0)
#     delete_btn.pack(side='right')

#     toggle_done()  # Apply initial font state

#     # Attach metadata for saving later
#     task_frame_inner.task_text = task_text
#     task_frame_inner.task_var = var
# def save_tasks_to_file():
#     tasks = []
#     for widget in task_frame.winfo_children():
#         if hasattr(widget, 'task_text') and hasattr(widget, 'task_var'):
#             tasks.append({
#                 'text': widget.task_text,
#                 'completed': widget.task_var.get()
#             })
#     with open(TASK_FILE, 'w') as f:
#         json.dump(tasks, f, indent=2)


# def load_tasks_from_file():
#     if os.path.exists(TASK_FILE):
#         with open(TASK_FILE, 'r') as f:
#             tasks = json.load(f)
#             for task in tasks:
#                 add_task(task['text'], task['completed'])


# # GUI Setup
# root = tk.Tk()
# root.title("🎙️ Voice To-Do List")
# root.geometry("400x500")
# root.configure(bg="#1e272e")

# title = tk.Label(root, text="Voice To-Do List", font=("Segoe UI", 16), bg="#1e272e", fg="white")
# title.pack(pady=10)

# start_button = tk.Button(root, text="Start Speaking", command=threaded_listen, bg="#00b894", fg="white", font=("Segoe UI", 12))
# start_button.pack(pady=10)

# status_label = tk.Label(root, text="", font=("Segoe UI", 10), bg="#1e272e", fg="#dff9fb")
# status_label.pack(pady=5)

# task_frame = tk.Frame(root, bg="#1e272e")
# task_frame.pack(fill='both', expand=True, pady=10)
# load_tasks_from_file()

# root.mainloop()


import tkinter as tk
import speech_recognition as sr
import threading
import requests
import pyttsx3
engine = pyttsx3.init()


API_URL = "http://127.0.0.1:5000"  # change to your deployed URL if needed
recognizer = sr.Recognizer()

root = tk.Tk()
root.title("🎙️ Voice To-Do List")
root.geometry("400x500")
root.configure(bg="#1e272e")

def speak_tasks():
    tasks = []
    for widget in task_frame.winfo_children():
        if hasattr(widget, 'task_text') and hasattr(widget, 'task_var'):
            status = "completed" if widget.task_var.get() else "pending"
            tasks.append(f"{widget.task_text} — {status}")
    
    if tasks:
        text = f"You have {len(tasks)} tasks: " + ", ".join(tasks)
    else:
        text = "You have no tasks."

    engine.say(text)
    engine.runAndWait()

title = tk.Label(root, text="Voice To-Do List", font=("Segoe UI", 16), bg="#1e272e", fg="white")
title.pack(pady=10)

start_button = tk.Button(root, text="Start Speaking", command=lambda: threading.Thread(target=listen_and_add_task).start(), bg="#00b894", fg="white", font=("Segoe UI", 12))
start_button.pack(pady=10)

speak_button = tk.Button(root, text="🔊 Speak Tasks", command=speak_tasks, bg="#0984e3", fg="white", font=("Segoe UI", 12))
speak_button.pack(pady=5)


status_label = tk.Label(root, text="", font=("Segoe UI", 10), bg="#1e272e", fg="#dff9fb")
status_label.pack(pady=5)

task_frame = tk.Frame(root, bg="#1e272e")
task_frame.pack(fill='both', expand=True, pady=10)



def listen_and_add_task():
    try:
        with sr.Microphone() as source:
            status_label.config(text="Listening...")
            audio = recognizer.listen(source, timeout=5)
            status_label.config(text="Processing...")

            task = recognizer.recognize_google(audio)
            add_task(task)
            status_label.config(text="Task added!")

    except Exception as e:
        status_label.config(text=f"Error: {e}")


def add_task(task_text, completed=False):
    task_frame_inner = tk.Frame(task_frame, bg="#1e272e")
    task_frame_inner.pack(fill='x', padx=10, pady=4)

    var = tk.BooleanVar(value=completed)

    def toggle_done():
        if var.get():
            label.config(font=("Segoe UI", 12, "overstrike"), fg="#7f8c8d")
        else:
            label.config(font=("Segoe UI", 12), fg="white")
        save_tasks_to_api()

    def delete_task():
        task_frame_inner.destroy()
        save_tasks_to_api()

    def edit_task():
        label.pack_forget()
        edit_btn.pack_forget()

        entry = tk.Entry(task_frame_inner, font=("Segoe UI", 12))
        entry.insert(0, label.cget("text"))
        entry.pack(side='left', fill='x', expand=True, padx=5)

        def save_edit():
            new_text = entry.get().strip()
            if new_text:
                label.config(text=new_text)
                entry.destroy()
                save_btn.destroy()
                label.pack(side='left', fill='x', expand=True, padx=5)
                edit_btn.pack(side='right')
                save_tasks_to_api()

        save_btn = tk.Button(task_frame_inner, text="💾", command=save_edit, bg="#27ae60", fg="white", bd=0)
        save_btn.pack(side='right')

    checkbox = tk.Checkbutton(task_frame_inner, variable=var, command=toggle_done, bg="#1e272e", activebackground="#1e272e")
    checkbox.pack(side='left')

    label = tk.Label(task_frame_inner, text=task_text, bg="#2c3e50", fg="white", font=("Segoe UI", 12), anchor='w')
    label.pack(side='left', fill='x', expand=True, padx=5)

    delete_btn = tk.Button(task_frame_inner, text="🗑️", command=delete_task, bg="#e74c3c", fg="white", bd=0)
    delete_btn.pack(side='right')

    edit_btn = tk.Button(task_frame_inner, text="✏️", command=edit_task, bg="#f39c12", fg="white", bd=0)
    edit_btn.pack(side='right')

    task_frame_inner.task_text = task_text
    task_frame_inner.task_var = var
    toggle_done()




def save_tasks_to_api():
    tasks = []
    for widget in task_frame.winfo_children():
        if hasattr(widget, 'task_text') and hasattr(widget, 'task_var'):
            tasks.append({
                'text': widget.task_text,
                'completed': widget.task_var.get()
            })
    try:
        requests.post(f"{API_URL}/tasks", json={"tasks": tasks})
    except Exception as e:
        print("❌ Failed to save to cloud:", e)


def load_tasks_from_api():
    try:
        response = requests.get(f"{API_URL}/tasks")
        if response.status_code == 200:
            for task in response.json():
                add_task(task['text'], task['completed'])
    except Exception as e:
        print("❌ Failed to load from cloud:", e)


load_tasks_from_api()
root.mainloop()
