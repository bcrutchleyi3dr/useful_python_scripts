import tkinter as tk

root = tk.Tk()

switch_frame = tk.Frame(root)
switch_frame.pack()

switch_variable = tk.StringVar(value="off")
on_button = tk.Radiobutton(switch_frame, text="Not a Sharp", variable=switch_variable,
                            indicatoron=False, value="off", width=20)
off_button = tk.Radiobutton(switch_frame, text="Sharp Not Detected", variable=switch_variable,
                            indicatoron=False, value="low", width=20)
on_button.pack(side="left")
off_button.pack(side="left")


root.mainloop()
