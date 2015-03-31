class Find:
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
