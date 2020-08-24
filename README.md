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

So decomposing the structure, we need 5 *RE* to accept all parts of the structure:

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

In this case we use de concatenation of the all *RE's* with the comma *RE* except the last one, becase after every word in the structure is followed by a comma. But we have problem, and is that if we concatenate de *Optional RE* with the *Comma RE* we can accept a word that is just the comma, before the second name, so we have to modify the *Optional RE*.

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
([a-z]+,)([a-z]+,)([a-z]+,)?(2[8-9]|[3-9][0-9]),[CD]
```

How you can see, its very similar to the definitions that we constructed in each step, even if you dont know about *REs* in programming, its very understable.



### Converting the obtained RE to an ℇ-NFA;

Now we will convert our *RE* to his equivalent ℇ-NFA following the *Thompson method*. For that we will transform each sub *Re* into a ℇ-NFA and then concatenate all the parts.

#### Names

The names was a *RE* N that the defines the language N that is composed by all the combinations of alphabet letters, to simplify the automata, we will define all the possible letter as "letter'

![names automata](/assets/name.jpg)

#### Optional Name

The optional name is just the same *RE* that name but optional, so the automata, using *Kleene closure* and the *Thomson method* the automata is:

![optional name automata](/assets/name_optional.jpg)

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

To convert a NFA to DFA  we only need one thing, add a new state and substitute the "empty set" with a transition
to that state for each entry symbol. This new state will be named by "X" and is a dead state, that's means that wen is reached
it's not possible to get out over it and the word is rejected.

This type of states is very important and useful because if we want the complementary of the language that 
define the automata, we just have to convert this state in final state, and delete de original final states.
Getting as accepted all the words that reject the original automata.

To represent this on the automata and trying to be cleaner as possible, we will define the transition to this new
state "X" with set notation. "Σ" will represent the alphabet (every entry value) of our automata and "Σ - {symbols}" will represent
any entry on the alphabet but not the symbols intro brackets. Even doing this, the automata turned messy:

![complete_automata](/assets/DFA.jpg)


So its better work with the transition table representation, in blue the transitions to the same state, the dead state X.

![complete_automata](/assets/dfa-transition-table.jpg)
























