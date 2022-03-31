from tkinter import *

#main
window = Tk()
window.title("game title")
window.configure(background='black')

#My photo
photo = PhotoImage(file="raw/download.png")
Label(window, image=photo, bg='black').grid(row=0, column=0, sticky=E)


#run the main loop
window.mainloop()