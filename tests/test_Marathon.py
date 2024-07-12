import sys
import os
import unittest

# sys.path 설정
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'problems')))

from Marathon import solution  # 경로를 설정한 후 직접 파일명을 임포트

class TestMarathonSolution(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(solution(["leo", "kiki", "eden"], ["eden", "kiki"]), "leo")
    
    def test_case_2(self):
        self.assertEqual(solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"]), "vinko")
    
    def test_case_3(self):
        self.assertEqual(solution(["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]), "mislav")

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
