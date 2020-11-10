# Test Driven Development test task

**TDD Task**
- Create a new Repo on gihub
- Create a new project in pycharm
- name tdd_test_task
- create a file to write tests
- create a file to write code
- implement sudo coding
- create a README to document the steps to successfully achieve the task

- create a test to check is the number divisible/remainder 0 if True pass the test if False fail
- create a class and method to write code to pass the test

- create a test to check if the given values are positive 
- create a method in the class to pass the test

### Walk Through
- create a file that holds a class called CodeMethods
```python
class CodeMethods:
```
- Define a method that returns True if 1 number is divisible by another number
```python
    def divisible(self, numer, denom):
        return numer % denom == 0
```
- Define a method that returns if the numbers given are positive
```python
    def positive(self, *args):
        for arg in args:  #loop round the args given
            if arg < 0:
                return f"{False}, one of these numbers is negative" #returns false if any of the numbers are negative
        return True
```
- Create a second file, that holds a class with testing methods
- import the CodeMethods class from our first file
```python
from code_files import CodeMethods
```
- import all the testing files needed to test out the code methods
```python
import pytest
import unittest
```
- Then you should install pytest in the terminal using `pip install pytest`
- Create the class to hold the testing methods
- Make the class inherit the test functionality from the unittest module
```python
class TestMethods(unittest.TestCase())
```
- Create an instance of the CodeMethods class inside the TestMethods class to test the functions with
```python
    code_object = CodeMethods()
```
- Test the divisible method with any 2 numbers
- Make sure test_ is in the testing method
- assertEqual is a method in the unittest module that checks if this is equal to that `self.assertEqual(this, that)`
```python    
    def test_divisible(self):
        self.assertEqual(self.code.divisible(124, 4), True) # Using the methods from code methods
```
- Repeat this, testing if the positive method works
```python    
    def test_positive(self):
        self.assertEqual(self.code.positive(3, 5, 6, 7, 9, 1000), True)
```
- To run the tests on the completed test filed, go to the terminal and the test files folder
- run the command `python -m pytest`
- or for more information on each method you can run `python -m unittest discover -v`