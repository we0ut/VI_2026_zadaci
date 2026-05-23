import os

os.environ['OPENBLAS_NUM_THREADS'] = '1'
from dataset_script import dataset


from sklearn.naive_bayes import GaussianNB
from sklearn.preprocessing import MinMaxScaler

if __name__ == '__main__':
    c = int(input())
    p = int(input())

    class1 = [row for row in dataset if row[-1] == 'bad']
    class0 = [row for row in dataset if row[-1] == 'good']

    X_0, y_0 = [row[:-1] for row in class0], [row[-1] for row in class0]
    for row in X_0:
        row[0] += row[10]

    X_0 = [row[:10] + row[11:] for row in X_0]

    X_1, y_1 = [row[:-1] for row in class1], [row[-1] for row in class1]
    for row in X_1:
        row[0] += row[10]

    X_1 = [row[:10] + row[11:] for row in X_1]

    model = GaussianNB()

    if c == 1:
        split_0 = int(len(X_0)*(100-p)/100 )
        split_1 = int(len(X_1)*(100-p)/100 )
        train_X = X_0[split_0:] + X_1[split_1:]
        train_y = y_0[split_0:] + y_1[split_1:]
        test_X = X_0[:split_0] + X_1[:split_1]
        test_y = y_0[:split_0] + y_1[:split_1]

    else:
        split_0 = int(p / 100 * len(X_0))
        split_1 = int(p / 100 * len(X_1))
        train_X = X_0[:split_0] + X_1[:split_1]
        train_y = y_0[:split_0] + y_1[:split_1]
        test_X = X_0[split_0:] + X_1[split_1:]
        test_y = y_0[split_0:] + y_1[split_1:]


    model.fit(train_X, train_y)
    scaler = MinMaxScaler(feature_range=(-1,1))
    scaler.fit(train_X)

    acc = model.score(test_X, test_y)

    train_X = scaler.transform(train_X)
    test_X = scaler.transform(test_X)

    model_new = GaussianNB()
    model_new.fit(train_X, train_y)

    print(f'''Tochnost so zbir na koloni: {acc}
Tochnost so zbir na koloni i skaliranje: {model_new.score(test_X, test_y)}''')








