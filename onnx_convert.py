# import keras2onnx
# from keras.applications.resnet50 import preprocess_input
# from keras.applications.resnet50 import ResNet50
# model = ResNet50(include_top=True, weights='imagenet')
# import tensorflow as tf
# tf.config.experimental_run_functions_eagerly(True)
# mm="C:/Users/melek.turan/Desktop/AffectNet4GB/keras-onnx-master/model_saved_150_epoch.h5"
# m1="C:/Users/melek.turan/Desktop/AffectNet4GB/keras-onnx-master/model_saved_150_epoch.onnx"
# keras2onnx.convert_keras(model, name=m1, doc_string='', target_opset=None, channel_first_inputs=None)
import tensorflow as tf
from  tensorflow.keras.models import load_model

print(tf.__version__)

model = load_model("model_saved_150_epoch.h5" )

model.summary()

import keras2onnx

onnx_model= keras2onnx.convert_keras(model,name="simple-model",target_opset=9)

keras2onnx.save_model(onnx_model,"simple-model.onnx")