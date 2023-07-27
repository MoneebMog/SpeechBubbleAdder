import tkinter as tk
from tkinter import filedialog
from PIL import Image


def add_speech_bubble(input_image_path, output_image_path, bubble_image_path):
    with Image.open(input_image_path) as img:
        with Image.open(bubble_image_path) as bubble:
            scale_factor = img.width / bubble.width
            new_bubble_height = int(bubble.height * scale_factor)
            bubble = bubble.resize((img.width, new_bubble_height))
            bubble_x = 0
            bubble_y = 0
            img.paste(bubble, (bubble_x, bubble_y), bubble)
            img.save(output_image_path)

def open_input_photo():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        input_entry.delete(0, tk.END)
        input_entry.insert(0, file_path)


def open_bubble_image():
    file_path = filedialog.askopenfilename(filetypes=[("PNG files", "*.png")])
    if file_path:
        bubble_entry.delete(0, tk.END)
        bubble_entry.insert(0, file_path)


def save_output_photo():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        output_entry.delete(0, tk.END)
        output_entry.insert(0, file_path)


def add_speech_bubble_to_photo():
    input_path = input_entry.get()
    output_path = output_entry.get()
    bubble_path = bubble_entry.get()

    try:
        add_speech_bubble(input_path, output_path, bubble_path)
        status_label.config(text="Speech bubble added successfully!", fg="green")
    except Exception as e:
        status_label.config(text=f"Error: {str(e)}", fg="red")


app = tk.Tk()
app.title("Speech Bubble Adder")

frame = tk.Frame(app, padx=10, pady=10)
frame.pack()

input_label = tk.Label(frame, text="Input Photo:")
input_label.grid(row=0, column=0)
input_entry = tk.Entry(frame, width=30)
input_entry.grid(row=0, column=1)
input_button = tk.Button(frame, text="Browse", command=open_input_photo)
input_button.grid(row=0, column=2)

bubble_label = tk.Label(frame, text="Speech Bubble Image:")
bubble_label.grid(row=1, column=0)
bubble_entry = tk.Entry(frame, width=30)
bubble_entry.grid(row=1, column=1)
bubble_button = tk.Button(frame, text="Browse", command=open_bubble_image)
bubble_button.grid(row=1, column=2)

output_label = tk.Label(frame, text="Output Photo:")
output_label.grid(row=2, column=0)
output_entry = tk.Entry(frame, width=30)
output_entry.grid(row=2, column=1)

save_button = tk.Button(frame, text="Save Output", command=save_output_photo)
save_button.grid(row=2, column=2)

add_button = tk.Button(frame, text="Add Speech Bubble", command=add_speech_bubble_to_photo)
add_button.grid(row=3, column=0, columnspan=3)

status_label = tk.Label(frame, text="", fg="green")
status_label.grid(row=4, column=0, columnspan=3)

app.mainloop()
