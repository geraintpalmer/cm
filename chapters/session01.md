---
layout: page
permalink: /chapters/session01/
---

# Goals

+ Download and install Anaconda, either on a university machine or your personal computer if you have one.
+ Use pre-written code to solve a problem for Shed Josie.

# Shed Josie

Shed Josie is a chain of garden stores based in Grenoble. Customers arrive and join a queue to be served at a counter. When a staff member is available they begin serving the customer at the front of the queue.

[Queue diagram]

At the Rue de Paris store, customers on average arrive at a rate of 1.5 per hour, and are served ar a rate of 0.15 per hour. There are 10 members of staff on duty.
They have recently had a number of complaints as some of customers are waiting longer than half an hour to be served.

Upper management would like to know how many servers are needed in order to ensure the number of customers waiting longer than half an hour falls below 1%.

Using code
==========

The code below defines a Python function that can be used to calculate the proportion of customers in a given `time_period` that wait longer than a given `limit`:

{% highlight python %}
>>> import ciw

>>> def get_proportion_waiting_over_limit(arrival_rate=1.5, service_rate=0.15, number_of_staff=2, limit=0.5, time_period=14*24, number_of_repetitions=100):
...     N = ciw.create_network(arrival_distributions=[ciw.dists.Exponential(arrival_rate)], service_distributions=[ciw.dists.Exponential(service_rate)], number_of_servers=[number_of_staff])
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

## Question 1

Under the current system, managers believe that 78% of customers are waiting longer than 1 hour. The following code shows this.

Click the cell and then click the run bottom above, or press the shift+return keys together, to run the sell.

{% highlight python %}
>>> get_proportion_waiting_over_limit(number_of_staff=10, limit=0.5)
0.7819238389315349
{% endhighlight %}

## Question 2

If Shed Josie put on four extra members of staff, what proportion of the customers would wait longer than half an hour?

Write your code in the cell below and run it as before.

{% highlight python %}
>>> # Write your code here...
{% endhighlight %}



## Question 3

In this scenario, what proportion of the customers wait longer than fifteen minutes?

Create a cell below using the create a cell button, write the appropriate code and run it.



## Question 4

Experiment with a number of scenarios and determine the least number of staff required such that no more than 1% of customers wait longer than half an hour.









## Further work

By looking ahead at the class resources, attempt to automate the above.



{% highlight python %}

{% endhighlight %}

