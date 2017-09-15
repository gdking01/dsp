# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

### Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

>> Lists are mutable, which means their entries can be changed in place. They can't be used as keys in dictionaries because of this property. Tuples are very similar but are immutable -- once created, they cannot be changed, only copied. They can be used as dictionary keys because if two tuples are identical now they will be identical forever. (specifically, tuples of immutable objects can be used as dictionary keys.)

---

### Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

>> A set doesn't store order information or duplicates, where a list does. The reason to use a set is that operations like set membership, union and intersection are faster with lists. Also, the set structure makes duplicate removal fast.

---

### Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

>> `lambda` defines a function, usually a temporary and anonymous one that doesn't need to stick around.
```
x=[4,7,-9,2]
sorted(x, key=(lambda x: x**2)) #sort the list by square (which works out to absolute value)
```

---

### Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> List comprehensions are a list construction syntax that works similar to the mathematical concept of a set constructor. At their most basic, they look like `[f(x) for x in iter]`, where `f(x)` is some expression in terms of `x`, and `iter` is some iterable type like a list, tuple, or dictionary.

>> Some examples:
```
#return the squares of the first ten numbers
[x**2 for x in range(10)]
list(map(lambda x:x**2, [x for x in range(10)]))

#add two lists entrywise
[x+y for (x,y) in zip(list1, list2)]
list(map(lambda x:x[0]+x[1], zip(list1, list2)))

#Return the lengths of the strings in a list L
[len(x) for x in L if type(x)==str ]
list(map(len, filter(lambda x:type(x)==str, L)))
```

---

### Complete the following problems by editing the files below:

### Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> 937

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> 513

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

>> 7850


Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

### Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

### Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

### Q8. Parsing
Write a script as indicated (using the football data) in [q8_parsing.py](python/q8_parsing.py)
