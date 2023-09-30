# Files:
- search.py: contains DFS, BFS, uniform-cost search, and AStar search algorithms.
- searchAgents.py: generates the corners heuristic and solves the corners problem.

# Running Tests:
DFS: Run the following:

```python3 -m pacai.bin.pacman --layout tinyMaze --pacman SearchAgent --agent-args fn=pacai.student.search.depthFirstSearch```

```python3 -m pacai.bin.pacman --layout mediumMaze --pacman SearchAgent --agent-args fn=pacai.student.search.depthFirstSearch```

```python3 -m pacai.bin.pacman --layout bigMaze --pacman SearchAgent --agent-args fn=pacai.student.search.depthFirstSearch```

BFS: Run the following:

```python3 -m pacai.bin.pacman --layout mediumMaze --pacman SearchAgent --agent-args fn=pacai.student.search.breadthFirstSearch```

```python3 -m pacai.bin.pacman --layout bigMaze --pacman SearchAgent --agent-args fn=pacai.student.search.breadthFirstSearch```

Uniform-cost search: Run the following:

```python3 -m pacai.bin.pacman --layout mediumMaze --pacman SearchAgent --agent-args fn=pacai.student.search.uniformCostSearch```

```python3 -m pacai.bin.pacman --layout mediumDottedMaze --pacman StayEastSearchAgent```

```python3 -m pacai.bin.pacman --layout mediumScaryMaze --pacman StayWestSearchAgent```

AStar search: Run the following:

```python3 -m pacai.bin.pacman --layout bigMaze --pacman SearchAgent --agent-args fn=pacai.student.search.aStarSearch,heuristic=pacai.core.search.heuristic.manhattan```
