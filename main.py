import tkinter as tk
import tkintermapview

# Define the Drone class
class Drone:
    def __init__(self, id, x_long, y_lat):
        self.id = id
        self.x_long = x_long
        self.y_lat = y_lat



# Initialize variables to store the selected location's longitude and latitude
target_longitude = 52.3946656
target_latitude = 16.9206653
drone_area_size=200
drone_area_overlap=40
# Initialize the list of drones
drones = []

def calculate_clicked():
    print("Calculate clicked")

def set_target(coords):
    global target_latitude
    global target_longitude
    target_latitude = coords[1]
    target_longitude = coords[0]
    update_target()

def update_target():
    entry_target_x = display_controls_frame.nametowidget("target_x")
    entry_target_x.delete(0, tk.END)  # Clear the current value
    entry_target_x.insert(0, str(target_latitude))  # Insert the new value
    entry_target_y = display_controls_frame.nametowidget("target_y")
    entry_target_y.delete(0, tk.END)  # Clear the current value
    entry_target_y.insert(0, str(target_longitude))  # Insert the new value

# Functions for updating the drone list in the Listbox
def update_drone_list():
    drone_list.delete(0, tk.END)  # Clear the current list
    for drone in drones:
        drone_list.insert(tk.END, f"ID: {drone.id}, X: {drone.x_long}, Y: {drone.y_lat}")


# Functions for the '+' and '-' buttons
def plus_clicked():
    global drones
    new_drone_id = len(drones) + 1
    new_drone = Drone(new_drone_id, target_longitude, target_latitude)
    drones.append(new_drone)
    print(f"Added Drone {new_drone_id}")
    update_drone_list()

def minus_clicked():
    global drones
    selection = drone_list.curselection()  # Get the index of the selected item
    if selection:
        selected_index = selection[0]
        if 0 <= selected_index < len(drones):
            del drones[selected_index]
            print(f"Removed Drone at index {selected_index}")
            update_drone_list()
    else:
        print("No drone selected")


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
pride_frame_width = 200  # Adjust this as needed
pride_frame = tk.Frame(full_frame, bg='lightgreen', width=pride_frame_width)
pride_frame.pack(side=tk.RIGHT, fill=tk.Y)

pride_controls_frame = tk.Frame(pride_frame, bg='lightgreen')
pride_controls_frame.pack(side=tk.TOP, fill=tk.X)

# Adding '+' and '-' buttons
plus_button = tk.Button(pride_controls_frame, text="+", command=plus_clicked)
plus_button.pack(side=tk.LEFT, padx=5, pady=5)

minus_button = tk.Button(pride_controls_frame, text="-", command=minus_clicked)
minus_button.pack(side=tk.LEFT, padx=5, pady=5)

calculate_button = tk.Button(pride_controls_frame, text="Calculate", command=calculate_clicked)
calculate_button.pack(side=tk.LEFT, padx=5, pady=5)

# Create the drone_list_frame
drone_list_frame = tk.Frame(pride_frame, bg='lightyellow')  # Use a different background color for visibility
drone_list_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)

# Create and add the Listbox to drone_list_frame
drone_list = tk.Listbox(drone_list_frame)
drone_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Optionally, add a scrollbar to the Listbox
scrollbar = tk.Scrollbar(drone_list_frame, orient="vertical", command=drone_list.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
drone_list.config(yscrollcommand=scrollbar.set)

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
map_widget.add_right_click_menu_command(label="Set Target",
                                        command=set_target,
                                        pass_coords=True)

# Calculate and set the total window size
total_width = map_widget_width + pride_frame_width
total_height = map_widget_height + display_controls_frame.winfo_reqheight()
root.geometry(f"{total_width}x{total_height}")

# After creating the controls
update_target()  # Call this function to initialize the value

# Run the application
root.mainloop()

