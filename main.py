from tkinter import *
import tkinter
from tkinter import messagebox
from time import time, sleep
from main_video import main


while True:
  root = tkinter.Tk()
  root.withdraw()

  messagebox.showwarning("Important Reminder", "Get of that fucking chair and Go drink some water!")

  main()
  sleep(60)

