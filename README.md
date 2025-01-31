# Medic database checking
Design a system to check incorrect/correct entries of a database using Finite Automatas and Regular Expressions.


# Description - Work to do

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


# Technical Report

There is a lot of ways to do this, in this case the main strategy will be try to reduce the number of states or 
parts of the automata when it possible, because work with automatas and operate with them or transition tables is really
a painstaking work. Analyzing the structure we can observe that is formed for several repetitions of the same part.For example the
"city" part describe the same behavior than "name, name" so we can reduce it and then apply in the same way that the final
result of "name, name" just like a lego. Even you can separate each part, work with them and finally concatenate the
resulting automatas, because for the properties of the *RE's* the language defined by the concatenation is the same
than the concatenation of the languages of each *RE's*.

Another thing is that if you have a automata that accept a define a language, the negation, in this case obtain the 
incorrect entries it's easily achieved sending that words to a dead state and turning that dead state into a final state.
So we will develop the automata in that way, getting the correct ones and manage the transitions to implement a dead state
and in the end get both languages.

### RE Design

We have to design the regular expression according with the following structure:

``` python
'First Name,First Family Name,Second Family Name (optional),Age,City,Marital Status'
```

So, decomposing the structure, we need 5 *RE* to accept all parts of the structure:

##### Names

The names and city could be represented with the same *sub regular expression* less the **Second Family Name** that is optional and the Marital Status that are just composed by two letters {C,S}. That is one that match a group of alphabetic letters without numbers or other types of characters so, being A = {'a','b','c',...,'y','z'} our alphabet then our RE = A+ so the language it defines is L(A+)={'a', 'ab',...} in other words, defines the language of all combinations of the letters in the alphabet. In any programming language this will be achieved with the *RE*:

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

We will represent this RE with the letter *O*.
 

#### Age

Now we need a *RE* that accepts numbers greater or equal than 28 and less or equal than 99. So being the alphabet B = {0, 1, 2 ,3 ,4 ,5 ,6 ,7, 8 ,9} we can generate de *RE* that accepts the language L(B+) which is the language that accepts all the words compound by all the possible combinations of the digits in B. But we need a subset of B we will define this *RE* with the letter *D*. For one hand we need all the number greater or equal than 28 so we can construct a *RE* that accepts that language using the alphabet B' = {2} and the alphabet B'' = {8, 9} and concatenate both creating a *RE* = L(B'B''). We can do the same for the numbers greater or equal than 30 and less or equal than 99 using the alphabets B''' = {3, 4, 5, 6, 7 ,8, 9} and B and concatenate both resulting in the *RE* = L(B'''B) = {30, 31, 32, ... , 51, 52, ... , 89, 90, ... 99} and we will define this *RE* with the letter *D'*. Finally to get the *RE* that defines the language that we need we will use the union of both *RE*, so our new *RE* = L(D U D') = {28, 29, 30, 31, ..., 99}, and we will rename this  *RE* with the letter *G*.

In any programming language whis will be achieves with the *RE*:

```python
(2[8-9])|([3-9][0-9])
```
We will represent this RE with the letter *G*.

#### Status

To accept the words that represent de marital status we just need a *RE* that defines the language composed by {C,S}. So being a alphabet T = {C,S} and our *RE* a symbol of that alphabet, defined as *S*, we got the *RE* that defines the language L(S) = {C, S}. We can achieve the same result defining two *RE's* per each symbol {C,S} and doing the union of the *RE's*

In any programming language whis will be achieves with the *RE*:
```python
[CD]
```

We will represent this RE with the letter *S*.

#### Comma

The next one will be comma, so the symbol "," is a RE and L(',') = {','}, we will represent this RE with the letter *C*. 
Also, most of words are follows by comma, so to do that, we will use the concatenation with that RE's to impose de condition that the words accepted are followed by a comma.

In any programming language this will be achieved with the *RE*:

```python
,
```

We will represent this RE with the letter *C*.


### Putting it all together

With this five *RE's* we can accept all correct parts of the structure of the entries, but we have to accept the entire entries, so we need a *RE* that allows us accept a entire entry (correct). We will achieve that constructing that *RE* joining and combining our five *RE's* using the available operations.

In this case we use de concatenation of the all *RE's* with the comma *RE* except the last one, because after every word in the structure is followed by a comma. But we have problem, and is that if we concatenate de *Optional RE* with the *Comma RE* we can accept a word that is just the comma, before the second name, so we have to modify the *Optional RE*.

#### Modifying Optional RE
Using the same alphabet A = {'a','b','c',...,'y','z'} the *Comma RE* , a new *RE* composed by ɛ which language is L(ɛ) = {ɛ}  the *positive closure* of A = L(A+) and the concatenation and the union operation we will get our desired * Optional RE*.

