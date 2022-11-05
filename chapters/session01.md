---
layout: page
permalink: /chapters/session01/
title: Using Code 1 - Ciw
---

## Goals

+ Download and install Anaconda, either on a university machine or your personal computer if you have one.
+ Use pre-written code to solve a problem for Shed Josie.

# Using Jupyter

+ If you are using a university computer, all relevant software will already be installed.
+ If you are using your own computer you will need to have installed the Anaconda software on your machine. [Please follow the instructions at the bottom of this page](/cm/chapters/session00/).
+ On both university computers and your own machine, you will need to install the `Ciw` Python package. Do this (after installing anaconda), by opening up your command prompt and typing:

  + `pip install ciw` or
  + `pip install --user ciw` on a university computer.
  
  Tutors will be around to help with this.

One the software is installed you will need to launch the software.
Double click on 'Anaconda Navigator':

<img src="/cm/assets/navigator.png" width="70">{: .center-image }

To write and run Python code, we will be using 'Jupyter Notebooks'. These are just one way to use Python, but is a popular tool when conducting data analysis, and is great for learning the language.
Launch Jupyter:

<img src="/cm/assets/jupyter.png" width="70">{: .center-image }

  + This will launch a local server in a web browser. *It is not connected to the internet*, and will still work if you are not connected to the web.
  + A notebook contains a number of 'cells', in which code can be written and then run. After the cell is run, any output will be displayed below the cell.
  + In a cell type `2 + 2`.
  + In order to run this cell click on the 'run cell' button on the top menu bar:

  <img src="/cm/assets/run.png" width="500">{: .center-image }

  
  + You can also run cells by pressing the `shift`+`return` keys together.
  + You should see the relevant output displayed below.
  + To manually create a new cell, click on the 'insert new cell' button on the top menu bar:
  
  <img src="/cm/assets/new-cell.png" width="500">{: .center-image }

Now you are ready to begin using code!

# Josie's Shed

Josie's Shed is a chain of garden stores based in Grenoble. Customers arrive and join a queue to be served at a counter. When a staff member is available they begin serving the customer at the front of the queue.

<img src="/cm/assets/queue_diagram.svg" width="500">{: .center-image }

At a particular shop, customers on average arrive at a rate of 1.5 per hour, and are served ar a rate of 0.15 per hour. There are 10 members of staff on duty.
They have recently had a number of complaints as some of customers are waiting longer than half an hour to be served.

Upper management would like to know how many servers are needed in order to ensure the number of customers waiting longer than half an hour falls below 1%.

Using code
==========

The code below defines a Python function that can be used to calculate the proportion of customers in a given `time_period` that wait longer than a given `limit`:

{% highlight python %}
>>> import ciw

>>> def get_proportion_waiting_over_limit(
...     arrival_rate=1.5,
...     service_rate=0.15,
...     number_of_staff=2,
...     limit=0.5,
...     time_period=14*24,
...     number_of_repetitions=100,
... ):
...     N = ciw.create_network(
...         arrival_distributions=[ciw.dists.Exponential(arrival_rate)],
...         service_distributions=[ciw.dists.Exponential(service_rate)],
...         number_of_servers=[number_of_staff])
...     proportions = []
...     for repetition in range(number_of_repetitions):
...         ciw.seed(repetition)
...         Q = ciw.Simulation(N)
...         Q.simulate_until_max_time(time_period)
...         all_recs = Q.get_all_records()
...         over_limit = [r.waiting_time > limit for r in all_recs]
...         proportions.append(sum(over_limit) / len(all_recs))
...     return sum(proportions) / len(proportions)
{% endhighlight %}

Copy this code into a new cell and run that cell.
This function is a pre written function that you will use to answer the questions below.
Once the cell is run, that function will be in memory and available to use:

## Question 1

Under the current system, managers believe that 78% of customers are waiting longer than half an hour. The following code shows this.

{% highlight python %}
>>> get_proportion_waiting_over_limit(number_of_staff=10, limit=0.5)
0.7819238389315349
{% endhighlight %}

## Question 2

If Josie's Shed put on four extra members of staff, what proportion of the customers would wait longer than half an hour?



## Question 3

In this scenario, what proportion of the customers wait longer than fifteen minutes?



## Question 4

Experiment with a number of scenarios and determine the least number of staff required such that no more than 1% of customers wait longer than half an hour.









## Question 5

Experiment with a number of scenarios and determine the least number of staff required such that no more than 1% of customers wait longer than five minutes.





## Further work

By looking ahead at the class resources, attempt to automate the above.





---

[Previous](/cm/chapters/session00/) - [Home](/cm/) - [Next](/cm/chapters/session02/)
{:style="text-align: right;"}

