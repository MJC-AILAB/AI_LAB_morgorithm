import sys
import os
import unittest
<<<<<<< HEAD
=======
print("Current directory:", os.getcwd())
print("File directory:", os.path.dirname(__file__))
print("sys.path:", sys.path)
print("+++++++++++++")
>>>>>>> 973174d (test setting)

# sys.path 설정
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'problems')))

from Fraction import solution

class TestFractionSolution(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(solution(1, 2, 3, 4), [5, 4])
    
    def test_case_2(self):
        self.assertEqual(solution(9, 2, 1, 3), [29, 6])

class CustomTestResult(unittest.TextTestResult):
    def addSuccess(self, test):
        super().addSuccess(test)
        print(f"PASSED: {test}")

    def addFailure(self, test, err):
        super().addFailure(test, err)
        print(f"FAILED: {test}\n{err}")

class CustomTestRunner(unittest.TextTestRunner):
    def _makeResult(self):
        return CustomTestResult(self.stream, self.descriptions, self.verbosity)

if __name__ == '__main__':
    unittest.main(testRunner=CustomTestRunner())
