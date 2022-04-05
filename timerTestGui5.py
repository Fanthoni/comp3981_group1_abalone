import time
from tkinter import *
import threading
import abalone
root = Tk()

test_abalone = abalone.Abalone()
test_abalone.set_up_board_for_testing()


def cd(timer_label_obj, ts):
    while ts > 0:
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
    th = threading.Thread(target=cd,args=[timer,ts])
    th.start()


timerFrame = LabelFrame(root, padx=50, pady=50, bd=0)


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

def main():
    root = Tk()
    root.title('timer test')
    root.geometry("400x600")
    my_label3 = Label(root, text="", font=("Helvetica, 48"), fg="green", bg="black")
    my_label3.pack(pady=20)

    my_label4 = Label(root, text="test label 4", font=("Helvetica, 48"), fg="green", bg="black")
    my_timer = Timer(root, my_label4)
    my_label4.pack(pady=20)

    # my_timer.count_down_timer(20)
    my_timer.count_down_timer2(20.0, datetime.now(), datetime.now())

    my_button = Button(root, text="off", width=6, command=my_timer.do_something2)
    my_button.pack(pady=20)

    my_button2 = Button(root, text="3()", width=6, command=my_timer.do_something3)
    my_button2.pack(pady=20)
    clock(my_label3)

    my_button3 = Button(root, text="noPro()", width=6, command=my_timer.do_something)
    my_button3.pack(pady=20)

    my_button4 = Button(root, text="test datetime", width=6, command=my_timer.do_something4)
    my_button4.pack(pady=20)

    print(type((datetime.now() - datetime.now()).total_seconds()))

    # loop root
    root.mainloop()

if __name__ == '__main__':
    main()