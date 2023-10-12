import tkinter as tk
from tkinter import ttk

from aica_api.client import AICA

class Slider(tk.Tk):
  def __init__(self, *args, **kwargs):
    # root window
    super().__init__(*args, **kwargs)
    self.geometry('300x100')
    self.resizable(False, False)
    self.title('Velocity limit demo')

    self.aica = AICA('127.0.0.1')
    print(self.aica.check())

    self.columnconfigure(0, weight=1)
    self.columnconfigure(1, weight=3)

    # slider current value
    self.current_value = tk.DoubleVar()

    # label for the slider
    slider_label = ttk.Label(
      self,
      text='Slider:'
    )

    slider_label.grid(
      column=0,
      row=0,
      sticky='w'
    )

    #  slider
    slider = ttk.Scale(
      self,
      from_=0,
      to=100,
      orient='horizontal',  # vertical
      command=self.slider_changed,
      variable=self.current_value
    )

    slider.grid(
      column=1,
      row=0,
      sticky='we'
    )

    # current value label
    current_value_label = ttk.Label(
      self,
      text='Current Value:'
    )

    current_value_label.grid(
      row=1,
      columnspan=2,
      sticky='n',
      ipadx=10,
      ipady=10
    )

    # value label
    self.value_label = ttk.Label(
      self,
      text=self.get_current_value()
    )
    self.value_label.grid(
      row=2,
      columnspan=2,
      sticky='n'
    )

  def get_current_value(self):
    return '{:.2f}'.format(self.current_value.get())


  def slider_changed(self, event):
    self.value_label.configure(text=self.get_current_value())
    self.aica.set_controller_parameter("robot", "ik", "max_linear_velocity", str(self.get_current_value()))



if __name__ == "__main__":
  root = Slider()
  root.mainloop()