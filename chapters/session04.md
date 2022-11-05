---
layout: page
permalink: /chapters/session04/
title: Programming Concepts 1 - Excersises
---

## Goals
+ Understand the following programming concepts:
  + Variables
  + Booleans
  + If statements
  + While loops
  + Lists
  + For Loops
  + Functions
+ Practise using and writing code using these conceps.

## Variables

Variable are pointers to Python objects such as integers, floats or strings.
They are defined using `=`, for example:

{% highlight python %}
>>> my_variable = 6.2
{% endhighlight %}

We can look at this variable using `print`:

{% highlight python %}
>>> print(my_variable)
6.2

{% endhighlight %}

In Jupyter, sometimes we do not need to use `print` if a variable is written on the final line of the cell, for example:

{% highlight python %}
>>> my_variable
6.2
{% endhighlight %}

# Question 1
a) Create two variables, one representing Alan's current amount of money (£1500), and one representing Alan's monthly wages (£762).



b) Alan get's paid. Update the value of the variable representing Alan's money to reflect this.



c) Alan has a pay rise. He now earns 10% more than before. Update the value of the variable representing alan's wage to reflect this.



# Question 2

a) Consider the following code:

{% highlight python %}
>>> first_name = 'Bianca'
>>> middle_name = 'Betty'
>>> surname = 'Brown'

>>> full_name = first_name + middle_name + surname
{% endhighlight %}

How would you ensure that the variable `full_name` included spaces between the names?







b) Create the same three (or more if required) variables to correspond with your own name.



## Booleans, If-statements & While-loops

Boolean variables can be created from numerical variables using:
+ Equality `==`
+ Inequality `!=`
+ Greater than `>`
+ Less than `<`
+ Greater than or equal to `>=`
+ Less than or equal to `<=`

For example:

{% highlight python %}
>>> 4 > 8
False
{% endhighlight %}

{% highlight python %}
>>> 4 <= 8
True
{% endhighlight %}

# Question 3

Create all possible Boolean variables from the numbers 6 and 2.5 (e.g. `6 == 2.5` is a Boolean variable).



# Question 4
The following code gives the number of roots to a polynomial $$ax^2 + bx + c$$ with coefficients `a`, `b` and `c` respectively.

{% highlight python %}
>>> a = 1
>>> b = 1
>>> c = 1

>>> discriminant = (b ** 2) - (4 * a * c)

>>> if discriminant < 0:
...     number_of_roots = 0
>>> if discriminant == 0:
...     number_of_roots = 1
>>> if discriminant > 0:
...     number_of_roots = 2

>>> number_of_roots
0
{% endhighlight %}

Use the above code to find the numbers of roots to the following polynomials:

a) $$x^2 - 3x + 4$$



b) $$2x^2 - 10x + 1$$



c) $$4x^2 + 4x + 1$$



d) $$-7x^2 + 7x - 7$$



# Question 5

Write some code that assigns a value to the variable `v` according to the Heavyside function:

$$
H(x) = \begin{cases}
0 & \text{ if } x < 0\\
0.5 & \text{ if } x = 0\\
1 & \text{ otherwise.}
\end{cases}
$$



# Question 6
An if-statement checks a Boolean, and runs the next indented bit of code if the Boolean is True. A while-loop checks a Boolean, and repeats the next indented bit of code *until* the Boolean becomes False.

The following code will run 10 times:

{% highlight python %}
>>> n = 0
>>> while n < 10:
...     n += 1
...     print('I have run ' + str(n) + ' times.')
I have run 1 times.
I have run 2 times.
I have run 3 times.
I have run 4 times.
I have run 5 times.
I have run 6 times.
I have run 7 times.
I have run 8 times.
I have run 9 times.
I have run 10 times.

{% endhighlight %}

Find _two different ways_ of adapting the code so that it only runs 5 times.





# Question 7
The code below verifies the following identity for $$n = 20$$:

$$
\sum_{i=0}^{n} i^2 = \frac{n(n+1)(2n+1)}{6}
$$

{% highlight python %}
>>> n = 20
>>> rhs = n * (n +  1) * (2 * n + 1) / 6
>>> lhs = 0
>>> i = 0
>>> while i < n:
...     i += 1
...     lhs += i ** 2
>>> lhs == rhs
True
{% endhighlight %}

Using a while-loop, verify this identity for every interger value of $$n$$ below 100.



# Question 8
In the same way as in Question 7, verify the following identity for the first 250 natural numbers:

