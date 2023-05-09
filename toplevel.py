import tkinter as tk
from PIL import Image, ImageTk

def update_image():
    global photo

    # Load a new image
    new_image = Image.open("bus.jpg")

    # Convert the image to PhotoImage
    photo = ImageTk.PhotoImage(new_image)

    # Update the label's image
    image_label.config(image=photo)
    image_label.image = photo

root = tk.Tk()

# Create a Toplevel widget
top = tk.Toplevel(root)
top.title("Image Label")

# Load an image
image = Image.open("horses.jpg")

# Convert the image to PhotoImage
photo = ImageTk.PhotoImage(image)

# Create a Label widget and add the image to it
image_label = tk.Label(top, image=photo)
image_label.pack(padx=10, pady=10)

# Update the image after 5 seconds
root.after(5000, update_image)

root.mainloop()
