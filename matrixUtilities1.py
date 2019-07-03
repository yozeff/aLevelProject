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
                self.elems.append(list(arg))
            #for first col
            elif len(self.elems) == 0:
                rows = len(arg)
                self.elems.append(arg)
            #check correct dimensions
            elif len(arg) == rows:
                self.elems.append(arg)
            else:
                raise ValueError('inconsistant dimensions')

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

    #matrix multiplication
    def __mul__(self,other):
        #for two matrices
        if isinstance(other,Matrix):
            #check that cols of self is
            #equal to the rows of other
            if self.cols == other.rows:
                #init our result matrix
                result = [[0 for i in range(self.rows)]
                          for j in range(other.cols)]
                #matrix mult algorithm:
        #https://en.wikipedia.org/wiki/Matrix_multiplication_algorithm
                for i in range(self.rows):
                    for j in range(other.cols):
                        total = 0
                        for k in range(self.cols):
                            total += self[k][i] * other[j][k]
                        result[j][i] = total
                return Matrix.return_object(result)
            else:
                raise ValueError('inconsistant dimensions')
        #multiplication by scalar
        elif isinstance(other,int) or isinstance(other,float):
            result = [[self[j][i] * other for i in range(self.rows)
                       ] for j in range(self.cols)]
            return Matrix.return_object(result)
        else:
            raise TypeError(("unsupported type(s) for *: 'matrix'"
                             f"and {str(type(other))[7:-1]}"))

    #decide if result of
    #method should be a
    #vector or matrix
    @staticmethod
    def return_object(array):
        if len(array) == 1:
            return Vector(*array[0])
        else:
            return Matrix(*array)

    #transpose of self
    @property
    def trans(self):
        result = [[0 for i in range(self.cols)]
                  for j in range(self.rows)]
        #append switched elements to result
        for i,col in enumerate(self):
            for j,elem in enumerate(col):
                result[j][i] = elem
        return Matrix.return_object(result)

    #implements dot product
    #between two matrices or
    #vectors
    @staticmethod
    def dot(self,other):
        if isinstance(other,Matrix):
            return (self.trans * other).elems[0][0]
        else:
            raise TypeError(('bad operand type for dot():'
                            f'{str(type(other))[7:-1]}'))

    #convert a matrix to a string
    def to_string(self):
        result = ''
        #add each element to the string
        for col in self:
            for elem in col:
                result += str(elem) + ';'
        #remove final seperator
        result = result[:-1]
        #indicate the dimensions so that the
        #matrix can be reconstructed
        result += f':{self.rows}:{self.cols}'
        return result

    #convert a string formatted matrix
    #back to an object
    @staticmethod
    def to_matrix(string,elemtype=float):
        #place where dimensions start
        dimst = string.find(':')
        #split into elements and dimensions
        elems, dims = string[:dimst], string[dimst:]
        #split elements at element seperator
        elems = [elemtype(elem) for elem in elems.split(';')]
        #split dimensions at ':'
        #first element of the list is always
        #an empty string due to ':' seperator
        rows,cols = [int(elem) for elem in dims.split(':')[1:]]
        #add elements to matrix
        result = [[elems[j * rows + i]
                   for i in range(rows)]
                  for j in range(cols)]
        return Matrix.return_object(result)

    #serialise a list of
    #matrices to a file
    @staticmethod
    def serialise(filename,matlist):
        #get string formats
        #of each matrix
        matlist = [mat.to_string() for
                   mat in matlist]
        #write each string format
        file = open(filename,'w')
        for string in matlist:
            file.write(string + '\n')
        file.close()

    #deserealise a file into
    #matrix objects
    @staticmethod
    def deserealise(filename,elemtype=float):
        #read each string format
        #from file
        matlist = []
        file = open(filename,'r')
        for string in file.readlines():
            #convert to matrix and append to
            #list
            string = string.replace('\n','')
            matlist.append(Matrix.to_matrix(string,elemtype))
        file.close()
        return matlist

class Vector(Matrix):

    def __init__(self,*args):
        #use validation from matrix
        Matrix.__init__(self,args)

    #allows for easy distinction
    #between vectors and matrices
    def __repr__(self):
        string = ''
        for elem in self[0]:
            string += str(elem) + '\n'
        return f'{string}{self.rows}x1 Vector'

if __name__ == '__main__':
    import random as r
    matlist = [Matrix(*[[r.randint(0,9)
              for i in range(2)]
              for j in range(2)])
              for k in range(2)]
    print('matrices to serialise')
    for mat in matlist:
        print(mat)
    Matrix.serialise('someMats.txt',matlist)
    print('matrices deserealised from file')
    for mat in Matrix.deserealise('someMats.txt',int):
        print(mat)
                
