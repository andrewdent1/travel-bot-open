import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

# Function to create itinerary
def create_itinerary():
    place = entry_place.get()
    duration = entry_duration.get()
    activities = entry_activities.get()
    extra_info = entry_extra.get()

    if place and duration and activities:
        itinerary = f"""
        Travel Itinerary Outline
        ------------------------
        Destination: {place}
        Duration: {duration}
        
        Suggested Activities:
        {activities}
        
        Additional Information:
        {extra_info if extra_info else "None"}
        """
        display_itinerary(itinerary)
    else:
        messagebox.showwarning("Input Error", "Please fill in all required fields.")

# Function to display itinerary and export option
def display_itinerary(itinerary):
    itinerary_window = tk.Toplevel(root)
    itinerary_window.title("Your Travel Itinerary")

    text_box = tk.Text(itinerary_window, height=15, width=50)
    text_box.insert(tk.END, itinerary)
    text_box.config(state=tk.DISABLED)
    text_box.pack()

    save_button = tk.Button(itinerary_window, text="Save Itinerary", command=lambda: save_itinerary(itinerary))
    save_button.pack()

# Function to save itinerary to a file
def save_itinerary(itinerary):
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text file", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            file.write(itinerary)
        messagebox.showinfo("Saved", f"Itinerary saved as {file_path}")

# Set up the UI
root = tk.Tk()
root.title("Travel Inspiration Bot")

label_place = tk.Label(root, text="Where do you want to go?")
label_place.pack()

entry_place = tk.Entry(root, width=50)
entry_place.pack()

label_duration = tk.Label(root, text="How long do you want to stay?")
label_duration.pack()

entry_duration = tk.Entry(root, width=50)
entry_duration.pack()

label_activities = tk.Label(root, text="What activities do you like to do?")
label_activities.pack()

entry_activities = tk.Entry(root, width=50)
entry_activities.pack()

label_extra = tk.Label(root, text="Anything else?")
label_extra.pack()

entry_extra = tk.Entry(root, width=50)
entry_extra.pack()

submit_button = tk.Button(root, text="Generate Itinerary", command=create_itinerary)
submit_button.pack()

root.mainloop()
