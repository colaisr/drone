import tkinter as tk
import tkintermapview

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

# Calculate and set the total window size
total_width = map_widget_width + pride_list_width
total_height = map_widget_height + display_controls_frame.winfo_reqheight()
root.geometry(f"{total_width}x{total_height}")

# Run the application
root.mainloop()






# import tkinter
# import tkinter as tk
# import tkintermapview
#
# # Create the main window
# root = tk.Tk()
# root.title("Drone Control Network")
#
# # Set the size of the window (width x height)
# root.geometry("1200x1000")
#
# # Create a frame that takes up the whole window
# full_frame = tk.Frame(root, bg='lightgrey')
# full_frame.pack(fill=tk.BOTH, expand=True)
#
# # Calculate the width for the child frames based on the desired percentage
# total_width = 1200  # This should match the width set in geometry
# pride_display_width = int(total_width * 0.7)  # 80% of the total width
# pride_list_width = total_width - pride_display_width  # Remaining 20% of the total width
#
# # Create a frame for the pride_display with 80% of the window width
# pride_display = tk.Frame(full_frame, bg='lightblue', width=pride_display_width)
# pride_display.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
#
# # Create a frame for the controls at the top of the pride_display frame
# display_controls_frame = tk.Frame(pride_display, bg='lightblue')
# display_controls_frame.pack(side=tk.TOP, fill=tk.X)
#
# # Adding controls in the specified order
# controls = [
#     ("Target", None),
#     ("X (long)", "target_x"),
#     ("Y (lat)", "target_y"),
#     ("Size", "drone_size"),
#     ("Overlap", "drone_overlap")
# ]
#
# column = 0
# for label_text, entry_name in controls:
#     # Create and place the label
#     label = tk.Label(display_controls_frame, text=label_text)
#     label.grid(row=0, column=column, padx=5, pady=5)
#     column += 1
#
#     # Create and place the textbox if entry_name is not None
#     if entry_name:
#         entry = tk.Entry(display_controls_frame, name=entry_name)
#         entry.grid(row=0, column=column, padx=5, pady=5)
#         column += 1
#
# # Create the map_frame which will take the remaining space in pride_display
# map_frame = tk.Frame(pride_display, bg='lightgrey')
# map_frame.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True)
#
# # Create a frame for the pride_list with 20% of the window width
# pride_list = tk.Frame(full_frame, bg='lightgreen', width=pride_list_width)
# pride_list.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)
#
# # create map widget
# map_widget = tkintermapview.TkinterMapView(map_frame, width=800, height=600, corner_radius=0)
# map_widget.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
# # Run the application
# root.mainloop()
