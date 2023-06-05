## Trybe Project 34 - Algorithms


## PROJECT OVERVIEW

  This is project #4 of the Computer Science Module at [Trybe Bootcamp](https://www.betrybe.com/).

  This project is a series of 5 programming challenges to be solved using what was learned during the Algorithms section from this Module. One of the tasks is on Unit Testing. Stack: Python3, Pytest.

  <strong>FYI: every file that does not have a code authorship comment, was originally made by Trybe Bootcamp.</strong>


## PROJECT TASKS

<details>
  <summary>
    <b>Tasks and Status</b>
  </summary>

  * tasks 5 and 6 are bonus tasks

    *Description* | *Status*
    --- | :---:
    1.1 - return the amount of present students, given a certain input entry | :heavy_check_mark:
    1.2 - return  `None` if on `permanence_period` there is a invalid input | :heavy_check_mark:
    1.3 - return  `None` if `target_time` receives an empty value | :heavy_check_mark:
    1.4 - the function should have maximium complexity of O(n) | :heavy_check_mark:
    2 - write the unit test dor function `encrypt_message` | :heavy_check_mark:
    3.1 - return `True` if the word passed as a parameter is a palindrome | :heavy_check_mark:
    3.2 - return `False` if the word passed as parameter is not a palindrome | :heavy_check_mark:
    3.3 - return `False` if no word is passed as parameter | :heavy_check_mark:
    4.1 - return `True` if the words passed are anagrams | :heavy_check_mark:
    4.2 - return `False` if the words passed by parameter are not anagrams | :heavy_check_mark:
    4.3 - return `false` if any of the words passed by parameter is an empty string | :heavy_check_mark:
    4.4 - the function should have maximium complexity of O(n log n)  | :heavy_check_mark:
    4.5 - return `True` if the words passed are non-case-insensitive anagrams | :heavy_check_mark:
    5.1 - return the repeated number if the function receives, as a param, a list with repeated numbers | :heavy_check_mark:
    5.2 - return `False` if the function takes no parameters | :heavy_check_mark:
    5.3 - return `False` if the function takes a string as a parameter | :heavy_check_mark:
    5.4 - return `False` if the function receives, as a param, a list without repeated numbers | :heavy_check_mark:
    5.5 - return `False` if the function takes only one value as a parameter| :heavy_check_mark:
    5.6 - return `False` if the function takes a negative number as a parameter | :heavy_check_mark:
    5.7 - the function should have maximium complexity of O(n log n)  | :heavy_check_mark:
    6.1 - returns `True` if the word passed as a param is a palindrome, executing an iterative solution | :heavy_check_mark:
    6.2 - returns `False` if no word is passed as a parameter, executing an iterative solution | :heavy_check_mark:
    6.3 - the function should have maximium complexity of O(n)  | :heavy_check_mark:

</details>

<details>
  <summary><strong>How to Execute the Tests</strong></summary>

  To execute the tests, first check if you have the virtual environment up and running.

  <strong>To Execute All tests:</strong> ```$ python3 -m pytest```

  the file `pyproject.toml` already correctly configures pytest. However, in case you have issues with that and want a complete explicit output, the command is:

  ```bash
  python3 -m pytest -s -vv
  ```

  In case you need to execute just one test file, use the command:

  ```bash
  python3 -m pytest tests/filename.py
  ```

  In case you need to execute just one test function, use the command:

  ```bash
  python3 -m pytest -k test_function_name
  ```

  If you wish that the tests stop from being executed when the first error happens, use the param `-x`

  ```bash
  python3 -m pytest -x tests/filename.py
  ```

  To execute a specific test of a file, type the command:

  ```bash
  python3 -m pytest tests/filename.py::test_function_name
  ```
</details>


## HOW TO RUN THE APP


1. clone the repository

  - `git clone git@github.com:thiagoguarino/trybe-project33-tech-news.git`

2. enter the project's folder 

  - `cd trybe-project33-tech-news`

3. create and open the project's virtual environment

- `python3 -m venv .venv && source .venv/bin/activate`

4. install dependencies

- `python3 -m pip install -r dev-requirements.txt`

5. test the functions manually on each file. each file works on its on.

    a -  on file: challenges/challenge_anagrams.py - declare the is_anagram() to a variable

    b - set the params: a = is_anagram("rosa", "raso"), then print it: print(a)

6. how to execute the functions: `python3 challenges/challenge_anagrams.py`
