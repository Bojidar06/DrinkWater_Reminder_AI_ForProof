### What does the program do?  

Every 15 minutes it runs and reminds you to drink water through an messagebox.  
Then, it opens your camera and AI detects most objects you show on the camera.  

You have 6 minutes to show the camera a cup, bottle or a glass.  
_If you do_: The window closes and you can continue using your computer.  
_If you don't_: Your computer shuts down.  

<br>

### What problems does it solve?  

We all are used to sitting on a computer for a lot of time, but lets be honest.  
It's not very good for our health.  
This app helps to not forget to move from time to time and **Drink Water** :).  
Cause water is nice.  

If you know you should move but you feel lazy and you don't want to.  
*You've got no choise:)*, your computer shuts down if you deny to drink water ;)  
Well, I mean of course you could fool the program by showing a empty cup, or by leaving the messagebox.  
But don't, buddy. Drink water.  

### How to Run it

First clone the repository:  
```console
git clone https://github.com/Bojidar06/DrinkWater_Reminder_AI_ForProof.git
```  

Then open it and install the required python modules:
```console
cd DrinkWater_Reminder_AI_ForProof/
pip install -r requirements.txt
```

Then run the Script:
```console
python3 main.py  
```

### How it looks:

 ![](/screenshots/box.png)

### Things you can add to improve the App:  

**Feel free to make pull requests!**  

1. You could find a way to always keep the windows on top of everything to pressure the user to do it.
2. You can make it autorun. Right now you need to run it manualy every time you restart the pc.  
   You could find a way to make it autorun. I tried with *cronjob* but it didn't work, so I removed it.
