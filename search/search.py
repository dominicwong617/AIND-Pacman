# search.py
# ---------
# Licensing Information: Please do not distribute or publish solutions to this
# project. You are free to use and extend these projects for educational
# purposes. The Pacman AI projects were developed at UC Berkeley, primarily by
# John DeNero (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# For more info, see http://inst.eecs.berkeley.edu/~cs188/sp09/pacman.html

"""
In search.py, you will implement generic search algorithms which are called 
by Pacman agents (in searchAgents.py).
"""

import util
import random

class SearchProblem:
  """
  This class outlines the structure of a search problem, but doesn't implement
  any of the methods (in object-oriented terminology: an abstract class).
  
  You do not need to change anything in this class, ever.
  """
  
  def getStartState(self):
     """
     Returns the start state for the search problem 
     """
     util.raiseNotDefined()
    
  def isGoalState(self, state):
     """
       state: Search state
    
     Returns True if and only if the state is a valid goal state
     """
     util.raiseNotDefined()

  def getSuccessors(self, state):
     """
       state: Search state
     
     For a given state, this should return a list of triples, 
     (successor, action, stepCost), where 'successor' is a 
     successor to the current state, 'action' is the action
     required to get there, and 'stepCost' is the incremental 
     cost of expanding to that successor
     """
     util.raiseNotDefined()

  def getCostOfActions(self, actions):
     """
      actions: A list of actions to take
 
     This method returns the total cost of a particular sequence of actions.  The sequence must
     be composed of legal moves
     """
     util.raiseNotDefined()
           

def tinyMazeSearch(problem):
  """
  Returns a sequence of moves that solves tinyMaze.  For any other
  maze, the sequence of moves will be incorrect, so only use this for tinyMaze
  """
  from game import Directions
  s = Directions.SOUTH
  w = Directions.WEST
  return  [s,s,w,s,w,w,s,w]

# Delete multiple values from a list, given values we want to delete, and return new list. lst not modified.
def delete_by_values(lst, values):
    values_as_set = set(values)
    return [ x for x in lst if x not in values_as_set ]

def depthFirstSearch(problem):
  """
  Search the deepest nodes in the search tree first
  [2nd Edition: p 75, 3rd Edition: p 87]

  Depth-First Search (instance of Graph-Search Algorithm)
  - DFS uses LIFO queue (where most recently generated node is chosen to be expansion),
  which must be deepest unexpanded node (one deeper than its parent)
  - Proceeds to deepest levels nodes in current frontier first
  (where nodes have no successors)
  - Expand deepest level nodes, then remove them from frontier, then
  "back up" the search in reverse to the next deepest node (that still
  has unexplored successors)
  - Graph-Search version avoids repeated states and redundant paths, and is
  complete (since all nodes eventually expanded)
  
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm 
  [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].

  function GRAPH-SEARCH(problem) returns a solution, or failure
    initialize the frontier using the initial state of problem
    initialize the explored set to be empty
    loop do
      if the frontier is empty then return failure
      choose a leaf node and remove it from the frontier
      if the node contains a goal state then return corresponding solution
      add the node to explored set
      expand chosen node, adding resulting nodes to frontier
        only if not in frontier or explored set

  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:

  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """

  frontier = util.Stack()
  frontier.push((problem.getStartState(), []))
  explored = set()

  while not frontier.isEmpty():
      (move, path) = frontier.pop()
      if problem.isGoalState(move):
          return path

      explored.add(move)
      successors = problem.getSuccessors(move)
      for state, action, cost in successors:
          if state not in explored:
              frontier.push((state, path + [action]))

  return []

def breadthFirstSearch(problem):
  """
  Search the shallowest nodes in the search tree first.
  [2nd Edition: p 73, 3rd Edition: p 82]

  Breadth-First Search (instance of Graph-Search Algorithm)
  - BFS uses FIFO queue
  """

  # Note: Try using Queue or PriorityQueue data structure since DFS uses FIFO
  frontier = util.Queue()
  frontier.push((problem.getStartState(), []))
  explored = set()

  while not frontier.isEmpty():
      (move, path) = frontier.pop()
      if problem.isGoalState(move):
          return path

      explored.add(move)
      successors = problem.getSuccessors(move)
      for state, action, cost in successors:
          if state not in explored:
              frontier.push((state, path + [action]))

  return []

def uniformCostSearch(problem):
  "Search the node of least total cost first. "
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()

def nullHeuristic(state, problem=None):
  """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
  return 0

def aStarSearch(problem, heuristic=nullHeuristic):
  "Search the node that has the lowest combined cost and heuristic first."
  "*** YOUR CODE HERE ***"
  util.raiseNotDefined()
    
  
# Abbreviations
bfs = breadthFirstSearch
dfs = depthFirstSearch
astar = aStarSearch
ucs = uniformCostSearch
