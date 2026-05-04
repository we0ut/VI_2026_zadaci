import os

from sklearn.metrics import accuracy_score
from sklearn.preprocessing import OrdinalEncoder
from sklearn.naive_bayes import CategoricalNB

os.environ['OPENBLAS_NUM_THREADS'] = '1'
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
    Xinput = int(input())

    encoder = OrdinalEncoder()
    encoder.fit([row[:-1] for row in dataset])

    X, y = [row[:-1] for row in dataset], [row[-1] for row in dataset]


    train_X, test_X = X[:int(Xinput * len(dataset) / 100)], X[int(Xinput * len(dataset) / 100):]
    train_y, test_y = y[:int(Xinput * len(dataset) / 100)], y[int(Xinput * len(dataset) / 100):]

    train_X_enc = encoder.transform(train_X)
    test_X_enc = encoder.transform(test_X)

    model = CategoricalNB()
    model.fit(train_X_enc, train_y)

    preds = model.predict(test_X_enc)
    accuracy = accuracy_score(test_y, preds)
    # print(f"Accuracy: {accuracy}")
    print(accuracy)

    new_sample = input()
    new_sample = new_sample.split()
    new_sample = encoder.transform([new_sample])

    predicted_class = model.predict(new_sample)[0]
    probabilities = model.predict_proba(new_sample)
    # print(f'Nov primerok: {new_sample}')
    # print(f'Predvidena klasa: {predicted_class}')
    # print(f'Verojatnosti za pripadnost vo klasite: {probabilities}')

    # print(new_sample)
    print(predicted_class)
    print(probabilities)

    # Na kraj potrebno e da napravite submit na podatochnoto mnozestvo,
    # klasifikatorot i encoderot so povik na slednite funkcii

    submit_train_data(train_X_enc, train_y)
    submit_test_data(test_X_enc, test_y)
    submit_classifier(model)
    submit_encoder(encoder)

    # submit na trenirachkoto mnozestvo
    # submit_train_data(train_X, train_Y)

    # submit na testirachkoto mnozestvo
    # submit_test_data(test_X, test_Y)

    # submit na klasifikatorot
    # submit_classifier(classifier)

    # submit na encoderot
    # submit_encoder(encoder)
