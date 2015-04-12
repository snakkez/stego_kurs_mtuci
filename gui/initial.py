
# импортирование модулей python
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
from gui.hide import Hide
from gui.find import Find


# класс главного окна
class main:
    def __init__(self, master):


        self.master = master
        self.master.title('Курсовая работа')
        self.master.resizable(width='false', height='false')
        self.master.geometry('500x165+300+225')

        self.initFrame = Frame(self.master, height=100, width=100)
        self.initFrame.pack(fill='both', expand=False)

        self.Label1 = Label(self.initFrame, text='Курсовая работа по дисциплине ')
        self.Label4 = Label(self.initFrame, text='ТЕХНОЛОГИИ СТЕГАНОГРАФИИ В СИСТЕМАХ ИНФОКОММУНИКАЦИЙ')
        self.Label2 = Label(self.initFrame, text='Выполнили студенты группы БПЗ101: ')
        self.Label3 = Label(self.initFrame, text='Кажемский М.А.  Шарыпин Е.М.')
        self.Label5 = Label(self.initFrame, text='')
        self.Label6 = Label(self.initFrame, text='Выберите метод')

        self.Label1.pack()
        self.Label4.pack()
        self.Label2.pack()
        self.Label3.pack()
        self.Label5.pack()
        self.Label6.pack()



        self.controlsFrame = Frame(self.master, height=100, width=100)
        self.controlsFrame.pack(fill='both', expand=False)

        self.frame = Frame(self.controlsFrame, height=50, width=250)
        self.frame.pack_propagate(0)
        self.frame.pack(side='left', fill='both', expand=True)

        self.frame2 = Frame(self.controlsFrame, height=50, width=250)
        self.frame2.pack_propagate(0)
        self.frame2.pack(side='left', fill='both', expand=True)


        self.button_hide = Button(self.frame, text='СКРЫТЬ', command=self.openDialog_hide)
        self.button_find = Button(self.frame2, text='РАСКРЫТЬ', command=self.openDialog_find)



        self.button_hide.pack(side=TOP, fill='both', expand=True)
        self.button_find.pack(side=TOP, fill='both', expand=True)


        """self.master.protocol('WM_DELETE_WINDOW',
                                self.exitMethod)"""
        self.master.mainloop()

    def openDialog_hide(self):
        Hide(self.master)

    def openDialog_find(self):
        Find(self.master)