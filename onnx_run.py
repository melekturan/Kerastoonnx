# qm-env ile çalışır
import json
import sys
import os
import time
import numpy as np
import onnx
import onnxruntime
from keras.preprocessing.image import load_img
from onnx import numpy_helper
model_dir ="C:/Users/melek.turan/Desktop/AffectNet4GB/keras2onnx/Kerastoonnx"
model=model_dir+"/simple-model.onnx"


for i in os.listdir('im/'):
    image = load_img("im/" + i, target_size=(224, 224))
    img = np.array(image)
    img = img / 255.0
    img = img.reshape(1, 224, 224, 3)

    data = json.dumps({'data': img.tolist()})
    data = np.array(json.loads(data)['data']).astype('float32')
    session = onnxruntime.InferenceSession(model, None)
    input_name = session.get_inputs()[0].name
    output_name = session.get_outputs()[0].name


    result = session.run([output_name], {input_name: data})
    prediction=int(np.argmax(np.array(result).squeeze(), axis=0))
    print(prediction)