Because every letter are a *RE* the concatenation is equal to the concatenation of the languages so having L(A+) we just have to use concatenation with the *Comma RE* to get a *RE* that defines the language that accept any combinations of the alphabet followed by the comma, we will represent that *RE* with the *O'*. Now to add the possibility of be optional (empty word) to the language we just use the union operation L(O' + ɛ) = {ɛ, 'a,', 'b,', ..., 'aabb,'...}.

We will represent this RE with the letter *O* again.

In any programming language this will be achieved with the *RE*:

```python
([a-z]+,)?
```

Now we can create a new *RE* to check the correctness of the entries just using the concatenation over all our *REs* just like that:

```python
NCNCOGCS
```

It we follow the recursive concatenation operations you will observe that the language that defines that *RE* is L(NCNCOGCS)= L(N)L(C)L(N)L(O)L(G)L(C)L(S) that follows the same structure and with the restriction that we was searching for.

In any programming language this will be achieved with the *RE*:

```python
([a-z]+,)([a-z]+,)([a-z]+,)?(2[8-9]|[3-9][0-9]),([a-z]+,)[CD]
```

How you can see, its very similar to the definitions that we constructed in each step, even if you dont know about *REs* in programming, its very understandable.



### Converting the obtained RE to an ℇ-NFA;

Now we will convert our *RE* to his equivalent ℇ-NFA following the *Thompson method*. For that we will transform each sub *Re* into a ℇ-NFA and then concatenate all the parts.

#### Names

The names was a *RE* N that the defines the language N that is composed by all the combinations of alphabet letters, to simplify the automata, we will define all the possible letter as "letter'

![names automata](/assets/name.jpg)

#### Optional Name

The optional name is just the same *RE* that name but optional, so the automata, using *Kleene closure* and the *Thomson method* the automata is:

![optional name automata](/assets/name_optional.jpg)

This concatenate with the comma is the only one that you have to do some different to represent it, cannot be
generated just applying the *Thompson method*, you have to do some modifications so we will to represent explicitly
in this section:

![optional name automata](/assets/optional-name-comma.jpg)

As you can see we use two more states to put the E-transitions correctly to accept the comma only if the optional
name is found.


#### Age

In the case of age, we used the union operation on two *REs* to accept for one hand = {28, 29} and for other and = {30, 31, 32, ..., 99} so using *Thomson method* the automata is:

![names automata](/assets/age.jpg)

#### Comma

The comma *RE* is the most simple of all our *REs* and the most simple automata because is a *RE* to accept one symbol:

![comma automata](/assets/comma.jpg)

#### Status

The status is the union of two *REs* one that accept the symbol 'C' and one that accept the symbol 'S' so :

![status automata](/assets/status.jpg)


#### Putting all together

Now to finish our ℇ-NFA we just have to concatenate all the parts like:
```python
NCNCOGCS
```

So again, using *Thompson method* definition to concatenate operation we get:

![complete_automata](/assets/complete-automata.jpg)

Remember that letter is any symbol of the alphabet and E is a epsilon transition.


# Transforming the ℇ-NFA to DFA


####  ℇ-NFA to NFA
To do that first we have to do the transformation from ℇ-NFA to NFA. So we have to remove all the ℇ(E) transitions.
For that we will apply the algorithm for ℇ removal. To apply this algorithm, the first step is to compute the closure of
every state so we first we will build the transition table and using it, we will get the closure of every state.

In this table we have a row for every state and a column for the entries "letter", ",",  every number(0 to 9) and "C" and "S".
It's possibly to reduce the number of columns, for example using a column for "numbers", other for ">=3" and other for {2,3}
but in this case we will use the columns named before.

The closure is showed in the blue column named CL. The E transitions is named with E with a red background


![complete_automata](/assets/enfa-transition-table-cl.jpg)


Now having the closure we can build our NFA. We just have to observe the values for each entry for the nodes
in the closure for each row. The result is:

![complete_automata](/assets/nfa-transition-table.jpg)

If you draw the automata, you can observe will observe some interesting things more clearly. 

![complete_automata](/assets/nfa-automata.jpg)

There are many unreachable 
steps! so before to go into the conversion from NFA to DFA, we will delete this states. Getting a more clean and simplified
automata to work with, and turning the conversion into a easier job. Doing that we get this automata:

![complete_automata](/assets/nfa-no-unreachable.jpg)

As you can see, it is a more easier automata to work with and more understandable. Now the last step before doing the
conversion to a DFA, will be rename the states to maintain the name linearity and get his transition table. Here is the 
automata:

![complete_automata](/assets/nfa-renamed.jpg)

And his transition table:

![complete_automata](/assets/enfa-clean-transition-table.jpg)

Just doing the conversion to NFA and removing the unreachable states, we pass from a automata with 37 states to 15 states.


### NFA to DFA

To convert a NFA to DFA, first we have to convert the sets of transitions to transition to only one state,
in this case we are so lucky because all our state sets only contain 1 state, so we have to nothing on the automata and
only remove the brackets on the transition table. So to finish the conversion from NFA we only need to do one thing, 
add a new state and substitute the "empty set" with a transition to that state for each entry symbol. 
This new state will be named by "X" and is a dead state, that's means that when is reached
it's not possible to leave it and the word is rejected no matter what the next symbols of the word, just like a black hole.

