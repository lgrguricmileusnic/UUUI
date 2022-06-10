import argparse


import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--train', default="", help="path to training set", required=True)
    parser.add_argument('--test',  default="", help="path to test set", required=True)
    parser.add_argument('--nn', choices=['5s', '20s', '5s5s'], required=True)
    parser.add_argument('--popsize', required=True, type=int)
    parser.add_argument('--elitism', required=True, type=int)
    parser.add_argument('--p', required=True, type=float)
    parser.add_argument('--K', required=True, type=float)
    parser.add_argument('--iter', required=True, type=int)
    args = parser.parse_args()
    
    return args

def parse_set(lines):
    # remove header line
    lines.pop(0)
    parsed_set = []
    for line in lines:
        parsed_set.append(tuple([float(value) for value in line.split(',')]))
    return parsed_set