$$
\sum_{i=0}^{n} i^3 = \frac{\left(n^2 + n\right)^2}{4}
$$



## Lists and For-loops

Lists are ordered containers pointing to variables, defined with square brackets `a = [1, 1, 7]`. There are a number of operations we can use on lists, including `len(a)`, `max(a)`, `min(a)`, and `sorted(a)`. Elements of lists can be chosen by indexing, e.g. the first element of a list is `a[0]`, the second from last is `a[-2]`, and so on.


# Question 9

a) In no particular order, create a list of 8 of your favourite numbers.

b) Find the maximum value in the list.

c) Find the minimum value in the list.

d) Find the length of the list.

e) Sort the list.

f) Find the 2nd element in the list.

g) Find the last element in the list.

h) Find the 3rd to 6th elements in the list.

















# Question 10
Items can be added to the back of a list using `.append(`:

{% highlight python %}
>>> some_numbers = [3, 4, 1]
>>> some_numbers.append(10)
>>> some_numbers
[3, 4, 1, 10]
{% endhighlight %}

The following code uses a while loop to create a list of the first 10 square numbers:

{% highlight python %}
>>> square_numbers = []
>>> x = 1
>>> while x <= 10:
...     square_numbers.append(x ** 2)
...     x += 1

>>> square_numbers
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
{% endhighlight %}

Adapt the code above so that it gives a list of the first 15 square numbers that are even.



# Question 11
For loops allow up to repeat code for every item in a list. Let's print the square root of each of the numbers in the list `square_numbers`:

{% highlight python %}
>>> for n in square_numbers:
...     print(n ** 0.5)
1.0
2.0
3.0
4.0
5.0
6.0
7.0
8.0
9.0
10.0

{% endhighlight %}

You can also use a for loop to repeat code over anything iterable, such as strings:

{% highlight python %}
>>> name = 'GERAINT'
>>> for letter in name:
...     print('Gimmie a ' + letter + '.')
Gimmie a G.
Gimmie a E.
Gimmie a R.
Gimmie a A.
Gimmie a I.
Gimmie a N.
Gimmie a T.

{% endhighlight %}

Or if you don't have a list ready, the `range` command gives an iterable:

{% highlight python %}
>>> for number in range(8):
...     print(number)
0
1
2
3
4
5
6
7

{% endhighlight %}

Rewrite the code for Question 8, using for loops instead of while loops.



## Functions

Functions are executable pieces of code, that can be used on demand. They are themselves variables, defined using `def`. They are useful to avoid repeating writing code.

Below is a function that finds the number of roots of a quadratic polynomial (see Question 4):

{% highlight python %}
>>> def find_number_of_roots(a, b, c):
...     discriminant = (b ** 2) - (4 * a * c)
...     if discriminant < 0:
...         return 0
...     if discriminant == 0:
...         return 1
...     if discriminant > 0:
...         return 2
{% endhighlight %}

This function works similar to a mathematical function, it takes three arguments, `a`, `b`, and `c`, the inputs. It gives one output, given by the `return` command. *As soon as the code hits `return` the function stops running*.

Now answering questions 4a) - 4d) is much easier, we simply call this function:

{% highlight python %}
>>> find_number_of_roots(1, -3, 4)
0
{% endhighlight %}

{% highlight python %}
>>> find_number_of_roots(2, -10, 1)
2
{% endhighlight %}

{% highlight python %}
>>> find_number_of_roots(4, 4, 1)
1
{% endhighlight %}

{% highlight python %}
>>> find_number_of_roots(-7, 7, -7)
0
{% endhighlight %}

# Question 12

Write the Heaveyside function (Question 5) as a Python function, and use it to evaluate $$H(-4)$$, $$H(7)$$, $$H(3.14)$$, and $$H(0)$$.











# Question 13
Write a function that checks the following identity for any given $$n$$:

$$
\sum_{i=0}^{n} i^2 = \frac{n(n+1)(2n+1)}{6}
$$

Use the function to check the identity for $$n = 3881$$.





# Question 14
This question asks you to write functions that do the following things:

a) Takes a list of elements and outputs the same list in reverse,

b) Checks is a number if prime,

c) Counts the number of prime numbers below a given limit,

d) Creates a list of the first $$m$$ prime numbers.

















---

[Previous](/cm/chapters/session03/) - [Home](/cm/) - [Next](/cm/chapters/session05/)
{:style="text-align: right;"}

{% highlight python %}

{% endhighlight %}

