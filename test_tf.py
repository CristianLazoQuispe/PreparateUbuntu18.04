# Creates a graph.
#import tensorflow as tf
import tensorflow.compat.v1 as tf

from tensorflow.python.client import device_lib

print("names of tensorflow gpu devices:")
print(device_lib.list_local_devices())



tf.disable_v2_behavior()
c = []
for d in ['/device:XLA_GPU:0']:#'/device:GPU:0']:
  with tf.device(d):
    a = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[2, 3])
    b = tf.constant([1.0, 2.0, 3.0, 4.0, 5.0, 6.0], shape=[3, 2])
    c.append(tf.matmul(a, b))
with tf.device('/cpu:0'):
  sum = tf.add_n(c)
# Creates a session with log_device_placement set to True.
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
# Runs the op.
print(sess.run(sum))
