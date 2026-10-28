import unittest
from functions.get_file_content import get_file_content

class TestGetFileContent(unittest.TestCase):
    def test_lorem_file(self) -> None:
        result = get_file_content("calculator", "lorem.txt")
        print(f"lorem.txt length: {len(result)}")
        print(f"lorem.txt truncated: {'truncated' in result}")
        self.assertIn("truncated", result)

    def test_main_file(self) -> None:
        result = get_file_content("calculator", "main.py")
        print(result)
        self.assertIn("def main()", result)

    def test_calculator_file(self) -> None:
        result = get_file_content("calculator", "pkg/calculator.py")
        print(result)
        self.assertIn("def _apply_operator", result)

    def test_cat(self) -> None:
        result = get_file_content("calculator", "/bin/cat")
        print(result)
        self.assertIn("Error", result)

    def test_not_exist(self) -> None:
        result = get_file_content("calculator", "pkg/does_not_exist.py")
        print(result)
        self.assertIn("Error", result)

if __name__ == "__main__":
    unittest.main()