import tkinter as tk
from tkinter import ttk

from aica_api.client import AICA

class Slider(tk.Tk):
    def __init__(self, *args, **kwargs):
        # root window
        super().__init__(*args, **kwargs)

        self.aica = AICA('127.0.0.1')
        print(self.aica.check())
        print(self.aica.get_application())
        print(self.aica.controller_descriptions())

        # Create the main Tkinter window
        # root = tk.Tk()
        self.title("Slider UI")

        # Create and configure the first slider
        self.slider1 = tk.Scale(self, from_=0.0, to=3.0, orient=tk.HORIZONTAL, label="Slider 1", length=300, resolution=0.1)
        self.slider1.pack(pady=10)
        self.slider1.set(0.5)  # Set an initial value

        # Create and configure the second slider
        self.slider2 = tk.Scale(self, from_=0.0, to=3.0, orient=tk.HORIZONTAL, label="Slider 2", length=300, resolution=0.1)
        self.slider2.pack(pady=10)
        self.slider2.set(0.5)  # Set an initial value

        # Create a button to trigger the update function
        self.update_button = tk.Button(self, text="Update Values", command=self.update_values)
        self.update_button.pack(pady=10)

        # Create a label to display the current values
        self.label_result = tk.Label(self, text="")
        self.label_result.pack(pady=10)

    def update_values(self):
        value1 = float(self.slider1.get())
        value2 = float(self.slider2.get())
        self.label_result.config(text=f"Slider 1: {value1}, Slider 2: {value2}")
        self.aica.set_controller_parameter("robot", "ik", "max_linear_velocity", str(value1))
        self.aica.set_controller_parameter("robot", "ik", "max_angular_velocity", str(value2))


if __name__ == "__main__":
    root = Slider()
    root.mainloop()