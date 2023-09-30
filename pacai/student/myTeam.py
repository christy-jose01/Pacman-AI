from pacai.core.directions import Directions
from pacai.agents.capture.reflex import ReflexCaptureAgent
import random
from pacai.agents.base import BaseAgent
from pacai.agents.search.multiagent import MultiAgentSearchAgent
from pacai.core import actions
from pacai.core import distance
from pacai.agents.capture.capture import CaptureAgent
from pacai.util import util

import abc

# from pacai.agents.base import BaseAgent
from pacai.core import distanceCalculator
# from pacai.util import util

def createTeam(firstIndex, secondIndex, isRed,
        first = ReflexCaptureAgent,
        second = ReflexCaptureAgent):

    """
    This function should return a list of two agents that will form the capture team,
    initialized using firstIndex and secondIndex as their agent indexed.
    isRed is True if the red team is being created,
    and will be False if the blue team is being created.
    """

    firstAgent = OffensiveReflexAgent
    secondAgent = DefensiveReflexAgent

    return [
        firstAgent(firstIndex),
        secondAgent(secondIndex),
    ]

# class ReflexAgent(BaseAgent):
#     def __init__(self, index, **kwargs):
#         super().__init__(index, **kwargs)
    
#     def getFeatures(self, gameState, action):
#         features = {}
#         successor = self.getSuccessor(gameState, action)
#         features['successorScore'] = self.getScore(successor)

#         # Compute distance to the nearest food.
#         foodList = self.getFood(successor).asList()

#         # This should always be True, but better safe than sorry.
#         if (len(foodList) > 0):
#             myPos = successor.getAgentState(self.index).getPosition()
#             minDistance = min([self.getMazeDistance(myPos, food) for food in foodList])
#             features['distanceToFood'] = minDistance

#         return features
    
#     def getWeights(self, gameState, action):
#         return {
#             'successorScore': 100,
#             'distanceToFood': -1
#         }
    
#     def evaluate(self, gameState, action): 
#         SuccScore = getFeatures(gameState, action)['succesorScore']
#         SuccWeight = getWeights(gameState, action)['succesorScore']
#         return SuccScore * SuccWeight
    


class OffensiveReflexAgent(ReflexCaptureAgent):
    def __init__(self, index, **kwargs):
        super().__init__(index)

    def getFeatures(self, gameState, action):
        features = {}
        successor = self.getSuccessor(gameState, action)
        features['successorScore'] = self.getScore(successor)

        # Compute distance to the nearest food.
        foodList = self.getFood(successor).asList()

        # This should always be True, but better safe than sorry.
        if (len(foodList) > 0):
            myPos = successor.getAgentState(self.index).getPosition()
            minDistance = min([self.getMazeDistance(myPos, food) for food in foodList])
            features['distanceToFood'] = minDistance

        enemies = [successor.getAgentState(i) for i in self.getOpponents(successor)]
        Ghosts = [a for a in enemies if a.isPacman() and a.getPosition() is not None]
        if (len(Ghosts) > 0):
            dists = [self.getMazeDistance(myPos, a.getPosition()) for a in Ghosts]
            features['GhostDistance'] = min(dists)


        return features
    
    def evaluation(self, gameState, action):
        """
        Computes a linear combination of features and feature weights.
        """

        features = self.getFeatures(gameState, action)
        weights = self.getWeights(gameState, action)
        stateEval = sum(features[feature] * weights[feature] for feature in features)

        return stateEval
    
    def chooseAction(self, gameState):
        actions = gameState.getLegalActions(self.index)
    #     OpponentIndices = [o for o in CaptureAgent.getOpponents(gameState)]
    #     OpponentStates = [gameState.getAgentState(i) for i in OpponentIndices]

        bestAction = actions[0] # This is temp
        bestEval = self.evaluation(gameState, actions[0])
        for a in actions:
            if a != Directions.STOP:
                eval = self.evaluation(gameState, a)
                if eval >= bestEval:
                    bestEval = eval
                    bestAction = a
        
        return bestAction


    def getWeights(self, gameState, action):
        return {
            'successorScore': 100,
            'distanceToFood': -1,
            'GhostDistance': 100
        }

class DefensiveReflexAgent(ReflexCaptureAgent):
    """
    A reflex agent that tries to keep its side Pacman-free.
    This is to give you an idea of what a defensive agent could be like.
    It is not the best or only way to make such an agent.
    """

    def __init__(self, index, **kwargs):
        super().__init__(index)

    def getFeatures(self, gameState, action):
        features = {}

        successor = self.getSuccessor(gameState, action)
        myState = successor.getAgentState(self.index)
        myPos = myState.getPosition()

        # Computes whether we're on defense (1) or offense (0).
        features['onDefense'] = 1
        if (myState.isPacman()):
            features['onDefense'] = 0

        # Computes distance to invaders we can see.
        enemies = [successor.getAgentState(i) for i in self.getOpponents(successor)]
        invaders = [a for a in enemies if a.isPacman() and a.getPosition() is not None]
        features['numInvaders'] = len(invaders)

        if (len(invaders) > 0):
            dists = [self.getMazeDistance(myPos, a.getPosition()) for a in invaders]
            features['invaderDistance'] = min(dists)

        if (action == Directions.STOP):
            features['stop'] = 1

        rev = Directions.REVERSE[gameState.getAgentState(self.index).getDirection()]
        if (action == rev):
            features['reverse'] = 1

        return features

    def getWeights(self, gameState, action):
        return {
            'numInvaders': -1000,
            'onDefense': 100,
            'invaderDistance': -10,
            'stop': -100,
            'reverse': -2
        }

