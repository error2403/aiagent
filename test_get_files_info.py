import unittest
from functions.get_files_info import get_files_info

class TestGetFilesInfo(unittest.TestCase):
    def test_working_dir(self) -> None:
        result = get_files_info("calculator", ".")
        print(result)
        self.assertIn("Success", result)

    def test_sub_dir(self) -> None:
        result = get_files_info("calculator", "pkg")
        print(result)
        self.assertIn("Success", result)

    def test_absolute_dir(self) -> None:
        result = get_files_info("calculator", "/bin")
        print(result)
        self.assertIn("Error", result)
        self.assertIn("outside", result)

    def test_outside(self) -> None:
        result = get_files_info("calculator", "../")
        print(result)
        self.assertIn("Error", result)
        self.assertIn("outside", result)

    def test_not_dir(self) -> None:
        result = get_files_info("calculator", "main.py")
        print(result)
        self.assertIn("Error", result)
        self.assertIn("not a directory", result)


if __name__ == "__main__":
    unittest.main()