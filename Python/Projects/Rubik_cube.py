#You can install the rubik-cube library using pip if you haven't already:


# pip install rubik-cube
# Here's a simple Python script to scramble and solve a Rubik's Cube:

import rubik_cubesolver as rc

# Create a new Rubik's Cube and scramble it
cube = rc.RubikCube()
scramble_moves = "R U R' U'"
cube.apply_moves(scramble_moves)

# Solve the scrambled cube
solution = rc.solve(cube)

if solution is not None:
    print("Scramble moves:", scramble_moves)
    print("Solution:", solution)
else:
    print("The cube is unsolvable.")
#In this code:
"""
We import the rubik_cubesolver module.
Create a new Rubik's Cube using rc.RubikCube().
Apply scramble moves to the cube using the apply_moves method.
Use the rc.solve function to find a solution.
Print the scramble moves and the solution if one is found.

"""