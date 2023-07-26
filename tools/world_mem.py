import os

class World_mem:
    _base_path = "/workspaces/Yui/world/"
    def __init__(self):
        pass
    
    def create_person(self, name, information):
        f = open(_base_path+name+".txt", w)
        f.write(information)


    # def add_to_person(self):

