# maze-generator-solver

## Motivation:
I really like mazes. This is the main motivation behind chosing this project. My goal is to have a small modular library for maze generator algorithms and solvers.

## Description:
The project goal is to generates mazes using [maze generation algorithms](https://en.wikipedia.org/wiki/Maze_generation_algorithm) (like Depth-First Search (DFS) algorithm) and solves them using [search algorithms](https://en.wikipedia.org/wiki/Maze-solving_algorithm) (like in our case A* (A STAR), tremaux, routing search algorithms (see ./src/solvers/*)).

To introduce additional algorithms, inherit from the MazeGenerator class from base_maze_generator.py for maze generation algorithms. Likewise, for maze-solving algorithms, inherit from the BaseSolver class found in base_solver.py.

## Commands:
To run a simulation:
```
python ./src/run.py --solver solver_name
```
where solver_name:
* 'astar': for A star algorithm
* 'tremaux': for Trémaux's algorithm
* 'routing': for Maze-routing algorithm

You can edit config.py file for your personal settings.

You can use `Q` to quit the pygame window.


## Demonstration:

![MAZE GENERATOR AND SOLVER](./gen_solver.gif)

## Improvements:
- Implementing additional maze generation algorithms (e.g., Prim's, Kruskal's ...).
- A metric to compare the complexity of generated mazes.
- Enhancing the user interface for a more interactive experience.

## Contribution:
Contributions are welcome. If you have ideas for improvements.
