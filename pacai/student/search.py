"""
In this file, you will implement generic search algorithms which are called by Pacman agents.
"""
import pacai.util.stack as s
import pacai.util.queue as q
import pacai.util.priorityQueue as pq

def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first [p 85].

    Your search algorithm needs to return a list of actions that reaches the goal.
    Make sure to implement a graph search algorithm [Fig. 3.7].

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:
    ```
    print("Start: %s" % (str(problem.startingState())))
    print("Is the start a goal?: %s" % (problem.isGoal(problem.startingState())))
    print("Start's successors: %s" % (problem.successorStates(problem.startingState())))
    ```
    """

    # *** Your Code Here ***
    to_visit = s.Stack()
    actionPath = []
    visited = set()

    to_visit.push([problem.startingState(), actionPath])

    while to_visit:
        exploring, extention = to_visit.pop()
        # check if starting state is the goal
        if (problem.isGoal(exploring)):
            return extention
        if exploring not in visited:
            visited.add(exploring)
            # add neightbors
            for n, d, w in problem.successorStates(exploring):
                newLst = list(extention)
                newLst.append(d)
                to_visit.push([n, newLst])

    raise NotImplementedError()

def breadthFirstSearch(problem):
    """
    Search the shallowest nodes in the search tree first. [p 81]
    """

    # *** Your Code Here ***
    to_visit = q.Queue()
    actionPath = []
    visited = set()

    to_visit.push([problem.startingState(), actionPath])

    while to_visit:
        exploring, extention = to_visit.pop()
        # check if starting state is the goal
        if (problem.isGoal(exploring)):
            return extention
        if exploring not in visited:
            visited.add(exploring)
            # add neightbors
            for n, d, w in problem.successorStates(exploring):
                newLst = list(extention)
                newLst.append(d)
                to_visit.push([n, newLst])

    raise NotImplementedError()

def uniformCostSearch(problem):
    """
    Search the node of least total cost first.
    """

    # *** Your Code Here ***
    to_visit = pq.PriorityQueue()
    actionPath = []
    visited = set()
    mass = 0

    to_visit.push([problem.startingState(), actionPath, mass], mass)

    while to_visit:
        exploring, extention, weight = to_visit.pop()
        # check if starting state is the goal
        if (problem.isGoal(exploring)):
            return extention
        if exploring not in visited:
            visited.add(exploring)
            # add neightbors
            for n, d, w in problem.successorStates(exploring):
                n_weight = w + weight
                newLst = list(extention)
                newLst.append(d)
                to_visit.push([n, newLst, n_weight], n_weight)

    raise NotImplementedError()

def aStarSearch(problem, heuristic):
    """
    Search the node that has the lowest combined cost and heuristic first.
    """

    # *** Your Code Here ***
    to_visit = pq.PriorityQueue()
    actionPath = []
    visited = set()
    mass = 0
    starting_h = heuristic(problem.startingState(), problem)

    to_visit.push([problem.startingState(), actionPath, mass], starting_h)

    while to_visit:
        exploring, extention, weight = to_visit.pop()
        # check if starting state is the goal
        if (problem.isGoal(exploring)):
            return extention
        if exploring not in visited:
            visited.add(exploring)
            # add neightbors
            for n, d, w in problem.successorStates(exploring):
                n_weight = w + weight
                newLst = list(extention)
                newLst.append(d)
                n_heu = heuristic(n, problem) + n_weight
                to_visit.push([n, newLst, n_weight], n_heu)

    raise NotImplementedError()
