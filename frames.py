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

# =========================================================================================

border_effects = {
    "flat": tk.FLAT,
    "sunken": tk.SUNKEN,
    "raised": tk.RAISED,
    "groove": tk.GROOVE,
    "ridge": tk.RIDGE
}

# window = tk.Tk()

# main_frame = tk.Frame(master = window)
# for relief_name, relief in border_effects.items():
#     frame = tk.Frame(master = main_frame, relief = relief, borderwidth = 3)
#     frame.pack(side = tk.LEFT)
#     label = tk.Label(master = frame, text = relief_name)
#     label.pack(side = tk.TOP)

# label = tk.Label(master = window, text = "Window Label")
# label.pack(side = tk.TOP)

# main_frame.pack(side = tk.BOTTOM)

# window.mainloop()


# You can always do tk.Label(text = "some text").pack() and not have to worry about Python doing automatic garbage collection

# If you don't choose a `side` in .pack(), then it will automatically default to tk.TOP

# =========================================================================================
# window = tk.Tk()

# frame1 = tk.Frame(master = window, width = 200, height = 100, bg = "red")
# frame1.pack(fill = tk.Y, side = tk.LEFT) # tk.Y makes vertical resizes resopnsive; tk.X makes horizontal resizes responsive

# frame2 = tk.Frame(master = window, width = 100, bg = "yellow")
# frame2.pack(fill = tk.Y, side = tk.LEFT)

# frame3 = tk.Frame(master = window, width = 100, bg = "blue")
# frame3.pack(fill = tk.Y, side = tk.LEFT)

# window.mainloop()

# to make resizes in both directions responsive, set the `fill` attribute to tk.BOTH and set `expand` to True

# =========================================================================================

# the .place() geometry manager allows you to place the widget in the exact location you want it to be
# however, since it's non-responsive and is difficult to manage layouts with, it isn't normally used
# people more often use the .grid() geometry manager since it's more intuitive


window = tk.Tk()

for i in range(3):
    for j in range(3):
        frame = tk.Frame(
            master = window,
            relief = tk.RAISED,
            borderwidth = 1
        )

        frame.grid(row = i, column = j, padx = 3, pady = 3) # the padx and pady are between the frames
        label = tk.Label(master = frame, text = f"Row: {i}, Column: {j}")
        label.pack() # can also add padx and pady here

window.mainloop()

# Even though .grid() is called on each Frame, the geometry manager actually acts upon the window object
# Even though .pack() is called on each Label, the geometry manager acts on the Frame
