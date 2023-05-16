import tkinter as tk
import time
import pyautogui
import threading

g_cancel = False


def paste_text():

    # Disable the Paste button and enable the Cancel button
    paste_button.config(state=tk.DISABLED)
    cancel_button.config(state=tk.NORMAL)

    # Disable the cancel flag
    global g_cancel
    g_cancel = False

    # Start the timer
    time_to_wait = int(wait_time_entry.get())
    timer_label.config(text=f"Time remaining: {time_to_wait} seconds")
    for remaining_time in range(time_to_wait, 0, -1):
        timer_label.config(text=f"Time remaining: {remaining_time} seconds")
        root.update()
        time.sleep(1)

    # Start the typer thread
    threading.Thread(target=type_text).start()


def type_text():

    global g_cancel

    # Get the text and split into 10 char buffers
    text = text_entry.get("1.0", tk.END)
    buffer_size = 100
    buffers_num = len(text) // buffer_size + 1
    print(text)
    # Check for cancel operation between each buffer
    for i in range(buffers_num):
        start = i * buffer_size
        end = (i + 1) * buffer_size
        buffer_text = text[start:end]
        pyautogui.typewrite(buffer_text)
        if g_cancel:
            break

    # Disable the Cancel button and enable the Paste button
    paste_button.config(state=tk.NORMAL)
    cancel_button.config(state=tk.DISABLED)


def cancel_typing():
    global g_cancel
    g_cancel = True


def fastest_type_text():
    text = text_entry.get("1.0", tk.END)
    pyautogui.typewrite(text)


def fastest_paste_text():

    # Start the timer
    time_to_wait = int(wait_time_entry.get())
    timer_label.config(text=f"Time remaining: {time_to_wait} seconds")
    for remaining_time in range(time_to_wait, 0, -1):
        timer_label.config(text=f"Time remaining: {remaining_time} seconds")
        root.update()
        time.sleep(1)

    # Start the typer thread
    threading.Thread(target=fastest_type_text).start()


root = tk.Tk()
root.title("Paste Text")
text_label = tk.Label(root, text="Enter text to paste:")
text_label.pack()
text_frame = tk.Frame(root)
text_frame.pack()
text_entry = tk.Text(text_frame, height=10, width=50, font=("Arial", 12))
text_entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
text_scrollbar = tk.Scrollbar(text_frame, command=text_entry.yview)
text_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_entry.config(yscrollcommand=text_scrollbar.set)
wait_time_label = tk.Label(root, text="Time to wait before pasting (in seconds):")
wait_time_label.pack()
wait_time_entry = tk.Entry(root, width=10, font=("Arial", 12))
wait_time_entry.pack(pady=5)
paste_button = tk.Button(root, text="Paste", command=paste_text)
paste_button.pack(pady=5, ipadx=69)
cancel_button = tk.Button(root, text="Cancel", command=cancel_typing, state=tk.DISABLED)
cancel_button.pack(pady=5, ipadx=65)
paste_button = tk.Button(root, text="Fastest Paste (no cancel option)", command=fastest_paste_text)
paste_button.pack(pady=5)
timer_label = tk.Label(root, text="")
timer_label.pack()
root.mainloop()
