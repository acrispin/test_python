"""
http://stackoverflow.com/questions/3774328/implementing-use-of-with-object-as-f-in-custom-class-in-python
http://effbot.org/zone/python-with-statement.htm
"""


class FileTest():
    def __init__(self, _file):
        print("receive file", _file)
        self.file = _file
        # call_exception()
    def __enter__(self):
        #here before opening and returning the file object
        print("open file", self.file)
        self.file_open = open(self.file, 'r')
        # call_exception()
        return self.file_open
    def __exit__(self, type, value, traceback):
        #Exception handling here
        # call_exception()
        print("close file", self.file)
        self.file_open.close()

def call_exception():
    a, b = 1, 0
    c = a/b
    print(c)


if __name__ == '__main__':
    with FileTest('testps.out') as f:
        #here you work with the file object.
        # call_exception()
        print(f.read())
        # call_exception()
