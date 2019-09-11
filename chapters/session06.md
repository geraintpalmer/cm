---
layout: page
permalink: /chapters/session06/
---

## Algorithmic Thinking 2 - Optimisation


In the last session you used code that to solve the advertising campaign problem.
As a reminder:

  + There are number of cities which we would like to broadcast an advertisment to.
  + Each city has their own radio station to transmit the advertisment.
  + If a city is chosen to broadcast the advertisment, then all cities close by can also hear the advertisment ('close by' is determined by a network, or adjacency matrix).
  + What is cities should we broadcast from in order for the advertisment to reach every city, that would minismise the number of broadcasts?

<img src="/assets/france_map.png" width="450"><img src="/assets/france_map_sol.png" width="450">

Thinking of this in terms of graphs, this is an example of finding a [dominating set](https://en.wikipedia.org/wiki/Dominating_set).
You may find throughout your degree and beyond, that well defined and commonly studied problems have clever and specific methods of solving them.
Recognising that your problem can be generalised to one of these well studied problems, and then identifying the appropriate solution method, is a skill you will learn with experience.
Otherwise, a more generic solution method is required.


# Generic solution methods

If a specialised solution method is not known, we usually use a generic or naive method, or a clever version of this (called a [heuristic](https://optimization.mccormick.northwestern.edu/index.php/Heuristic_algorithms), you may study these further in your degree).
In order to do this, we need to be able to *easily check how well a solution performs*, even if finding the optimal solution is difficult.
Naive heuristics usually follow the following outline:

1. Evaluate initial guess at solution
2. Change the solution slightly
3. Evaluate solution
4. If better than pervious best, call this previous best
5. Go back to 2.

In today's task you will be thinking about how you can write an algorithm to solve the advertising campaign problem in this way. What does 'evaluate' mean in this case? What does a 'solution' look like? How would you 'change' the solution? Are there any other steps you could add that to make the algorithm better or more efficient?

The heart of the problem is the adjacency matrix, let's recap.


# Adjacency matrices

You used adjacency matrices in the previous section.
Here is a reminder:

> The adjacency matrix of a simple graph is a matrix with rows and columns labeled by graph vertices, with a 1 or 0 in position $$(v_i, v_j)$$ according to whether $$v_i$$ and $$v_j$$ are adjacent or not.

An example:

<img src="/assets/adj_matrix.png" width="350">{: .center-image }

$$
\begin{array}{c c} &
\begin{array}{c c c c c c} A & B & C & D & E & F \\
\end{array} 
\\
\begin{array}{c c c c c c}
A \\
B \\
C \\
D \\
E \\
F
\end{array} 
&
\left(
\begin{array}{c c c c c c}
1 & 1 & 0 & 1 & 0 & 1 \\
1 & 1 & 1 & 1 & 0 & 1 \\
0 & 1 & 1 & 1 & 0 & 0 \\
1 & 1 & 1 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 & 1 & 1 \\
1 & 0 & 0 & 0 & 1 & 1 \\
\end{array}
\right)
\end{array}
$$

Think about how this is connected to the advertising campaign problem.
If an advert is broadcast in city A, then all cities with a 1 in the A row will be able to hear it.
(Usually an adjacency matrix has 0s in the diagonal, but it has ben adapted in ths case for a more meaningful interpretation.)


# Task

**In groups of 4 or 5, write down *in English* a precise algorithm for solving the advertising campaign problem. It should take as inputs the adjacency matrix, and any other parameters you feel is needed. It should output a list of cities.**

*You should consider:*

  + Mathematically, what does a 'solution' look like?
  + How would we generate or change solutions?
  + What is the easiest way to check if a solution is **feasible** (it is a dominating set, it does cover every city)?
  + How can we compare two feasible solutions?
  + When should the algorithm stop?

*Some **advanced** questions to consider:*

  + What information do you need to store?
  + What does the **rank** of the adjacency matrix give you? How could this help?
  + Are you confident your solution is the *optimal*?