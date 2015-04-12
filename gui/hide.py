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
from helpers.exceptions import *


class Hide:
    def __init__(self, master):
        self.slave = Toplevel(master)
        self.slave.resizable(width='false', height='false')
        self.slave.title('СКРЫТИЕ')
        self.slave.geometry('1000x640+200+50')
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

        self.commands_for_rbuttons()

        self.slave.wait_window()

    def on_main_frame(self):
        """
        Рамка для меню
        """

        self.option_frame = Frame(self.slave, height=640, width=350)
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

        self.container = tkinter.Frame(self.slave, height=510, width=350)
        self.container.pack_propagate(0)  # Рамка для вывода стеганоконтейнера
        self.container.place(x=350, y=190)

        self.logs = tkinter.Frame(self.slave, height=530, width=300)
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

        self.cont_type = tkinter.Frame(self.option_frame, height=60, width=350,
                                       bd=1)  # Рамка для выбора типа контейнера
        self.cont_type.place(x=0, y=0, width=350, height=60)

        self.file_type = tkinter.Frame(self.option_frame, height=60, width=350, bd=1)
        self.file_type.place(x=0, y=60, width=350, height=60)  # Рамка для выбора типа файла

        self.compression_method_video = tkinter.Frame(self.option_frame, height=80, width=350, bd=1)
        self.compression_method_video.place(x=0, y=120, width=350, height=80)  # Рамка для выбора способа сжатия в видео

        self.compression_method_audio = tkinter.Frame(self.option_frame, height=60, width=350, bd=1)
        self.compression_method_audio.place(x=0, y=200, width=350, height=60)  # Рамка для выбора способа сжатия в аудио

        self.hiding_method_video = tkinter.Frame(self.option_frame, height=60, width=350, bd=1)
        self.hiding_method_video.place(x=0, y=260, width=350, height=60)  # Рамка для выбора способа скрытия в видео

        self.hiding_stegomethod_video = tkinter.Frame(self.option_frame, height=100, width=350, bd=1)
        self.hiding_stegomethod_video.place(x=0, y=320, width=350,
                                            height=100)  # Рамка для выбора метода скрытия в видео

        self.hiding_algorithm_video = tkinter.Frame(self.option_frame, height=120, width=350, bd=1)
        self.hiding_algorithm_video.place(x=0, y=420, width=350,
                                          height=120)  # Рамка для выбора алгоритма скрытия в видео

        self.hiding_method_audio = tkinter.Frame(self.option_frame, height=80, width=350, bd=1)
        self.hiding_method_audio.place(x=0, y=540, width=350, height=100)  # Рамка для выбора метода скрытия в аудио

        self.sub_add_on_cont_type()
        self.sub_add_on_file_type()
        self.sub_add_on_compression_method_video()
        self.sub_add_on_compression_method_audio()
        self.sub_add_on_hiding_method_video()
        self.sub_add_on_hiding_stegomethod_video()
        self.sub_add_on_hiding_algorithm_video()
        self.sub_add_on_hiding_method_audio()


    def add_on_file_open_file(self):
        """
        Рамка для выбора файла
        """

        self.open_file = Frame(self.file_open_file, height=100, width=300)
        self.open_file.place(x=0, y=0, width=300, height=100)  # Рамка для выбора скрываемого файла

        self.stego_file = Frame(self.file_open_file, height=100, width=300)
        self.stego_file.place(x=300, y=0, width=300, height=100)  # Рамка для выбора контейнера

        self.sub_add_on_open_file()
        self.sub_add_on_stego_file()


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
        self.button3 = Button(self.execute, text='СКРЫТЬ', command=self.hide)
        self.button3.pack()


    def add_on_container(self):
        """
        Рамка для вывода изоражений
        """

        self.empty_container = tkinter.Frame(self.container, height=200, width=175)
        self.empty_container.place(x=0, y=0, width=175, height=200)  # Рамка для вывода пустого контейнера

        self.stegocontainer = tkinter.Frame(self.container, height=200, width=175)
        self.stegocontainer.place(x=175, y=0, width=175, height=200)  # Рамка для вывода стеганоконтейнера

        self.empty_container_inside = tkinter.Frame(self.container, height=250, width=175)
        self.empty_container_inside.place(x=0, y=200, width=175,
                                          height=240)  # Рамка для вывода пустого контейнера изнутри

        self.stegocontainer_inside = tkinter.Frame(self.container, height=240, width=175)
        self.stegocontainer_inside.place(x=175, y=200, width=175,
                                         height=240)  # Рамка для вывода стеганоконтейнера изнутри

        self.sub_add_on_empty_container()
        self.sub_add_on_stegocontainer()
        self.sub_add_on_empty_container_inside()
        self.sub_add_on_stegocontainer_inside()


    def add_on_logs(self):
        self.label26 = Label(self.logs, text='Лог:', style='BW.TLabel')
        self.label26.pack(anchor='w')

        self.logbox_all = Text(self.logs, width=34, height=5)
        self.scrollbar_all = Scrollbar(self.logs)
        self.scrollbar_all['command'] = self.logbox_all.yview
        self.logbox_all['yscrollcommand'] = self.scrollbar_all.set
        self.logbox_all.pack(side='left', fill='both', expand=True)
        self.scrollbar_all.pack(side='left', fill='y', expand=True)

    def sub_add_on_cont_type(self):
        """
        # Рамка для выбора типа контейнера
        """

        self.var_cont_type = StringVar()
        self.label1 = Label(self.cont_type, text='Тип контейнера:', style='BW.TLabel')
        self.rbutton1 = Radiobutton(self.cont_type, text='Видео', variable=self.var_cont_type, value='video')
        self.rbutton2 = Radiobutton(self.cont_type, text='Аудио', variable=self.var_cont_type, value='audio')

        self.rbutton2.configure(state=DISABLED)

        self.label1.place(x=0, y=0)
        self.rbutton1.place(x=10, y=20)
        self.rbutton2.place(x=10, y=40)


    def sub_add_on_file_type(self):
        """
        Рамка для выбора типа скрываемого файла
        """

        self.var_file_type = StringVar()
        self.label2 = Label(self.file_type, text='Тип скрываемого сообщения:', style='BW.TLabel')

        self.rbutton3 = Radiobutton(self.file_type, text='Цифровой водяной знак',
                                    variable=self.var_file_type, value='cvz')
        self.rbutton4 = Radiobutton(self.file_type, text='Текстовый файл',
                                    variable=self.var_file_type, value='text')

        self.label2.place(x=0, y=0)
        self.rbutton3.place(x=10, y=20)
        self.rbutton4.place(x=10, y=40)

    def sub_add_on_compression_method_video(self):
        """
        Рамка для выбора способа сжатия в видеоконтейнере
        """

        self.var_comp_method_vid = StringVar()
        self.label3 = Label(self.compression_method_video, text='Тип сжатия в видеоконтейнере:', style='BW.TLabel')
        self.rbutton5 = Radiobutton(self.compression_method_video, text='bmp',
                                    variable=self.var_comp_method_vid, value='bmp')
        self.rbutton6 = Radiobutton(self.compression_method_video, text='jpeg',
                                    variable=self.var_comp_method_vid, value='jpeg')
        self.rbutton7 = Radiobutton(self.compression_method_video, text='mpeg',
                                    variable=self.var_comp_method_vid, value='mpeg')

        self.rbutton6.configure(state=DISABLED)
        self.rbutton7.configure(state=DISABLED)

        self.label3.place(x=0, y=0)
        self.rbutton5.place(x=10, y=20)
        self.rbutton6.place(x=10, y=40)
        self.rbutton7.place(x=10, y=60)

    def sub_add_on_compression_method_audio(self):
        """
        Рамка для выбора способа сжатия в аудиоконтейнер
        """

        self.var_comp_method_audio = StringVar()
        self.label4 = Label(self.compression_method_audio, text='Тип сжатия в аудиоконтейнере:', style='BW.TLabel')
        self.rbutton8 = Radiobutton(self.compression_method_audio, text='waw',
                                    variable=self.var_comp_method_audio, value='waw')
        self.rbutton9 = Radiobutton(self.compression_method_audio, text='mp4',
                                    variable=self.var_comp_method_audio, value='mp4')

        self.rbutton8.configure(state=DISABLED)
        self.rbutton9.configure(state=DISABLED)

        self.label4.place(x=0, y=0)
        self.rbutton8.place(x=10, y=20)
        self.rbutton9.place(x=10, y=40)

    def sub_add_on_hiding_method_video(self):
        """
        Рамка для способа скрытия в видео
        """

        self.var_hiding_method_vid = StringVar()
        self.label5 = Label(self.hiding_method_video, text='Способ скрытия информации в видеоконтейнере:',
                            style='BW.TLabel')
        self.rbutton10 = Radiobutton(self.hiding_method_video, text='В пространственной области',
                                     variable=self.var_hiding_method_vid, value='spatial')
        self.rbutton11 = Radiobutton(self.hiding_method_video, text='В частотной области',
                                     variable=self.var_hiding_method_vid, value='frequency')

        self.label5.place(x=0, y=0)
        self.rbutton10.place(x=10, y=20)
        self.rbutton11.place(x=10, y=40)

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

    def sub_add_on_hiding_algorithm_video(self):
        """
        Рамка для алгоритма скрытия в видео
        """

        self.var_hiding_algorithm_vid = StringVar()
        self.label20 = Label(self.hiding_algorithm_video, text='Алгоритм скрытия информации в видеоконтейнере:',
                             style='BW.TLabel')
        self.rbutton18 = Radiobutton(self.hiding_algorithm_video,
                                     text='Алгоритм Куттера',
                                     variable=self.var_hiding_algorithm_vid, value='Kutter')
        self.rbutton19 = Radiobutton(self.hiding_algorithm_video,
                                     text='Алгоритм Брайндокса',
                                     variable=self.var_hiding_algorithm_vid, value='Braindoks')
        self.rbutton20 = Radiobutton(self.hiding_algorithm_video,
                                     text='Алгоритм Дармстедтера-Делейгла',
                                     variable=self.var_hiding_algorithm_vid, value='D-D')
        self.rbutton21 = Radiobutton(self.hiding_algorithm_video,
                                     text='Алгоритм Фридриха',
                                     variable=self.var_hiding_algorithm_vid, value='Fridrih')

        self.rbutton22 = Radiobutton(self.hiding_algorithm_video,
                                     text='Алгоритм Хсу и Ву',
                                     variable=self.var_hiding_algorithm_vid, value='H&V')

        self.rbutton18.configure(state=DISABLED)
        self.rbutton19.configure(state=DISABLED)
        self.rbutton20.configure(state=DISABLED)
        self.rbutton21.configure(state=DISABLED)
        self.rbutton22.configure(state=DISABLED)

        self.label20.place(x=0, y=0)
        self.rbutton18.place(x=10, y=20)
        self.rbutton19.place(x=10, y=40)
        self.rbutton20.place(x=10, y=60)
        self.rbutton21.place(x=10, y=80)
        self.rbutton22.place(x=10, y=100)


    def sub_add_on_hiding_method_audio(self):
        """
        Рамка для метода скрытия в аудио
        """

        self.var_hiding_method_audio = StringVar()
        self.label7 = Label(self.hiding_method_audio, text='Метод скрытия информации в аудиоконтейнере:',
                            style='BW.TLabel')
        self.rbutton23 = Radiobutton(self.hiding_method_audio,
                                     text='Метод кодирования наименее значащих бит',
                                     variable=self.var_hiding_method_audio, value='LSBaudio')
        self.rbutton16 = Radiobutton(self.hiding_method_audio,
                                     text='Метод расширения спектра',
                                     variable=self.var_hiding_method_audio, value='expand')
        self.rbutton17 = Radiobutton(self.hiding_method_audio,
                                     text='Метод фазового кодирования',
                                     variable=self.var_hiding_method_audio, value='phase')

        self.rbutton23.configure(state=DISABLED)
        self.rbutton16.configure(state=DISABLED)
        self.rbutton17.configure(state=DISABLED)

        self.label7.place(x=0, y=0)
        self.rbutton23.place(x=10, y=20)
        self.rbutton16.place(x=10, y=40)
        self.rbutton17.place(x=10, y=60)


    def sub_add_on_open_file(self):
        """
        Рамка для выбора скрываемого файла
        """

        self.label8 = Label(self.open_file, text='Выбрать стегосообщение:')
        self.label9 = Label(self.open_file, text='')
        self.button1 = Button(self.open_file, text='Выбрать файл', command=self.load_open_file)
        self.open_file_path = Entry(self.open_file, width=40)

        self.label8.pack(side=TOP)
        self.button1.pack(side=TOP)

        self.open_file_path.pack(side=TOP)

    def sub_add_on_stego_file(self):
        """
        Рамка для выбора контейнера
        """
        self.label10 = Label(self.stego_file, text='Выбрать пустой контейнер:')
        self.label11 = Label(self.stego_file, text='')
        self.button2 = Button(self.stego_file, text='Выбрать пустой контейнер', command=self.load_container_file)
        self.stego_file_path = Entry(self.stego_file, width=40)
        self.button4 = Button(self.stego_file, text='Выбрать файл для стегоконтейнера',
                              command=self.load_stegocontainer_file)
        self.stego_cont_path = Entry(self.stego_file, width=40)

        self.button2.pack(side=TOP)
        self.stego_file_path.pack(side=TOP)
        self.button4.pack(side=TOP)
        self.stego_cont_path.pack(side=TOP)

    def sub_add_on_empty_container(self):
        """
        Рамка для вывода пустого контейнера
        """
        self.label12 = Label(self.empty_container, text='Пустой контейнер:')
        self.label12.pack()



    def sub_add_on_stegocontainer(self):
        """
        Рамка для вывода стеганоконтейнера
        """
        self.label14 = Label(self.stegocontainer, text='Стегоконтейнер')

        self.label14.pack()



    def sub_add_on_empty_container_inside(self):
        """
        Рамка для вывода пустого контейнера изнутри
        """
        self.label16 = Label(self.empty_container_inside, text='Битмап')
        self.label16.pack()

        self.logbox1 = Text(self.empty_container_inside, width=19, height=5)
        self.scrollbar1 = Scrollbar(self.empty_container_inside)
        self.scrollbar1['command'] = self.logbox1.yview
        self.logbox1['yscrollcommand'] = self.scrollbar1.set
        self.logbox1.pack(side='left', fill='both', expand=True)
        self.scrollbar1.pack(side='left', fill='y', expand=True)

    def sub_add_on_stegocontainer_inside(self):
        """"
        Рамка для вывода стеганоконтейнера изнутри
        """

        self.label17 = Label(self.stegocontainer_inside, text='Битмап')
        self.label17.pack()

        self.logbox2 = Text(self.stegocontainer_inside, width=19, height=5)
        self.scrollbar2 = Scrollbar(self.stegocontainer_inside)
        self.scrollbar2['command'] = self.logbox2.yview
        self.logbox2['yscrollcommand'] = self.scrollbar2.set
        self.logbox2.pack(side='left', fill='both', expand=True)
        self.scrollbar2.pack(side='left', fill='y', expand=True)


    def commands_for_rbuttons(self):
        self.rbutton1.configure(command=self.command_for_rbutton1)
        self.rbutton2.configure(command=self.command_for_rbutton2)
        self.rbutton3.configure(command=self.command_for_rbutton3)
        self.rbutton4.configure(command=self.command_for_rbutton4)
        self.rbutton5.configure(command=self.command_for_rbutton5)
        self.rbutton6.configure(command=self.command_for_rbutton6)
        self.rbutton7.configure(command=self.command_for_rbutton7)
        self.rbutton8.configure(command=self.command_for_rbutton8)
        self.rbutton9.configure(command=self.command_for_rbutton9)
        self.rbutton10.configure(command=self.command_for_rbutton10)
        self.rbutton11.configure(command=self.command_for_rbutton11)
        self.rbutton12.configure(command=self.command_for_rbutton12)
        self.rbutton13.configure(command=self.command_for_rbutton13)
        self.rbutton14.configure(command=self.command_for_rbutton14)
        self.rbutton15.configure(command=self.command_for_rbutton15)
        self.rbutton16.configure(command=self.command_for_rbutton16)
        self.rbutton17.configure(command=self.command_for_rbutton17)
        self.rbutton18.configure(command=self.command_for_rbutton18)
        self.rbutton19.configure(command=self.command_for_rbutton19)
        self.rbutton20.configure(command=self.command_for_rbutton20)
        self.rbutton21.configure(command=self.command_for_rbutton21)
        self.rbutton22.configure(command=self.command_for_rbutton22)
        self.rbutton23.configure(command=self.command_for_rbutton23)

    def command_for_rbutton1(self):
        pass

    def command_for_rbutton2(self):
        pass

    def command_for_rbutton3(self):
        pass

    def command_for_rbutton4(self):
        pass

    def command_for_rbutton5(self):
        pass

    def command_for_rbutton6(self):
        pass

    def command_for_rbutton7(self):
        pass

    def command_for_rbutton8(self):
        pass

    def command_for_rbutton9(self):
        pass

    def command_for_rbutton10(self):
        self.rbutton12.configure(state=NORMAL)
        self.rbutton13.configure(state=NORMAL)
        self.rbutton15.configure(state=DISABLED)


    def command_for_rbutton11(self):
        self.rbutton12.configure(state=DISABLED)
        self.rbutton13.configure(state=DISABLED)
        self.rbutton15.configure(state=NORMAL)

    def command_for_rbutton12(self):
        pass

    def command_for_rbutton13(self):
        pass

    def command_for_rbutton14(self):
        pass

    def command_for_rbutton15(self):
        pass

    def command_for_rbutton16(self):
        pass

    def command_for_rbutton17(self):
        pass

    def command_for_rbutton18(self):
        pass

    def command_for_rbutton19(self):
        pass

    def command_for_rbutton20(self):
        pass

    def command_for_rbutton21(self):
        pass

    def command_for_rbutton22(self):
        pass

    def command_for_rbutton23(self):
        pass

    def load_open_file(self):
        fn = ''
        if self.var_file_type.get() == 'cvz':
            fn = tkinter.filedialog.askopenfilename(filetypes=[('*.bmp files', '.bmp')],
                                                    initialdir=(os.path.expanduser('~/')))
        elif self.var_file_type.get() == 'text':
            fn = tkinter.filedialog.askopenfilename(filetypes=[('*.txt file', '.txt')],
                                                    initialdir=(os.path.expanduser('~/')))

        if fn == '':
            fn = 'Выберите тип скрываемого сообщения!'

        self.open_file_path.delete(0, END)
        self.open_file_path.insert('insert', fn)

    def load_container_file(self):
        fn = ''
        if self.var_cont_type.get() == 'video':
            if self.var_comp_method_vid.get() == 'bmp':
                fn = tkinter.filedialog.askopenfilename(filetypes=[('*.bmp', '.bmp')],
                                                        initialdir=(os.path.expanduser('~/')))
            elif self.var_comp_method_vid.get() == 'jpeg':
                fn = tkinter.filedialog.askopenfilename(filetypes=[('*.jpeg', '.jpeg')],
                                                        initialdir=(os.path.expanduser('~/')))
            elif self.var_comp_method_vid.get() == 'mpeg':
                fn = tkinter.filedialog.askopenfilename(filetypes=[('*.mpeg', '.mpeg')],
                                                        initialdir=(os.path.expanduser('~/')))

        elif self.var_file_type.get() == 'audio':
            if self.var_comp_method_vid.get() == 'waw':
                fn = tkinter.filedialog.askopenfilename(filetypes=[('*.waw', '.waw')],
                                                        initialdir=(os.path.expanduser('~/')))
            elif self.var_comp_method_vid.get() == 'mp4':
                fn = tkinter.filedialog.askopenfilename(filetypes=[('*.mp4', '.mp4')],
                                                        initialdir=(os.path.expanduser('~/')))

        if fn == '':
            fn = 'Выберите параметры контейнера!'

        self.stego_file_path.delete(0, END)
        self.stego_file_path.insert('insert', fn)

    def load_stegocontainer_file(self):
        fn = ''
        if self.var_cont_type.get() == 'video':
            if self.var_comp_method_vid.get() == 'bmp':
                fn = tkinter.filedialog.askopenfilename(filetypes=[('*.bmp', '.bmp')],
                                                        initialdir=(os.path.expanduser('~/')))
            elif self.var_comp_method_vid.get() == 'jpeg':
                fn = tkinter.filedialog.askopenfilename(filetypes=[('*.jpeg', '.jpeg')],
                                                        initialdir=(os.path.expanduser('~/')))
            elif self.var_comp_method_vid.get() == 'mpeg':
                fn = tkinter.filedialog.askopenfilename(filetypes=[('*.mpeg', '.mpeg')],
                                                        initialdir=(os.path.expanduser('~/')))

        elif self.var_file_type.get() == 'audio':
            if self.var_comp_method_vid.get() == 'waw':
                fn = tkinter.filedialog.askopenfilename(filetypes=[('*.waw', '.waw')],
                                                        initialdir=(os.path.expanduser('~/')))
            elif self.var_comp_method_vid.get() == 'mp4':
                fn = tkinter.filedialog.askopenfilename(filetypes=[('*.mp4', '.mp4')],
                                                        initialdir=(os.path.expanduser('~/')))

        if fn == '':
            fn = 'Выберите файл для стегоконтейнера'

        self.stego_cont_path.delete(0, END)
        self.stego_cont_path.insert('insert', fn)

    def hide(self):

        self.stego_file_path_str = self.stego_file_path.get().rstrip()
        self.open_file_path_str = self.open_file_path.get().rstrip()
        self.stego_cont_path_str = self.stego_cont_path.get().rstrip()
        if self.stego_file_path_str == '':
            self.stego_file_path.insert('insert', 'Выберите тип контейнера!')

        elif self.open_file_path_str == '':
            self.stego_file_path.insert('insert', 'Выберите тип контейнера!')
        else:
            print(self.stego_file_path_str)

            file = open(self.stego_file_path_str, 'rb')
            file_bytes = file.read()
            file.close()

            img = BMPImage(file_bytes)
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

            file = open(self.open_file_path_str, 'rb')
            open_file_bytes = file.read()
            file.close()

            stego_msg = []
            if self.var_file_type.get() == 'text':
                stego_msg = bytearray(open_file_bytes)

            if self.var_file_type.get() == 'cvz':
                stego_msg = bytearray(open_file_bytes)

            k = time.process_time()
            stego_img = ''

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
                        stego_img = BMPLSB.put_stego(img, stego_msg, depth=depth, density=density)
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
                        stego_img = BMPLSBInterval.put_stego(img, stego_msg, seed, ceil, depth=depth)
                    elif hiding_stegomethod_vid == 'K&J':
                        self.logbox_all.insert('insert', '\n--------------\n'
                                                         '--------------\n'
                                                         'Метод стеганографического скрытия:\n'
                                                         '%s\n' % 'Коха и Жао')
                        stego_img = KochZhao.put_stego(img, stego_msg)

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

                    mse = calculate_MSE(img, stego_img)
                    psnr = calculate_PSNR(img, stego_img, mse)
                    nmse = calculate_NMSE(img, stego_img, mse)
                    snr = calculate_SNR(img, stego_img)
                    n = time.process_time()
                    print(m - k, n - m, n - k)

                    self.logbox_all.insert('insert', '\n--------------\n'
                                                     'Среднеквадратичная ошибка:\n'
                                                     '%.4f\n'
                                                     'Норм. среднеквадратиная ошибка:\n'
                                                     '%.4f\n'
                                                     'Отношение сигнал/шум:\n'
                                                     '%.4f\n'
                                                     'Максимальное отношение с/ш:\n'
                                                     '%.4f' % (mse, nmse, snr, psnr))




                    opf = open(self.stego_cont_path_str, 'wb')
                    opf.write(stego_img.export())
                    opf.close()

                    file = open(self.stego_cont_path_str, 'rb')
                    file_stego = file.read()
                    file.close()
                    print(file_bytes == file_stego)
                    self.bitmap(file_stego, self.logbox2)
                    self.bitmap(file_bytes, self.logbox1)


                    image = Image.open(self.stego_file_path_str)
                    image = image.resize((170, 170))
                    photo = ImageTk.PhotoImage(image)
                    label = Label(self.empty_container, image=photo)
                    label.image = photo # keep a reference!
                    label.bind("<Button-1>", self.open_empty_image)
                    label.pack()




                    image2 = Image.open(self.stego_cont_path_str)
                    image2 = image2.resize((170, 170))
                    photo2 = ImageTk.PhotoImage(image2)
                    label2 = Label(self.stegocontainer, image=photo2)
                    label2.image = photo2
                    label2.bind("<Button-1>", self.open_stego_image)
                    label2.pack()

    def bitmap(self, file, vidget):
        arr = bytearray(file)
        arr2 = []
        for x in range(1000):
            arr2.append(str(int(arr[x])))
        vidget.delete(1.0, END)
        strin = '.' * 19 + '\n'
        vidget.insert('insert', " ".join(x.zfill(3) for x in arr2))
        vidget.insert('insert', '\n%s%s%s' % (strin, strin, strin))
        arr3 = []
        for x in range(-999, 1):
            arr3.append(str(int(arr[x])))
        vidget.insert('insert', " ".join(x.zfill(3) for x in arr3))





    def open_empty_image(self, event):
        EmptyImage(self.slave, self.stego_file_path_str)

    def open_stego_image(self, event):
        StegoImage(self.slave, self.stego_cont_path_str)


class EmptyImage:
    def __init__(self, master, path):
        self.slave1 = Toplevel(master)
        self.slave1.resizable(width='true', height='true')
        self.slave1.title('Пустой контейнер')

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
        self.slave1.title('Cтегоконтейнер')

        image = Image.open(path)
        photo = ImageTk.PhotoImage(image)
        h = photo.height()
        w = photo.width()
        label1 = Label(self.slave1, image=photo)
        label1.pack()


        self.slave1.geometry('%dx%d+%d+100' % (w, h, (200 + w)))

        self.slave1.wait_window()




