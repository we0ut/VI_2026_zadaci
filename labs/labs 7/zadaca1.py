import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from submission_script import *
from dataset_script import dataset
from sklearn.preprocessing import OrdinalEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier

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
    criterion = input()

    X, y = [row[:-1] for row in dataset], [row[-1] for row in dataset]

    encoder = OrdinalEncoder()
    encoder.fit(X)

    # split_index = int(len(dataset) * (100-Xinput) / 100)
    train_X, test_X = X[int(len(dataset)*(100-Xinput)/100):], X[:int(len(dataset)*(100-Xinput)/100)]
    train_Y, test_Y = y[int(len(dataset)*(100-Xinput)/100):], y[:int(len(dataset)*(100-Xinput)/100)]

    train_X_enc = encoder.transform(train_X)
    test_X_enc = encoder.transform(test_X)

    params_1 = {
        'criterion': criterion,
        'random_state': 0
    }

    classifier = DecisionTreeClassifier(**params_1)

    classifier.fit(train_X_enc, train_Y)

    # Depth
    print(f"Depth: {classifier.get_depth()}")

    # Number of leaves
    print(f"Number of leaves: {classifier.get_n_leaves()}")

    # Accuracy
    preds = classifier.predict(test_X_enc)
    print(f"Accuracy: {accuracy_score(preds, test_Y)}")

    # Most important feature
    feature_imps = classifier.feature_importances_.tolist()
    most_important_feature_index = feature_imps.index(max(feature_imps))
    print(f"Most important feature: {most_important_feature_index}")

    # Least important feature
    least_important_feat_index = feature_imps.index(min(feature_imps))
    print(f"Least important feature: {least_important_feat_index}")


    # Na kraj potrebno e da napravite submit na podatochnoto mnozestvo,
    # klasifikatorot i encoderot so povik na slednite funkcii

    # submit na trenirachkoto mnozestvo
    submit_train_data(train_X_enc, train_Y)

    # submit na testirachkoto mnozestvo
    submit_test_data(test_X_enc, test_Y)

    # submit na klasifikatorot
    submit_classifier(classifier)

    # submit na encoderot
    submit_encoder(encoder)
