import tkinter
from tkinter import *
from tkinter.ttk import *
import tkinter.filedialog
import os
import time
from PIL import Image, ImageTk
from algorithms.bmplsb import BMPLSB
from algorithms.bmplsbinterval import BMPLSBInterval
from algorithms.kochzhao import KochZhao
from file_io.bmpimage import BMPImage
from errors.errors import *
import helpers.exceptions
from helpers.exceptions import *
from random import choice
from string import ascii_letters


class Find:
    def __init__(self, master):
        self.slave = Toplevel(master)
        self.slave.resizable(width='false', height='false')
        self.slave.title('Раскрытие')
        self.slave.geometry('1000x400+200+50')
        self.slave.grab_set()
        self.slave.focus_set()

        st = Style()
        st.configure('BW.TLabel', font='Verdana 8 bold')
        st.configure('TRadiobutton', font='Verdana 9')
        st.configure('TLabel', font='Verdana 9')
        st.configure('TButton', font='Verdana 9')
        st.configure('TText', font='Verdana 9')
        st.configure('MY.TFrame')

        self.on_main_frame()

        self.slave.wait_window()

    def on_main_frame(self):
        """
        Рамка для меню
        """
        self.option_frame = tkinter.Frame(self.slave, height=400, width=3250)
        self.option_frame.pack_propagate(0)  # Рамка для выбора параметров скрытия
        self.option_frame.place(x=0, y=0)

        self.file_open_file = tkinter.Frame(self.slave, height=100, width=600)
        self.file_open_file.pack_propagate(0)  # Рамка для выбора файла
        self.file_open_file.place(x=350, y=0)

        self.depth_and_density = tkinter.Frame(self.slave, height=60, width=300)
        self.depth_and_density.pack_propagate(0)
        self.depth_and_density.place(x=350, y=100, width=350, height=60)  # Рамка для выбора метода скрытия в аудио

        self.execute = tkinter.Frame(self.slave, height=20, width=350)
        self.execute.pack_propagate(0)
        self.execute.place(x=350, y=160, width=300, height=20)  # Рамка для выбора метода скрытия в аудио

        self.container = tkinter.Frame(self.slave, height=210, width=350)
        self.container.pack_propagate(0)  # Рамка для вывода стеганоконтейнера
        self.container.place(x=350, y=190)

        self.logs = tkinter.Frame(self.slave, height=290, width=300)
        self.logs.pack_propagate(0)  # Рамка для вывода стеганоконтейнера
        self.logs.place(x=700, y=100)

        self.add_on_option_frame()
        self.add_on_file_open_file()
        self.add_on_depth_and_density()
        self.add_on_execute()
        self.add_on_container()
        self.add_on_logs()

    def add_on_option_frame(self):
        """
        Рамка для выбора параметров скрытия
        """

        self.hiding_stegomethod_video = tkinter.Frame(self.option_frame, height=100, width=350, bd=1)
        self.hiding_stegomethod_video.place(x=0, y=60, width=350,
                                            height=100)  # Рамка для выбора метода скрытия в видео

        self.stegomsg_type = Frame(self.option_frame, height=60, width=350)
        self.stegomsg_type.place(x=0, y=0, width=350, height=60)  # Рамка для выбора контейнера

        self.sub_add_on_stegomsg_type()
        self.sub_add_on_hiding_stegomethod_video()

    def add_on_file_open_file(self):
        """
        Рамка для выбора файла
        """

        self.stegocontainer_file = Frame(self.file_open_file, height=100, width=300)
        self.stegocontainer_file.place(x=0, y=0, width=300, height=100)  # Рамка для выбора скрываемого файла

        self.stegomsg_file = Frame(self.file_open_file, height=100, width=300)
        self.stegomsg_file.place(x=300, y=0, width=300, height=100)  # Рамка для выбора контейнера

        self.sub_add_on_stegocontainer_file()
        self.sub_add_on_stegomsg_file()


    def add_on_depth_and_density(self):
        self.label18 = Label(self.depth_and_density, text='Глубина скрытия:')
        self.label19 = Label(self.depth_and_density, text='Плотность скрытия:')
        self.label27 = Label(self.depth_and_density, text='Зерно для МПИ:')
        self.label28 = Label(self.depth_and_density, text='Интервал для МПИ:')

        self.depth_entry = Entry(self.depth_and_density, width=4)
        self.density_entry = Entry(self.depth_and_density, width=4)
        self.seed_entry = Entry(self.depth_and_density, width=4)
        self.ceil_entry = Entry(self.depth_and_density, width=4)

        self.label18.grid(row=0, column=0)
        self.depth_entry.grid(row=0, column=1)
        self.label19.grid(row=0, column=2)
        self.density_entry.grid(row=0, column=3)
        self.label27.grid(row=1, column=0)
        self.seed_entry.grid(row=1, column=1)
        self.label28.grid(row=1, column=2)
        self.ceil_entry.grid(row=1, column=3)

    def add_on_execute(self):
        self.button3 = Button(self.execute, text='РАСКРЫТЬ', command=self.find)
        self.button3.pack()


    def add_on_container(self):
        """
        Рамка для вывода изоражений
        """

        self.stegocontainer = tkinter.Frame(self.container, height=200, width=175)
        self.stegocontainer.place(x=0, y=0, width=175, height=200)  # Рамка для вывода стеганоконтейнера

        self.stegomsg = tkinter.Frame(self.container, height=200, width=175)
        self.stegomsg.place(x=180, y=0, width=175, height=200)  # Рамка для вывода пустого контейнера изнутри

        self.sub_add_on_stegomsg_exported()
        self.sub_add_on_stegocontainer()


    def add_on_logs(self):
        self.label26 = Label(self.logs, text='Лог:', style='BW.TLabel')
        self.label26.pack(anchor='w')

        self.logbox_all = Text(self.logs, width=34, height=5)
        self.scrollbar_all = Scrollbar(self.logs)
        self.scrollbar_all['command'] = self.logbox_all.yview
        self.logbox_all['yscrollcommand'] = self.scrollbar_all.set
        self.logbox_all.pack(side='left', fill='both', expand=True)
        self.scrollbar_all.pack(side='left', fill='y', expand=True)

    def sub_add_on_stegomsg_type(self):
        """
        Рамка для выбора типа скрываемого файла
        """

        self.var_file_type = StringVar()
        self.label2 = Label(self.stegomsg_type, text='Тип скрытого сообщения:', style='BW.TLabel')

        self.rbutton3 = Radiobutton(self.stegomsg_type, text='Цифровой водяной знак',
                                    variable=self.var_file_type, value='cvz')
        self.rbutton4 = Radiobutton(self.stegomsg_type, text='Текстовый файл',
                                    variable=self.var_file_type, value='text')

        self.label2.place(x=0, y=0)
        self.rbutton3.place(x=10, y=20)
        self.rbutton4.place(x=10, y=40)

    def sub_add_on_stegomsg_file(self):
        """
        Рамка для выбора скрываемого файла
        """

        self.label8 = Label(self.stegomsg_file, text='Выбрать файл для записи стегосообщения:')
        self.label9 = Label(self.stegomsg_file, text='')
        self.button1 = Button(self.stegomsg_file, text='Выбрать файл', command=self.load_stegomsg_export)
        self.open_file_path = Entry(self.stegomsg_file, width=40)

        self.label8.pack(side=TOP)
        self.button1.pack(side=TOP)
        self.label9.pack(side=TOP)
        self.open_file_path.pack(side=TOP)

    def sub_add_on_hiding_stegomethod_video(self):
        """
        Рамка для метода скрытия в видео
        """

        self.var_hiding_stegomethod_vid = StringVar()
        self.label6 = Label(self.hiding_stegomethod_video, text='Метод скрытия информации в видеоконтейнере:',
                            style='BW.TLabel')
        self.rbutton12 = Radiobutton(self.hiding_stegomethod_video,
                                     text='Метод кодирования наименее значащих бит',
                                     variable=self.var_hiding_stegomethod_vid, value='LSBvid')
        self.rbutton13 = Radiobutton(self.hiding_stegomethod_video,
                                     text='Метод псевдослучайного интервала',
                                     variable=self.var_hiding_stegomethod_vid, value='PRI')
        self.rbutton14 = Radiobutton(self.hiding_stegomethod_video,
                                     text='Метод псевдослучайной перестановки',
                                     variable=self.var_hiding_stegomethod_vid, value='PRP')
        self.rbutton15 = Radiobutton(self.hiding_stegomethod_video,
                                     text='Метод Коха и Жао',
                                     variable=self.var_hiding_stegomethod_vid, value='K&J')

        self.rbutton14.configure(state=DISABLED)

        self.label6.place(x=0, y=0)
        self.rbutton12.place(x=10, y=20)
        self.rbutton13.place(x=10, y=40)
        self.rbutton14.place(x=10, y=60)
        self.rbutton15.place(x=10, y=80)


    def sub_add_on_stegocontainer_file(self):
        """
        Рамка для выбора контейнера
        """
        self.label10 = Label(self.stegocontainer_file, text='Выбрать стегоконтейнер:')
        self.button2 = Button(self.stegocontainer_file, text='Выбрать файл', command=self.load_stegofile)
        self.label11 = Label(self.stegocontainer_file, text='')
        self.stego_cont_path = Entry(self.stegocontainer_file, width=40)

        self.label10.pack()
        self.button2.pack(side=TOP)
        self.label11.pack()
        self.stego_cont_path.pack(side=TOP)





    def sub_add_on_stegocontainer(self):
        """
        Рамка для вывода стеганоконтейнера
        """
        self.label14 = Label(self.stegocontainer, text='Стегоконтейнер:')


        self.label14.pack()


    def sub_add_on_stegomsg_exported(self):
        self.label16 = Label(self.stegomsg, text='Раскрытое сообщение:')


        self.label16.pack()


    def load_stegomsg_export(self):
        fn = ''
        if self.var_file_type.get() == 'cvz':
            fn = tkinter.filedialog.askopenfilename(filetypes=[('*.bmp files', '.bmp')],
                                                    initialdir=(os.path.expanduser('~/')))
        elif self.var_file_type.get() == 'text':
            fn = tkinter.filedialog.askopenfilename(filetypes=[('*.txt file', '.txt')],
                                                    initialdir=(os.path.expanduser('~/')))

        if fn == '':
            fn = 'Выберите тип скрытого сообщение!'

        self.open_file_path.delete(0, END)
        self.open_file_path.insert('insert', fn)

    def load_stegofile(self):

        fn = ''
        fn = tkinter.filedialog.askopenfilename(filetypes=[('*.bmp', '.bmp')],
                                                        initialdir=(os.path.expanduser('~/')))
        if fn == '':
            fn = 'Выберите контейнер!'

        self.stego_cont_path.delete(0, END)
        self.stego_cont_path.insert('insert', fn)

    def find(self):

        self.stego_cont_path_str = self.stego_cont_path.get().rstrip()
        self.open_file_path_str = self.open_file_path.get().rstrip()

        if self.stego_cont_path_str == '':
            self.stego_cont_path.insert('insert', 'Выберите параметры контейнера!')

        elif self.open_file_path_str == '':
            self.open_file_path.insert('insert', 'Выберите тип контейнера!')
        else:
            print(self.stego_cont_path_str)

            file = open(self.stego_cont_path_str, 'rb')
            stego_file_bytes = file.read()
            file.close()

            img = BMPImage(stego_file_bytes)
            depth = 1
            density = 1
            seed = 300
            ceil = 1

            if self.depth_entry.get() != '':
                depth = int(self.depth_entry.get())
            if self.density_entry.get() != '':
                density = int(self.density_entry.get())
            if self.seed_entry.get() != '':
                seed = int(self.seed_entry.get())
            if self.ceil_entry.get() != '':
                ceil = int(self.ceil_entry.get())


            k = time.process_time()
            extracted_data = ''


            hiding_stegomethod_vid = self.var_hiding_stegomethod_vid.get()
            if hiding_stegomethod_vid == '':
                    self.logbox_all.insert('insert', 'Не выбран метод скрытия информации\n')
            else:
                try:
                    if hiding_stegomethod_vid == 'LSBvid':
                        self.logbox_all.insert('insert', '\n--------------\n'
                                                         '--------------\n'
                                                         'Метод стеганографического скрытия:\n'
                                                         '%s\n'
                                                         'Глубина скрытия:\n'
                                                         '%s\n'
                                                         'Плотность скрытия:\n'
                                                         '%s\n' % ('Кодирование наименее значимых бит', depth, density))
                        extracted_data = BMPLSB.get_stego(img, depth=depth, density=density)
                    elif hiding_stegomethod_vid == 'PRI':
                        self.logbox_all.insert('insert', '\n--------------\n'
                                                         '--------------\n'
                                                         'Метод стеганографического скрытия:\n'
                                                         '%s\n'
                                                         'Глубина скрытия:\n'
                                                         '%s\n'
                                                         'Плотность скрытия:\n'
                                                         '%s\n'
                                                         'Зерно псевдослучайного интервала:\n'
                                                         '%s\n'
                                                         'Интервал МПИ:\n'
                                                         '%s\n' % ('Кодирование наименее значимых бит', depth,
                                                                   density, seed, ceil))
                        extracted_data = BMPLSBInterval.get_stego(img, seed, ceil, depth=depth)
                    elif hiding_stegomethod_vid == 'K&J':
                        self.logbox_all.insert('insert', '\n--------------\n'
                                                         '--------------\n'
                                                         'Метод стеганографического скрытия:\n'
                                                         '%s\n' % 'Коха и Жао')
                        extracted_data = KochZhao.get_stego(img)

                except DepthException as var1:
                    self.logbox_all.insert('insert', '-----------\n'
                                                     'Ошибка!!!\n'
                                                     '%s\n'
                                                     '----------\n' % str(var1))
                except DensityException as var2:
                    self.logbox_all.insert('insert', '-----------\n'
                                                     'Ошибка!!!\n'
                                                     '%s\n'
                                                     '----------\n' % str(var2))
                except StegomessageSizeException as var3:
                    self.logbox_all.insert('insert', '-----------\n'
                                                     'Ошибка!!!\n'
                                                     '%s\n'
                                                     '----------\n' % str(var3))
                except NoHeaderFoundException as var4:
                    self.logbox_all.insert('insert', '-----------\n'
                                                     'Ошибка!!!\n'
                                                     '%s\n'
                                                     '----------\n' % str(var4))
                except ImageTooSmallException as var5:
                    self.logbox_all.insert('insert', '-----------\n'
                                                     'Ошибка!!!\n'
                                                     '%s\n'
                                                     '----------\n' % str(var5))
                except ImageDimensionsException as var6:
                    self.logbox_all.insert('insert', '-----------\n'
                                                     'Ошибка!!!\n'
                                                     '%s\n'
                                                     '----------\n' % str(var6))
                except DCTDimensionException as var7:
                    self.logbox_all.insert('insert', '-----------\n'
                                                     'Ошибка!!!\n'
                                                     '%s\n'
                                                     '----------\n' % str(var7))

                else:
                    m = time.process_time()
                    print(m - k)

                    opf = open(self.open_file_path_str, 'wb')
                    opf.write(extracted_data)
                    opf.close()


                    self.logbox_all.insert('insert', '\n-----------\n'
                                                     'Данные успешно экспортированы.\n'
                                                     '----------\n')
                    image = Image.open(self.stego_cont_path_str)
                    image = image.resize((170, 170))
                    photo = ImageTk.PhotoImage(image)
                    label = Label(self.stegocontainer, image=photo)
                    label.image = photo
                    label.bind("<Button-1>", self.open_stegocontainer)
                    label.pack()

                    if self.var_file_type.get() == 'cvz':
                        image2 = Image.open(self.open_file_path_str)
                        image2 = image2.resize((170, 170))
                        photo2 = ImageTk.PhotoImage(image2)
                        label2 = Label(self.stegomsg, image=photo2)
                        label2.image = photo2
                        label2.bind("<Button-1>", self.open_stegomsg_image)
                        label2.pack()
                    elif self.var_file_type.get() == 'text':
                        file = open(self.open_file_path_str, 'rb')
                        file_bytes = file.read()
                        file.close()


                        logbox1 = Text(self.stegomsg, width=15, height=5)
                        scrollbar1 = Scrollbar(self.stegomsg)
                        scrollbar1['command'] = logbox1.yview
                        logbox1['yscrollcommand'] = scrollbar1.set
                        logbox1.pack(side='left', fill='both', expand=True)
                        scrollbar1.pack(side='left', fill='y', expand=True)
                        logbox1.insert('insert', file_bytes)






    def bitmap(self, file, vidget):

        arr = bytearray(file)
        arr2 = []
        for x in range(2000):
            arr2.append(str(int(arr[x])))
        print(len(arr2))
        vidget.delete(1.0, END)
        vidget.insert('insert', " ".join(arr2))


    def open_stegocontainer(self, event):
        StegoImage(self.slave, self.stego_cont_path_str)

    def open_stegomsg_image(self, event):
        StegomsgImage(self.slave, self.open_file_path_str)


class StegomsgImage:
    def __init__(self, master, path):
        self.slave1 = Toplevel(master)
        self.slave1.resizable(width='true', height='true')
        self.slave1.title('Стегоконтейнер')

        image = Image.open(path)
        photo = ImageTk.PhotoImage(image)
        h = photo.height()
        w = photo.width()
        label1 = Label(self.slave1, image=photo)
        label1.pack()

        self.slave1.geometry('%dx%d+200+100' % (w, h))

        self.slave1.wait_window()


class StegoImage:
    def __init__(self, master, path):
        self.slave1 = Toplevel(master)
        self.slave1.resizable(width='true', height='true')
        self.slave1.title('Cтегосообщение')

        image = Image.open(path)
        photo = ImageTk.PhotoImage(image)
        h = photo.height()
        w = photo.width()
        label1 = Label(self.slave1, image=photo)
        label1.pack()

        self.slave1.geometry('%dx%d+%d+100' % (w, h, (200 + w)))

        self.slave1.wait_window()

