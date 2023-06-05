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
    1.1 - return , para uma entrada específica, a quantidade de estudantes presentes | :heavy_check_mark:
    1.2 - return  `None` se em `permanence_period` houver alguma entrada inválida | :heavy_check_mark:
    1.3 - return  `None` se  `target_time` recebe um valor vazio | :heavy_check_mark:
    1.4 - A função deverá, por meio de análise empírica, se comportar (no avaliador remoto em sua Pull Request) como no máximo O(n), ou seja, com complexidade assintótica linear | :heavy_check_mark:
    2 - Implementar adequadamente o teste para a função `encrypt_message` | :heavy_check_mark:
    3.1 - return `True` se a palavra passada por parâmetro for um palíndromo | :heavy_check_mark:
    3.2 - return `False` se a palavra passada por parâmetro não for um palíndromo | :heavy_check_mark:
    3.3 - return `False` se nenhuma palavra for passada por parâmetro | :heavy_check_mark:
    4.1 - return `True` se as palavras passadas forem anagramas | :heavy_check_mark:
    4.2 - return `False` se as palavras passadas por parâmetro não forem anagramas | :heavy_check_mark:
    4.3 - return `false` se alguma das palavras passadas por parâmetro for uma string vazia | :heavy_check_mark:
    4.4 - A função deverá, por meio de análise empírica, se comportar (no avaliador remoto em sua Pull Request) como no máximo O(n log n), ou seja, com complexidade assintótica linearítmica | :heavy_check_mark:
    4.5 - return `True` se as palavras passadas forem anagramas sem diferenciar maiúsculas e minúsculas | :heavy_check_mark:
    5.1 - return o número repetido se a função receber, como parâmetro, uma lista com números repetidos | :heavy_check_mark:
    5.2 - return `False` se a função não receber nenhum parâmetro | :heavy_check_mark:
    5.3 - return `False` se a função receber, como parâmetro, uma string | :heavy_check_mark:
    5.4 - return `False` se a função receber, como parâmetro, uma lista sem números repetidos | :heavy_check_mark:
    5.5 - return `False` se a função receber, como parâmetro, apenas um valor | :heavy_check_mark:
    5.6 - return `False` se a função receber, como parâmetro, um número negativo | :heavy_check_mark:
    5.7 - A função deverá, por meio de análise empírica, se comportar (no avaliador remoto em sua Pull Request) como no máximo O(n log n), ou seja, com complexidade assintótica linearítmica. | :heavy_check_mark:
    6.1 - return `True` se a palavra passada como parâmetro for um palíndromo, executando uma função iterativa | :heavy_check_mark:
    6.2 - return `True` se a palavra passada como parâmetro for um palíndromo, executando uma função iterativa | :heavy_check_mark:
    6.3 - return `False` se nenhuma palavra for passada como parâmetro, executando uma função iterativa | :heavy_check_mark:
    6.4 - A função deverá, por meio de análise empírica, se comportar (no avaliador remoto em sua Pull Request) como no máximo O(n), ou seja, com complexidade assintótica linear. | :heavy_check_mark:

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

5. how to execute the app: `python3 filename.py`

- each file works on its own. don't forget to call the functions on the file so it prints the outputs.