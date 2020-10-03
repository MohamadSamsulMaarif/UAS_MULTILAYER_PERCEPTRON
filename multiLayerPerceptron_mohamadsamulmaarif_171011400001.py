import numpy as np

def sigmoid(x):
	return 1 / (1 + np.exp(-x))

class Perceptron:
	def __init__(self, inputNumber):
		self.weights = 2*np.random.random(inputNumber) - 1
		self.bias = 2*np.random.random() - 1
		self.Kp = 0.1
		self.data = 0

	def feedForward(self, inputData):
		sum = np.sum(self.weights*inputData) + self.bias
		self.data = sigmoid(sum)
		return self.data

	def train(self, point, answer, guess = ""):
		if guess != "": pass
		else: guess = self.feedForward(point)
		error = answer - guess
		self.weights += error*point*Kp
		self.bias += error*Kp

class MultiLayerPerceptron():
	#numberOfNodes is an array with each element refering to a layer
	def __init__(self, numberOfLayers, numberOfNodesPerLayer): 
		self.nodes = []

		for i in range(numberOfLayers):
			self.nodes.append([])
			for j in range(numberOfNodesPerLayer[i]):
				if (i==0):
					self.nodes[i].append(Perceptron(1))
				else:
					self.nodes[i].append(Perceptron(numberOfNodesPerLayer[i-1]))

		for i in range(numberOfLayers):
			self.nodes[i] = np.array(self.nodes[i])
		self.nodes = np.array(self.nodes)

	def feedForward(self, inputData):
		for i in range(self.nodes.size):
			for j in range(self.nodes[i].size):
				if(i==0):
					self.nodes[i][j].feedForward(inputData)
				else:
					data = []
					for w in range(self.nodes[i-1].size):
						data.append(self.nodes[i-1][w].data)
					data = np.array(data)
					self.nodes[i][j].feedForward(data)


brain = MultiLayerPerceptron(7, [64, 128, 128, 10, 10, 10, 10])
brain.feedForward([1,1])
for i in range(brain.nodes.size):
	for j in range(brain.nodes[i].size):
		print(brain.nodes[i][j].weights)
		print(brain.nodes[i][j].bias)
		print(brain.nodes[i][j].data)
		print("")