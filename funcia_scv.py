class csv:
    pass


def new_file():
    file_neme = input("Enter file name: ")
    columns = input("Enter name columns ,: ")
    column = columns.split(',')
    new_colum = [col.strip() for col in column]