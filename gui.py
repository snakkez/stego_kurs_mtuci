__author__ = 'Михаил'
# импортирование модулей python
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk
from datetime import *
import tkinter.filedialog
import random
import os

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
        HideChild(self.master)

    def openDialog_find(self):
        FindChild(self.master)



class HideChild:
    def __init__(self, master):
        self.slave = Toplevel(master)
        self.slave.resizable(width='false', height='true')
        self.slave.title('СКРЫТИЕ')
        self.slave.geometry('900x600+200+50')
        self.slave.grab_set()
        self.slave.focus_set()

        # Рамка для меню
        #####################################################################################################
        #####################################################################################################

        self.optionFrame =Frame(self.slave, height=570, width=300)
        self.optionFrame.pack_propagate(0)          ### Рамка для выбора параметров скрытия
        self.optionFrame.place(x=0, y=0)

        self.file_open_file = tkinter.Frame(self.slave, height=100, width=600)
        self.file_open_file.pack_propagate(0)      ### Рамка для выбора файла
        self.file_open_file.place(x=300, y=0)

        self.container = tkinter.Frame(self.slave, height=400, width=600)
        self.container.pack_propagate(0)        ### Рамка для вывода стеганоконтейнера
        self.container.place(x=300, y=100)

        self.errors = tkinter.Frame(self.slave, height=100, width=600, bg="gray", colormap="new")
        self.errors.pack_propagate(0)        ### Рамка для вывода стеганоконтейнера
        self.errors.place(x=300, y=500)



    ##################################################################################################################
    ##################################################################################################################

        ### Рамка для выбора параметров скрытия

        self.cont_type = tkinter.Frame(self.optionFrame, height=70, width=300, bd=5)  # Рамка для выбора типа контейнера
        self.cont_type.place(x=0, y=0, width=300, height=70)

        self.file_type = tkinter.Frame(self.optionFrame, height=70, width=300, bd=5)
        self.file_type.place(x=0, y=70, width=300, height=70)  # Рамка для выбора типа файла

        self.compression_method_video = tkinter.Frame(self.optionFrame, height=90, width=300, bd=5)
        self.compression_method_video.place(x=0, y=140, width=300, height=90)  # Рамка для выбора способа сжатия в видео

        self.compression_method_audio = tkinter.Frame(self.optionFrame, height=70, width=300, bd=5)
        self.compression_method_audio.place(x=0, y=230, width=300, height=70)  # Рамка для выбора способа сжатия в аудио

        self.hiding_method_video = tkinter.Frame(self.optionFrame, height=70, width=300, bd=5)
        self.hiding_method_video.place(x=0, y=300, width=300, height=70)  # Рамка для выбора способа скрытия в видео

        self.hiding_stegomethod_video = tkinter.Frame(self.optionFrame, height=110, width=300, bd=5)
        self.hiding_stegomethod_video.place(x=0, y=370, width=300, height=110)  # Рамка для выбора метода скрытия в видео

        self.hiding_method_audio = tkinter.Frame(self.optionFrame, height=110, width=300, bd=5)
        self.hiding_method_audio.place(x=0, y=480, width=300, height=90)  # Рамка для выбора метода скрытия в аудио



    ###############################################################################################################
    # фрейм для выбора типа контейнера

        self.var_cont_type = IntVar()
        self.label1 = Label(self.cont_type, text='Тип контейнера:')
        self.rbutton1 = Radiobutton(self.cont_type, text='Видео', variable=self.var_cont_type, value=1)
        self.rbutton2 = Radiobutton(self.cont_type, text='Аудио', variable=self.var_cont_type, value=2)

        self.label1.place(x=0, y=0)
        self.rbutton1.place(x=10, y=20)
        self.rbutton2.place(x=10, y=40)
    ##############################################################################################################
        # Рамка для выбора типа скрываемого файла

        self.var_file_type = IntVar()
        self.label2 = Label(self.file_type, text='Тип скрываемого файла:')

        self.rbutton3 = Radiobutton(self.file_type, text='Цифровой Водяной Знак',
                                            variable=self.var_file_type, value=1)
        self.rbutton4 = Radiobutton(self.file_type, text='Текстовый файл',
                                            variable=self.var_file_type, value=2)

        self.label2.place(x=0, y=0)
        self.rbutton3.place(x=10, y=20)
        self.rbutton4.place(x=10, y=40)
    ##############################################################################################################
        # Рамка для выбора способа сжатия в видеоконтейнере

        self.var_comp_method_vid = IntVar()
        self.label3 = Label(self.compression_method_video, text='Тип сжатия в видеоконтейнере:')
        self.rbutton5 = Radiobutton(self.compression_method_video, text='bmp',
                                            variable=self.var_comp_method_vid, value=1)
        self.rbutton6 = Radiobutton(self.compression_method_video, text='jpeg',
                                            variable=self.var_comp_method_vid, value=2)
        self.rbutton7 = Radiobutton(self.compression_method_video, text='mpeg',
                                            variable=self.var_comp_method_vid, value=3)

        self.label3.place(x=0, y=0)
        self.rbutton5.place(x=10, y=20)
        self.rbutton6.place(x=10, y=40)
        self.rbutton7.place(x=10, y=60)

        ######################################################################################################
        # Рамка для выбора способа сжатия в аудиоконтейнер

        self.var_comp_method_audio = IntVar()
        self.label4 = Label(self.compression_method_audio, text='Тип сжатия в ауиоконтейнере:')
        self.rbutton8 = Radiobutton(self.compression_method_audio, text='waw',
                                            variable=self.var_comp_method_audio, value=1)
        self.rbutton9 = Radiobutton(self.compression_method_audio, text='Mp4',
                                            variable=self.var_comp_method_audio, value=2)

        self.label4.place(x=0, y=0)
        self.rbutton8.place(x=10, y=20)
        self.rbutton9.place(x=10, y=40)


        ######################################################################################################
        # Рамка для способа скрытия в видео

        self.var_hiding_method_vid = IntVar()
        self.label5 = Label(self.hiding_method_video, text='Способ скрытия информации в видеоконтейнере:')
        self.rbutton10 = Radiobutton(self.hiding_method_video, text='В пространственной области',
                                             variable=self.var_hiding_method_vid, value=1)
        self.rbutton11 = Radiobutton(self.hiding_method_video, text='В частотной области',
                                             variable=self.var_hiding_method_vid, value=2)

        self.label5.place(x=0, y=0)
        self.rbutton10.place(x=10, y=20)
        self.rbutton11.place(x=10, y=40)


        ######################################################################################################
        # Рамка для метода скрытия в видео

        self.var_hiding_stegomethod_vid = IntVar()
        self.label6 = Label(self.hiding_stegomethod_video, text='Метод скрытия информации в видеоконтейнере:')
        self.rbutton12 = Radiobutton(self.hiding_stegomethod_video,
                                             text='Метод кодирования наименее значащих бит',
                                             variable=self.var_hiding_stegomethod_vid, value=1)
        self.rbutton13 = Radiobutton(self.hiding_stegomethod_video,
                                             text='Метод псевдослучайного интервала',
                                             variable=self.var_hiding_stegomethod_vid, value=2)
        self.rbutton14 = Radiobutton(self.hiding_stegomethod_video,
                                             text='Метод псевдослучайной перестановки',
                                             variable=self.var_hiding_stegomethod_vid, value=3)
        self.rbutton15 = Radiobutton(self.hiding_stegomethod_video,
                                             text='Метод Коха и Жао',
                                             variable=self.var_hiding_stegomethod_vid, value=4)

        self.label6.place(x=0, y=0)
        self.rbutton12.place(x=10, y=20)
        self.rbutton13.place(x=10, y=40)
        self.rbutton14.place(x=10, y=60)
        self.rbutton15.place(x=10, y=80)
        ######################################################################################################
        # Рамка для метода скрытия в аудио

        self.var_hiding_method_audio = IntVar()
        self.label7 = Label(self.hiding_method_audio, text='Метод скрытия информации в аудиоконтейнере:')
        self.rbutton15 = Radiobutton(self.hiding_method_audio,
                                             text='Метод кодирования наименее значащих бит',
                                             variable=self.var_hiding_method_audio, value=1)
        self.rbutton16 = Radiobutton(self.hiding_method_audio,
                                             text='Метод расширения спектра',
                                             variable=self.var_hiding_method_audio, value=2)
        self.rbutton17 = Radiobutton(self.hiding_method_audio,
                                             text='Метод фазового кодирования',
                                             variable=self.var_hiding_method_audio, value=3)

        self.label7.place(x=0, y=0)
        self.rbutton15.place(x=10, y=20)
        self.rbutton16.place(x=10, y=40)
        self.rbutton17.place(x=10, y=60)

        ######################################################################################################
        ######################################################################################################
        ### Рамка для выбора файла

        self.open_file = Frame(self.file_open_file, height=100, width=300)
        self.open_file.place(x=0, y=0, width=300, height=100)  # Рамка для выбора скрываемого файла

        self.stego_file = Frame(self.file_open_file, height=100, width=300)
        self.stego_file.place(x=300, y=0, width=300, height=100)  # Рамка для выбора контейнера

        ######################################################################################################
        # Рамка для выбора скрываемого файла
        self.label8 = Label(self.open_file, text='Выбрать скрываемый файл:')
        self.label9 = Label(self.open_file, text='')
        self.button1 = Button(self.open_file, text='Выбрать файл')
        self.open_file_path = Entry(self.open_file, width=40)

        self.label8.pack(side=TOP)
        self.button1.pack(side=TOP)
        self.label9.pack(side=TOP)
        self.open_file_path.pack(side=TOP)
        ######################################################################################################
        # Рамка для выбора контейнера
        self.label10 = Label(self.stego_file, text='Выбрать контейнер:')
        self.label11 = Label(self.stego_file, text='')
        self.button2 = Button(self.stego_file, text='Выбрать файл')
        self.stego_file_path = Entry(self.stego_file, width=40)

        self.label10.pack(side=TOP)
        self.button2.pack(side=TOP)
        self.label11.pack(side=TOP)
        self.stego_file_path.pack(side=TOP)
        ######################################################################################################
        ######################################################################################################
        # Рамка для вывода изоражений
        self.empty_container = tkinter.Frame(self.container, height=200, width=300, bg='yellow')
        self.empty_container.place(x=0, y=0, width=300, height=200)  # Рамка для вывода пустого контейнера

        self.stegocontainer = tkinter.Frame(self.container, height=200, width=300, bg='cyan')
        self.stegocontainer.place(x=300, y=0, width=300, height=200)  # Рамка для вывода стеганоконтейнера

        self.empty_container_inside = tkinter.Frame(self.container, height=200, width=300, bg='green')
        self.empty_container_inside.place(x=0, y=200, width=300, height=200)  # Рамка для вывода пустого контейнера изнутри

        self.stegocontainer_inside = tkinter.Frame(self.container, height=200, width=300, bg='red')
        self.stegocontainer_inside.place(x=300, y=200, width=300, height=200)  # Рамка для вывода стеганоконтейнера изнутри


        #########################################################################################################
        # Рамка для вывода пустого контейнера

        self.label12 = tkinter.Label(self.empty_container, text='здесь типо контейнер')
        self.label12.pack()




        # canv = tkinter.Canvas(self.empty_container, width=300, height=150)

        image = Image.open('Lenna.png')
        image = image.resize((300, 180))
        photo = ImageTk.PhotoImage(image)

        self.label13 = tkinter.Label(self.empty_container, image=photo)
        self.label13.pack()
        #########################################################################################################
        # Рамка для вывода стеганоконтейнера
        self.label13 = tkinter.Label(self.stegocontainer, text='здесь типо уже изменный файл')
        self.label13.pack()
        #########################################################################################################
        # Рамка для вывода пустого контейнера изнутри
        self.label14 = tkinter.Label(self.empty_container_inside, text='здесь то, что внутри контейнера')
        self.label14.pack()
        #########################################################################################################
        self.label15 = tkinter.Label(self.stegocontainer_inside, text='здесь то, что внутри измененного файла')
        self.label15.pack()


        ######################################################################################################
        ######################################################################################################

        self.label15 = tkinter.Label(self.errors, text='здесь ошибки')
        self.label15.pack()



        self.slave.wait_window()




