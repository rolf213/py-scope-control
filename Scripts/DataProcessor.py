import RawData as rd
import FeatureVector as fv
import math

class DataProcessor:

	def __init__(self, referenceNodeIndex, rotationNodeIndexes, normalizationNodeIndexes):
		self.referenceNodeIndex = referenceNodeIndex
		self.rotationNodeIndexes = rotationNodeIndexes
		self.normalizationNodeIndexes = normalizationNodeIndexes
		
	def calculateFeatureVector(self, rawData):
		featureVector = fv.FeatureVector()
		if rawData.hasData == True:
			for nodeIndex in range (rawData.nodesCount):
				featureVector.nodesX.append(rawData.nodesX[nodeIndex] - rawData.nodesX[0])
				featureVector.nodesY.append(-(rawData.nodesY[nodeIndex] - rawData.nodesY[0]))
			currentOrientation = math.atan2(featureVector.nodesY[self.rotationNodeIndexes[1]] - featureVector.nodesY[self.rotationNodeIndexes[0]], featureVector.nodesX[self.rotationNodeIndexes[1]] - featureVector.nodesX[self.rotationNodeIndexes[0]])
			desiredOrientation = math.pi/2
			rotationAngle = desiredOrientation - currentOrientation
			for nodeIndex in range (rawData.nodesCount):
				x = featureVector.nodesX[nodeIndex]*math.cos(rotationAngle) - featureVector.nodesY[nodeIndex]*math.sin(rotationAngle)
				y = featureVector.nodesX[nodeIndex]*math.sin(rotationAngle) + featureVector.nodesY[nodeIndex]*math.cos(rotationAngle)
				featureVector.nodesX[nodeIndex] = x
				featureVector.nodesY[nodeIndex] = y
			normalizationDistance = 0.0
			for nodeIndex in range(len(self.normalizationNodeIndexes)-1):
				normalizationDistance = normalizationDistance + self.euclidesDistance(
				featureVector.nodesX[self.normalizationNodeIndexes[nodeIndex]], 
				featureVector.nodesY[self.normalizationNodeIndexes[nodeIndex]], 
				featureVector.nodesX[self.normalizationNodeIndexes[nodeIndex+1]], 
				featureVector.nodesY[self.normalizationNodeIndexes[nodeIndex+1]])
			for nodeIndex in range (rawData.nodesCount):
				featureVector.nodesX[nodeIndex] = featureVector.nodesX[nodeIndex]/normalizationDistance
				featureVector.nodesY[nodeIndex] = featureVector.nodesY[nodeIndex]/normalizationDistance
		return featureVector
	
	def euclidesDistance(self, x1, y1, x2, y2):
		distance = math.sqrt((x2-x1)*(x2-x1)+(y2-y1)*(y2-y1))
		return distance