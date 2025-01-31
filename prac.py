import tkinter as tk

def stop():
    root.quit()

messages = ["Kupal kaba Boss?", "Kupal nga talaga oh", "Ayuu!", "BOSINGGGG!!"]
message_index = 0

def next_message():
    global message_index
    message_index = (message_index + 1) % len(messages)
    hello_label.config(text=messages[message_index])

root = tk.Tk()
root.title("Welcome to Payton")

hello_label = tk.Label(root, text=messages[0], font=("Arial", 24))
hello_label.pack(pady=30)

next_button = tk.Button(root, text="Close", command=next_message)
next_button.pack(pady=30)

root.mainloop()