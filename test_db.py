"""
https://dev.to/mistermocha/python-unit-testing-with-mock---part-two
"""



import unittest
# from unittest import mock # python3.5
import mock # python2.7
import db

class Test_DB(unittest.TestCase):

    @mock.patch('db.DBWriter.commit_to_db', autospec=True)
    def test_save(self, mock_commit):
        writer = db.DBWriter()

        def fake_commit(self, sql):
            writer.counter += 1

        mock_commit.side_effect = fake_commit
        writer.save("Hello-World")
        mock_commit.assert_called_with(writer,
            "INSERT INTO mytable VALUES ('Hello-World')")
        self.assertEqual(writer.counter, 1)

    @mock.patch('db.DBLibrary', autospec=True)
    def test_save2(self, mock_dblib):
        writer = db.DBWriter()
        writer.save("Hello-World2")
        mock_dblib.return_value.commit.assert_called_with(
            "INSERT INTO mytable VALUES ('Hello-World2')")


if __name__ == '__main__':
    unittest.main()
