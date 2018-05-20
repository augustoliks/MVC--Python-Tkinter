from tkinter import *

from ToolboxUI import UI

class Controller():
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def strategy_read_file(self):
        self.model.file_path = UI.get_path_file("*.py")

        self.model.read_file(self.view.txt_condition.get())
        self.view.lbl_msg["text"] = self.model.data_set

    def strategy_open_file(self, event):
        self.model.text = UI.get_path_file("*.py")
        self.view.lbl_msg["text"] = self.model.text
