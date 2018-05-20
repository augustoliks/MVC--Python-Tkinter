from tkinter import *

from ToolboxUI import UI

class Controller():
    def __init__(self, view, model):
        self.view = view
        self.model = model

        self.view.btn_hello_world.bind("<Button>",self.search_behaviour)

    def search_behaviour(self, event):
        self.model.text = UI.get_path_file(self, "*.py")
        self.view.lbl_msg["text"] = self.model.text
