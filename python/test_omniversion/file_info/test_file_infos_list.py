import unittest

from omniversion.file_info import FileMetadata, FileInfosList


class FileInfosListTestCase(unittest.TestCase):
    def test_hosts(self):
        file_infos_list = FileInfosList([
            FileMetadata(host="test2"),
            FileMetadata(host="test1"),
            FileMetadata(host="test1")])
        self.assertEqual(["test1", "test2"], file_infos_list.hosts())

    def test_pretty_print(self):
        file_infos_list = FileInfosList([
            FileMetadata(host="test2"),
            FileMetadata(host="localhost"),
            FileMetadata(host="test1")])
        self.assertIn("test1", file_infos_list.__str__())
        self.assertIn("test1", file_infos_list.__str__())
        self.assertNotIn("localhost", file_infos_list.__str__())


if __name__ == '__main__':
    unittest.main()