class FindChild:
    def __init__(self, master):
        self.des_key = ''
        self.open_text = ''

        self.slave = Toplevel(master)
        self.slave.resizable(width='false', height='true')
        self.slave.title('РАСКРЫТИЕ')
        self.slave.geometry('533x450+500+100')
        self.slave.grab_set()
        self.slave.focus_set()


        self.slave.wait_window()





        """self.master = master
        self.master.title('Курсовая работа стеганография')
        self.master.resizable(width='false', height='false')
        self.master.geometry('500x165+300+225')





        self.variable = StringVar(self.master)
        self.variable.set("--") # default value
        self.variable2 = StringVar(self.master)
        self.variable2.set("---") # default value

        self.w = OptionMenu(master, self.variable, self.variable.get(), "1", "2", "3")
        self.w.pack()

        self.w2 = OptionMenu(master, self.variable2, self.variable2.get())
        self.w2.pack()
        list1 = [1,2,3]
        list2 = [4,5,6]
        self.combobox = Combobox(master,values = list1,width=3,state='readonly')
        self.combobox.set("---")
        self.combobox.pack()

        self.combobox2 = Combobox(master,values='--',width=3,state='readonly')
        self.combobox2.set("--")
        self.combobox2.pack()





        button = Button(self.master, text="OK", command=self.ok)

        button.pack()
        self.master.mainloop()


    def ok(self):
        new_list =[4,5,6]
        self.combobox.configure(values = new_list)
        print("value is", self.variable.get())
"""





