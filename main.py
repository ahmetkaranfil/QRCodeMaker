import tkinter as tk  # For creating the GUI
from tkinter import filedialog  # For opening a save dialog
import pyqrcode  # For generating QR codes
from pyqrcode import QRCode  # Specifically importing the QRCode module

# Function to create and save a QR code
def create_qr_code():
    url = url_input.get()  # Retrieve the URL entered by the user

    if url:  # Check if the URL field is not empty
        qr_code = pyqrcode.create(url)  # Generate the QR code for the URL
        # Open a dialog to save the QR code as an SVG file
        file_path = filedialog.asksaveasfilename(
            defaultextension=".svg",
            filetypes=[("SVG Files", "*.svg")]
        )

        if file_path:  # Check if a file path was selected
            qr_code.svg(file_path, scale=8)  # Save the QR code as an SVG
            # Update the status label to inform the user
            status_label.config(text="QR Code created and saved successfully.")

# Tkinter GUI setup
app_window = tk.Tk()  # Create the main application window
app_window.title("QR Code Generator")  # Set the title of the window

# Create widgets
label = tk.Label(app_window, text="Enter the URL")  # Label for URL input
url_input = tk.Entry(app_window, width=40)  # Input field for URL
# Button to trigger the QR code creation function
create_qr_button = tk.Button(app_window, text="Generate QR Code", command=create_qr_code)
status_label = tk.Label(app_window, text="")  # Label to display the status of the operation

# Arrange widgets in a grid layout
label.grid(row=0, column=0, padx=10, pady=10)  # Position the label
url_input.grid(row=0, column=1, padx=10, pady=10)  # Position the input field
create_qr_button.grid(row=1, column=0, columnspan=2, padx=10, pady=10)  # Position the button
status_label.grid(row=2, column=0, columnspan=2, padx=10, pady=10)  # Position the status label

app_window.mainloop()  # Run the main event loop