from tkinter import *
from tkinter import messagebox
from main_video import main
import time

while True:
  root = Tk()
  root.withdraw()

  messagebox.showwarning("Important Reminder", "Get of that fucking chair and Go drink some water!")

  main()
  time.sleep(900)
