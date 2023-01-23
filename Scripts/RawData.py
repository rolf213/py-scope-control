class RawData:
	
	def __init__(self, mediaPipeResults, imageWidth, imageHeight):
		self.nodesCount = 21
		self.nodesX = list()
		self.nodesY = list()
		if mediaPipeResults.multi_hand_landmarks:
			self.hasData = True
			for nodeIndex in range (self.nodesCount):
				node = mediaPipeResults.multi_hand_landmarks[0].landmark[nodeIndex]
				self.nodesX.append(node.x*imageWidth)
				self.nodesY.append(node.y*imageHeight)
		else:
			self.hasData = False