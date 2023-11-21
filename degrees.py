import sys

#Note: THIS FILE WILL HAVE ERRORS AS IT IS A TEMPLATE


#Frontier
class StackStyleFrontier():
    def __init__(self):
        self.frontier = []

    #Add node to frontier
    def add(self, node):
        self.frontier.append(node)

    #Check the node for any state
    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    #Check if empty
    def empty(self):
        return len(self.frontier) == 0 

    #Remove node from Frontier
        #stack - LIFO
            #Depth-first search DEEPEST
                #Goes to deadend then backs up to last decision
        #queue
            #Breadth-first search SHALLOW
                #Looks at each decision at same time (back and forth)
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return node

class QueueStyleFrontier(StackStyleFrontier):

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]
            self.frontier = self.frontier[1:]
            return node

#Current node
class Node():
    def __init__(self, state, parent, action):
        self.state = state
        self.parent = parent
        self.action = action

#GENERAL FUNCTIONS NEEDED 
    #Intialize frontier to starting postion
def starting_pos(self):
    start = Node(state=self.start, parent=None, action=None)
    frontier = StackStyleFrontier()
    frontier.add(start)

#Explored set
def explored_nodes():
    explored = set() 

#Path cost
def path_cost():
    num_explored = 0
    
    #Repeat until solution found
def repeat_loop():
    while True:
        #if nothing left in frontier, then no path
        if frontier.empty():
            raise Exception("no solution!!")

        #Choose a node from the frontier
        node = frontier.remove()
        num_explored += 1

        #Is node the goal, is so then solution
        if node.state == goal:
            actions = []
            cells = []

            #Follow parent nodes to find solution
            while node.parent is not None:
                actions.append(node.action)
                cells.append(node.state)
                node = node.parent
            actions.reverse()
            cells.reverse()
            solution = (actions, cells)
            return
        
        #Mark node as explored
        explored.add(node.state)
        
        #Add neighbor nodes to frontier
        for action, state in self.neightbors(node.state):
            if not frontier.contains_state(state) and state not in self.explored:
                child = Node(state=state, parent=node, action=action)
                frontier.add(child)