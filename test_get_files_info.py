import unittest
from functions.get_files_info import get_files_info

class TestGetFilesInfo(unittest.TestCase):
    def test_current_dir(self) -> None:
        result = get_files_info("calculator", ".")
        print("Result for current directory:")
        print(result)
        self.assertIn("pkg", result)
        self.assertIn("main.py", result)
        self.assertIn("tests.py", result)

    def test_sub_dir(self) -> None:
        result = get_files_info("calculator", "pkg")
        print("Result for 'pkg' directory:")
        print(result)
        self.assertIn("calculator.py", result)
        self.assertIn("render.py", result)

    def test_absolute_dir(self) -> None:
        result = get_files_info("calculator", "/bin")
        print("Result for '/bin' directory:")
        print(result)
        self.assertIn("Error", result)
        self.assertIn("outside", result)

    def test_outside(self) -> None:
        result = get_files_info("calculator", "../")
        print("Result for '../' directory:")
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