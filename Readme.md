# CREATING A PYTHON APPLICATION - LIST COMPREHENSIONS
# BY ISRAEL MAFABI EMMANUEL

A simple test of list comprehensions in Python. 

## List Comprehensions Example

This Python application includes two functions:
1. `return_evens`: Filters even numbers from a given list.
2. `make_exclamation`: Adds an exclamation mark to each string in a given list.

### Functions

Below are the Python functions for this application:

```python
def return_evens(_list_: list) -> list:
    return [n for n in _list_ if n % 2 == 0]

def make_exclamation(_list_: list) -> list:
    return [n + "!" for n in _list_ if n]
```

### Tests

I also included a test file to validate the functionality of these functions. The test file is structured as follows:

python

```python
from list_comprehension import return_evens, make_exclamation

import io
import sys

class TestPrintFibonacci:

    def test_return_empty_list_if_odds(self):
        '''returns empty list when num_list has no evens'''
        num_list = range(1,10,2)
        assert return_evens(num_list) == []

    def test_return_evens(self):
        '''returns evens from num_list'''
        num_list = range(10)
        assert return_evens(num_list) == [0, 2, 4, 6, 8]

class TestMakeExclamation:
    '''function make_exclamation()'''
    def test_return_empty_list_if_empty_input(self):
        '''returns empty list when sentence_list is empty'''
        assert make_exclamation([]) == []

    def test_return_exclamation_list(self):
        '''returns list of sentences with exclamation marks'''
        sentence_list = [
            "I like computers",
            "I require coffee",
            "Live long and prosper",
        ]
        
        assert(make_exclamation(sentence_list) == [
            "I like computers!",
            "I require coffee!",
            "Live long and prosper!",
        ])
```

### Usage of `pytest`

To run the tests and ensure the functions work correctly, I used `pytest`. Follow these steps to execute the tests:

1. Install `pytest` if you haven't already:

```shell
pip install pytest
```

2. Run the tests by navigating to the directory containing the test file and executing:

```shell
pytest test_list_comprehension.py #but it's located in lib folder!!!
```

This will run all the tests and display the results, ensuring that your functions behave as expected.

## Conclusion

This test demonstrates how to utilize list comprehensions in Python to filter even numbers and modify string elements in a list. 

~ Glory be to God!!!

Happy coding! 😍😉🤭