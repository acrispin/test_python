"""
https://dev.to/mistermocha/python-unit-testing-with-mock---part-one
https://pymotw.com/2/subprocess/
"""

import subprocess
import unittest
# from unittest.mock import Mock, patch # python3.5
from mock import Mock, patch # python2.7

# Clase a testear
class MyClass():
    """
    Las clases que se van a testear deberian estar en otro modulo de python
    """
    def sub_method(self, first, this):
        print("call sub_method()")
    def visible_method(self):
        self.sub_method("arg1", this="arg2")
        print("call visible_method()")

# Metodo a testear
def count_the_shells():
    """
    si se usa el import: from subprocess import Popen, PIPE
    y se llama al Popen asi: p = Popen(['ps', '-ax'], stdout=PIPE, stderr=PIPE)
    los test no funcionaban
    se tenia que usar el import asi: import subprocess
    y el popen como esta indicado abajo
    Para eso es mejor poner los metodos que se van a testear en otro modulo o archivo python
    e importarlos desde los test como en test_proc.py
    """
    p = subprocess.Popen(['ps', '-ax'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if p.wait():
        raise Exception('We had a fail')
    count = 0
    for proc in p.stdout.readlines():
        # http://stackoverflow.com/questions/33054527/python-3-5-typeerror-a-bytes-like-object-is-required-not-str-when-writing-t
        # http://stackoverflow.com/questions/17615414/how-to-convert-binary-string-to-normal-string-in-python3
        if b"bash" in proc: # en python3.5 y python2.7 se tenie que usar binary string: b"bash"
        # if "bash" in proc: # solo funciona en python2.7
            print(type(proc))
            print(type(proc) is bytes, type(proc) is str)
            print(proc)
            count += 1
    return count


class MyTest(unittest.TestCase):
    ### code ###
    def double_up(self, number):
        return number * 2

    ### test ###
    def test_double_up(self):
        self.assertEqual(self.double_up(2), 4)
        # assert double_up(2) == 46

    ### test ###
    def test_double_up2(self):
        self.assertEqual(self.double_up(3), 6)


class MyTestMock(unittest.TestCase):
    def test_myclass(self):
        my_object = MyClass()
        my_object.sub_method = Mock()
        my_object.visible_method()
        # my_object.sub_method.assert_called_with()
        my_object.sub_method.assert_called_with("arg1", this="arg2")


class MyTestMock2(unittest.TestCase):
    # @patch.object(subprocess, 'Popen', autospec=True)
    @patch('subprocess.Popen')
    def test_count_the_shells(self, mocked_popen):
        """
        http://www.psf.upfronthosting.co.za/issue20529
        El open() en python3 daba el siguiente warning: ResourceWarning: unclosed file <_io.BufferedReader name=6>
        No se quitaba ni con el bloque with
        Se tuvo usar el siguiente flag para quitarlo: -W ignore:ResourceWarning
        $ python3 -W ignore:ResourceWarning test1.py
        """
        mocked_popen.return_value.stdout = open('testps.out')
        # with open('testps.out', 'r') as f:
        #     mocked_popen.return_value.stdout = f
        mocked_popen.return_value.wait.return_value = False
        # assert count_the_shells() == 2
        self.assertEqual(count_the_shells(), 1)

    @patch.object(subprocess, 'Popen', autospec=True)
    def test_count_the_shells2(self, mocked_popen):
        mocked_popen.return_value.stdout = open('testps.out')
        mocked_popen.return_value.wait.return_value = False
        self.assertEqual(count_the_shells(), 1)

    def test_count_the_shells3(self):
        with patch("subprocess.Popen") as mocked_popen:
            mocked_popen.return_value.stdout = open('testps.out')
            mocked_popen.return_value.wait.return_value = False
            self.assertEqual(count_the_shells(), 1)


if __name__ == '__main__':
    unittest.main(exit=False)
