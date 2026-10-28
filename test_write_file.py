import unittest
from functions.write_file import write_file

class TestWriteFile(unittest.TestCase):
    def test_lorem_file(self) -> None:
        result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
        print(result)
        self.assertIn("Successfully", result)
        self.assertIn("28 characters written", result)

    def test_pkg_lorem(self) -> None:
        result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
        print(result)
        self.assertIn("Successfully", result)
        self.assertIn("26 characters written", result)

    def test_temp_file(self) -> None:
        result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
        print(result)
        self.assertIn("Error", result)
        self.assertIn("outside", result)

if __name__ == "__main__":
    unittest.main()