import tkinter as tk
import tkintermapview


# Function to be called when "Set Target" is clicked in the context menu
def set_target(longitude, latitude):
    # Store the longitude and latitude in variables
    global target_longitude, target_latitude
    target_longitude = longitude
    target_latitude = latitude
    print(f"Target set to longitude: {target_longitude}, latitude: {target_latitude}")


# Function to display the context menu
def show_context_menu(event):
    # Try to get the longitude and latitude from the map widget
    # For demonstration, we'll just use placeholder values
    longitude = 37.12345
    latitude = -121.54321

    # Update the command for the "Set Target" menu item with the current coordinates
    context_menu.entryconfigure("Set Target", command=lambda: set_target(longitude, latitude))

    # Show the context menu at the cursor's position
    context_menu.post(event.x_root, event.y_root)


# Define the size of the map widget
map_widget_width = 1000
map_widget_height = 900


# Create the main window
root = tk.Tk()
root.title("Drone Control Network")

# Create a frame that takes up the whole window
full_frame = tk.Frame(root, bg='lightgrey')
full_frame.pack(fill=tk.BOTH, expand=True)

# Create a frame for the pride_list with a fixed width
pride_list_width = 200  # Adjust this as needed
pride_list = tk.Frame(full_frame, bg='lightgreen', width=pride_list_width)
pride_list.pack(side=tk.RIGHT, fill=tk.Y)

# Create a frame for the pride_display
pride_display = tk.Frame(full_frame, bg='lightblue')
pride_display.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a frame for the controls at the top of the pride_display frame
display_controls_frame = tk.Frame(pride_display, bg='lightblue')
display_controls_frame.pack(side=tk.TOP, fill=tk.X)

# Adding controls in the specified order
controls = [
    ("Target", None),
    ("X (long)", "target_x"),
    ("Y (lat)", "target_y"),
    ("Size", "drone_size"),
    ("Overlap", "drone_overlap")
]

column = 0
for label_text, entry_name in controls:
    # Create and place the label
    label = tk.Label(display_controls_frame, text=label_text)
    label.grid(row=0, column=column, padx=5, pady=5)
    column += 1

    # Create and place the textbox if entry_name is not None
    if entry_name:
        entry = tk.Entry(display_controls_frame, name=entry_name)
        entry.grid(row=0, column=column, padx=5, pady=5)
        column += 1


# Create the map_frame which will take the remaining space in pride_display
map_frame = tk.Frame(pride_display, bg='grey')
map_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

# Create map widget
map_widget = tkintermapview.TkinterMapView(map_frame, width=map_widget_width, height=map_widget_height, corner_radius=0)
map_widget.pack()

# Create a context menu
context_menu = tk.Menu(map_widget, tearoff=0)
context_menu.add_command(label="Set Target")

# Bind the right-click event to show the context menu
map_widget.bind("<Button-3>", show_context_menu)  # <Button-3> is the right-click event on Windows/Linux

# Initialize variables to store the selected location's longitude and latitude
target_longitude = None
target_latitude = None

# Calculate and set the total window size
total_width = map_widget_width + pride_list_width
total_height = map_widget_height + display_controls_frame.winfo_reqheight()
root.geometry(f"{total_width}x{total_height}")

# Run the application
root.mainloop()





