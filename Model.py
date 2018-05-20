class Model():

    def __init__(self):
        self.data_set = ""
        self.file_path = ""
        print (self.data_set)
        
    def read_file(self):
        load = open(self.file_path)
        self.data_set = load.read()
        load.close()
