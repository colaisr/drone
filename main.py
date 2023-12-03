import math
import tkinter as tk
import tkintermapview
from PIL import Image, ImageTk
import os


# Define the Drone class
class Drone:
    def __init__(self, id, x_long, y_lat):
        self.id = id
        self.x_long = x_long
        self.y_lat = y_lat

    def place_on_map(self, map_widget, plane_image):

        area_size=drone_area_size
        # Create a marker for the drone with its ID as text
        marker = map_widget.set_marker(self.y_lat, self.x_long, icon=plane_image, text=str(self.id), text_color="red")

        # Constants for converting meters to degrees
        meters_in_latitude_degree = 111320  # Approximately true for all latitudes
        meters_in_longitude_degree_at_equator = 111320  # Approximately true at the equator

        # Adjust the longitude degree size based on latitude
        meters_in_longitude_degree = meters_in_longitude_degree_at_equator * math.cos(math.radians(self.y_lat))

        # Calculate half the size of the square in degrees
        half_square_size_lat = (area_size / 2) / meters_in_latitude_degree
        half_square_size_long = (area_size / 2) / meters_in_longitude_degree

        top_left_x=self.x_long - half_square_size_long
        top_left_y=self.y_lat + half_square_size_lat
        top_right_x=self.x_long + half_square_size_long
        top_right_y=self.y_lat + half_square_size_lat
        bottom_left_x=self.x_long - half_square_size_long
        bottom_left_y=self.y_lat - half_square_size_lat
        bottom_right_x=self.x_long + half_square_size_long
        bottom_right_y=self.y_lat - half_square_size_lat


        # Calculate corner coordinates of the square
        top_left = (top_left_y,top_left_x )
        top_right = ( top_right_y,top_right_x)
        bottom_left = (bottom_left_y, bottom_left_x)
        bottom_right = (bottom_right_y, bottom_right_x)

        # Define the polygon points (corners of the square)
        polygon_points = [top_left, top_right,bottom_right,bottom_left]

        # Draw the polygon on the map
        map_widget.set_polygon(polygon_points, fill_color=None, outline_color="red", border_width=2)

# Initialize variables to store the selected location's longitude and latitude
target_longitude_x = 13.377695
target_latitude_y =  52.516268
drone_area_size = 200
drone_area_overlap = 40
# Initialize the list of drones
drones = []

# Global variable to store the current target marker
current_target_marker = None


def set_target_marker():
    global current_target_marker
    global map_widget

    # Remove the existing marker, if any
    if current_target_marker is not None:
        map_widget.delete_all_marker()

    # Create a marker with the target image
    current_target_marker = map_widget.set_marker(target_latitude_y, target_longitude_x, icon=target_image)


import math

def calculate_clicked():
    map_widget.delete_all_polygon()
    map_widget.delete_all_marker()
    set_target_marker()
    global drones
    global drone_area_size
    num_drones = len(drones)
    if num_drones == 0:
        return  # No drones to place

    # Retrieve drone area size and overlap from the textboxes
    drone_area_size = float(display_controls_frame.nametowidget("drone_size").get())
    drone_area_overlap = float(display_controls_frame.nametowidget("drone_overlap").get())

    # Constants for converting meters to degrees
    meters_in_latitude_degree = 111320  # Approximately true for all latitudes
    meters_in_longitude_degree_at_equator = 111320  # Approximately true at the equator

    # Adjust the longitude degree size based on latitude
    meters_in_longitude_degree = meters_in_longitude_degree_at_equator * math.cos(math.radians(target_latitude_y))

    # Calculate the effective size for each drone area considering the overlap
    effective_drone_size = drone_area_size - drone_area_overlap
    drone_lat_deg = effective_drone_size / meters_in_latitude_degree
    drone_long_deg = effective_drone_size / meters_in_longitude_degree

    # Calculate the number of drones per row (and column)
    drones_per_row = math.ceil(math.sqrt(num_drones))
    drones_per_column = math.ceil(num_drones/drones_per_row)

    # Calculate the top-left start position for the grid
    start_lat = target_latitude_y + (drone_lat_deg * (drones_per_column - 1)) / 2
    start_long = target_longitude_x - (drone_long_deg * (drones_per_row - 1)) / 2

    # Assign positions to each drone
    for i, drone in enumerate(drones):
        # Calculate row and column for the current drone
        row = i // drones_per_row
        col = i % drones_per_row

        # Calculate the longitude and latitude for the drone
        drone.x_long = start_long + col * drone_long_deg
        drone.y_lat = start_lat - row * drone_lat_deg

        # Place the drone on the map
        drone.place_on_map(map_widget, plane_image)

def set_target(coords):
    global target_latitude_y
    global target_longitude_x
    target_latitude_y = coords[0]
    target_longitude_x = coords[1]
    update_target()


def update_target():
    entry_target_x = display_controls_frame.nametowidget("target_x")
    entry_target_x.delete(0, tk.END)  # Clear the current value
    entry_target_x.insert(0, str(target_longitude_x))  # Insert the new value
    entry_target_y = display_controls_frame.nametowidget("target_y")
    entry_target_y.delete(0, tk.END)  # Clear the current value
    entry_target_y.insert(0, str(target_latitude_y))  # Insert the new value
    set_target_marker()
    entry_target_size = display_controls_frame.nametowidget("drone_size")
    entry_target_size.delete(0, tk.END)  # Clear the current value
    entry_target_size.insert(0, str(drone_area_size))  # Insert the new value
    entry_target_overlap = display_controls_frame.nametowidget("drone_overlap")
    entry_target_overlap.delete(0, tk.END)  # Clear the current value
    entry_target_overlap.insert(0, str(drone_area_overlap))  # Insert the new value


# Functions for updating the drone list in the Listbox
def update_drone_list():
    drone_list.delete(0, tk.END)  # Clear the current list
    for drone in drones:
        drone_list.insert(tk.END, f"ID: {drone.id}, X: {drone.x_long}, Y: {drone.y_lat}")


# Functions for the '+' and '-' buttons
def plus_clicked():
    global drones
    new_drone_id = len(drones) + 1
    new_drone = Drone(new_drone_id, target_longitude_x, target_latitude_y)
    drones.append(new_drone)
    print(f"Added Drone {new_drone_id}")
    update_drone_list()


def minus_clicked():
    global drones
    selection = drone_list.curselection()  # Get the index of the selected item
    if selection:
        selected_index = selection[0]
        if 0 <= selected_index < len(drones):
            # Remove the marker of the selected drone
            selected_drone = drones[selected_index]
            # Remove the drone from the list
            del drones[selected_index]
            print(f"Removed Drone at index {selected_index}")

            # Update the drone list in the UI
            update_drone_list()
    else:
        print("No drone selected")


# Define the size of the map widget
map_widget_width = 1000
map_widget_height = 900

# Create the main window
root = tk.Tk()
root.title("Drone Control Network")

# Get the current path of the script and the plane and target images
current_path = os.path.join(os.path.dirname(os.path.abspath(__file__)))
plane_image_path = os.path.join(current_path, "images", "plane.png")
target_image_path = os.path.join(current_path, "images", "target.png")
target_image = ImageTk.PhotoImage(Image.open(target_image_path).resize((40, 40)))
plane_image = ImageTk.PhotoImage(Image.open(plane_image_path).resize((40, 40)))

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

set_target_marker()

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
