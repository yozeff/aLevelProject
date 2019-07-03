#Joseph Harrison 2019
#A Level Project
#Module 8: Storing Datasets
import sqlite3 as sql
import string as s

class Session:

    #create our session connection
    #and cursor instances
    def __init__(self,dbname):
        self.conn = sql.connect(dbname)
        self.cursor = self.conn.cursor()

    #make a table by importing a file
    def make_table(self, filename, lflag, sep, name, dtypes):
        #open file and read the
        #data into an array
        data = []
        file = open(filename,'r')
        lines = file.readlines()
        file.close()
        if lflag:
            #make the first record the labels
            #of the dataset
            labels = lines.pop(0)
            labels = labels.replace('\n','')
            labels = labels.split(sep)
            dimension = len(labels)
        else:
            #create unique labels for each field
            dimension = len(lines[0].split(sep))
            print(f'dimension: {dimension}')
            #detect the minimum length strings required
            #to create labels
            labels = Session.make_codes(['' for i in range(dimension)],
                                        s.ascii_lowercase)
        fields = [labels[i] + ' ' + dtypes[i] for i in range(dimension)]
        #make table
        arg = f'CREATE TABLE {name} ('
        for field in fields:
            arg += field + ', '
        #slice off the last comma and space
        arg = arg[:-2]
        arg += ')'
        self.cursor.execute(arg)
        for record in lines:
            record = record.replace('\n', '')
            record = record.split(';')
            arg = f"INSERT INTO {name} VALUES ({'?, ' * (len(record) - 1) + '?'})"
            self.cursor.execute(arg, record)
        #commit changes
        self.conn.commit()
        return labels
        
    #create a unique set of
    #codes
    #data is the current codes
    #to generate and symbols is
    #the symbol set
    @staticmethod
    def make_codes(data, symbols):
        #edge case if data can fit one
        #code in each symbol group
        if len(data) <= len(symbols):
            for i in range(len(data)):
                #add final symbols
                data[i] += symbols[i]
            return data
        else:
            results = []
            #seperate data into groups
            groups = [[] for i in range(len(symbols))]
            for i in range(len(data)):
                #add symbols to end of data
                data[i] += symbols[i % len(symbols)]
                #add data to corresponding groups
                groups[i % len(symbols)].append(data[i])
            #recursive call
            for group in groups:
                results += Session.make_codes(group, symbols)
            return results
            
    #close our connection
    def close(self):
        self.conn.close()

session = Session(':memory:')
labels = session.make_table('wineData.csv', True, ';',
                   'wineData', ['integer', 'real', 'real',
                                'real', 'real', 'integer',
                                'integer', 'real', 'real',
                                'real', 'real', 'integer'])

import statistics
import matplotlib.pyplot as plt

for label in labels:

    #don't plot quality against quality
    if label == '"quality"':
        continue

    master = []
    control = []
    for i in range(10):

        data = session.cursor.execute(f"""SELECT {label}
                                          FROM wineData
                                          WHERE "quality" == {i}""")
        data = [item[0] for item in data]
        if len(data) != 0:
            master.append(statistics.mean(data))
            control.append(i)

    plt.plot(control, master, 'o-', label=label)
    plt.xlabel('quality')
    plt.ylabel(label)

    plt.title(label)
    plt.show()


