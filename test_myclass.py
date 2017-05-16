"""
https://dev.to/mistermocha/python-unit-testing-with-mock---part-two
http://stackoverflow.com/questions/25323361/what-is-spec-and-spec-set
http://www.voidspace.org.uk/python/mock/mock.html
http://www.voidspace.org.uk/downloads/mock-1.0.1.pdf
"""



import unittest
# from unittest import mock # python3.5
import mock # python2.7
import myclass

class Test_MyClass(unittest.TestCase):
    def test_my_class(self):
        my_obj = myclass.MyClass("fake this", "fake that")
        my_obj.this = mock.Mock(spec_set=myclass.AnotherThing)
        my_obj.that = mock.Mock(spec_set=myclass.AnotherThing)
        # print(isinstance(my_obj.this, myclass.AnotherThing))
        # print(dir(my_obj.this))
        # print(my_obj.this.__dir__())
        my_obj.do_this()
        my_obj.do_that()
        my_obj.this.do.assert_called_with() # assert_called_once_with()
        my_obj.that.do.assert_called_with()

    @mock.patch('myclass.AnotherThing', autospec=True)
    def test_my_class2(self, mock_thing):
        def fake_init(*args):
            return mock.Mock(*args, spec_set=myclass.AnotherThing)
        mock_thing.side_effect = fake_init
        # print(dir(mock_thing))
        my_obj = myclass.MyClass("fake this", "fake that")
        """
        con assert_called_with solo toma en cuenta la ultima reciente llamada, funcionaria solo para este caso:
        mock_thing.assert_called_with("fake that")
        """
        mock_thing.assert_called_with("fake that")
        mock_thing.assert_any_call("fake this")
        mock_thing.assert_any_call("fake that")

    @mock.patch('myclass.AnotherThing', autospec=True)
    def test_my_class3(self, mock_thing):
        def fake_init(*args):
            return mock.Mock(*args, spec_set=myclass.AnotherThing)
        mock_thing.side_effect = fake_init
        # print(dir(mock_thing))
        my_obj = myclass.MyClass("fake this", "fake that")
        calls = [mock.call("fake this"), mock.call("fake that")]
        # mock_thing.assert_has_calls(calls, any_order=True) # any_order por defecto es False, con True no importaria el orden en las llamadas
        mock_thing.assert_has_calls(calls)


if __name__ == '__main__':
    unittest.main()