This type of states is very important and useful because if we want the complementary of the language that 
define the automata, we just have to convert this state in final state, and delete de original final states.
Getting as accepted all the words that reject the original automata.

To represent this on the automata and trying to be cleaner as possible, we will define the transition to this new
state "X" with set notation. "Σ" will represent the alphabet (every entry value) of our automata and "Σ - {symbols}" will represent
any entry on the alphabet but not the symbols intro brackets. Even doing this, the automata turned messy:

![complete_automata](/assets/DFA.jpg)


So its better work with the transition table representation, in blue the transitions to the same state, the dead state X.

![complete_automata](/assets/dfa-transition-table.jpg)


#### Getting the minimum DFA

To finish the conversion we will try to reduce more our automata using the "State minimization algorithm". The algorithm
is quite easy to apply in this case because we have a lot of transitions with the same states, and after marking de final
states with all other states except themselves, using the "X" state value to open almost every state with "L" over "I" and
"K" every state starts to be marked due to domino effect, getting:

![complete_automata](/assets/minimization.jpg)

The blocks coloured in red are the states marked the white ones the indistinguishable states, in this case
the states ["I","K"] and ["M", "N"] are the same states! so we can simplify the automata even more:

![complete_automata](/assets/dfa-automata-minimized.jpg)

And the transition table:

![complete_automata](/assets/dfa-minimized-transition-table-.jpg)


### DFA age < 30   

Now we have to design a automata that accept entries (correct or not) with age < 30. In other words,
a simple DFA that in the word contains one two digits number less than 30, no matter what the position in the word
or if follow the correct structure. Our alphabet will be the same of the first DFA, so the entry symbols could 
be alphanumeric and the comma:

![complete_automata](/assets/30less-dfa.jpg)

In this case to simply the transition we use "Σ - {symbols}" like before, to represent any symbol except {symbols}, 
"digit" it's a number in the range [0-9], it's the same than {<3, >=3} so in the automata we will use the 
two notations and "<3" its a digit in the range [0-2] and ">=3" a number in the range [3,9].

Whe need one final state with a transition to itself because the age could be anywhere in the structure, in the end, middle or end of the word, and in 
the case that are two ages or ages greater or equal than 30, or ages with only a digit or more than 2 digits, we have a transition to 
a dead state "X".

![complete_automata](/assets/30-less-transition-table.jpg)

### Combine the two DFA's

Now we will combine the two *DFa's* to accepting the correct entries with age less than 30. To do that we will
apply the product automaton method and chose the final state as the combination of both final states. We will use the the two *DFA's* transition table and combine 
all the states by pairs:

![complete_automata](/assets/two-transition-tables-product.jpg)

Then create a new table per each combination of states of the two *DFA's* and fill with the values of 
each cell. The trick to not die doing this is just observe the cells in which both the values are different
that "X". Remember that X is a dead state to the words rejected. To not die doing this we will reduce all "-X | X-" 
states with "X" through all the process, and using the notation "<3, ">3", digit, letter, etc in our automata.

![complete_automata](/assets/three-transition-table-product.jpg)

And we will use this to generate our DFA:

![complete_automata](/assets/dfa-product.jpg)

As you can see if your aren't blind yet, there are a lot of unreachable states, so we will remove it:

![complete_automata](/assets/dfa-minimized-product.jpg)

And here is renamed more structured:

![complete_automata](/assets/dfa-automata-product-renamed.jpg)

And his transition table:

![complete_automata](/assets/dfa-minimized-product-transition-table.jpg)


We get this automata, that as you can see accept the same words that the first automata but with
age 28 or 29! if you think about it has sense, the restriction about the age in the first automata was
28<= age <=30 and the second automata accept words with age < 30, so the combination of both is the first automata
with a restriction on the age=  28<= age < 30.

To finish we will add the automata of "City", to accept the complete structure, and finish our DFA:

![complete_automata](/assets/dfa-automata-product-renamed-city.jpg)

And here is the transition table:

![complete_automata](/assets/dfa-minimized-product-transition-table-city.jpg)

We will use this transition table to create a final program in python to accept or reject the entries.

### Python implementation

Now we will implement and use the transition table to read from a file with *n* entries and accept or reject according
to our automata. Thanks to the previous work this will be quite simple, because it's just implement the transition
table as a list of lists and then, each symbol will represent the column and the row will be the value in that (row, column)
starting by the initial state (row = A = 0). And in case that the row is equal to "X" (a dead state) we have not to check the entry until the end
the entry its automatically a not valid entry, and if it finish in the row = "M" (final state), the entry is accepted.

The source code is in the \src folder and the program read a file of possible entries located in \data folder. And when it's executed
generate two files, one with the accepted entries and another with the rejected entries in the same location of the program (\src).

#### Python version 3.7























