class CaptureAgent(BaseAgent):
    """
    A base class for capture agents.
    This class has some helper methods that students may find useful.

    The recommended way of setting up a capture agent is just to extend this class
    and implement `CaptureAgent.chooseAction`.
    """

    def __init__(self, index, timeForComputing = 0.1, **kwargs):
        super().__init__(index, **kwargs)

        # Whether or not you're on the red team
        self.red = None

        # Agent objects controlling you and your teammates
        self.agentsOnTeam = None

        # Maze distance calculator
        self.distancer = None

        # A history of observations
        self.observationHistory = []

        # Time to spend each turn on computing maze distances
        self.timeForComputing = timeForComputing

    def registerInitialState(self, gameState):
        """
        This method handles the initial setup of the agent and populates useful fields,
        such as the team the agent is on and the `pacai.core.distanceCalculator.Distancer`.
        """

        self.red = gameState.isOnRedTeam(self.index)
        self.distancer = distanceCalculator.Distancer(gameState.getInitialLayout())

        self.distancer.getMazeDistances()

    def final(self, gameState):
        self.observationHistory = []

    def registerTeam(self, agentsOnTeam):
        """
        Fills the self.agentsOnTeam field with a list of the
        indices of the agents on your team.
        """

        self.agentsOnTeam = agentsOnTeam

    def getAction(self, gameState):
        """
        Calls `CaptureAgent.chooseAction` on a grid position, but continues on partial positions.
        If you subclass `CaptureAgent`, you shouldn't need to override this method.
        It takes care of appending the current state on to your observation history
        (so you have a record of the game states of the game) and will call your
        `CaptureAgent.chooseAction` method if you're in a proper state.
        """

        self.observationHistory.append(gameState)

        myState = gameState.getAgentState(self.index)
        myPos = myState.getPosition()

        if (myPos != util.nearestPoint(myPos)):
            # We're halfway from one position to the next.
            return gameState.getLegalActions(self.index)[0]
        else:
            return self.chooseAction(gameState)

    @abc.abstractmethod
    def chooseAction(self, gameState):
        """
        Override this method to make a good agent.
        It should return a legal action within the time limit
        (otherwise a random legal action will be chosen for you).
        """

        pass

    def getFood(self, gameState):
        """
        Returns the food you're meant to eat.
        This is in the form of a `pacai.core.grid.Grid`
        where `m[x][y] = True` if there is food you can eat (based on your team) in that square.
        """

        if (self.red):
            return gameState.getBlueFood()
        else:
            return gameState.getRedFood()

    def getFoodYouAreDefending(self, gameState):
        """
        Returns the food you're meant to protect (i.e., that your opponent is supposed to eat).
        This is in the form of a `pacai.core.grid.Grid`
        where `m[x][y] = True` if there is food at (x, y) that your opponent can eat.
        """

        if (self.red):
            return gameState.getRedFood()
        else:
            return gameState.getBlueFood()

    def getCapsules(self, gameState):
        if (self.red):
            return gameState.getBlueCapsules()
        else:
            return gameState.getRedCapsules()

    def getCapsulesYouAreDefending(self, gameState):
        if (self.red):
            return gameState.getRedCapsules()
        else:
            return gameState.getBlueCapsules()

    def getOpponents(self, gameState):
        """
        Returns agent indices of your opponents. This is the list of the numbers
        of the agents (e.g., red might be 1, 3, 5)
        """

        if self.red:
            return gameState.getBlueTeamIndices()
        else:
            return gameState.getRedTeamIndices()

    def getTeam(self, gameState):
        """
        Returns agent indices of your team. This is the list of the numbers
        of the agents (e.g., red might be the list of 1,3,5)
        """

        if (self.red):
            return gameState.getRedTeamIndices()
        else:
            return gameState.getBlueTeamIndices()

    def getScore(self, gameState):
        """
        Returns how much you are beating the other team by in the form of a number
        that is the difference between your score and the opponents score.
        This number is negative if you're losing.
        """

        if (self.red):
            return gameState.getScore()
        else:
            return gameState.getScore() * -1

    def getMazeDistance(self, pos1, pos2):
        """
        Returns the distance between two points using the builtin distancer.
        """

        return self.distancer.getDistance(pos1, pos2)

    def getPreviousObservation(self):
        """
        Returns the `pacai.core.gamestate.AbstractGameState` object corresponding to
        the last state this agent saw.
        That is the observed state of the game last time this agent moved,
        this may not include all of your opponent's agent locations exactly.
        """

        if (len(self.observationHistory) <= 1):
            return None

        return self.observationHistory[-2]

    def getCurrentObservation(self):
        """
        Returns the GameState object corresponding this agent's current observation
        (the observed state of the game - this may not include
        all of your opponent's agent locations exactly).

        Returns the `pacai.core.gamestate.AbstractGameState` object corresponding to
        this agent's current observation.
        That is the observed state of the game last time this agent moved,
        this may not include all of your opponent's agent locations exactly.
        """

        if (len(self.observationHistory) == 0):
            return None

        return self.observationHistory[-1]