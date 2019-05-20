import scipy.io

import csv
import random
import math
import operator
import cv2

training_data = scipy.io.loadmat("./training_dataset/cars_train_annos.mat")
test_data = scipy.io.loadmat("./training_dataset/cars_test_annos.mat")


def main(training_data, test_data):
    training_feature_vector = []  # training feature vector
    test_feature_vector = []  # test feature vector
    loadDataset(training_data, test_data, training_feature_vector, test_feature_vector)
    classifier_prediction = []  # predictions
    k = 3  # K value of k nearest neighbor
    for x in range(len(test_feature_vector)):
        neighbors = kNearestNeighbors(training_feature_vector, test_feature_vector[x], k)
        result = responseOfNeighbors(neighbors)
        classifier_prediction.append(result)
        print(classifier_prediction[0])
    return classifier_prediction[0]

