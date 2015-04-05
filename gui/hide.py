import tkinter
from tkinter import *
from tkinter.ttk import *
from PIL import Image, ImageTk

class Hide:
    def __init__(self, master):
        self.slave = Toplevel(master)
        self.slave.resizable(width='false', height='true')
        self.slave.title('СКРЫТИЕ')
        self.slave.geometry('950x640+200+50')
        self.slave.grab_set()
        self.slave.focus_set()

        st = Style()
        st.configure('BW.TLabel', font='Verdana 8 bold')
        st.configure('TRadiobutton', font='Verdana 9')
        st.configure('TLabel', font='Verdana 9')
        st.configure('TButton', font='Verdana 9')
        st.configure('MY.TFrame')

        self.on_main_frame()
        self.commands_for_rbuttons()

        self.slave.wait_window()

    def on_main_frame(self):
        """
        Рамка для меню
        """

        self.option_frame =Frame(self.slave, height=640, width=350)
        self.option_frame.pack_propagate(0)          # Рамка для выбора параметров скрытия
        self.option_frame.place(x=0, y=0)

        self.file_open_file = tkinter.Frame(self.slave, height=100, width=600)
        self.file_open_file.pack_propagate(0)      # Рамка для выбора файла
        self.file_open_file.place(x=350, y=0)

        self.depth_and_density = tkinter.Frame(self.slave, height=30, width=600)
        self.depth_and_density.pack_propagate(0)
        self.depth_and_density.place(x=350, y=100, width=600, height=50)  # Рамка для выбора метода скрытия в аудио

        self.container = tkinter.Frame(self.slave, height=400, width=600, bg='yellow')
        self.container.pack_propagate(0)        # Рамка для вывода стеганоконтейнера
        self.container.place(x=350, y=130)

        self.errors = tkinter.Frame(self.slave, height=100, width=600, bg="gray", colormap="new")
        self.errors.pack_propagate(0)        # Рамка для вывода стеганоконтейнера
        self.errors.place(x=350, y=530)

        self.add_on_option_frame()
        self.add_on_file_open_file()
        self.add_on_depth_and_density()
        self.add_on_container()
        self.add_on_errors()

    def add_on_option_frame(self):
        """
        Рамка для выбора параметров скрытия
        """

        self.cont_type = tkinter.Frame(self.option_frame, height=60, width=350, bd=1)  # Рамка для выбора типа контейнера
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
        self.hiding_stegomethod_video.place(x=0, y=320, width=350, height=100)  # Рамка для выбора метода скрытия в видео

        self.hiding_algorithm_video = tkinter.Frame(self.option_frame, height=120, width=350, bd=1)
        self.hiding_algorithm_video.place(x=0, y=420, width=350, height=120)  # Рамка для выбора алгоритма скрытия в видео

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
        self.depth_entry = Entry(self.depth_and_density, width=4)
        self.density_entry = Entry(self.depth_and_density, width=4)

        self.label18.place(x=70, y=0)
        self.depth_entry.place(x=190, y=0)
        self.label19.place(x=380, y=0)
        self.density_entry.place(x=520, y=0)


    def add_on_container(self):
        """
        Рамка для вывода изоражений
        """

        self.empty_container = tkinter.Frame(self.container, height=200, width=175, bg='yellow')
        self.empty_container.place(x=0, y=0, width=175, height=200)  # Рамка для вывода пустого контейнера

        self.stegocontainer = tkinter.Frame(self.container, height=200, width=175, bg='cyan')
        self.stegocontainer.place(x=175, y=0, width=175, height=200)  # Рамка для вывода стеганоконтейнера

        self.empty_container_inside = tkinter.Frame(self.container, height=200, width=175, bg='green')
        self.empty_container_inside.place(x=0, y=200, width=175, height=200)  # Рамка для вывода пустого контейнера изнутри

        self.stegocontainer_inside = tkinter.Frame(self.container, height=200, width=175, bg='red')
        self.stegocontainer_inside.place(x=175, y=200, width=175, height=200)  # Рамка для вывода стеганоконтейнера изнутри


        self.sub_add_on_empty_container()
        self.sub_add_on_stegocontainer()
        self.sub_add_on_empty_container_inside()
        self.sub_add_on_stegocontainer_inside()

    def add_on_errors(self):
        """
        Рамка для вывода ошибок
        """

        self.label15 = tkinter.Label(self.errors, text='здесь ошибки')
        self.label15.pack()

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
        self.label2 = Label(self.file_type, text='Тип скрываемого файла:', style='BW.TLabel')

        self.rbutton3 = Radiobutton(self.file_type, text='Цифровой Водяной Знак',
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

        self.label8 = Label(self.open_file, text='Выбрать скрываемый файл:')
        self.label9 = Label(self.open_file, text='')
        self.button1 = Button(self.open_file, text='Выбрать файл')
        self.open_file_path = Entry(self.open_file, width=40)

        self.label8.pack(side=TOP)
        self.button1.pack(side=TOP)
        self.label9.pack(side=TOP)
        self.open_file_path.pack(side=TOP)

    def sub_add_on_stego_file(self):
        """
        Рамка для выбора контейнера
        """
        self.label10 = Label(self.stego_file, text='Выбрать контейнер:')
        self.label11 = Label(self.stego_file, text='')
        self.button2 = Button(self.stego_file, text='Выбрать файл')
        self.stego_file_path = Entry(self.stego_file, width=40)

        self.label10.pack(side=TOP)
        self.button2.pack(side=TOP)
        self.label11.pack(side=TOP)
        self.stego_file_path.pack(side=TOP)

    def sub_add_on_empty_container(self):
        """
        Рамка для вывода пустого контейнера
        """
        self.label12 = Label(self.empty_container, text='здесь типо контейнер')
        self.label12.pack()
        # canv = tkinter.Canvas(self.empty_container, width=300, height=150)
        image = Image.open('Lenna.png')
        image = image.resize((170, 170))
        photo = ImageTk.PhotoImage(image)

        self.label13 = tkinter.Label(self.empty_container, image=photo)
        self.label13.pack()

    def sub_add_on_stegocontainer(self):
        """
        Рамка для вывода стеганоконтейнера
        """
        self.label14 = Label(self.stegocontainer, text='здесь типо уже измененный файл')
        self.label14.pack()
        image = Image.open('ts2.bmp')
        image = image.resize((170, 170))
        photo = ImageTk.PhotoImage(image)

        self.label15 = Label(self.stegocontainer, image=photo)
        self.label15.pack()


    def sub_add_on_empty_container_inside(self):
        """
        Рамка для вывода пустого контейнера изнутри
        """
        self.label16 = Label(self.empty_container_inside, text='здесь то, что внутри контейнера')
        self.label16.pack()

    def sub_add_on_stegocontainer_inside(self):
        """"
        Рамка для вывода стеганоконтейнера изнутри
        """

        self.label17 = Label(self.stegocontainer_inside, text='здесь то, что внутри измененного файла')
        self.label17.pack()


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
        self.rbutton14.configure(state=NORMAL)
        self.rbutton15.configure(state=DISABLED)


    def command_for_rbutton11(self):
        self.rbutton12.configure(state=DISABLED)
        self.rbutton13.configure(state=DISABLED)
        self.rbutton14.configure(state=DISABLED)
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
        
        

    

    

    
        

    
        
