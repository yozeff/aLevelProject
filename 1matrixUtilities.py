#Joseph Harrison 2019
#A Level Project
#Module 1: Matrix Utilities

class Matrix:

    #initialise new matrix
    #*args allows for an iterator
    #object to be passed as an
    #argument
    def __init__(self,*args):
        self.elems = []
        for arg in args:
            #check arg type
            if not isinstance(arg,list):
                raise TypeError('args must be lists')
            #for first col
            elif len(self.elems) == 0:
                rows = len(arg)
                self.elems.append(arg)
            #check correct dimensions
            elif len(arg) == rows:
                self.elems.append(arg)
            else:
                raise ValueError('inconsistant dimensions')
                
