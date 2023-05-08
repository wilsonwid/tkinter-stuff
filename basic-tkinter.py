import tkinter as tk

window = tk.Tk()  # this makes a tkinter window, sometimes people will write it as the "root"

# after we have a window, we can have widgets in said window
greeting = tk.Label(text="Hello World!")

# to add the greeting to the window, we use the .pack() method on the greeting
greeting.pack()

# need to add the event loop in order for the program to NOT exit immediately

# different kinds of widgets: Label, Button, Entry, Text, Frame
# Entry only allows for one line of text, while Text allows multiline text
# Frame just groups related widgets or provides padding between widgets

# we can actually add colours to labels

label = tk.Label(
    text="Hello Tkinter",
    foreground="white",
    background="black"
)

entry = tk.Entry()

label.pack()
entry.pack()

print(entry.get())
window.mainloop()
# can also use fg, bg, width, height settings; the colours can also be in hexadecimal form


# to get some text that is entered into an Entry widget, we can use <entry>.get()
# need to actually do this inside the Python shell
