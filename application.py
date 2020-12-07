from tkinter import *
from sqlalchemy import create_engine

engine = create_engine('sqlite:///PressoTestWare/data/db.db', echo=True)


class Table:

    def __init__(self, root):

        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=20, fg='blue',
                               font=('Arial', 16, 'bold'))

                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])

            # take the data


lst = [(1, 'x', 'x', 19),
       (2, 'x', 'x', 18),
       (3, 'x', 'x', 20),
       (4, 'x', 'x', 21),
       (5, 'x', 'x', 21)]

# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])
create_model('test')

# create root window
root = Tk()
t = Table(root)
root.mainloop()