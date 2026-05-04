import os

from sklearn.naive_bayes import GaussianNB

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset

from sklearn.metrics import accuracy_score, precision_score, recall_score

# Ova e primerok od podatochnoto mnozestvo, za treniranje/evaluacija koristete ja
# importiranata promenliva dataset
dataset_sample = [['1', '35', '12', '5', '1', '100', '0'],
                  ['1', '29', '7', '5', '1', '96', '1'],
                  ['1', '50', '8', '1', '3', '132', '0'],
                  ['1', '32', '11.75', '7', '3', '750', '0'],
                  ['1', '67', '9.25', '1', '1', '42', '0']]

if __name__ == '__main__':
    # Vashiot kod tuka

    X, y = [list(map(float, row[:-1])) for row in dataset] , [row[-1] for row in dataset]

    class0 = [row for row in dataset if row[-1] == '0']
    class1 = [row for row in dataset if row[-1] == '1']

    split0 = int(len(class0) * 0.85)
    split1 = int(len(class1) * 0.85) # 0.10

    train_set = class0[:split0] + class1[:split1]
    train_X = [[float(x) for x in row[:-1]] for row in train_set]
    train_y = [int(row[-1]) for row in train_set]

    test_set = class0[split0:] + class1[split1:]
    test_X = [[float(x) for x in row[:-1]] for row in test_set]
    test_y = [int(row[-1]) for row in test_set]

    classifier = GaussianNB()
    classifier.fit(train_X,train_y)
    acc = 0

    preds = classifier.predict(test_X)
    # for pred, gt in zip(preds, test_y):
    #     if gt == pred:
    #         acc += 1

    accuracy = accuracy_score(test_y, preds) # accuracy = acc / (len(test_set))
    # print(f"accuracy : {accuracy}")
    print(accuracy)

    new_sample = input()
    new_sample = [float(el) for el in new_sample.split()]

    predicted_class = classifier.predict([new_sample])[0]
    probabilities = classifier.predict_proba([new_sample])

    print(predicted_class)
    print(probabilities)

    # Na kraj potrebno e da napravite submit na podatochnoto mnozestvo,
    # klasifikatorot i encoderot so povik na slednite funkcii

    # submit na trenirachkoto mnozestvo
    submit_train_data(train_X, train_y)

    # submit na testirachkoto mnozestvo
    submit_test_data(test_X, test_y)

    # submit na klasifikatorot
    submit_classifier(classifier)

    # povtoren import na kraj / ne ja otstranuvajte ovaa linija

    # posle print(accuracy)
    # index_line = input().strip()
    # indices = [int(i) for i in index_line.split()]
    #
    # # Земи ги записите и вистинските класи по индекси од целото dataset
    # indexed_X = [[float(x) for x in dataset[i][:-1]] for i in indices]
    # indexed_y = [int(dataset[i][-1]) for i in indices]
    #
    # indexed_preds = classifier.predict(indexed_X)
    # indexed_accuracy = accuracy_score(indexed_y, indexed_preds)
    # print(indexed_accuracy)

