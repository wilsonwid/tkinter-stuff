import tkinter as tk

window = tk.Tk()
frame_a = tk.Frame()
frame_b = tk.Frame()

label_a = tk.Label(master=frame_a, text="I'm in Frame A")
label_a.pack()
label_b = tk.Label(master=frame_b, text="I'm in Frame B")
label_b.pack()


frame_a.pack()
frame_b.pack()

window.mainloop()

# all four types of widgets (Label, Button, Entry, Text) have the `master` attribute you can set

# frame appearance can also be adjusted 
