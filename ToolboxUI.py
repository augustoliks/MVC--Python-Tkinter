from tkinter import *
from tkinter import filedialog

class UI():

    @staticmethod
    def make_button(self, container, text, font, width):
        self.btn = Button(container)
        self.btn["text"] = text
        self.btn["font"] = font
        self.btn["width"] = width

        return self.btn

    @staticmethod
    def make_label(self, container, text, font, size):

        self.lbl = Label(container, text=text)
        self.lbl["font"] = (font, size)

        return self.lbl

    @staticmethod
    def make_container(self, tk_object):
        return Frame(tk_object)

    def get_path_file(self, extensions):
        filename = filedialog.askopenfile()
        return filename.name

    def hello():
        print ("Hello")

    def make_top_menu(self, container):
        menubar = Menu(container)

        # create a pulldown menu, and add it to the menu bar
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_command(label="Save", command=self.hello())
        filemenu.add_separator()
        filemenu.add_command(label="Exit", command=container.quit)
        menubar.add_cascade(label="File", menu=filemenu)

        return filemenu
