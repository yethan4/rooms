# ROOMS

This is my solution to a discrete mathematics assignment from which I received 15/15 points.

The content of the task can be found in the file [rooms.pdf](https://github.com/yethan4/rooms/blob/main/pokoje.pdf) (in polish)

An additional requirement was that the program for each file was to execute in about 5 seconds, and to get the maximum number of points you had to make a short description of your solution [opis.txt](https://github.com/yethan4/rooms/blob/main/opisPL.txt) (in polish)

# How did I deal with it?

At the beginning the solution was based on checking each stage of the game. Naturally, this method only worked for the first two files and failed for the rest.
So I started looking for a suitable graph search algorithm, but none of the ones I found was the answer to the task. And then I thought, after all, we have not had any graph search algorithm on discrete mathematics yet so this would not be the solution.
In the end, I took the step I should really have taken at the very beginning,
which is to redirect the various stages of the game to a file for analysis. That's when I noticed a pattern: if a child reaches the target room for the first time at stage 
𝑥 and the second time at stage 𝑦 they will reach it for the third time at stage 𝑦+(𝑦−𝑥). 
This realization was a breakthrough because I immediately saw the connection to congruence equations, which ultimately became the basis of the solution.

# How to run?

```bash
  git clone https://github.com/yethan4/rooms.git
  cd rooms
  python3 rooms
```

