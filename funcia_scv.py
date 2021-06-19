class csv(object):

    def initializ(self, file, new_colon):
        pass


def new_file():
    file_neme = input("Enter file name: ").strip()
    columns = input("Enter name columns ,: ")
    column = columns.split(',')
    new_colum = [col.strip() for col in column]
    file = csv()
    new_fil = file.initializ(file_neme, new_colum)
    print("Create file with colums: ", new_fil)
