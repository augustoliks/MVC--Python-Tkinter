from tkinter import *

from ToolboxUI import UI

class Controller():
    def __init__(self, view, model):
        self.view = view
        self.model = model

    def search_behaviour(self):
        self.model.text = UI.get_path_file("*.py")
        self.view.lbl_msg["text"] = self.model.text

    def search_open_file(self, event):
        self.model.text = UI.get_path_file("*.py")
        self.view.lbl_msg["text"] = self.model.text
