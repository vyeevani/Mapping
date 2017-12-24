import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
mnist = input_data.read_data_sets("MNIST_data/", one_hot=True)

sess = tf.InteractiveSession()

guess = tf.placeholder(tf.float32, shape=[None, 784])
found = tf.placeholder(tf.float32, shape=[None, 10])

layer_one_weight = tf.Variable(tf.zeros([784, 500]))
layer_one_bias = tf.Variable(tf.zeros([500]))

layer_two_weight = tf.Variable(tf.zeros([500, 10]))
layer_two_bias = tf.Variable(tf.zeros([10]))

sess.run(tf.global_variables_initializer())

layer_one_output = tf.matmul(guess, layer_one_weight) + layer_one_bias
#layer_one_output = tf.nn.softmax(layer_one_synapse_output)
layer_two_output = tf.matmul(layer_one_output, layer_two_weight) + layer_two_bias

cross_entropy = tf.nn.softmax_cross_entropy_with_logits(labels=found, logits=layer_two_output)

train_step = tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

for _ in range(1000):
    xs, ys = mnist.train.next_batch(100)
    print(ys)
    train_step.run(feed_dict={guess:xs, found:ys})

correct_predictions = tf.equal(tf.argmax(found,1), tf.argmax(layer_two_output, 1))
accuracy = tf.reduce_mean(tf.cast(correct_predictions, tf.float32))

print(accuracy.eval(feed_dict={guess:mnist.test.images, found:mnist.test.labels}))




