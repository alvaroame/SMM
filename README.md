# SMM
Smallest minimum multiple

## Description
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

## Task
✅ Task 1 → What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20? 

## How did I solve  it?

I noticed that the answer is the LCM (Least Common Multiple), so I implemented the division method.

1.- I created a list of numbers from 1 to n.

2.- From the previous list, I created a second list just adding all prime numbers from 1 to n.

3.- I used both lists to compute the LCM Method.

4.- Starting with the lowest prime number, I divided all numbers by a prime number that is evenly divisible into at least one. I overwrote the numbers with the result or kept the numbers if they are not evenly divisible. I did this loop until the list of numbers was full of ones.

5.- The result was the multiplication of the prime numbers that were divided.


### Created by
- **Alvaro Ramírez**
