import numpy as np

class ArtificalNeuralNetwork:
    def __init__(self) -> None:
        self.weight_matrices = []
        self.bias_vectors = []

    def __repr__(self) -> str:
        return "Weight matrices: " + str(self.weight_matrices) + "\nBias vectors: " + str(self.bias_vectors)
    
    def __str__(self) -> str:
        print("Weight matrices: " + str(self.weight_matrices) + "\nBias vectors: " + str(self.bias_vectors))

def generate_ANN(layerdims):

    ann = ArtificalNeuralNetwork()
    
    for i in range(len(layerdims) - 1):
        ann.weight_matrices.append(np.random.normal(0.0, 0.1, (layerdims[i+1], layerdims[i])))
        ann.bias_vectors.append(np.random.normal(0.0, 0.1, (1, layerdims[i+1])))
    return ann

def shift_fun(vect):
    res = []
    for x in vect:
        res.append(sigmoid(x))
    return np.array(res)

def sigmoid(x):
  return 1 / (1 + np.exp(-x))

def apply_layer(input_vect, weights_matrix, bias_vect):
    return np.add(np.dot(weights_matrix, input_vect.transpose()).transpose(), bias_vect)

def apply_network(input, ann: ArtificalNeuralNetwork):
    current = np.array([input])
    l = len(ann.weight_matrices)
    for i in range(l):
        current = apply_layer(current, ann.weight_matrices[i], ann.bias_vectors[i])
        if i != l - 1:
            current = shift_fun(current)
    return current

def err(expected, actual):
    sum = 0.0
    for x, y in zip(actual, expected):
        sum += np.square(y - x)
    return np.divide(sum, len(actual))