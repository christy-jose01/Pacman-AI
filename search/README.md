# Files:
- search.py: contains DFS, BFS, uniform-cost search, and AStar search algorithms.
- searchAgents.py: generates the corners heuristic and solves the corners problem.

# Running Tests:
DFS: Run the following:
```python3 -m pacai.bin.pacman --layout tinyMaze --pacman SearchAgent --agent-args fn=pacai.student.search.depthFirstSearch```
```python3 -m pacai.bin.pacman --layout mediumMaze --pacman SearchAgent --agent-args fn=pacai.student.search.depthFirstSearch```
```python3 -m pacai.bin.pacman --layout bigMaze --pacman SearchAgent --agent-args fn=pacai.student.search.depthFirstSearch```
