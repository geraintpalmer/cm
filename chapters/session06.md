---
layout: page
permalink: /chapters/session06/
---

## Programming Concepts 2

Below is Python code for a greedy algorithm that finds the dominating set of a graph. Notice that this is structured as a class, with attributes and methods.

{% highlight python %}
>>> import numpy as np
>>> import random

>>> class AdvertisingCampaign:
...     def __init__(self, cities, adjacency_matrix):
...         self.cities = cities
...         self.number_of_cities = len(self.cities)
...         self.adjacency_matrix = adjacency_matrix
...         self.best_score = len(self.cities)
...         self.best_solution = np.array([1 for _ in self.cities])
...         self.number_broadcasts_to_try = np.linalg.matrix_rank(self.adjacency_matrix)
...     
...     def evalutate_solution(self, solution):
...         coverage = np.matmul(solution, self.adjacency_matrix)
...         if 0 in coverage:
...             return self.number_of_cities
...         return sum(solution)
...     
...     def new_solution(self):
...         number_empty = self.number_of_cities - self.number_broadcasts_to_try
...         sol = [1 for _ in range(self.number_broadcasts_to_try)] + [0 for _ in range(number_empty)]
...         random.shuffle(sol)
...         return np.array(sol)
...     
...     def optimise(self, num_itrs):
...         for iteration in range(num_itrs):
...             solution = self.new_solution()
...             score = self.evalutate_solution(solution)
...             if score <= self.best_score:
...                 self.best_solution = solution
...                 self.best_score = score
...                 self.number_broadcasts_to_try = self.best_score - 1
...     
...     def print_solution(self):
...         for i, city in enumerate(self.cities):
...             if self.best_solution[i] == 1:
...                 print(self.cities[i])
{% endhighlight %}

{% highlight python %}
>>> with open('french_cities.txt', 'r') as f:
...     cities = f.read()
...     cities_list = cities.split('\n')
>>> adjacency_matrix = np.genfromtxt('french_distances.csv', delimiter=',')
{% endhighlight %}

{% highlight python %}
>>> R = AdvertisingCampaign(cities_list, adjacency_matrix)
>>> R.optimise(10000)
>>> R.print_solution()
Avignon
Bordeaux
Brest
La Rochelle
Le Havre
Nancy
Nice
Rouen

{% endhighlight %}

{% highlight python %}
>>> R.best_score
8
{% endhighlight %}

Study the code above, ensure that you understand what it is doing, and how it relates to the overall task of finding the dominating set of a graph. The image below points out some key Python concepts used in the code:

![](/assets/concepts1-diagram-blank.svg)

Use the sentences below to fill in the blank boxes in the image above with the sentences below. Match the key concept with some description of its use:

![](/assets/concepts1-diagram-sentences.svg)

You will have a print out of these sheets.

***Complete the task by the next session,*** you may wish to look ahead in the course notes.

{% highlight python %}

{% endhighlight %}

