---
layout: page
permalink: /chapters/session02/
title: Algorithmic Thinking 1 - Simulation
---


In order to be able to tell a computer how to do something, we need to ourselves be able to think like a computer.
This means thinking in clear and precise logical steps made up from well defined (and not impossible) activities, in meaningful chronological order.
Furthermore it is vital we can communicate this thinking by giving clear and precise directions, including instructions for all data flows (where any information is kept and how it is kept updated), and leaving nothing ambiguous or impossible to carry out.

Consider my morning routine: the instructions *'get ready and get to work'* are ambiguous.
I could make this clearer by writing out the instructions step by step:

1. Wake up when alarm clock goes off.
2. Have a shower.
3. Put on clothes.
4. Put on coat if raining, or take coat in bag.
5. Walk to coffee shop.
6. Buy coffee, croissant and banana.
7. Eat breakfast.
8. Walk to the office.

To an English speaker this might seem very clear, precise and logical.
However there are are still some ambiguities, which humans fill in from context, but a computer would not be able to.
For example what was I doing before waking up? What is breakfast?

Let's fix that:

1. **While** the alarm clock hasn't gone off:
  + Sleep.
2. Have a shower.
3. Put on clothes.
4. **If** raining:
    + Put on coat.

   **Else**:
   + Put coat in bag.
5. Walk to coffee shop.
6. Buy coffee, croissant and banana. **Define** these as breakfast.
7. **For all** breakfast items:
  + Eat item.
8. Walk to the office.

This is a far better written set of instructions.

Notice some of the highlighted words, these were deliberately chosen to reflect well-defined concepts that computers can follow. You will investigate these further in the next session.

Once these instructions have been written like this, it is straightforward to translate them to code.

# Algorithms

A set of well defined instructions like this is called an ***algorithm***.

According to Donald Knuth ([The Art of Computer Programming, 1997](https://learning.oreilly.com/library/view/art-of-computer/9780321635754/)), an algorithm must have five important features:
  + *Finiteness*: An algorithm must terminate, it cannot go on forever. Thus an algorithm cannot include mathematical steps such as $$\sum_{k=1}^{\infty} \frac{1}{k^2}$$, but can include approximations or truncations.
  + *Definiteness*: Each step must be precisely defined with no ambiguity.
  + *Inputs*: An algorithm can take any number of inputs, including zero inputs.
  + *Outputs*: An algorithm has one or more outputs, that is the reason to carry out the algorithm.
  + *Effectiveness*: Each step of the algorithm must be possible to carry out. For example an algorithm cannot contain a step which states 'define $$n$$ as the smallest odd perfect number', as it is not known whether any odd perfect numbers exist.


# Example

Here's Euclid's algorithm for finding the greatest common divisor of two numbers, `A` and `B` where `A > B` initially:

    Input: Integers A and B, A > B
    Output: gcd

    1. While A > B:
        2. Define R as the remainder when A is divided by B.
        3. If R = 0:
            + B is the gcd, the algorithm ends.
           Else:
            + Set A as B.
            + Set B as R.
            + Go to step 2.

This algorithm has all five of Knuth's properties of an algorithm:

  + Definiteness: Each step is precisely defined with no ambiguity.
  + Effectiveness: Each step is possible (another algorithm may be needed to carry out step 2).
  + Inputs: Integers `A` and `B`, with the condition that `A > B`.
  + Outputs: the greatest common divisor of `A` and `B`.
  + Finiteness: This is more difficult to assert, note that:
     + Step 2 ensures `R` is an *positive integer* smaller than both `A` and `B`,
     + Step 3 ensures that `A` and `B` are monotonically decreasing with each iteration,
     + Together these ensure that `A` is always greater than `B`,
     + `B` will always decrease to a divisor of `A`, as 1 is a divisor of everything,
     + Therefore the algorithm will always end.


# Task

In the last session you used code that ran a simulation of a queueing system.
In a queueing system:

  + There are a finite number servers.
  + Customers arrive randomly according to some arrival rate.
  + If there are any free servers at the time of arrival, they begin service. Else they join the queue.
  + Customers spend a random period of time in service, at some service rate.
  + When a customer finishes service they leave the system. The server is then free to begin service with the customer at the head of the queue.
  + The time between arriving and being served is the customers' waiting time.

**In groups of 4 or 5, write down *in English* a precise algorithm for the simulation a queue. It should take as inputs the number of servers, the arrival rate, the service rate, a maximum simulation time, and a waiting time limit. It should output the percentage of customers who have waited over the limit for service.**

Think about:

  + What events need to happen?
  + In what order do these events need to occur?
  + How will you keep track of all the customer's arrival, service, and waiting times?
  + How will you decide when a customer begins service?
  + When does the simulation end?

---

[Previous](/cm/chapters/session01/) - [Home](/cm/) - [Next](/cm/chapters/session03/)
{:style="text-align: right;"}