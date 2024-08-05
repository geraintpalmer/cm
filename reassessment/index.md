---
layout: page
title: Re-assessment
---

# Brief
+ Write code that implements [Kruskal's algorithsm ](https://en.wikipedia.org/wiki/Kruskal%27s_algorithm) for a set of cities. It should take in a set of cities and a distance matrix, and return a set of edges that form a minimum spanning tree (MST).
+ Download the [set of 100 Spanish towns and cities](spain.csv) and [distance matrix](spain_distances.csv).
+ Use the above code to find the minimum spanning tree for set of cities. Once the MST has been built, see if you can visualise the minimum spanning tree in any way.
+ Write a two page report on your work.

# Kruskal's Algorithm
Start with a set of **N** cities and distance matrix.
+ Begin with two empty lists:
  + `MST_edges` -  containing the edges of the minimum spanning tree,
  + `MST_cities` - containing cities incident to the edges in the minimum spanning tree
+ While `MST_edges` does not contain (**V - 1**) edges:
    + Search the distance matrix for the shortest edge.
    + If that edge does not form a loop (that _both_ cities incident to that edge are not in `MST_cities`):
        + Add edge to `MST_edges'
        + Add any city incident to that edge _not_ already in `MST_cities` to `MST_cities`
    + Relabel that edge distance in the distance matrix as infinity


# Further Details

+ You will submit ***a maximum of two pages*** *including any references, figures and tables;* ***and*** one fully documented Jupyter Notebook.
+ If you exceed 2 pages only the first three pages will be read and the rest discarded.
+ You are free to use whatever report structure you wish.
+ You will also submit a single Jupyter Notebook including all code used to solve the problem. This includes any functions or classes used to write the heuristic algorithm, the use of those functions or classes to solve the problem, and any analysis.
+ ***A marker should be able to exactly reproduce all reported results using the provided Jupyter Notebook.***


# How it will be marked

+ THE CODE (50%)
  + **Correctness (20%)**
  + **Clarity & Readability (20%)**
  + **Appropriateness (10%)**

+ THE REPORT (50%)
  + **Comprehension & Understanding (25%)**
  + **Organisation & Clarity (25%)**
