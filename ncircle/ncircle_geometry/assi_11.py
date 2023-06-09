import tkinter as tk

# Create the main window
window = tk.Tk()

# Set the window title
window.title("Button Example")

# Set the window size
window.geometry("300x100")

# Create a frame to hold the buttons
frame = tk.Frame(window)

# Create the Start button
start_button = tk.Button(frame, text="Start", width=10)
start_button.pack(side=tk.LEFT, padx=10)

# Create the Stop button
stop_button = tk.Button(frame, text="Stop", width=10)
stop_button.pack(side=tk.LEFT, padx=10)

# Create the Pause button
pause_button = tk.Button(frame, text="Pause", width=10)
pause_button.pack(side=tk.LEFT, padx=10)

# Pack the frame
frame.pack()

# Start the main loop
window.mainloop()
