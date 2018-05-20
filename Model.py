class Model():

    def __init__(self):
        self.data_set = None
        self.file_path = None
        self.condition = None
        print (self.data_set)


    def read_file(self, condition):

        self.condition = condition

        load = open(self.file_path)
        self.data_set = load.read()
        load.close()

        self.data_set += self.condition
