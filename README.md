This program computes a policy of movement for a 2d grid given by input.txt, which has a fixed set of unmoving obstacles and one destination location.
The policy is a mapping that tells you, in each location, the direction you should go to achieve the highest accumulated reward over time with the greatest likelihood.
Each movement has a 70% chance to be in the desired direction, and a 10% chance to move in any other cardinal direction.
There is a small cost associated with each movement, a large cost for moving into a space with an obstacle, and a large benefit for reaching the destination.

Input (input.txt):

[grid size] (strictly positive integer)

[number of obstacles] (non-negative)

(next (number of obstacle) lines) [location of each obstacle] (in format x,y)

[destination] (in format x,y)


Output (output.txt):
- obstacles are represented by 'o'
- cardinal directions NESW  are represented by '^' '>' 'v' '<', respectively
- destination is represented by '.'

Example:

input.txt:				&nbsp;output.txt

4						&nbsp;&nbsp;ovvo

2						&nbsp;&nbsp;vvvv

0,0						&nbsp;&nbsp;>>.<

3,0						&nbsp;&nbsp;>>^<

2,2
