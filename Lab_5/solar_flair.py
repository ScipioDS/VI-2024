import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import OrdinalEncoder
from submission_script import *
from dataset_script import dataset

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [['C', 'S', 'O', '1', '2', '1', '1', '2', '1', '2', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['C', 'S', 'O', '1', '3', '1', '1', '2', '1', '1', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['D', 'A', 'O', '1', '3', '1', '1', '2', '1', '2', '0']]

if __name__ == '__main__':
    # Vashiot kod tuka
    encoder = OrdinalEncoder()
    classifier = CategoricalNB()

    encoder.fit([row[:-1] for row in dataset])

    train_dataset = dataset[:int(len(dataset)*0.75)]
    test_dataset = dataset[int(len(dataset)*0.75):]

    train_X = [row[:-1] for row in train_dataset]
    train_Y = [row[-1] for row in train_dataset]

    test_X = [row[:-1] for row in test_dataset]
    test_Y = [row[-1] for row in test_dataset]

    train_X = encoder.transform(train_X)
    test_X = encoder.transform(test_X)

    classifier.fit(train_X, train_Y)

    accuracy = 0
    for i in range(0, len(test_dataset)):
        actual = test_Y[i]
        predicted = classifier.predict([test_X[i]])[0]
        if actual == predicted:
            accuracy += 1
    accuracy = accuracy / len(test_dataset)
    print(accuracy)

    input_str = input().split(" ")
    input_encoder = encoder.transform([input_str])
    print(classifier.predict(input_encoder)[0])
    string = str(classifier.predict_proba(input_encoder)[0]).replace("\n", "\n ")
    print(f'[{string}]')

    # Na kraj potrebno e da napravite submit na podatochnoto mnozestvo,
    # klasifikatorot i encoderot so povik na slednite funkcii

    # submit na trenirachkoto mnozestvo
    submit_train_data(train_X, train_Y)

    # submit na testirachkoto mnozestvo
    submit_test_data(test_X, test_Y)

    # submit na klasifikatorot
    submit_classifier(classifier)

    # submit na encoderot
    submit_encoder(encoder)

    # povtoren import na kraj / ne ja otstranuvajte ovaa linija
    from submission_script import *
