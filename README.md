# Exercise 10 for Min-Max Algorithm (Kmeans)

## Task
The goal of the exercise is to implement the Min-Max algorithm that would make a smart AI agent.

## Input
At the start of the program, it asks the user if it wants be X or O and then asks if he/she wants to play first.

## Required Output
The output of the exercise is a TicTacToe game with a GUI and a SMART AI agent. The user should not by any means win and the best possible state only is a draw or the AI wins.

## Programming language used
- Python

## Problems encountered
- It was not easy for me to grasp the entirety of the minmax algorithm. The recursive calls were confusing. This is especially because I think this is the first time I dealt with an AI that actually fights a user. I also did not immediately understand how I can get the action/successor after the value is computed. Lastly, I had a hard time implementing alternate turns because of how tkinter works.

## How the problems were resolved
- As usual, I just spent more time understanding the algorithm's pseudocode. I realized that even though the algorithm was confusing, I think the pseudocode given was quite straightforward. What I did to get the action/successor after the value is computed is associate the action (index) done to arrive at a successor and its value by placing them in an array. Regarding the alternate turns, what solved my problem is the update() function which updates the GUI despite not iterating completely. (by iterating, what I mean is the iteration caused by the mainloop())

## Learnings from the exercise
- Despite difficulties, I had fun doing this exercise. I learned how to implement an AI agent for the Tic-Tac-Toe game. I was able to make an AI that decides (intelligently) what move to pick given a game state through the use of minmax algorithm. This is great because it felt like I implemented an algorithm that enables a computer/program to "think." Also, even though I did not implement the Alpha-Beta pruning because I still have many requirements to do, I understand the idea of it and how it makes the minmax algorithm more efficient. Lastly, I learned more about python's tkinter.

