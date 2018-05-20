from tkinter import *
from Controller import Controller
from ToolboxUI import UI

class View():
    def __init__(self, model):
        self.model = model
        self.controller = Controller(self, self.model)

        self.root = Tk()

        self.topbar_menu = UI.make_menu(self.root)
        self.topbar_container = UI.make_menu_container(self.root, self.topbar_menu)

        self.submenu_file = UI.make_submenu(self.topbar_menu, "file")
        self.submenu_file.add_command(label="Open", command=self.hello)
        self.submenu_file.add_separator()
        self.submenu_file.add_command(label="Save", command=self.hello)

        self.submenu_help = UI.make_submenu(self.topbar_menu, "help")
        self.submenu_help.add_command(label="Loadfile", command=self.controller.strategy_read_file)
        self.submenu_help.add_command(label="New", command=self.hello)

        self.root_container = UI.make_container(self.root)
        self.root_container.pack()

        self.lbl_msg = UI.make_label(self.root_container, "Hello World", "Calibri", "10")
        self.lbl_msg.pack()

        self.btn_hello_world = UI.make_button(self.root_container, "Clique aqui", "Calibri", "10")
        self.btn_hello_world.pack()

        self.txt_condition = UI.make_textbox(self.root_container, "10")
        self.txt_condition.pack(side=BOTTOM)


        self.btn_hello_world["command"] = self.controller.strategy_read_file


    def run(self):
        self.root.title("MVC example")
        self.root.deiconify()
        self.root.mainloop()

    def hello(self):
        print ("Hello")
