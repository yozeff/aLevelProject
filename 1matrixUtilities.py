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

    #repr string allows for more
    #readable representation when
    #printing
    def __repr__(self):
        result = ''
        for i in range(self.rows):
            #list of all elements in one row
            row = [str(self[j][i]) for
                   j in range(self.cols)]
            #append string of row to result
            result += ' '.join(row) + '\n'
        return f'{result}{self.rows}x{self.cols} Matrix'

    #rows and cols properties
    #allow for more readable syntax
    @property
    def rows(self):
        return len(self.elems[0])

    @property
    def cols(self):
        return len(self.elems)

    #allows matrices to be indexed
    #and spliced
    def __getitem__(self,key):
        return self.elems[key]
    
                
