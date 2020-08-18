# Medic database checking
Desing a system to check the incorrect entries of a database using Finite Automatas and Regular Expression


# Description
At the Spanish Ministry of Health they have a file containing a database of all medical doctors in the country. It is a list of the entries of all doctors, and each entry is a list of comma separated values with the following structure:

First Name,First Family Name,Second Family Name (optional),Age,City,Marital Status

An explanation of every field is detailed next:

    First Name: a sequence of letters in the alphabet. Notice that compound names are NOT allowed (updated April 14th). For simplicity, only lower case letters are used.
    First Family Name: a sequence of letters in the alphabet. Notice that compound names are NOT allowed (updated April 14th). For simplicity, only lower case letters are used.
    Second Family Name: a sequence of letters in the alphabet. This field is optional, because foreigners usually do not have a second family name. Notice that compound names are NOT allowed (updated April 14th). For simplicity, only lower case letters are used.
    Age: a two digits integer with the restriction 28 ≤ Age ≤ 99.
    City: The city where the doctor works. Notice that compound names are NOT allowed (updated April 14th).
    Marital Status: Whether the person is married (C) or not (S). Note that here we use capital letters.

The Ministry of Health is asking you for your help, and needs you to perform the following tasks:

- Analyze the correctness of the entries in their database

    - Task 1: Design a Regular Expression to check the entries of their database, in order to discover the wrong ones. Define the alphabet of the Language represented by the RE.
    - Task 2: Convert the obtained RE to an ℇ-NFA following the Thompson method.
    - Task 3: Get the minimum DFA equivalent to the designed ℇ-NFA

- There is a need of doctors in Madrid because of COVID-19, and the Ministry needs to allocate doctors from other cities in Spain to Hospitals in Madrid. Because the sickness produced by COVID-19 is less dangerous in young people, the Ministry needs a list of all doctors younger than 30 years old.

    - Task 4: Design a minimal DFA that accepts database entries, correct or not, where Age < 30, ages less than 28 may be accepted or not. We can assume that 028 is an incorrect age (updated April 18th).
    - Task 5: Combine the DFAs designed in tasks 3 and 4 with the product automaton method to find a DFA that accepts only correct entries in which the Age field is below 30. Minimize the resulting DFA.
    - Task 6: Implement in your favorite language the obtained DFA using the table method. The program must read a file with the database of doctors and print the correct entries where Age < 30.

Submit a zip file named with your initials, including:
- Report showing all steps followed, from the design of the initial RE, the ℇ-NFA and its minimum DFA, the DFA designed in Task 4, the product DFA and the result of minimizing it. There are alternative ways to solve the problem, but it must be done following the tasks specified.
- The report must include details of intermediate steps of the different algorithms you need to apply, for instance: renaming of states, the different transition tables generated, the minimization table, the closure of the states, ...
- Include the source code of your program.

- Add a file with a representative set of input test cases (for both accepted and rejected strings).


# Report

### RE Desing

We have to desing the regular expression according with the following structure:

``` python
'First Name,First Family Name,Second Family Name (optional),Age,City,Marital Status'
```

##### Names

The names could be represented with the same *sub regular expression* less the **Second Family Name** that is optional and the Marital Status that are just comoposed by two letters {C,S}. That is one that match a group of alphabetic letters without numbers or other types of characters so, being A = {'a','b','c',...,'y','z'} our alphabet then our RE = A+ so the language it defines is L(A+)={'a', 'ab',...} in other words, defines the language of all combinations of the letters in the alphabet. In any programming language this will be achieved with the *RE*:

```python
[a-z]+
```
We will represent this RE with the letter *N*.

#### Optional Name

The optional name its the same than the before *RE* *N*, we will use the same alphabet but with a significant difference, now we will apply the *Kleene closure* over the alphabet *A* to accept the empty word \epsilon so this *RE* accepts the language L(A*) = {ɛ, 'a', 'ab', ... }. In other words, a language that accepts *names* or nothing.

In any programming language this will be achieved with the *RE*:

```python
[a-z]*
```
 
### Comma

The next one will be comma, so the symbol "," is a RE and L(',') = {','}, we will represent this RE with the letter *C*. 
Also, most of words are follows by comma, so to do that, we will use the concatenation with that RE's to impose de condition that the words accepted are followed by a comma.





