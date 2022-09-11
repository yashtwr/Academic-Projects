#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

import matplotlib.pyplot as plt
import seaborn as sns
sns.set_style("darkgrid")

get_ipython().run_line_magic('matplotlib', 'inline')


# In[4]:


df = pd.read_csv(r'.\train_data.csv')


# In[5]:


y = pd.read_csv(r'.\train_labels.csv')
x = df

# Split the data in train_validate_test: 80:20 Train:Test
X_train_val, X_test, Y_train_val, Y_test = train_test_split(x, y, test_size=0.2, random_state=50)
# Split the data in train_validate_test: 90:10 Train:Validate
x_train, x_test, y_train, y_test = train_test_split(X_train_val, Y_train_val, test_size=0.1, random_state=50)

N = y_train.size


# In[6]:


def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def mean_squared_error(predictions, labels):
    N = labels.size
    mse = ((predictions - labels)**2).sum() / (2*N)
    
    return mse

def accuracy(predictions, labels):
    predicions_correct = predictions.max(axis=1) == labels.max(axis=1)
    accuracy = predicions_correct.mean()
    
    return accuracy


# In[13]:


# hyperparameters
learning_rate = 0.5
epochs = 100

n_input = 784
n_hidden = 10
n_output = 4
bias = [np.zeros(n_hidden), np.zeros(n_output)]
np.random.seed(10)
weights_1 = np.random.normal(scale=0.5, size=(n_input, n_hidden))   # (4, 2)
weights_2 = np.random.normal(scale=0.5, size=(n_hidden, n_output))  # (2, 3)
print("OLD weights are:")
print("Weights from input to hidden layer:", weights_1)
print("Weights from hidden to outpu layer:", weights_2)
# training the neural net
monitoring = {"mean_squared_error": [], "accuracy": []}
for epoch in range(epochs):    
    
    # feedforward
    hidden_layer_inputs = np.dot(x_train, weights_1) + bias[-2]
    hidden_layer_outputs = sigmoid(hidden_layer_inputs)

    output_layer_inputs = np.dot(hidden_layer_outputs, weights_2) + bias[-1]
    output_layer_outputs = sigmoid(output_layer_inputs)
    
    
    # monitor training process
    mse = mean_squared_error(output_layer_outputs, y_train)
    acc = accuracy(output_layer_outputs, y_train)
    
    monitoring["mean_squared_error"].append(mse)
    monitoring["accuracy"].append(acc)
    
    
    # backpropagation
    output_layer_error = output_layer_outputs - y_train
    output_layer_delta = output_layer_error * output_layer_outputs * (1 - output_layer_outputs)

    hidden_layer_error = np.dot(output_layer_delta, weights_2.T)
    hidden_layer_delta = hidden_layer_error * hidden_layer_outputs * (1 - hidden_layer_outputs)

    
    # weight updates
    weights_2_update = np.dot(hidden_layer_outputs.T, output_layer_delta) / N
    weights_1_update = np.dot(x_train.T, hidden_layer_delta) / N

    weights_2 = weights_2 - learning_rate * weights_2_update
    weights_1 = weights_1 - learning_rate * weights_1_update
    #bias updates
    bias[-1] = bias[-1] - learning_rate*output_layer_delta/N
    bias[-2] = bias[-2] - learning_rate*hidden_layer_delta/N
print("Updated weights are:")
print("Weights from input to hidden layer:", weights_1)
print("Weights from hidden to outpu layer:", weights_2)
print("bias of output layer:",bias[-1])
monitoring_df = pd.DataFrame(monitoring)
monitoring_df


# In[10]:


# feedforward
hidden_layer_inputs = np.dot(x_test, weights_1)
hidden_layer_outputs = sigmoid(hidden_layer_inputs)

output_layer_inputs = np.dot(hidden_layer_outputs, weights_2)
output_layer_outputs = sigmoid(output_layer_inputs)
outs = output_layer_outputs
outs


# In[11]:


# encode the data
for i in range(len(outs)):
    max_Val = np.max(outs[i])
    
    for j in range(len(outs[i])):
        if outs[i][j] == max_Val:
            outs[i][j] = 1
        else:
            outs[i][j] = 0
        
outs


# In[12]:


print("Actual output{} predicted out {}".format(y_test, outs))
acc = accuracy(outs, y_test)
print("Accuracy: {}".format(acc))


# In[ ]:





# In[ ]:




