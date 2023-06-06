## Trybe Project 34 - Algorithms


## PROJECT OVERVIEW

  This is project #4 of the Computer Science Module at [Trybe Bootcamp](https://www.betrybe.com/).

  This project is a series of 5 programming challenges to be solved using what was learned during the Algorithms section from this Module. One of the tasks is on Unit Testing. Stack: Python3, Pytest.

  <strong>FYI: every file that does not have a code authorship comment, was originally made by Trybe Bootcamp.</strong>

  <details>
    <summary>
      <b>skills developed building the product</b>
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

    Você trabalha na maior empresa de educação do Brasil. Certo dia, a pessoa Product Manager (PM) quer saber qual horário tem a maior quantidade de pessoas estudantes acessando o conteúdo da plataforma. Com esse dado em mãos, a pessoa PM saberá qual é o melhor horário para disponibilizar os materiais de estudo para ter o maior engajamento possível.

    O horário de entrada e saída do sistema é cadastrado no banco de dados toda vez que uma pessoa estudante entra e sai do sistema. Esses dados estarão contidos em uma lista de tuplas (permanence_period) em que cada tupla representa o período de permanência de uma pessoa estudante no sistema com seu horário de entrada e de saída.

    Seu trabalho é descobrir qual o melhor horário para disponibilizar os conteúdos de estudo. Para isso, utilize a estratégia de resolução de problemas chamada força bruta em que a função desenvolvida por você será chamada várias vezes com valores diferentes para a variável target_time e serão analisados os retornos da função.

    De olho na Dica: O melhor horário será aquele no qual o contador retornado pela função for o maior

    O algoritmo deve utilizar a solução iterativa;

    Caso o target_time passado seja nulo, o valor retornado pela função deve ser None (considere o horário 0 como um horário válido);

  </details>
    <details>
  <summary>
    <b>Challenge 2</b>
  </summary>

    Durante a dinâmica em grupos de um processo seletivo, a empresa contratante definiu um desafio em duplas, e cada pessoa terá um papel. A primeira pessoa deve criar uma função de criptografia, e a segunda pessoa deve implementar os testes da função implementada pela primeira pessoa.

    Você fará o papel da segunda pessoa nessa dinâmica, ou seja: deve implementar os testes de uma função de criptografia.

    Esse teste deve se chamar test_encrypt_message, e ele deve garantir que a função de criptografia encrypt_message deve respeitar uma lógica específica.

    Entenda a lógica da função de criptografia
    Recebe uma string message e um inteiro key como parâmetros

    Se key e message não possuírem os tipos corretos, uma exceção deve ser lançada

    Se key não for um índice positivo válido de message, retorna a string message invertida
    
    Se key for ímpar:
    divide message no índice key, inverte os caracteres de cada parte, e retorna a união das partes novamente com "_" entre elas

    Se key for par:
    divide message no índice key, inverte a posição das partes, inverte os caracteres de cada parte, e retorna a união das partes novamente com "_" entre elas

  </details>
  <details>
  <summary>
    <b>Challenge 3</b>
  </summary>

    Escreva uma função que irá determinar se uma palavra é um palíndromo ou não. A função irá receber uma string de parâmetro e o retorno será um booleano, True ou False.

    Mas o que é um palíndromo?

    Um palíndromo é uma palavra, frase ou número que mantém seu sentido mesmo sendo lido de trás para frente. Por exemplo, "ABCBA".

    Neste projeto iremos focar somente em palavras palíndromas e não em frases ou números.

    O algoritmo deve ser feito utilizando a solução recursiva;

    Não se preocupe com a análise da complexidade desse algoritmo;

    Se for passado uma string vazia, retorne False;

  </details>
  <details>
  <summary>
    <b>Challenge 4</b>
  </summary>

    Faça um algoritmo que consiga comparar duas strings, ordená-las e identificar se uma é um anagrama da outra. Ou seja, sua função irá receber duas strings de parâmetro e o retorno da função será uma tupla () com a primeira string ordenada, a segunda string ordenada e um booleano, True ou False representando se são anagramas.

    O algoritmo deve considerar letras maiúsculas e minúsculas como iguais durante a comparação das entradas, ou seja, ser case insensitive.

    Mas o que é um anagrama?

    "Um anagrama é uma espécie de jogo de palavras criado com a reorganização das letras de uma palavra ou expressão para produzir outras palavras ou expressões, utilizando todas as letras originais exatamente uma vez."

    Utilize algoritmos de ordenação para realizar este requisito.

    Você pode utilizar qualquer algoritmo que quiser (Selection sort, Insertion sort, Bubble sort, Merge sort, Quick sort ou TimSort), desde que atinja a complexidade O(n log n).
    
    Dentre esses algoritmos citados acima, você deve escolher um que atinja a complexidade desejada pelo requisito e deverá adequá-lo ao problema. Para isso, você pode se basear nos algoritmos do course ou de alguma fonte de estudo, mas não esqueça de referenciá-la. O uso de funções prontas do Python não é permitido.

    Exemplos de funções prontas do Python não permitidas: sort, sorted e Counter;
    Não será permitido realizar nenhuma importação neste arquivo!

    A função retorna True caso uma string seja um anagrama da outra independente se as letras são maiúsculas ou minúsculas;

    A função retorna False caso uma string não seja um anagrama da outra;

    O código deve ser feito dentro do arquivo challenges/challenge_anagrams.py.

  </details>
  <details>
  <summary>
    <b>Challenge 5</b>
  </summary>

    Dada um array de números inteiros contendo n + 1 inteiros, chamado de nums, em que cada inteiro está no intervalo [1, n].

    Retorne apenas um número duplicado em nums.

    Caso não passe nenhum valor ou uma string ou não houver números repetidos retorne False;

    O array montado deve:

    Ter apenas números inteiros positivos maiores do que 1;

    Ter apenas um único número repetindo duas ou mais vezes, todos os outros números devem aparecer apenas uma vez;

    Ter, no mínimo, dois números.

    O código deve ser feito dentro do arquivo challenge_find_the_duplicate.py.

    De olho na Dica: ordene o array.

  </details>
  <details>
  <summary>
    <b>Challenge 6</b>
  </summary>

    Resolva o mesmo problema apresentado no requisito 2 - Palíndromos, porém dessa vez utilizando a solução iterativa.
  
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

5. test the functions manually on each file. each file works on its on.
