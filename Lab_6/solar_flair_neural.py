import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import OrdinalEncoder

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [['C', 'S', 'O', '1', '2', '1', '1', '2', '1', '2', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['C', 'S', 'O', '1', '3', '1', '1', '2', '1', '1', '0'],
                  ['D', 'S', 'O', '1', '3', '1', '1', '2', '1', '2', '0'],
                  ['D', 'A', 'O', '1', '3', '1', '1', '2', '1', '2', '0']]

if __name__ == '__main__':
    # Vashiot kod tuka
    percent = float(input())/100.0
    criterion = input()

    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])

    train_dataset = dataset[int(len(dataset) * percent):]
    test_dataset = dataset[:int(len(dataset) * percent)]

    train_X = [row[:-1] for row in train_dataset]
    train_Y = [row[-1] for row in train_dataset]

    test_X = [row[:-1] for row in test_dataset]
    test_Y = [row[-1] for row in test_dataset]

    train_X = encoder.transform(train_X)
    test_X = encoder.transform(test_X)



    # classifier = DecisionTreeClassifier(criterion='entropy', max_depth=5, max_leaf_nodes=20, random_state=0)
    classifier = DecisionTreeClassifier(criterion=criterion, random_state=0)
    classifier.fit(train_X, train_Y)

    print(f'Depth: {classifier.get_depth()}')
    print(f'Number of leaves: {classifier.get_n_leaves()}')

    accuracy = 0
    for i in range(0, len(test_dataset)):
        actual = test_Y[i]
        predicted = classifier.predict([test_X[i]])[0]
        if actual == predicted:
            accuracy += 1
    accuracy = accuracy / len(test_dataset)
    print(f'Accuracy: {accuracy}')

    features_importances = list(classifier.feature_importances_)
    most_important_feature = features_importances.index(max(features_importances))
    print(f'Most important feature: {most_important_feature}')

    least_important_feature = features_importances.index(min(features_importances))
    print(f'Least important feature: {least_important_feature}')

    # Na kraj potrebno e da napravite submit na podatochnoto mnozestvo,
    # klasifikatorot i encoderot so povik na slednite funkcii

    #submit na trenirachkoto mnozestvo
    submit_train_data(train_X, train_Y)

    #submit na testirachkoto mnozestvo
    submit_test_data(test_X, test_Y)

    #submit na klasifikatorot
    submit_classifier(classifier)

    #submit na encoderot
    submit_encoder(encoder)
