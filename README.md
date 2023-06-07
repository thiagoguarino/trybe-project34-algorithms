## Trybe Project 34 - Algorithms


## PROJECT OVERVIEW

  This is project #4 of the Computer Science Module at [Trybe Bootcamp](https://www.betrybe.com/).

  This project is a series of 5 programming challenges to be solved using what was learned during the Algorithms section from this Module. One of the tasks is on Unit Testing. Stack: Python3, Pytest.

  <strong>FYI: every file that does not have a code authorship comment, was originally made by Trybe Bootcamp.</strong>

  <details>
    <summary>
      <b>skills developed coding the project</b>
    </summary>
    <ul>
      <li>logic</li>
      <li>problem solving</li>
      <li>develop optimal solutions</li>
    </ul>
  </details>

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
    2 - write the unit test for function `encrypt_message` | :heavy_check_mark:
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

<details>
  <summary>
    <b>Challenges Guide</b>
  </summary>
  <details>
  <summary>
    <b>Challenge 1</b>
  </summary>

    You work at the largest education company in Brazil. One day, the Product Manager wants to know which time has the highest number of students accessing the platform's content. With this data in hand, the PM will know the best time to make the study materials available to have the greatest possible engagement.

    The entry and exit time of the system is registered in the database every time a student enters and exits the system. This data will be contained in a list of tuples (permanence_period) in which each tuple represents the period of permanence of a student in the system with his entry and exit time. [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]

    Your job is to figure out the best time to make the study content available. To do so, use the problem-solving strategy called brute force in which the function you developed will be called several times with different values ​​for the target_time variable and the function returns will be analyzed.

    Hint: The best time will be the one at which the counter returned by the function is the greatest

    The algorithm must use the iterative solution;

    If the target_time passed is null, the value returned by the function must be None (consider the time 0 as a valid time);

  </details>
    <details>
  <summary>
    <b>Challenge 2</b>
  </summary>

    You will play the role of the second person in this dynamic, that is: you must implement the tests of a cryptographic function.

    This test should be called test_encrypt_message, and it should ensure that the encrypt_message encryption function must respect specific logic.

    Understand the logic of the encryption function

    Takes a string message and an integer key as parameters

    If key and message do not have the correct types, an exception must be thrown

    If key is not a valid positive index of message, return the inverted message string
    
    If key is odd:
    splits message at index key, reverses the characters of each part, and returns the union of the parts again with "_" between them

    If key is even:
    splits message at index key, reverses the position of the parts, reverses the characters of each part, and returns the union of the parts again with "_" between them

  </details>
  <details>
  <summary>
    <b>Challenge 3</b>
  </summary>

    Write a function that will determine if a word is a palindrome or not. The function will receive a parameter string and the return will be a boolean, True or False.

    But what is a palindrome?

    A palindrome is a word, phrase, or number that retains its meaning even when read backwards. For example, "ABCBA".

    In this project we will only focus on palindromic words and not on sentences or numbers.

    The algorithm must be done using the recursive solution;

    Don't worry about analyzing the complexity of this algorithm;

    If passed an empty string, return False;

  </details>
  <details>
  <summary>
    <b>Challenge 4</b>
  </summary>

    Make an algorithm that can compare two strings, order them and identify if one is an anagram of the other. That is, your function will receive two parameter strings and the function return will be a tuple () with the first ordered string, the second ordered string and a boolean, True or False representing if they are anagrams.

    The algorithm must consider uppercase and lowercase letters as equal when comparing entries, that is, be case insensitive.

    But what is an anagram?

    "An anagram is a kind of wordplay created by rearranging the letters of a word or phrase to produce other words or phrases, using all the original letters exactly once."

    Use sorting algorithms to accomplish this requirement.

    You can use any algorithm you want (Selection sort, Insertion sort, Bubble sort, Merge sort, Quick sort or TimSort), as long as it reaches O(n log n) complexity.
    
    Among these algorithms mentioned above, you must choose one that reaches the desired complexity by the requirement and must adapt it to the problem. For this, you can base yourself on the course algorithms or on some study source, but don't forget to reference it. The use of built-in Python functions is not allowed.

    Examples of not allowed built-in Python functions: sort, sorted and Counter;
    It will not be allowed to use mports in this file!

    The function returns True if a string is an anagram of the other, regardless of whether the letters are uppercase or lowercase;

    The function returns False if one string is not an anagram of the other;

  </details>
  <details>
  <summary>
    <b>Challenge 5</b>
  </summary>

    Given an array of integers containing n + 1 integers, called nums, where each integer is in the range [1, n], return a duplicate number in nums.

    If you do not pass any value or a string or there are no repeated numbers, return False;

    The assembled array must:
     - Have only positive integers greater than 1;

     - Have only a single number repeating two or more times, all other numbers must appear only once;

     - Have at least two numbers.

    Hint: Sort the array.

  </details>
  <details>
  <summary>
    <b>Challenge 6</b>
  </summary>

    Solve the same problem presented in task 2, but this time using the iterative solution.
  
  </details>

</details>

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

5. to run the Evaluator just run the unit test command: `$ python3 -m pytest`
