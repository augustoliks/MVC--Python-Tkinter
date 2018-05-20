from tkinter import *

from Model import Model
from View import View


if __name__ == '__main__':
    model = Model()
    view = View(model)
    view.run()
