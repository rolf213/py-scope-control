import os
import pickle

import RawData as rd
import FeatureVector as fv
import DataProcessor as dp

class HandshapeRecognizer:

	def __init__(self, modelFolder):
		self.templates = []
		self.labels = []
		for path in os.listdir(modelFolder):
			with open(modelFolder+"/"+path, "rb") as infile:
				model = pickle.load(infile)
				self.templates.append(model)
				self.labels.append(path)
		print(self.templates)
		print(self.labels)
		self.dataProcessor = dp.DataProcessor(0, [0, 9], [0, 9, 10, 11, 12])
		for index, rawData in enumerate(self.templates):
			featureVector = self.dataProcessor.calculateFeatureVector(rawData)
			self.templates[index] = featureVector
		print(self.templates)
		print(self.labels)
		
	def run(self, mpResult, imageWidth, imageHeight):
		unknownRawData = rd.RawData(mpResult, imageWidth, imageHeight)
		unknownFeatureVector = self.dataProcessor.calculateFeatureVector(unknownRawData)
		for index, templateFeatureVector in enumerate(self.templates):
			if unknownFeatureVector == templateFeatureVector:
				return self.labels[index]
		return ""