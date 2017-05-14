"""
https://dev.to/mistermocha/python-unit-testing-with-mock---part-one
https://mail.python.org/pipermail/tutor/2014-January/099629.html
"""

import unittest
# from unittest import mock # python3.5
import mock # python2.7
import proc
import proc2

class Test_Pinger(unittest.TestCase):

    def test_ping_host_succeeds(self):
        ping = proc.Proc()
        with mock.patch("proc.subprocess") as subprocess:
            subprocess.Popen.return_value.returncode = 0
            ping.ping_host('localhost')
            subprocess.Popen.assert_called_once_with(['ping','localhost'], shell=True)

    def test_ping_host_fails_and_throws_exception(self):
        ping = proc.Proc()
        with mock.patch('proc.subprocess') as subprocess:
            subprocess.Popen.return_value.returncode = 1
            self.assertRaises(Exception, ping.ping_host, 'localhost')


class Test_Pinger2(unittest.TestCase):

    def test_ping_host_succeeds2(self):
        ping = proc2.Proc2()
        with mock.patch("proc2.Popen") as popen:
            popen.return_value.returncode = 0
            ping.ping_host('localhost')
            popen.assert_called_once_with(['ping','localhost'], shell=True)

    def test_ping_host_fails_and_throws_exception2(self):
        ping = proc2.Proc2()
        with mock.patch('proc2.Popen') as popen:
            popen.return_value.returncode = 1
            self.assertRaises(Exception, ping.ping_host, 'localhost')


class Test_Shell(unittest.TestCase):
    @mock.patch('proc.subprocess')
    def test_count_the_shells(self, mocked_popen):
        shell = proc.Proc()
        mocked_popen.Popen.return_value.stdout = open('testps.out')
        mocked_popen.Popen.return_value.wait.return_value = False
        self.assertEqual(shell.count_the_shells(), 1)

    @mock.patch.object(proc, 'subprocess', autospec=True)
    def test_count_the_shells2(self, mocked_popen):
        shell = proc.Proc()
        mocked_popen.Popen.return_value.stdout = open('testps.out')
        mocked_popen.Popen.return_value.wait.return_value = False
        self.assertEqual(shell.count_the_shells(), 1)

    def test_count_the_shells3(self):
        shell = proc.Proc()
        with mock.patch("proc.subprocess") as mocked_popen:
            mocked_popen.Popen.return_value.stdout = open('testps.out')
            mocked_popen.Popen.return_value.wait.return_value = False
            self.assertEqual(shell.count_the_shells(), 1)


class Test_Shell2(unittest.TestCase):
    @mock.patch('proc2.Popen')
    def test_count_the_shells(self, mocked_popen):
        shell = proc2.Proc2()
        mocked_popen.return_value.stdout = open('testps.out')
        mocked_popen.return_value.wait.return_value = False
        self.assertEqual(shell.count_the_shells(), 1)

    @mock.patch.object(proc2, 'Popen', autospec=True)
    def test_count_the_shells2(self, mocked_popen):
        shell = proc2.Proc2()
        mocked_popen.return_value.stdout = open('testps.out')
        mocked_popen.return_value.wait.return_value = False
        self.assertEqual(shell.count_the_shells(), 1)

    def test_count_the_shells3(self):
        shell = proc2.Proc2()
        with mock.patch("proc2.Popen") as mocked_popen:
            mocked_popen.return_value.stdout = open('testps.out')
            mocked_popen.return_value.wait.return_value = False
            self.assertEqual(shell.count_the_shells(), 1)


if __name__ == '__main__':
    unittest.main()
