import unittest
import sys
import os

class CustomTestResult(unittest.TextTestResult):
    def addSuccess(self, test):
        super().addSuccess(test)
        print(f"    PASSED: {test}")

    def addFailure(self, test, err):
        super().addFailure(test, err)
        print(f"    FAILED: {test}\n    {err}")

    def addError(self, test, err):
        super().addError(test, err)
        print(f"    ERROR: {test}\n    {err}")

class CustomTestRunner(unittest.TextTestRunner):
    def _makeResult(self):
        return CustomTestResult(self.stream, self.descriptions, self.verbosity)

def run_tests_for_module(module_name, description):
    print(f"\nRunning tests for {description}...")
    loader = unittest.defaultTestLoader
    suite = loader.loadTestsFromName(module_name)
    runner = CustomTestRunner(verbosity=2)
    result = runner.run(suite)
    return result

def run_all_tests():
    print("\n====================")
    print("Running all tests...")
    print("====================")
    
    marathon_result = run_tests_for_module('tests.test_Marathon', 'Marathon Problem')
    fraction_result = run_tests_for_module('tests.test_Fraction', 'Fraction Problem')
    
    print("\n====================")
    print("Summary")
    print("====================")
    
    print(f"Marathon Problem: {'PASSED' if marathon_result.wasSuccessful() else 'FAILED'}")
    print(f"Fraction Problem: {'PASSED' if fraction_result.wasSuccessful() else 'FAILED'}")

if __name__ == '__main__':
    run_all_tests()
