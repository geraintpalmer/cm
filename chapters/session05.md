---
layout: page
permalink: /chapters/session05/
title: Using Code 2 - NetworkX
---

## Goals

+ Read in data from files.
+ Use pre written code to minimise advertising costs for Shed Josie.

For this session you will be using the library `networkx`. This may need to be installed using `pip`:

  + `pip install networkx` or
  + `pip install --user networkx` on a university computer.


# Josie's Shed

Josie's Shed is a chain of garden stores based in Grenoble. They are going to embark on a national radio advertising campaign to promote their stores across the whole of France, using local radio station. They have identified 30 cities which much hear the radio advertisments. Furthermore they do not need to advertise on every local radio station, as cities close enough to one another can here eachothers' radio broadcasts:

<img src="/cm/assets/france_map.png" width="600">{: .center-image }

The 30 cities form a network, and cities with an edge between them are close enough to listen to one another's radio broadcasts.

Your task is to identify the minimum number of cities Josie's Shed needs to broadcats from, and identify which cities to broadcast from, in order to reach all 30 cities in France.

## Question 1

First let's download and read in some data.

Download:

+ [The list of 30 French cities](/cm/assets/french_cities.txt)
+ [The adjacency matrix](/cm/assets/french_distances.csv)

Save these in the same folder as the notebook you are working on.

Next, let's read in the list of cities:

{% highlight python %}
>>> with open('french_cities.txt', 'r') as f:
...     cities = f.read()
{% endhighlight %}

{% highlight python %}
>>> cities
'Amiens\nAvignon\nBiarritz\nBordeaux\nBrest\nCaen\nCalais\nDijon\nGrenoble\nLa Rochelle\nLe Havre\nLe Mans\nLille\nLimoges\nLyon\nMarseilles\nMontpellier\nNancy\nNantes\nNice\nOrleans\nParis\nPerpignon\nPoitiers\nReims\nRennes\nRouen\nStranbourg\nToulon\nToulouse'
{% endhighlight %}

This is a string of a list of cities, each separated by the line break character `\n`. Let's break this into a list:

{% highlight python %}
>>> cities_list = cities.split('\n')
>>> cities_list
['Amiens',
 'Avignon',
 'Biarritz',
 'Bordeaux',
 'Brest',
 'Caen',
 'Calais',
 'Dijon',
 'Grenoble',
 'La Rochelle',
 'Le Havre',
 'Le Mans',
 'Lille',
 'Limoges',
 'Lyon',
 'Marseilles',
 'Montpellier',
 'Nancy',
 'Nantes',
 'Nice',
 'Orleans',
 'Paris',
 'Perpignon',
 'Poitiers',
 'Reims',
 'Rennes',
 'Rouen',
 'Stranbourg',
 'Toulon',
 'Toulouse']
{% endhighlight %}

Now let's read in the adjacency matrix (a matrix where rows and columns represent cities, and entries are either a 1 or a 0 depending if those cities have an edge between them in the network). As this is a matrix of numbers, we'll use the `numpy` library to make things easier:

{% highlight python %}
>>> import numpy as np
{% endhighlight %}

{% highlight python %}
>>> adjacency_matrix = np.genfromtxt('french_distances.csv', delimiter=',')
{% endhighlight %}

Looking at `adjacency_matrix` we see it's a list of lists, each list containing 30 numbers, `0`s or `1`s.

Looking at the map, there is a link between `Marseilles` and `Nice`. Marseilles is city number 15, and Nice is number 19:

{% highlight python %}
>>> cities_list.index('Marseilles')
15
{% endhighlight %}

{% highlight python %}
>>> cities_list.index('Nice')
19
{% endhighlight %}

So we'd expect a link between these in the adjacency matrix:

{% highlight python %}
>>> adjacency_matrix[15, 19]
1.0
{% endhighlight %}

On the other hand, `Amiens` and `Avignon` (cities 0 and 1) are too far away to share radio waves, so they should not have a link:

{% highlight python %}
>>> adjacency_matrix[0, 1]
0.0
{% endhighlight %}

Now identifying which cities to broadcast from is a common problem when framed as a network. We are tyring to find the *minimum dominating set*. We can use `networkx` to find this:

{% highlight python %}
>>> import networkx as nx
>>> G = nx.from_numpy_array(adjacency_matrix)
>>> dominating_set = nx.dominating_set(G)
>>> dominating_set
{0, 1, 2, 4, 7, 9, 11, 19, 27, 29}
{% endhighlight %}

So Josie's Shed only needs to broadcast in 10 cities to reach every one of the 30 targeted cities.

What are those cities?

{% highlight python %}
>>> for city_number in dominating_set:
...     print(cities_list[city_number])
Amiens
Avignon
Biarritz
Brest
Dijon
La Rochelle
Le Mans
Nice
Stranbourg
Toulouse

{% endhighlight %}

That is:

<img src="/cm/assets/france_map_sol.png" width="600">{: .center-image }


## Question 2

Shed Josie want to begin an advertsing campaign in Italy. Repeat this analysis for Italy:

+ [The list of 14 Italian cities](/cm/assets/italian_cities.txt)
+ [The adjacency matrix](/cm/assets/italian_distances.csv)

<img src="/cm/assets/italy_map.png" width="600">{: .center-image }




## Question 3

Shed Josie want to begin an advertsing campaign in the USA. Repeat this analysis for the USA:

+ [The list of 40 American cities](/cm/assets/american_cities.txt)
+ [The adjacency matrix](/cm/assets/american_distances.csv)

<img src="/cm/assets/usa_map.png" width="600">{: .center-image }




---

[Previous](/cm/chapters/session04/) - [Home](/cm/) - [Next](/cm/chapters/session06/)
{:style="text-align: right;"}

{% highlight python %}

{% endhighlight %}

