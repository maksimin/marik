class csv(object):

    def initializ(self, file, neew_colum):
        pass


def new_file():
    file_neme = input("Enter file name: ")
    columns = input("Enter name columns ,: ")
    column = columns.split(',')
    new_colum = [col.strip() for col in column]
    file = csv()
    file.initializ(file_neme, new_colum)
    print("Create file with colums: ", file)
