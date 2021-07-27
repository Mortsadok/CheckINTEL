import time
from tkinter import *
import ast
from DateTime import Time, Date, Day
from Employee import Employees, Value_Is_Changed
from threading import Thread
import queue
from time import strftime

__copyright__ = "Copyright (C) 2021 Mor Tsadok"
__version__ = "1.0"


def EmployeeCheck(Values):
    Value = open(r'Dependencies\EmployeeCheck.txt', "w")
    Value.write(str(Values))
    Value.close()
    return Value


def EmployeeState(Values):
    Value = open(r'Dependencies\EmployeeState.txt', "w")
    Value.write(str(Values))
    Value.close()
    return Value


class App:

    def Start(self, getWWID):

        State = open(r'Dependencies\EmployeeState.txt', "r").read()
        EState = ast.literal_eval(State)

        Check = open(r'Dependencies\EmployeeCheck.txt', "r").read()
        CState = ast.literal_eval(Check)

        Values = open(r'Dependencies\Remembered_Values.txt', "r").read()
        ENUM = ast.literal_eval(Values)

        Let = 'E'
        Q = queue.Queue()

        for Employee in Employees:

            if getWWID == Employee.WWID:
                Location = Let + str(ENUM.get(getWWID))
                if (CState[Employee.WWID] != Date() and EState[Employee.WWID] == '0') \
                        or (CState[Employee.WWID] == Date() and EState[Employee.WWID] == '1') \
                        or (CState[Employee.WWID] != Date() and EState[Employee.WWID] == '1'):

                    Thread(target=Employee.WWID_SCAN, args=(Location, ENUM.get(getWWID), Q,)).start()
                    # Employee.WWID_SCAN(Location, ENUM.get(getWWID), Q)
                    Flag = Q.get()
                    if Flag is True:
                        self.State['text'] = f'Welcome to Intel, {Employee.Firstname}!'
                        self.StateIO['text'] = f'Check-in time: {Date()} {Time()[:5]}'

                    if Flag is False:
                        self.State['text'] = f'Good bye, {Employee.Firstname}!'
                        self.StateIO['text'] = f'Check-out time: {Date()} {Time()[:5]}'

                    if Employee.EndOfTheDay == 1:
                        Employee.CheckIn = None
                        Employee.CheckOut = None
                        ENUM[Employee.WWID] = str(int(ENUM[Employee.WWID]) + 1)
                        Value_Is_Changed(ENUM)

        time.sleep(3)
        self.State['text'] = ""
        self.StateIO['text'] = ""

    def StartThread(self):
        Thread(target=self.Start, args=(str(self.Scan.get()),)).start()
        self.Scan.delete(0, END)

    def __init__(self):
        def time():
            string = strftime('%H:%M:%S')
            lbl.config(text=string)
            lbl.after(1000, time)

        self.StateTEXT = ""
        self.CheckInOut = ""
        self.root = Tk()
        self.root.title('Check Intel')
        self.root.attributes('-fullscreen', True)
        self.root.configure(background='white')
        self.root.overrideredirect(1)

        canvas = Canvas(self.root, width=600, height=350, bg='white', highlightthickness=0)
        canvas.pack(pady=10)
        img = PhotoImage(file="Images/CHECK.png")
        canvas.create_image(0, 0, anchor=NW, image=img)
        canvas.pack(pady=(50, 50))

        lbl = Label(self.root, font=('calibri', 70),
                    background='white',
                    foreground='black')

        lbl.pack(anchor=N, pady=(10, 0))
        time()

        WWID = Canvas(self.root, width=600, height=214, bg='white', highlightthickness=0)
        WWIDimg = PhotoImage(file="Images/WWID.png")
        WWID.create_image(0, 0, anchor=NW, image=WWIDimg)
        WWID.pack(pady=(55, 0))

        self.menu_frame = Frame(self.root, bg='white')

        self.Scan = Entry(self.menu_frame, width=70, show='*', bg='black')
        self.Scan.focus()
        self.Scan.pack(pady=(10, 50))

        self.State = Label(self.menu_frame, text=self.StateTEXT, font=('Calibri', 28))
        self.State.config(bg='white')
        self.State.pack()

        self.StateIO = Label(self.menu_frame, text=self.CheckInOut, font=('Calibri', 23))
        self.StateIO.config(bg='white')
        self.StateIO.pack()

        self.menu_frame.pack()

        self.root.bind('<Return>', lambda event=None: self.StartThread())
        self.root.mainloop()


app = App()
