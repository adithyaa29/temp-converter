import tkinter as tk

def convert_temp():
    temp_celsius = entry.get()  # Get the temperature in Celsius from the entry widget
    try:
        temp_fahrenheit = float(temp_celsius) * (9/5) + 32  # Convert temperature to Fahrenheit
        # Display the converted temperature in a label widget
        result_label.config(text=f"The corresponding temperature in Fahrenheit is {temp_fahrenheit}°F.")
    except ValueError:
        result_label.config(text="Invalid input. Please enter a numeric value.")

# Create the main window
window = tk.Tk()
window.title("Temperature Converter")

# Create a label widget for instructions
instructions_label = tk.Label(window, text="Enter the temperature in Celsius(°C):")
instructions_label.pack()

# Create an entry widget to input the temperature
entry = tk.Entry(window)
entry.pack()

# Create a button widget to convert the temperature
button = tk.Button(window, text="Convert", command=convert_temp)
button.pack()

# Create a label widget to display the result
result_label = tk.Label(window, text="")
result_label.pack()

# Start the GUI event loop
window.mainloop()
