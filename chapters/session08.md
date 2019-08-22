---
layout: page
permalink: /chapters/session08/
---

## Goals
+ Understand the following programming concepts:
  + Recursion
  + List comprehension
  + Dictionaries
  + Classes, objects, attributes, and methods
+ Practise using and writing code using these conceps.

## Recursion

In mathemaics we can define some functions recursively, using a *base case* and a *recursion rule*. For example the factorial function:

$$
n! = \begin{cases}1 & \text{ if n = 0,}\\ n(n - 1)! & \text{ otherwise}\end{cases}
$$

We can also define Python functions in the same way:

{% highlight python %}
>>> def factorial(n):
...     if n == 0:
...         return 1
...     else:
...         return n * factorial(n - 1)
{% endhighlight %}

# Question 1

a) Use this recursive function to create a list of the factorial of the first 7 integers.



b) What happens when you try to use this to work out $$2000!$$, that is `factorial(2000)`? Why do you think this is?



# Question 2
Write a recursive function that gives the $$n^{\text{th}}$$ Fibonacci number, given by the recursion rule:

$$$$
f_n = f_{n - 1} + f_{n - 2}
$$$$

and the base case $$f_0 = f_1 = 1$$.
Then using a for-loop, print out the first 12 Fibonacci numbers.





## List comprehension & Dictionaries

We have already see how to use for and while loops, along with append, to create lists. For example he list of the first 10 square numbers:

{% highlight python %}
>>> square_numbers = []
>>> for n in range(1, 11):
...     square_numbers.append(n**2)
>>> square_numbers
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
{% endhighlight %}

This bit of code can also be done is a shorter way, using something called *list comprehension*:

{% highlight python %}
>>> square_numbers = [n**2 for n in range(1, 11)]
>>> square_numbers
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
{% endhighlight %}

# Question 3

a) Rewrite the following for loop as a list comprehension:

{% highlight python %}
>>> square_roots = []
>>> for x in range(1, 101):
...     square_roots.append(x ** 0.5)
{% endhighlight %}



b) Rewrite the following for loop as a list comprehension:

{% highlight python %}
>>> running_average = []
>>> data = [6, 8, 2, 3, 1, 1, 1, 6, 7, 3, 4, 3, 2, 1, 2, 8]
>>> for i in range(1, 17):
...     running_average.append(sum(data[:i]) / i)
{% endhighlight %}



c) Rewrite the following for loop as a list comprehension:

{% highlight python %}
>>> even = []
>>> for d in data:
...     if d % 2 == 0:
...         even.append(True)
...     else:
...         even.append(False)
{% endhighlight %}



# Question 4
Another data structure that Python uses are dictionaries. Unlike lists these are *unordered*, but each value is associated with a key. For example:

{% highlight python %}
>>> capitals = {
...     'Wales': 'Cardiff',
...     'England': 'London',
...     'Scotland': 'Edinburgh',
...     'Northern Ireland': 'Belfast',
...     'Ireland': 'Dublin',
...     'The Netherlands': 'Amsterdam',
...     'Belgium': 'Brussels'
>>> }
{% endhighlight %}

{% highlight python %}
>>> capitals['Scotland']
'Edinburgh'
{% endhighlight %}

{% highlight python %}
>>> capitals['The Netherlands']
'Amsterdam'
{% endhighlight %}

However if you try to access a key that does not exist, this will error. To overcome this, we can use `get`:

{% highlight python %}
>>> capitals['France']
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-17-295040abefb0> in <module>()
----> 1 capitals['France']

KeyError: 'France'

{% endhighlight %}

{% highlight python %}
>>> capitals.get('France', 'Not here')
'Not here'
{% endhighlight %}

{% highlight python %}
>>> capitals.get('Wales', 'Not here')
'Cardiff'
{% endhighlight %}

Or keys can be added on the go:

{% highlight python %}
>>> capitals['France'] = 'Paris'
{% endhighlight %}

