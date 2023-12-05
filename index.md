---
title: "Section 13: Final Exam Prep"
author: Jed Rembold and Eric Roberts
date: "Week of December 4th"
slideNumber: true
theme: monokai
highlightjs-theme: monokai
width: 1920
height: 1080
transition: fade
css:
  - css/codetrace.css
  - css/roberts.css
---


## Problem 1a: Tracing
- Trace the below function to determine its output

```mypython
def mystery(x, y=10):
  z = len(x)
  return x[y:] + enigma(z, 2) * "o"

def enigma(x, z):
  return x - z ** 2

chill = "Snowman"
print(mystery(chill, -3))
```

## Problem 1b: Tracing
- What is printed at the end?

```{.mypython style='max-height:850px; font-size:.75em;'}
class Frosty:
  def __init__(self, n, c):
    self.wild = [c]
    self.n = n

  def snowball(self, h=3):
    self.n -= h
    self.wild += [self.n]

  def cap(self):
    return self.wild

f = Frosty(5, 12)
f.snowball()
A = f.cap()
A.append(5)
print(sum(f.cap())
```

## Problem 2: Fundamentals
- The Racamán sequence starts at 0, termed $a_0$
- Future values in the sequence are given by:
  
  $$ a_n = \begin{cases} a_{n-1}-n, &\text{if $a_{n-1}-n > 0$ and has not already appeared in the sequence} \\ a_{n-1} + n, & \text{otherwise}\end{cases} $$
- Thus

  $$ \begin{aligned}
     a_0 &= 0\\
     a_1 &= 1\\
     a_2 &= 3\\
     a_3 &= 6\\
     a_4 &= 2\\
     a_5 &= 7\\
     \end{aligned} $$

## Problem 2 continued
- Write a function called `racaman(n)` which takes as an argument a single integer and returns the nth value of the Racamán sequence
  ```python-repl
  >>> print(racaman(3))
  6
  >>> print(racaman(6))
  13
  ```

## Problem 3: Interactive Graphics
- The "Fifteen Puzzle" is a sliding puzzle with the numbers 1 through 15 on a set of square tiles
- One space in open, allowing neighboring tiles to be slide into the space
- Goal is to arrange the numbered tiles in order, from upper left to bottom right


## Problem 3 - Step 1
::::::cols
::::col
- Write a program to display the starting state of the Fifteen Puzzle
- Each piece should be a `GCompound` containing a filled square and a centered number
- Should resemble the image to the right
::::

::::col

::::
::::::

## Problem 3 - Step 2
- Make the program interactive by having clicking on a piece move it to the open space if possible
  - Figure out which square you clicked on using `get_element_at`
  - Check all 4 directions to see if any are both inside the window and unoccupied. If that condition is met, move the clicked piece into the free space. Otherwise, do nothing.
