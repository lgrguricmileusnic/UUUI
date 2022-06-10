from heapq import heappop, heappush, heapify, nsmallest
from typing import List
from parsers import parse_args, parse_set
from neuralnet import *

n_inputs = 0
def main():
    global n_inputs
    args = parse_args()
    train_set = []
    test_set = []
    
    with open(args.train, "r") as train_set_file, open(args.test, "r") as test_set_file:
        train_set = parse_set(train_set_file.readlines())
        test_set = parse_set(test_set_file.readlines())

    n_inputs = len(train_set[0]) - 1

    if args.nn == "5s5s":
        population = generate_population(args.popsize, [n_inputs,5,5,1])
    elif args.nn == "5s":
        population = generate_population(args.popsize, [n_inputs,5,1])
    elif args.nn == "20s":
        population = generate_population(args.popsize, [n_inputs,20,1])
    
    for i in range(args.iter):
        evaluated = evaluate_population(population, train_set)
        if (i + 1) % 2000 == 0:
            print("[Train error @{}]: ".format(i+1), nsmallest(1, evaluated)[0][0])
        new_population = [x[1] for x in nsmallest(args.elitism, evaluated)]

        while len(new_population) != args.popsize:
            parent1, parent2 = select_parents(evaluated)
            child = crossover(parent1, parent2)
            child = mutate(child, args.p, args.K)
            new_population.append(child)
        population = new_population
    
    final = evaluate_population(population, test_set)
    print("[Test error]: ", nsmallest(1, final)[0][0])


def mutate(child: ArtificalNeuralNetwork, prob: float, deviation: float):
    mutated_child = ArtificalNeuralNetwork()
    for weights in child.weight_matrices:
        nrows = len(weights)
        ncolumns = len(weights[0])
        mask = np.random.choice([1,0], (nrows, ncolumns), p=[prob, 1 - prob])
        noise = np.random.normal(0.0, deviation, (nrows, ncolumns))
        noise = np.multiply(mask, noise)
        weights = np.add(weights, noise)
        mutated_child.weight_matrices.append(weights)

    for bias in child.bias_vectors:
        nrows = len(bias)
        ncolumns = len(bias[0])
        mask = np.random.choice([1,0], (nrows, ncolumns), p=[prob, 1 - prob])
        noise = np.random.normal(0.0, deviation, (nrows, ncolumns))
        noise = np.multiply(mask, noise)
        bias = np.add(bias, noise)
        mutated_child.bias_vectors.append(bias)
    
    return mutated_child


def crossover(parent1: ArtificalNeuralNetwork, parent2: ArtificalNeuralNetwork):
    child = ArtificalNeuralNetwork()

    for weights1, weights2 in zip(parent1.weight_matrices, parent2.weight_matrices):
        child.weight_matrices.append(np.add(weights1, weights2) / 2)

    for bias1, bias2 in zip(parent1.bias_vectors, parent2.bias_vectors):
        child_bias = np.add(bias1, bias2) / 2
        child.bias_vectors.append(child_bias)

    return child

def evaluate_population(population, train_set):
    expected = [t[n_inputs] for t in train_set]
    actual = []
    evaluated = []
    heapify(evaluated)
    inputs = [x[0:n_inputs] for x in train_set]

    for ann in population:
        for in_data in inputs:
            actual.append(apply_network(in_data, ann))
        error = err(expected, actual)[0][0]
        heappush(evaluated, (error, ann))
    return evaluated
    
    

def generate_population(n: int, layerdims):
    population = []
    for _ in range(n):
        population.append(generate_ANN(layerdims))
    return population

def select_parents(evaluated: List):
    evaluated_copy = evaluated[:]
    sum = 0
    for j in evaluated:
        sum += j[0]
    point = np.random.uniform(0, sum)

    area = 0
    parent1 = None
    parent2 = None
    for j in evaluated:
        area += j[0]
        if point <= area:
            parent1 = j[1]
            evaluated_copy.remove(j)
            break
        

    sum = 0
    for j in evaluated_copy:
        sum += j[0]
    
    point = np.random.uniform(0, sum)
    area = 0

    for j in evaluated_copy:
        area += j[0]
        if point <= area:
            parent2 = j[1]
            break;

    return parent1, parent2

if __name__ == "__main__":
    main()