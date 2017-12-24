import tensorflow as tf
from neural_net.Firebase.Data import Data

#TODO: add neural net framework
sess = tf.InteractiveSession()

guess = tf.placeholder(tf.float32, shape=[None, 3])
found = tf.placeholder(tf.float32, shape=[None, 3])

layer_one_weight = tf.Variable(tf.zeros([3, 500]))
layer_one_bias = tf.Variable(tf.zeros([500]))

layer_one_synapse_output = tf.matmul(guess, layer_one_weight) + layer_one_bias
layer_one_output = tf.nn.softmax(layer_one_synapse_output)

layer_two_weight = tf.Variable(tf.zeros([500, 3]))
layer_two_bias = tf.Variable(tf.zeros([3]))

sess.run(tf.global_variables_initializer())

layer_two_synapse_output = tf.matmul(layer_one_output, layer_two_weight) + layer_two_bias

cross_entropy = tf.nn.softmax_cross_entropy_with_logits(labels=found, logits=layer_two_synapse_output)

train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

#TODO: add imports for neural net
data = Data()
for measurements in data:
    accel, location = measurements
    train_step.run(feed_dict={guess:accel, found:location})

correct_predictions = tf.equal(tf.argmax(found, 1), tf.argmax(layer_two_synapse_output, 1))
accuracy = tf.reduce_mean(tf.cast(correct_predictions, tf.float32))
for test in data:
    print(1234)
    print(accuracy.eval(feed_dict={guess: test[0], found: test[1]}))
