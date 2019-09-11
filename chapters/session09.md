---
layout: page
title: Further Concepts in Programming
---

The purpose of this session is to *very briefly* point to some further topics that you may be interested in, and will doubtless be very useful when writing your own programs.


# 1. Scripts

We have been using Jupyter Notebooks to write and run Python, installed using Anaconda.
However this is only one way of doing this.
Python is just a language and, with Anaconda, your computer can read and run files written in this language. To help the computer out, we save these files with the extension `.py`.

For example, save the following bit of Python in a file on your computer called `hello-world.py` (you can do this using any text editor).

{% highlight python %}
sum = 0
for num in range(10):
    sum += num
print('Hello world! My sum is ' + str(sum))
{% endhighlight %}

Then open your *command line* or *command prompt*.
Navigate to the place where you saved the file, and then type:

{% highlight bash %}
python hello-world.py
{% endhighlight %}

This tells the computer to read and run the Python written in the file `hello-world.py`.

Running scripts is the usual way to run very large Python programs, maybe code that takes a long time to run, or would be inappropriate for the Jupyter Notebook environment.



# 2. Readable code

You may have noticed throughout this course that nearly all Python commands look like English, and reading some Python aloud is understandable as English.
This is on purpose, to make it easier to read.

When you have the freedom to name things yourselves, such as variables, functions and objects, it is good practice to ensure that these are meaningful English names, to ensure the overall readability of the code.

For example, consider the following code:

{% highlight python %}
>>> def f(l):
...     n = len(l)
...     s = sum(l)
...     return s / n

>>> a = [1.76, 1.73, 1.68, 1.75, 1.76, 1.82, 1.77, 1.73, 1.66, 1.68]
>>> f(a)
1.734
{% endhighlight %}

With some thinking we can work out what this is doing.
But with proper variable names this task would be much easier:

{% highlight python %}
>>> def mean(data):
...     number_of_observations = len(data)
...     sum_of_observations = sum(data)
...     return sum_of_observations / number_of_observations

>>> heights = [1.76, 1.73, 1.68, 1.75, 1.76, 1.82, 1.77, 1.73, 1.66, 1.68]
>>> mean(heights)
1.734
{% endhighlight %}


# 3. Libraries

A great strength of Python is that there are a number of high quality pre-written code available for free to download.
These are called libraries, and offer functions and objects to carry out common and specialised tasks.
You have already used some of these, and the [final set of exercises](/chapters/session10/) takes you through the use of some libraries that will be particulary relevant to data science, operational research, and applied statistics.

To show the diversity and range of libraries available, and as a reference for your future studies, below is a large list of libraries and their main uses:

+ [**Astropy**](https://www.astropy.org/): For commonly used astronomy tools.
+ [**BeautifulSoup**](https://www.crummy.com/software/BeautifulSoup/bs4/doc/): For pulling data from html and xml.
+ [**Ciw**](https://ciw.readthedocs.io/en/latest/): For discrete event simulations of queueing systems.
+ [**Dask**](https://dask.org/): For parellelising analytics.
+ [**datetime**](https://docs.python.org/3/library/datetime.html): For manipulating dates and times.
+ [**Django**](https://www.djangoproject.com/): For building web apps.
+ [**fastText**](https://fasttext.cc/): For text classification and representation.
+ [**Flask**](https://palletsprojects.com/p/flask/): For building web apps.
+ [**FuzzyWuzzy**](https://chairnerd.seatgeek.com/fuzzywuzzy-fuzzy-string-matching-in-python/): For fuzzy string matching.
+ [**Gambit**](http://www.gambit-project.org/gambit13/index.html): For game theory.
+ [**GeoPandas**](http://geopandas.org/): For manipulating and plotting geospacial data and maps.
+ [**itertools**](https://docs.python.org/3/library/itertools.html): For looping and combinatorics.
+ [**Keras**](https://keras.io/): For neural networks and deep learning.
+ [**kivy**](https://kivy.org/): For app development.
+ [**math**](https://docs.python.org/3/library/math.html): For mathematical functions and constants.
+ [**matplotlib**](https://matplotlib.org/): For 2D plotting.
+ [**Nashpy**](https://nashpy.readthedocs.io/en/stable/): For game theory.
+ [**NetworkX**](https://networkx.github.io/): For graph theory and networks.
+ [**NumPy**](https://numpy.org/): For efficient linear algebra.
+ [**pandas**](https://pandas.pydata.org/): For data frame, data manipulation, and data analysis.
+ [**PuLP**](https://pythonhosted.org/PuLP/): For optimisation and linear programming.
+ [**PyFlux**](https://pyflux.readthedocs.io/en/latest/): For time series analysis and prediction.
+ [**pygame**](https://www.pygame.org/): For making games.
+ [**PyTorch**](https://pytorch.org/): For machine learning.
+ [**random**](https://docs.python.org/2/library/random.html): For generating random numbers and sampling from distributions.
+ [**requests**](https://2.python-requests.org/en/master/): For sending HTTP requests and using APIs.
+ [**scikit-learn**](https://scikit-learn.org/stable/): For machine learning.
+ [**SciPy**](https://www.scipy.org/scipylib/index.html): For scientific computations, optimisation, and statistical functions.
+ [**SimPy**](https://simpy.readthedocs.io/en/latest/): For process-based discrete event simulation.
+ [**SymPy**](https://www.sympy.org/en/index.html): For symbolic mathematics and computer algebra.
+ [**TensorFlow**](https://www.tensorflow.org/): For neural networks and deep learning.
+ [**tqdm**](https://tqdm.github.io/): For progress bars.
+ [**turtle**](https://docs.python.org/3.3/library/turtle.html): For turtle graphics.