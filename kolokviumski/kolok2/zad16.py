import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'

from dataset_script import dataset

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

if __name__ == '__main__':
    p = int(input())
    c = input()
    l = int(input())

    split_index = int(p/100 * len(dataset))

    X, y = [row[:-1] for row in dataset], [row[-1] for row in dataset]

    train_X, train_y = X[:split_index], y[:split_index]
    test_X, test_y = X[split_index:], y[split_index:]

    model_dt = DecisionTreeClassifier(criterion=c, max_leaf_nodes=l, random_state=0)
    model_dt.fit(train_X, train_y)

    model_rf = RandomForestClassifier(criterion=c, max_leaf_nodes=l, n_estimators=3, random_state=0)
    model_rf.fit(train_X, train_y)

    y_perch, y_roach, y_bream = [],[],[]
    for tip in y:
        if tip == 'Perch':
            y_perch.append(1)
            y_roach.append(0)
            y_bream.append(0)
        if tip == 'Roach':
            y_perch.append(0)
            y_roach.append(1)
            y_bream.append(0)
        if tip == 'Bream':
            y_perch.append(0)
            y_roach.append(0)
            y_bream.append(1)

    acc_dt = model_dt.score(test_X, test_y)

    model_perch = DecisionTreeClassifier(criterion=c, max_leaf_nodes=l, random_state=0)
    model_roach = DecisionTreeClassifier(criterion=c, max_leaf_nodes=l, random_state=0)
    model_bream = DecisionTreeClassifier(criterion=c, max_leaf_nodes=l, random_state=0)

    train_y_perch, train_y_roach, train_y_bream = y_perch[:split_index], y_roach[:split_index], y_bream[:split_index]
    test_y_perch, test_y_roach, test_y_bream = y_perch[split_index:], y_roach[split_index:], y_bream[split_index:]

    model_roach.fit(train_X, train_y_roach)
    model_bream.fit(train_X, train_y_bream)
    model_perch.fit(train_X, train_y_perch)

    pred_roach, pred_bream, pred_perch = model_roach.predict(test_X), model_bream.predict(test_X), model_perch.predict(test_X)

    actual_pred=0
    for pred_r, pred_b, pred_p, actual_r, actual_b, actual_p in zip(pred_roach, pred_bream, pred_perch, test_y_roach, test_y_bream, test_y_perch):
        if pred_r == actual_r and pred_b == actual_b and pred_p == actual_p:
            actual_pred+=1

    acc_rf = actual_pred / len(test_X)
    print(f'Tochnost so originalniot klasifikator: {acc_dt}')
    print(f'Tochnost so kolekcija od klasifikatori: {acc_rf}')


