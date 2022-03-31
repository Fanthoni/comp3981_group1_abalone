from tkinter import *
import time
import abalone
import multiprocessing
from datetime import datetime


# test_abalone = abalone.Abalone()
# test_abalone.set_up_board_for_testing()

# test_abalone.


class TestAsync(multiprocessing.Process):
    def __init__(self, abalone_obj):
        self.abalone_obj = abalone_obj

    def run(self):
        self.abalone_obj.test_timer_ai_move()


class Timer:
    def __init__(self, root, my_label):
        self.root = root
        self.my_label = my_label
        self.keep_looping = True
        self.test_abalone = abalone.Abalone()
        self.test_abalone.set_up_board_for_testing()

    def count_down_timer(self, starting_time):
        """
        Primary timer.
        """
        self.my_label.config(text=starting_time)
        if starting_time != 0 and self.keep_looping is True:
            # print(self.test_abalone.keep_looping)
            self.my_label.after(1000, self.count_down_timer, starting_time - 1)
        # else:
        #     self.keep_looping = True

    def do_something(self):
        # process = multiprocessing.Process(target=self.test_abalone.test_timer_ai_move)
        # capture_bool = process.start()
        # self.count_down_timer(10)
        # capture_bool2 = process.join()
        #
        # print("capture_bool = " , capture_bool)
        # print("capture_bool2 = " , capture_bool2)
        # self.keep_looping = False
        self.test_abalone.test_timer_ai_move()  # Search
        print("ds1 is done!!")

    def do_something2(self):
        self.test_abalone.keep_looping = False

    def do_something3(self):
        # p = multiprocessing.Pool(processes=1)
        # data = p.map(test_abalone.test_timer_ai_move, [1])
        # p.close()
        # print(data)

        process = multiprocessing.Process(target=self.test_abalone.test_timer_ai_move)
        process.start()
        process.join()
        # self.keep_looping = False
        print("ds3 is done")

    def do_something4(self):
        val1 = datetime.now()
        time.sleep(2)
        val2 = datetime.now()
        print((val2 - val1).total_seconds())

    def count_down_timer2(self, time_limit: float, starting_time, passedtime):
        """
        Deduct elapsed time.
        """
        passed_time = (passedtime - starting_time).total_seconds()
        self.my_label.config(text=int(time_limit) - int(passed_time))

        if passed_time < time_limit and self.keep_looping is True:
            self.my_label.after(1000, self.count_down_timer2, time_limit, starting_time, datetime.now())


def clock(my_label):
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")

    my_label.config(text=hour + ":" + minute + ":" + second)
    my_label.after(1000, clock, my_label)


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
    # freeze.support()
    main()

# test_abalone = abalone.Abalone()
# test_abalone.set_up_board_for_testing()
# test_abalone.test_timer_ai_move()
# print(test_abalone.keep_looping)
