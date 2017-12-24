import tensorflow as tf
from neural_net.Firebase.Data import Data

#TODO: add neural net framework
guess = tf.placeholder(tf.float32, shape=[None, 3])
found = tf.placeholder(tf.float32, shape=[None, 3])

layer_one_weight = tf.Variable(tf.zeros([3, 500]))
layer_one_bias = tf.Variable(tf.zeros([500]))

layer_one_synapse_output = tf.matmul(guess, layer_one_weight) + layer_one_bias
layer_one_output = tf.nn.softmax(layer_one_synapse_output)

layer_two_weight = tf.Variable(tf.zeros([500, 3]))
layer_two_bias = tf.Variable(tf.zeros([3]))

layer_two_synapse_output = tf.matmul(layer_one_output, layer_two_weight) + layer_two_bias

cross_entropy = tf.nn.softmax_cross_entropy_with_logits(labels=found, logits=layer_two_synapse_output)

train_step = tf.train.AdamOptimizer().minimize(cross_entropy)

#TODO: add imports for neural net

#TODO: add neural net input

#TODO: add hyperparameters for neural net

#TODO: add output and error functions for neural net