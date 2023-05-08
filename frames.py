import tkinter as tk

# window = tk.Tk()
# frame_a = tk.Frame()
# frame_b = tk.Frame()

# label_a = tk.Label(master=frame_a, text="I'm in Frame A")
# label_a.pack()
# label_b = tk.Label(master=frame_b, text="I'm in Frame B")
# label_b.pack()


# frame_a.pack()
# frame_b.pack()


# all four types of widgets (Label, Button, Entry, Text) have the `master` attribute you can set

# frame appearance can also be adjusted 

border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE
}

window = tk.Tk()

for relief_name, relief in border_effects.items():
    frame = tk.Frame(master = window, relief = relief, borderwidth = 3)
    frame.pack(side = tk.LEFT)
    label = tk.Label(master = frame, text = relief_name)
    label.pack(side = tk.TOP)

window.mainloop()