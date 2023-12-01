import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Drone Network Layout")

# Set the size of the window
root.geometry("1200x800")

# Create a frame for the map placeholder
map_frame = tk.Frame(root, bg='lightgrey', width=800, height=600)
map_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
map_frame.pack_propagate(False)  # Prevents the frame from resizing to fit its contents

# Place a placeholder label where the map would go
map_placeholder = tk.Label(map_frame, text="Map Placeholder", bg='lightgrey')
map_placeholder.pack(expand=True)

# Create a frame for the list placeholder
list_frame = tk.Frame(root, bg='white', width=400, height=800)
list_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
list_frame.pack_propagate(False)  # Prevents the frame from resizing to fit its contents

# Place a placeholder label where the list would go
list_placeholder = tk.Label(list_frame, text="List Placeholder", bg='white')
list_placeholder.pack(expand=True)

# Run the application
root.mainloop()

