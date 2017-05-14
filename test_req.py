"""
https://dev.to/mistermocha/python-unit-testing-with-mock---part-two
http://engineroom.trackmaven.com/blog/mocking-mistakes/
"""

import unittest
# from unittest import mock # python3.5
import mock # python2.7
import req

class Test_Request(unittest.TestCase):
    @mock.patch('req.requests.get', autospec=True) # por defecto autospec es False
    def test_get_example_passing(self, mocked_get):
        mocked_req_obj = mock.Mock()
        mocked_req_obj.status_code = 200
        mocked_get.return_value = mocked_req_obj
        assert(req.get_example())
        mocked_get.assert_called_with('http://example.com/')

    @mock.patch('req.requests')
    def test_get_example_passing2(self, mocked_get):
        mocked_req_obj = mock.Mock()
        mocked_req_obj.status_code = 200
        mocked_get.get.return_value = mocked_req_obj
        assert(req.get_example())
        mocked_get.get.assert_called_with('http://example.com/')

    @mock.patch('req.requests') # usa autospec=False
    def test_get_example_passing3(self, mocked_get):
        """
        con autospec=False funciona el metodo assert_not_called
        caso contrario sale error: AttributeError: 'function' object has no attribute 'assert_not_called'
        """
        mocked_req_obj = mock.Mock()
        mocked_req_obj.status_code = 200
        mocked_get.get.return_value = mocked_req_obj
        assert(req.get_example_no_call_req())
        mocked_get.assert_not_called() # verifica si no ha sido llamado el metodo req.requests.get


if __name__ == '__main__':
    unittest.main()
