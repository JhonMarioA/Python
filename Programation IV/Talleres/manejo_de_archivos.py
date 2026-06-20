from io import *


"""" file modes:

"r" → read

"w" → write (overwrite)

"a" → append or "a+" -> append and read

"b" → binary (e.g., images, audio)

"x" → create new file (error if exists)

"r+" → read & write """


class File():
    def __init__(self, file_path):

        self.path = file_path
        self.file = open(file_path, "w+", encoding = "utf-8")

    def write(self, text):
        self.file.write(text)

    def read(self):
        self.file.seek(0)
        print(self.file.read())

    def append(self, text):
        self.file.close()
        self.file = open(self.path, "a+", encoding = "utf-8")
        self.file.write(text)

    def close(self):
        self.file.close()
        print("Closing")



f = File(r"C:\PROGRAMACIÓN\PYTHON\PROGRA IV\texto.txt")
f.write("Hola de nuevo")
f.read()
f.append("\nConcatenando")
f.read()
f.close()