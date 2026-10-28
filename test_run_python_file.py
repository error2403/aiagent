import unittest
from functions.run_python_file import run_python_file

class TestGetFilesInfo(unittest.TestCase):
    def test_calc_main(self) -> None:
        result = run_python_file("calculator", "main.py")
        print(result)
        self.assertIn("STDOUT:", result)
        self.assertIn("Calculator App", result)
        self.assertIn("Usage", result)

    def test_calc_add(self) -> None:
        result = run_python_file("calculator", "main.py", ["3 + 5"])
        print(result)
        self.assertIn("STDOUT:", result)
        self.assertIn("\"result\": 8", result)

    def test_calc_tests(self) -> None:
        result = run_python_file("calculator", "tests.py")
        print(result)
        self.assertIn("STDERR:", result)

    def test_outside_cwd(self) -> None:
        result = run_python_file("calculator", "../main.py")
        print(result)
        self.assertIn("Error:", result)
        self.assertIn("Cannot execute \"../main.py\" as it is outside", result)

    def test_not_exist(self) -> None:
        result = run_python_file("calculator", "nonexistent.py")
        print(result)
        self.assertIn("Error:", result)
        self.assertIn("\"nonexistent.py\" does not exist", result)

    def test_not_python(self) -> None:
        result = run_python_file("calculator", "lorem.txt")
        print(result)
        self.assertIn("Error:", result)
        self.assertIn("\"lorem.txt\" is not a Python file", result)

if __name__ == "__main__":
    unittest.main()