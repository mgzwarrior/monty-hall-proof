# Monty Hall Proof
## Author: Matt Grant
A program to prove the Monty Hall problem.

# Background
The [Monty Hall problem](https://en.wikipedia.org/wiki/Monty_Hall_problem "Monty Hall problem Wikipedia") is a brain teaser, in the form of a probability puzzle, loosely based on the American television game show *Let's Make a Deal* and named after its original host, *Monty Hall*.

## Problem Question
> Suppose you're on a game show, and you're given the choice of three doors: Behind one door is a car; behind the others, goats. You pick a door, say No. 1, and the host, who knows what's behind the doors, opens another door, say No. 3, which has a goat. He then says to you, "Do you want to pick door No. 2?" Is it to your advantage to switch your choice?

## Assertion
In theory, contestants who switch to the remaining unopened door will win the car two out of every three games.  On the other hand, contestants who choose to stay with their original choice will win the car only one out of every three games.  This program aims to prove this assertion by simulating both scenatios a given number of times to determine if it is truly in the contestant's best interest to switch their choice.

# Running Instructions
This section outlines how to run the script.

## Input Arguments
1. Number of games for each scenario (eg. 100, 1000, etc.)
2. Enable/disable logging (eg. True or False)

### Example
`python3 monty-hall-proof.py 100000 True`

# Results
TBD

# To-Do
+ Repalce 'empty' doors with goats
+ Review game scenarios for accuracy
+ Document results
+ Performance improvements