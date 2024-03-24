import tkinter as tk

window = tk.Tk()
window.title("My Window")
window.geometry("400x250")

# Add a label to the window
label = tk.Label(window, text="This is my first Tkinter window!")
label.pack()

# Add a button to the window
button = tk.Button(window, text="Click me!", command=lambda: print("Button clicked!"))
button.pack()

window.mainloop()