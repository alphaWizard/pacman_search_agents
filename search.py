# search.py
# ---------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


"""
In search.py, you will implement generic search algorithms which are called by
Pacman agents (in searchAgents.py).
"""

import util

class SearchProblem:
    """
    This class outlines the structure of a search problem, but doesn't implement
    any of the methods (in object-oriented terminology: an abstract class).

    You do not need to change anything in this class, ever.
    """

    def getStartState(self):
        """
        Returns the start state for the search problem.
        """
        util.raiseNotDefined()

    def isGoalState(self, state):
        """
          state: Search state

        Returns True if and only if the state is a valid goal state.
        """
        util.raiseNotDefined()

    def getSuccessors(self, state):
        """
          state: Search state

        For a given state, this should return a list of triples, (successor,
        action, stepCost), where 'successor' is a successor to the current
        state, 'action' is the action required to get there, and 'stepCost' is
        the incremental cost of expanding to that successor.
        """
        util.raiseNotDefined()

    def getCostOfActions(self, actions):
        """
         actions: A list of actions to take

        This method returns the total cost of a particular sequence of actions.
        The sequence must be composed of legal moves.
        """
        util.raiseNotDefined()


def tinyMazeSearch(problem):
    """
    Returns a sequence of moves that solves tinyMaze.  For any other maze, the
    sequence of moves will be incorrect, so only use this for tinyMaze.
    """
    from game import Directions
    s = Directions.SOUTH
    w = Directions.WEST
    return  [s, s, w, s, w, w, s, w]


class Path(object):
    #path sequences added additionally(for pushing/queuing into fringes)
    def __init__(self, locations, directions, cost):
        self.locations = locations
        self.directions = directions
        self.cost = cost


def depthFirstSearch(problem):
    """
    Search the deepest nodes in the search tree first.

    Your search algorithm needs to return a list of actions that reaches the
    goal. Make sure to implement a graph search algorithm.

    To get started, you might want to try some of these simple commands to
    understand the search problem that is being passed in:

    print("Start:", problem.getStartState())
    print("Is the start a goal?", problem.isGoalState(problem.getStartState()))
    print("Start's successors:", problem.getSuccessors(problem.getStartState()))
    """
    path = Path([problem.getStartState()],[],0)

    # if problem.isGoalState(problem.getStartState()):
    #     return path.directions

    fringe_dfs = util.Stack()
    fringe_dfs.push(path)

    while not fringe_dfs.isEmpty():
        current_path = fringe_dfs.pop()
        current_location = current_path.locations[-1]
        if problem.isGoalState(current_location):
            return current_path.directions
        else:
            successor_list = problem.getSuccessors(current_location)
            for successor in successor_list:
                next_location = successor[0]
                next_direction = successor[1]
                cost_of_edge = successor[2]
                if next_location not in current_path.locations:
                    next_locations = current_path.locations[:]
                    next_locations.append(next_location)
                    next_directions = current_path.directions[:]
                    next_directions.append(next_direction)
                    next_total_cost =current_path.cost + cost_of_edge
                    fringe_dfs.push(Path(next_locations,next_directions,next_total_cost))
    return []                 




def breadthFirstSearch(problem):
    """Search the shallowest nodes in the search tree first."""
    path = Path([problem.getStartState()],[],0)

    # if problem.isGoalState(problem.getStartState()):
    #     return path.directions

    fringe_bfs = util.Queue()
    fringe_bfs.push(path)
    visited = [problem.getStartState()]

    while not fringe_bfs.isEmpty():
        current_path = fringe_bfs.pop()
        current_location = current_path.locations[-1]
        if problem.isGoalState(current_location):
            return current_path.directions
        else:
            successor_list = problem.getSuccessors(current_location)
            for successor in successor_list:
                next_location = successor[0]
                next_direction = successor[1]
                cost_of_edge = successor[2]
                if next_location not in visited:
                    if not problem.isGoalState(next_location):
                        visited.append(next_location)
                    next_locations = current_path.locations[:]
                    next_locations.append(next_location)
                    next_directions = current_path.directions[:]
                    next_directions.append(next_direction)
                    next_total_cost =current_path.cost + cost_of_edge
                    fringe_bfs.push(Path(next_locations,next_directions,next_total_cost))
    return [] 

def uniformCostSearch(problem):
    """Search the node of least total cost first."""
    path = Path([problem.getStartState()],[],0)

    # if problem.isGoalState(problem.getStartState()):
    #     return path.directions

    fringe_ucs = util.PriorityQueue()
    fringe_ucs.push(path,0)
    visited = [problem.getStartState()]

    while not fringe_ucs.isEmpty():
        current_path = fringe_ucs.pop()
        current_location = current_path.locations[-1]
        if problem.isGoalState(current_location):
            return current_path.directions
        else:
            successor_list = problem.getSuccessors(current_location)
            for successor in successor_list:
                next_location = successor[0]
                next_direction = successor[1]
                cost_of_edge = successor[2]
                if next_location not in visited:
                    if not problem.isGoalState(next_location):
                        visited.append(next_location)
                    next_locations = current_path.locations[:]
                    next_locations.append(next_location)
                    next_directions = current_path.directions[:]
                    next_directions.append(next_direction)
                    next_total_cost =current_path.cost + cost_of_edge
                    fringe_ucs.push(Path(next_locations,next_directions,next_total_cost),next_total_cost)
    return []

def nullHeuristic(state, problem=None):
    """
    A heuristic function estimates the cost from the current state to the nearest
    goal in the provided SearchProblem.  This heuristic is trivial.
    """
    return 0

def aStarSearch(problem, heuristic=nullHeuristic):
    """Search the node that has the lowest combined cost and heuristic first."""
    path = Path([problem.getStartState()],[],0)

    # if problem.isGoalState(problem.getStartState()):
    #     return path.directions

    fringe_as = util.PriorityQueue()
    fringe_as.push(path,heuristic(problem.getStartState(),problem))
    visited = [problem.getStartState()]

    while not fringe_as.isEmpty():
        current_path = fringe_as.pop()
        current_location = current_path.locations[-1]
        if problem.isGoalState(current_location):
            return current_path.directions
        else:
            successor_list = problem.getSuccessors(current_location)
            for successor in successor_list:
                next_location = successor[0]
                next_direction = successor[1]
                cost_of_edge = successor[2]
                if next_location not in visited:
                    if not problem.isGoalState(next_location):
                        visited.append(next_location)
                    next_locations = current_path.locations[:]
                    next_locations.append(next_location)
                    next_directions = current_path.directions[:]
                    next_directions.append(next_direction)
                    next_total_cost =current_path.cost + cost_of_edge
                    fringe_as.push(Path(next_locations,next_directions,next_total_cost),next_total_cost+heuristic(next_location,problem))
    return []


# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
