import tensorflow as tf
from neural_net.Firebase.Data import Data

#Initialize session
sess = tf.InteractiveSession()

#Initialize placeholders for input numpy.ndarrays and output numpy.ndarrays
guess = tf.placeholder(tf.float32, shape=[None, 3])
found = tf.placeholder(tf.float32, shape=[None, 3])

#First layer initialized to increase dimensionality
layer_one_weight = tf.Variable(tf.zeros([3, 500]))
layer_one_bias = tf.Variable(tf.zeros([500]))

#First layer calculations for output
layer_one_synapse_output = tf.matmul(guess, layer_one_weight) + layer_one_bias
layer_one_output = tf.nn.softmax(layer_one_synapse_output)

#Second layer initialized to reduce dimensionality
layer_two_weight = tf.Variable(tf.zeros([500, 3]))
layer_two_bias = tf.Variable(tf.zeros([3]))

#Initialize all the variables in the computational graph
sess.run(tf.global_variables_initializer())

#Second layer calculation for second layer output
layer_two_synapse_output = tf.matmul(layer_one_output, layer_two_weight) + layer_two_bias

#Error function for the second layer synapse output with softmax
cross_entropy = tf.nn.softmax_cross_entropy_with_logits(labels=found, logits=layer_two_synapse_output)

#Add optimizer and select minimizing function for computation graph
train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

#Start a Data object
data = Data()

#For all measurements in data run the training step
for measurements in data:
    accel, location = measurements
    train_step.run(feed_dict={guess:accel, found:location})

#Set the correct_prediction and the accuracy function and print
correct_predictions = tf.equal(tf.argmax(found, 1), tf.argmax(layer_two_synapse_output, 1))
accuracy = tf.reduce_mean(tf.cast(correct_predictions, tf.float32))
for test in data:
    print(accuracy.eval(feed_dict={guess: test[0], found: test[1]}))
