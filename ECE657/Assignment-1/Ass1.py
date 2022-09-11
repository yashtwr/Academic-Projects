import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split



if __name__ == "__main__":
    # Read input data from train_data csv
    x = pd.read_csv(r'C:\Users\Yash Tiwari\Desktop\ECE657\Assignment-1\train_data.csv')

    # Read one hot encoded outputs from train_labels csv
    y = pd.read_csv(r'C:\Users\Yash Tiwari\Desktop\ECE657\Assignment-1\train_labels.csv')


    # Split the data in train_validate_test: 80:20 Train:Test
    X_train_val, X_test, Y_train_val, Y_test = train_test_split(x, y, test_size=0.2, random_state=50)

    # Split the data in train_validate_test: 90:10 Train:Validate
    x_train, x_test, y_train, y_test = train_test_split(X_train_val, Y_train_val, test_size=0.1, random_state=50)

    N = y_train.size

    # hyper-parameters initialization
    learning_rate = 0.1
    epochs = 100
    n_input = 784
    n_hidden = 10
    n_output = 4

    # Initialize b_1
    b_1 = np.zeros(n_hidden)
    b_2 = np.zeros(n_output)
    np.random.seed(10)

    # Weights initialization
    # Weights from Input layer to hidden layer
    w_1 = np.random.normal(scale=0.5, size=(n_input, n_hidden))
    # Weights from Hidden layer to Output layer
    w_2 = np.random.normal(scale=0.5, size=(n_hidden, n_output))

    print("OLD weights are:")
    print("Weights from input to hidden layer:", w_1)
    print("Weights from hidden to output layer:", w_2)
    # training the neural net
    monitoring = {"mean_squared_error": []}

# Activation function:
def sigmoid(x):
    return 1 / (1 + np.exp(-x))


def mean_squared_error(predictions, labels):
    N = labels.size
    mse = ((predictions - labels) ** 2).sum() / (2 * N)

    return mse


def accuracy(predictions, labels):
    predicions_correct = predictions.max(axis=1) == labels.max(axis=1)
    accuracy = predicions_correct.mean()

    return accuracy


for epoch in range(epochs):
# Feed-forward
    # In between Input layer and Output layer
    hidden_input = np.dot(x_train, w_1) + b_1
    hidden_output = sigmoid(hidden_input)

    # In between Hidden layer and output layer
    last_layer_inputs = np.dot(hidden_output, w_2) + b_2
    last_layer_outputs = sigmoid(last_layer_inputs)

    # monitor training process
    mse = mean_squared_error(last_layer_outputs, y_train)
    acc = accuracy(last_layer_outputs, y_train)

    monitoring["mean_squared_error"].append(mse)

# Backpropagation
    output_error = last_layer_outputs - y_train
    last_layer_delta = output_error * last_layer_outputs * (1 - last_layer_outputs)

    hidden_layer_error = np.dot(last_layer_delta, w_2.T)
    hidden_layer_delta = hidden_layer_error * hidden_output * (1 - hidden_output)

# Weight updates
    w_2_update = np.dot(hidden_output.T, last_layer_delta) / N
    w_1_update = np.dot(x_train.T, hidden_layer_delta) / N

    w_2 = w_2 - learning_rate * w_2_update
    w_1 = w_1 - learning_rate * w_1_update

# Bias updates
    b_1 = b_1 - learning_rate * hidden_layer_delta / N
    b_2 = b_2 - learning_rate * last_layer_delta / N


# Append b_1 and on weights and make a .npy file
weights_ary = np.array([[w_1], [w_2], [b_1], [b_2]])
np.save('weights.npy', weights_ary)

print("Updated weights are:")
print("Weights from input to hidden layer:", w_1)
print("Weights from hidden to outpu layer:", w_2)
print("bias of output layer:", b_2)


def encode_output():
    # encode the data
    for i in range(len(outs)):
        max_Val = np.max(outs[i])

        for j in range(len(outs[i])):
            if outs[i][j] == max_Val:
                outs[i][j] = 1
            else:
                outs[i][j] = 0
    return outs
import acc_calc



def test_mlp():
    # Load weights from trained data
    weights_arr = np.load('weights.npy', allow_pickle=True)
    # feedforward
    hidden_input = np.dot(Y_test, weights_arr[0]) + weights_arr[2]
    hidden_output = sigmoid(hidden_input)

    last_layer_inputs = np.dot(hidden_output, weights_arr[1]) + weights_arr[3]
    last_layer_outputs = sigmoid(last_layer_inputs)
    predicted_output = last_layer_outputs

    return predicted_output


# You need to fill up 'test_mlp.py' with your code. Once you train the model, you should save the weights (either in .npy or .pkl file)
# and load the weights in the test_mlp function to make prediction. The test_mlp function should return the predicted values using the test data.
#
# The file 'acc_calc.py' should not be changed and is only there for you to make sure that the format of your output is correct.
#
# You should comment out the training part in 'test_mlp.py' and only use the saved weights for prediction which you obtained on training.

