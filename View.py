from tkinter import *
from Controller import Controller
from ToolboxUI import UI

class View():
    def __init__(self, model):
        self.model = model
        self.root = Tk()

        self.root_container = UI.make_container(self, self.root)
        self.root_container.pack()

        self.lbl_msg = UI.make_label(self, self.root_container, "Hello World", "Calibri", "10")
        self.lbl_msg.pack()

        self.btn_hello_world = UI.make_button(self, self.root_container, "Clique aqui", "Calibri", "10")
        self.btn_hello_world.pack()

        self.controller = Controller(self, self.model)

    def run(self):
        self.root.title("MVC example")
        self.root.deiconify()
        self.root.mainloop()


    def hello(self):
        print ("Hello")
