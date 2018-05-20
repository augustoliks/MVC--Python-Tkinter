from tkinter import *
from tkinter import filedialog

class UI():

    @staticmethod
    def make_textbox(container, width):
        textbox = Entry(container)
        textbox["width"] = 30
        textbox["font"] = "Calibri"
        return textbox



    @staticmethod
    def make_button(container, text, font, width):
        btn = Button(container)
        btn["text"] = text
        btn["font"] = font
        btn["width"] = width

        return btn

    @staticmethod
    def make_label(container, text, font, size):

        lbl = Label(container, text=text)
        lbl["font"] = (font, size)

        return lbl

    @staticmethod
    def make_container(tk_object):
        return Frame(tk_object)

    @staticmethod
    def get_path_file(extensions):
        file_choose = filedialog.askopenfile()
        return file_choose.name

    @staticmethod
    def make_menu(tk_object):
        return Menu(tk_object)

    @staticmethod
    def make_submenu(menu_container, text):
        submenu = Menu(menu_container)
        menu_container.add_cascade(label=text, menu=submenu)
        return submenu

    @staticmethod
    def make_menu_container(tk_object, menu):
        return tk_object.config(menu=menu)
