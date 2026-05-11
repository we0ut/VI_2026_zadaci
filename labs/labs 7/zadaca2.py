import os

from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

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
    num_trees = int(input())
    criterion = input()
    new_sample = [float(i) for i in input().split()]

    filtered_new_sample = [new_sample[i] for i in range(len(new_sample)) if i != col_index]

    X = [[row[i] for i in range(len(row)-1) if i != col_index] for row in dataset]
    Y = [row[-1] for row in dataset]

    # split_index = int(len(X) * 0.85)
    # train_X, test_X = X[:split_index], X[split_index:]
    # train_Y, test_Y = Y[:split_index], Y[split_index:]
    train_X, test_X, train_Y, test_Y = train_test_split(X, Y, train_size=0.85, shuffle=False)

    params_1 = {
        'criterion': criterion,
        'n_estimators': num_trees,
        'random_state': 0
    }

    classifier = RandomForestClassifier(**params_1)

    classifier.fit(train_X, train_Y)

    preds = classifier.predict(test_X)
    acc = accuracy_score(preds, test_Y)
    print(f'Accuracy: {acc}')

    predicted_class = classifier.predict([filtered_new_sample])[0]
    print(predicted_class)

    probas = classifier.predict_proba([filtered_new_sample])[0]
    print(probas)
    # Na kraj potrebno e da napravite submit na podatochnoto mnozestvo
    # i klasifikatorot so povik na slednite funkcii

    # submit na trenirachkoto mnozestvo
    submit_train_data(train_X, train_Y)

    # submit na testirachkoto mnozestvo
    submit_test_data(test_X, test_Y)

    # submit na klasifikatorot
    submit_classifier(classifier)
