import tkinter as tk
from tkinter import Canvas
import serial
import math
import threading
import time

# Replace with your Arduino's device path and baud rate
SERIAL_PORT = "/dev/cu.usbserial-1140"  # Adjust based on your OS
BAUD_RATE = 9600

# Initialize serial connection
try:
    arduino = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
except Exception as e:
    arduino = None
    print(f"Error: Failed to connect to Arduino: {e}")

# Function to send angle data to Arduino
def send_angle():
    if not arduino:
        print("Error: Arduino is not connected.")
        return

    try:
        angle = int(angle_entry.get())
        if 0 <= angle <= 180:
            arduino.write(f"{angle}\n".encode())
            output_label.config(text=f"Angle {angle} sent!")
        else:
            output_label.config(text="Error: Enter a value between 0 and 180.")
    except ValueError:
        output_label.config(text="Error: Invalid input. Enter a number.")

# Function to update the angle display (gauge needle)
def update_angle_display(angle):
    print(f"Updating gauge with angle: {angle}")  # Debugging: Confirm gauge update
    current_angle_label.config(text=f"Current Angle: {angle}")
    angle_radians = math.radians(180 - angle)  # Convert to radians for correct direction
    needle_x = 200 + 150 * math.cos(angle_radians)  # Calculate needle end x-coordinate
    needle_y = 200 - 150 * math.sin(angle_radians)  # Calculate needle end y-coordinate
    gauge_canvas.coords(needle, 200, 200, needle_x, needle_y)  # Update needle position

# Function to read the servo's current angle dynamically
def read_servo_angle():
    while True:
        if arduino and arduino.in_waiting > 0:
            try:
                # Read and decode the data from Arduino
                line = arduino.readline().decode().strip()
                print(f"Raw received data: {line}")  # Debugging: Log all received data
                if "Current Angle:" in line:
                    # Extract the angle value after "Current Angle:"
                    angle = line.split(":")[1].strip()
                    if angle.isdigit():
                        update_angle_display(int(angle))
            except Exception as e:
                print(f"Error reading angle: {e}")
        time.sleep(0.1)  # Reduce delay for faster updates

# Function to close the serial connection properly
def on_closing():
    if arduino:
        arduino.close()
    root.destroy()

# Function to center the window
def center_window(window, width, height):
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

# GUI Setup
root = tk.Tk()
root.title("Servo Angle Gauge with Real-Time Updates")
center_window(root, 500, 550)  # Set window size and center it

# Current Angle Display
current_angle_label = tk.Label(root, text="Current Angle: 0", font=("Arial", 16))
current_angle_label.pack(pady=10)

# Gauge Canvas
gauge_canvas = Canvas(root, width=400, height=250, bg="black")
gauge_canvas.pack(pady=10)

# Draw Gauge Arc
gauge_canvas.create_arc(50, 50, 350, 350, start=0, extent=180, style=tk.ARC, width=4, outline="white")

# Draw Angle Markers
for angle in range(0, 181, 30):  # Mark every 30°
    angle_radians = math.radians(angle)
    x1 = 200 + 130 * math.cos(angle_radians)
    y1 = 200 - 130 * math.sin(angle_radians)
    x2 = 200 + 150 * math.cos(angle_radians)
    y2 = 200 - 150 * math.sin(angle_radians)
    gauge_canvas.create_line(x1, y1, x2, y2, fill="white", width=2)
    label_x = 200 + 175 * math.cos(angle_radians)
    label_y = 200 - 175 * math.sin(angle_radians)
    gauge_canvas.create_text(label_x, label_y, text=str(angle), fill="white", font=("Arial", 10))

# Draw Needle
needle = gauge_canvas.create_line(200, 200, 200, 50, width=4, fill="red")

# Angle Input Section
angle_label = tk.Label(root, text="Enter Angle (0-180):", font=("Arial", 12))
angle_label.pack(pady=5)
angle_entry = tk.Entry(root, width=10, font=("Arial", 12))
angle_entry.pack(pady=5)

# Send Button
send_button = tk.Button(root, text="Send Angle", font=("Arial", 12), command=send_angle)
send_button.pack(pady=10)

# Output Label
output_label = tk.Label(root, text="", font=("Arial", 10))
output_label.pack(pady=10)

# Start a thread to read the servo's angle dynamically
thread = threading.Thread(target=read_servo_angle, daemon=True)
thread.start()

# Graceful exit
root.protocol("WM_DELETE_WINDOW", on_closing)

# Run the app
root.mainloop()