Using either list comprehension or a for loop, create a list of the capital cities (from the dictionary `capitals` above, of the following countries (Give the number 404 if the key is not there):

{% highlight python %}
>>> countries = ['Wales', 'UK', 'Belgium', 'Ireland', 'Spain', 'England']
{% endhighlight %}





# Question 5
a) Create a dictionary that maps the countries above to the number of letters in their name.



b) Dictionaries can also be created in the same way as list comprehensions. Create the same dictionary in this way.



## Classes, Objects, Attributes and Methods

Objects as things that can store information.

Classes are recipes for creating objects.

Attributes are variables associated with an object, to store information.

Methods are functions associated with an object, enabling them to change themselves.

Consider the following piece of code which defines a class to store a Student (at the moment it does nothing):

{% highlight python %}
>>> class Student:
...     pass
{% endhighlight %}

Now we can create any number of students we like from this:

{% highlight python %}
>>> nikoleta = Student()
>>> henry = Student()
{% endhighlight %}

{% highlight python %}
>>> nikoleta
<__main__.Student at 0x1081a1278>
{% endhighlight %}

We can give those students attributes:

{% highlight python %}
>>> nikoleta.age = 24
>>> nikoleta.age
24
{% endhighlight %}

{% highlight python %}
>>> henry.subject = 'Maths'
>>> henry.subject
'Maths'
{% endhighlight %}

All students take maths, so it would make sense if they had this attribute upon their creation. We can also make it so that we give the objects an `age` upon creation. Let's redefine Student to do these things:

{% highlight python %}
>>> class Student:
...     def __init__(self, age):
...         self.subject = 'Maths'
...         self.age = age
{% endhighlight %}

{% highlight python %}
>>> emma = Student(25)
{% endhighlight %}

{% highlight python %}
>>> emma.age
25
{% endhighlight %}

{% highlight python %}
>>> emma.subject
'Maths'
{% endhighlight %}

Here `age` and `subject` are attributes of the object.
Let's redefine student so it has a method too. this method will increase the student's age by one year:

{% highlight python %}
>>> class Student:
...     def __init__(self, age):
...         self.subject = 'Maths'
...         self.age = age
...     
...     def have_a_birthday(self):
...         self.age += 1
{% endhighlight %}

{% highlight python %}
>>> lorenzo = Student(29)
{% endhighlight %}

{% highlight python %}
>>> lorenzo.age
29
{% endhighlight %}

{% highlight python %}
>>> lorenzo.have_a_birthday()
{% endhighlight %}

{% highlight python %}
>>> lorenzo.age
30
{% endhighlight %}

# Question 6
Now study the class below, which stores information about quadratic polynomials:

{% highlight python %}
>>> class Quadratic:
...     def __init__(self, a, b, c):
...         self.a = a
...         self.b = b
...         self.c = c
...     
...     def number_of_roots(self):
...         discriminant = self.b ** 2 - (4 * self.a * self.c)
...         if discriminant < 0:
...             return 0
...         if discriminant == 0:
...             return 1
...         return 2
{% endhighlight %}

Use this class to find the numbers of roots to the following quadratics:

a) $$x^2 - 10x + 2$$

b) $$-5x^2 + x + 80$$

c) $$4x^2 - 4x + 1$$







# Question 7

Adapt the class given in Question 6 so that it also has a method that gives the roots for the cases when there are two roots:

$$
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
$$

Find the roots for the three quadratics given in the previous question.









# Question 8
Write a class to represent a rectangle. When creating an instance it needs to take in a width and a length. Write three methods, one that gives the area, one that gives the perimeter, and one that checks if the rectangle s square or not.

Use this to create a list of all square objects with integer side length under 100.
Which squares have a larger perimeter than area?







# Question 9
Write a class to represent a circle. When creating an instance it needs to take in a radius. Write two methods, one that gives the area, and one that gives the circumference.

Use this to create a list of all circle objects with integer radius under 100.
Which circles have a larger circumference than area?

(You may need it *import the math library* in order to use $$\pi$$)







{% highlight python %}

{% endhighlight %}

