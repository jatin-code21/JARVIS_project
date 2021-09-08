import tkinter
import random
# list of colour.
my_colours = ['Red','Blue','Green','Pink','Black','Yellow','Orange','White','Purple','Brown']
my_score = 0
my_timeleft = 30
def my_startGame(event):
   if my_timeleft == 30:
      # start the countdown timer.
      my_countdown()
   my_nextColour()
def my_nextColour():
   global my_score
   global my_timeleft
   # if a game is currently in play
   if my_timeleft > 0:
      e.focus_set()
      if e.get().lower() == my_colours[1].lower():
         my_score += 1
      # clear the text entry box.
      e.delete(0, tkinter.END)
      random.shuffle(my_colours)
      label.config(fg = str(my_colours[1]), text = str(my_colours[0]))
      # update the score.
      my_scoreLabel.config(text = "Score: " + str(my_score))
# Countdown timer function
def my_countdown():
   global my_timeleft
   # if a game is in play
   if my_timeleft > 0:
      # decrement the timer.
      my_timeleft -= 1
      # update the time left label
      
      my_timeLabel.config(text = "Time left: "+ str(my_timeleft))
      # run the function again after 1 second.
      my_timeLabel.after(1000, my_countdown)
# Driver Code
root = tkinter.Tk()
root.title("COLORGAME")
root.geometry("375x200")
my_instructions = tkinter.Label(root, text = "Type in the color" "of the words, and not the word text!",
   font = ('Helvetica', 12))
my_instructions.pack()
my_scoreLabel = tkinter.Label(root, text = "Press enter to start",
   font = ('Helvetica', 12))
my_scoreLabel.pack()
my_timeLabel = tkinter.Label(root, text = "Time left: " +
   str(my_timeleft), font = ('Helvetica', 12))
my_timeLabel.pack()
label = tkinter.Label(root, font = ('Helvetica', 60))
label.pack()
e = tkinter.Entry(root)
root.bind('<Return>', my_startGame)
e.pack()
e.focus_set()
# start the GUI
root.mainloop()