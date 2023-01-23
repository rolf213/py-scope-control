import math

class FeatureVector:

	def __init__(self):
		self.nodesX = list()
		self.nodesY = list()
		self.epsilon = 0.25
		
	def __eq__(self, x):
		if len(self.nodesX) == 0:
			return False
		if len(self.nodesX) != len(x.nodesX):
			return False
		for index in range(len(self.nodesX)):
			if math.sqrt((self.nodesX[index]-x.nodesX[index])*(self.nodesX[index]-x.nodesX[index])+(self.nodesY[index]-x.nodesY[index])*(self.nodesY[index]-x.nodesY[index])) > self.epsilon:
				return False
		return True