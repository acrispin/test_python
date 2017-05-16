"""
https://dev.to/mistermocha/python-unit-testing-with-mock---part-two
http://stackoverflow.com/questions/1319615/proper-way-to-declare-custom-exceptions-in-modern-python
http://stackoverflow.com/questions/25323361/what-is-spec-and-spec-set
"""

class MyException(Exception):
    pass

class AnotherThing(object):
    def __init__(self, _name):
        self.id = hex(id(self))
        self.name = _name
        print(self.__class__.__name__, self.id, self.name)

    def do(self):
        print(self.__class__.__name__, "do", self.name)

    def get_it(self):
        return self.id

    def do_it(self, _id):
        if self.id == _id:
            raise MyException("Can not processing same object with id: %s" % _id)
            # raise MyException({'msg': 'Can not processing same object', 'id': self.id})
        return "Processing object with id: %s from object %s" % (_id, self.id)



class MyClass(object):
    def __init__(self, this, that):
        self.this = AnotherThing(this)
        self.that = AnotherThing(that)

    def do_this(self):
        self.this.do()

    def do_that(self):
        self.that.do()

    def do_more(self):
        got_it = self.this.get_it()
        that_too = self.that.do_it(got_it)
        return that_too


if __name__ == "__main__":
    c = MyClass('this text', 'that text')
    c.do_this()
    c.do_that()
    print(c.do_more())
