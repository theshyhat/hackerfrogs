# Chapter 1: What is AI?
## Key Terms
### Autonomy
The ability to perform tasks in complex environments without constant guidance by a user.
### Adaptivity
The ability to improve performance by learning from experience.
### Machine learning
Systems that improve their performance in a given task with more and more experience or data.
### Robot
A machine comprising sensors (which sense the environment) and actuators (which act on the environment) that can be programmed to perform sequences of actions
### General AI
Artificial General Intelligence (AGI) refers to a machine that can handle any intellectual task.
### Narrow AI
AI that handles one task.
### Strong AI
A “mind” that is genuinely intelligent and self-conscious.
### Weak AI
Systems that exhibit intelligent behaviors despite being “mere“ computers.
## Forecasts
* a system which predicts whether something will happen or not is not proven to be good or bad with a single event
* a system has to be observed over a large number of events to be determine if its predictions are reliable or not
## Odds
* the odds of something happening are expressed in the `times it happens:times it doesn't happen` format, e.g., `3:1` odds means that something happens 3 times for every time it doesn't happen
* the total number of events involved is the sum of the two numbers, so `3:1` odds means that there are `3 + 1 = 4` events in total, in which 3 times it happens, and 1 time it doesn't
* if we divide the total number of events by the the first number, we get the percentage that the event occurs, e.g., `3:1` odds means there are `3 + 1 = 4` events, then we divide 3 by 4 and get `0.75`, meaning that the event happens 75 percent of the time
## The Bayes Rule
* method of updating probability of something upon gaining new evidence or changing circumstances
* when applying Bayes, we have two sets of odds:
  * `prior odds` is the first set, which is the probability of something prior to learning the new information
  * we can also think of these as "original odds" or "initial odds"
  * `posterior odds` is the second set, which is the probability after new information is obtained, and is calculated using the following formula: `posterior odds = prior odds * likelihood ratio`
  * `likelihood ratio` is the combination of odds between an event happening and an event not happening
    * it is calculated in the following way: `odds of happening / odds of not happening`
    * in this calculation, we must express the odds as a number, e.g., `0.5`, in the case of `1:1` odds
    * we could use this Python script to perform the calculation:
# Chapter 4: Machine Learning
## Key Terms
### Types of Machine Learning
#### Supervised Learning
We are given an input, for example a photograph with a traffic sign, and the task is to predict the correct output or label, for example which traffic sign is in the picture (speed limit, stop sign, etc.). In the simplest cases, the answers are in the form of yes/no (we call these binary classification problems).
#### Unsupervised Learning
There are no labels or correct outputs. The task is to discover the structure of the data: for example, grouping similar items to form “clusters”, or reducing the data to a small number of important “dimensions”. Data visualization can also be considered unsupervised learning.
#### Reinforcement Learning
Commonly used in situations where an AI agent like a self-driving car must operate in an environment and where feedback about good or bad choices is available with some delay. Also used in games where the outcome may be decided only at the end of the game.
### Regression
A supervised learning method used to predict a continuous value, such as the price of a house, temperature, or sales volume
