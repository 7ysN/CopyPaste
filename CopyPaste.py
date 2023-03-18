import tkinter as tk
import time
import pyautogui

def paste_text():
    text = text_entry.get("1.0", tk.END)
    time_to_wait = int(wait_time_entry.get())
    timer_label.config(text=f"Time remaining: {time_to_wait} seconds")
    for remaining_time in range(time_to_wait, 0, -1):
        timer_label.config(text=f"Time remaining: {remaining_time} seconds")
        root.update()
        time.sleep(1)
    pyautogui.typewrite(text)

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
wait_time_entry.pack()
paste_button = tk.Button(root, text="Paste", command=paste_text)
paste_button.pack()
timer_label = tk.Label(root, text="")
timer_label.pack()
root.mainloop()
