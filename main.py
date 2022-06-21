from tkinter import *
import tkinter
from tkinter import messagebox
from main_video import main
import time

while True:
  root = tkinter.Tk()
  root.withdraw()

  messagebox.showwarning("Important Reminder", "Get of that fucking chair and Go drink some water!")

  main()
  time.sleep(900)
