import time
from tkinter import *
import threading
import abalone
root = Tk()

test_abalone = abalone.Abalone()
test_abalone.set_up_board_for_testing()


def cd(timer_label_obj, ts):
    while ts > 0 and test_abalone.keep_looping:
        timer_label_obj.config(text=ts)
        ts-=1
        timer_label_obj.pack()
        time.sleep(1)
        if ts ==0:
            timer_label_obj.destroy()
            completeTimer = Label(timerFrame, text="Time is complete")
            completeTimer.pack()


def countdown(t):
    timer = Label(timerFrame)
    ts = int(t)
    # th = threading.Thread(target=cd,args=[timer, ts])
    th = threading.Thread(target=cd, args=[timerFrame, ts])
    th.start()


timerFrame = LabelFrame(root, text="TimerFrame", padx=50, pady=50, bd=0)
timerFrame.pack(pady=20)

timerFrameText = Label(timerFrame,
    text="Enter time in seconds for countdown",
    font=("Arial", 20, "bold")
)
countdownBox= Entry(timerFrame, bd=3)


submitCountdown = Button(timerFrame,
    padx=5,
    pady=5,
    text="Submit",
    font=("Arial", 20),
    command= lambda:countdown(countdownBox.get())
   )


def do_something():
    t1 = threading.Thread(target=do_something2)
    t1.start()


def do_something2():
    test_abalone.test_timer_ai_move()


my_button = Button(root, text="off", width=6, command=do_something)
my_button.pack(pady=20)



timerFrame.pack()


timerFrameText.pack()
countdownBox.pack()
submitCountdown.pack()


root.mainloop()

