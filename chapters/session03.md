---
layout: page
permalink: /chapters/session03/
---

# Programming Concepts 1

Below is Python code that simulates a queueing system. I should reflect the algorithm you developed in your groups.

{% highlight python %}
>>> import random

>>> def simulate_queue(arrival_rate, service_rate, number_of_staff, time_period, limit):
...     """
...     Simulates one run of a queue and returns the proportion of customers
...     waiting over a given limit. The parameters are:
...     
...     + arrival_rate
...     + service_rate
...     + number_of_staff
...     + time_period
...     + limit
...     """
...     number_of_customers = 0
...     number_over_limit = 0
...     now = 0
...     server_available_dates = [0] * number_of_staff
...     service_times = []

...     while now < time_period:
...         inter_arrival_time = random.expovariate(arrival_rate)
...         now += inter_arrival_time
...         number_of_customers += 1
...         
...         service_start_date = max(now, min(server_available_dates))
...         
...         service_time = random.expovariate(service_rate)
...         service_end_date = service_start_date + service_time
...         
...         server_available_dates.append(service_end_date)
...         server_available_dates.sort()
...         server_available_dates = server_available_dates[-number_of_staff:]
...                 
...         wait = service_start_date - now
...         if wait > limit:
...             number_over_limit += 1
...     
...     return number_over_limit / number_of_customers


>>> def get_proportion_waiting_over_limit(
...     arrival_rate=1.5,
...     service_rate=0.15,
...     number_of_staff=10,
...     limit=0.5,
...     time_period=31*24,
...     number_of_repetitions=100,
>>> ):
...     """
...     Gives the average proportion of customers waiting over a given limit,
...     over number_of_repetitions repetitions. The parameters are:
...     
...     + arrival_rate
...     + service_rate
...     + number_of_staff
...     + time_period
...     + limit
...     + number_of_repetitions
...     """
...     proportions = []
...     for repetition in range(number_of_repetitions):
...         proportions.append(simulate_queue(arrival_rate=arrival_rate, service_rate=service_rate, number_of_staff=number_of_staff, limit=limit, time_period=time_period))
...     return sum(proportions) / len(proportions)
{% endhighlight %}

{% highlight python %}
>>> get_proportion_waiting_over_limit()
0.8528070471422103
{% endhighlight %}

Study the code above, ensure that you understand what it is doing, and how it relates to the overall task of simulating a queue. The image below points out some key Python concepts used in the code:

![](/assets/concepts1-diagram-blank.svg)

Use the sentences below to fill in the blank boxes in the image above with the sentences below. Match the key concept with some description of its use:

![](/assets/concepts1-diagram-sentences.svg)

You will have a print out of these sheets.

***Complete the task by the next session,*** you may wish to look ahead in the course notes.

{% highlight python %}

{% endhighlight %}

