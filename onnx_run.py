# qm-env ile çalışır
import json
import sys
import os
import time
import numpy as np
import cv2
import onnx
import onnxruntime
from onnx import numpy_helper
model_dir ="C:/Users/melek.turan/Desktop/AffectNet4GB/keras2onnx/Kerastoonnx"
model=model_dir+"/simple-model.onnx"

from keras.preprocessing.image import load_img
#Preprocess the image

    # img = cv2.imread("im/"+img1)
    # img = np.dot(img[...,:3], [0.299, 0.587, 0.114])
    # img = cv2.resize(img, dsize=(224, 224), interpolation=cv2.INTER_AREA)
    # img.resize((1, 224, 224, 3))
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