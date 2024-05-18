import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset
from sklearn.naive_bayes import GaussianNB
from math import floor
# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [['1', '35', '12', '5', '1', '100', '0'],
                  ['1', '29', '7', '5', '1', '96', '1'],
                  ['1', '50', '8', '1', '3', '132', '0'],
                  ['1', '32', '11.75', '7', '3', '750', '0'],
                  ['1', '67', '9.25', '1', '1', '42', '0']]


def convert_data():
    float_data = []
    for row in dataset:
        new_row = [float(element) for element in row[:-1]]
        new_row.append(int(row[-1]))
        float_data.append(new_row)
    return float_data


if __name__ == '__main__':
    # Vashiot kod tuka
    classifier = GaussianNB()

    dataset = convert_data()

    train_dataset = dataset[:int(len(dataset) * 0.85)]
    test_dataset = dataset[int(len(dataset) * 0.85):]

    train_X = [row[:-1] for row in train_dataset]
    train_Y = [row[-1] for row in train_dataset]

    test_X = [row[:-1] for row in test_dataset]
    test_Y = [row[-1] for row in test_dataset]

    classifier.fit(train_X, train_Y)

    accuracy = 0
    for i in range(0, len(test_dataset)):
        actual = test_Y[i]
        predicted = classifier.predict([test_X[i]])[0]
        if actual == predicted:
            accuracy += 1
    accuracy = accuracy / len(test_dataset)
    print(accuracy)

    input_str = [float(element) for element in input().split(" ")]
    print(classifier.predict([input_str])[0])
    print(classifier.predict_proba([input_str]))

    # Na kraj potrebno e da napravite submit na podatochnoto mnozestvo,
    # klasifikatorot i encoderot so povik na slednite funkcii

    # submit na trenirachkoto mnozestvo
    submit_train_data(train_X, train_Y)

    # submit na testirachkoto mnozestvo
    submit_test_data(test_X, test_Y)

    # submit na klasifikatorot
    submit_classifier(classifier)

    # povtoren import na kraj / ne ja otstranuvajte ovaa linija
    from submission_script import *
