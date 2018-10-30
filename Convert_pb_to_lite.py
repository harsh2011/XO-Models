import tensorflow as tf

#Enter the model path
graph_def_file = "./GAN_X/frozen_gan_X.pb"
# input and output array
input_arrays = ["noise_input_x"]
output_arrays = ["gen_x"]


# initializing the Converter
converter = tf.contrib.lite.TFLiteConverter.from_frozen_graph(graph_def_file, input_arrays, output_arrays)

# converting the model and save it in a file
tflite_model = converter.convert()
open("./GAN_X/frozen_gan_X.tflite", "wb").write(tflite_model)
