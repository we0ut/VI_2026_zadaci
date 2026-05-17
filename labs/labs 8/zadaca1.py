import os

from sklearn.neural_network import MLPClassifier

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [[180.0, 23.6, 25.2, 27.9, 25.4, 14.0, 'Roach'],
                  [12.2, 11.5, 12.2, 13.4, 15.6, 10.4, 'Smelt'],
                  [135.0, 20.0, 22.0, 23.5, 25.0, 15.0, 'Perch'],
                  [1600.0, 56.0, 60.0, 64.0, 15.0, 9.6, 'Pike'],
                  [120.0, 20.0, 22.0, 23.5, 26.0, 14.5, 'Perch']]

if __name__ == '__main__':
    # Vashiot kod tuka
    col_index = int(input())
    n_neurons = int(input())
    new_record = []

    vlez = input().split()
    vlez = list(map(float, vlez))
    vlez = vlez[:col_index] + vlez[col_index+1:]
    new_record.append(vlez)

    dataset_bez_col = [row[:col_index] + row[col_index+1:] for row in dataset]

    X = [row[:-1] for row in dataset_bez_col]
    y= [row[-1] for row in dataset_bez_col]

    split_index = int(0.8 * len(dataset))

    train_X, test_X = X[:split_index], X[split_index:]
    train_Y, test_Y= y[:split_index], y[split_index:]
    # train_X, test_X = [row[:-1] for row in train_set_X], [row[:-1] for row in test_set_X]
    # train_Y, test_Y  = [row[-1] for row in train_set_y], [row[-1] for row in test_set_y]

    params = {
        'hidden_layer_sizes': (n_neurons,),
        'activation': 'relu',
        'random_state': 0,
        'learning_rate_init': 0.001,
        'max_iter': 500
    }

    classifier = MLPClassifier(**params)

    classifier.fit(train_X, train_Y)
    accs = []
    # accuracy
    accuracy = classifier.score(test_X, test_Y)
    print(f'Tochnost: {accuracy}')

    # predict
    preds = classifier.predict(new_record)[0]
    print(f'Predvidena klasa: {preds}')

    # probabilities
    probas = classifier.predict_proba(new_record)[0]
    print(f'Verojatnosti: {probas}')

    # Na kraj potrebno e da napravite submit na podatochnoto mnozestvo
    # i klasifikatorot so povik na slednite funkcii

    # submit na trenirachkoto mnozestvo
    submit_train_data(train_X, train_Y)

    # submit na testirachkoto mnozestvo
    submit_test_data(test_X, test_Y)

    # submit na klasifikatorot
    submit_classifier(classifier)
