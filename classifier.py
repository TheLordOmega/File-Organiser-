

#perceptrons
from tkinter.constants import X

import numpy as np
import sklearn.datasets as skl_data


#a single neuron
def perceptron (inputs, weights, threshold):
    assert len(inputs) == len(weights)

    values= np.multiply(inputs,weights)

    total= sum(values)

    if total < threshold:
        return 0
    else:
        return 1


#arrays of daya , labels for images and the image data itself
data, labels= skl_data.fetch_openml(
    'mnist_784',
    version=1,
    return_X_y=True
)

print(data.shape)
data.head()
data= data / 255.0


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data, labels, test_size=.10, random_state=42, stratify=labels)
print(X_train.shape)
print(X_test.shape)

import sklearn.neural_network as skl_nn
mlp = skl_nn.MLPClassifier(hidden_layer_sizes=(50), max_iter=50, verbose=1, random_state=1)
mlp.fit(X_train,y_train)

print("Training set score", mlp.score(X_train, y_train))
print("testing set score", mlp.score(X_test, y_test))






index=0
test_digit= X_test.iloc[index].to_numpy().reshape(1,784)
test_digit_prediction= mlp.predict(test_digit)[0]
print("Predicted value",test_digit_prediction)
print("Actual value",y_test.iloc[index])
