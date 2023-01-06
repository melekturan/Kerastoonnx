from keras.models import load_model
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
import numpy as np
import os
from keras.models import load_model

model = load_model('model_saved_150_epoch.h5')
for i in os.listdir('im/'):
    image = load_img("im/"+i, target_size=(224, 224))
    img = np.array(image)
    img = img / 255.0
    img = img.reshape(1, 224, 224, 3)
    label = model.predict(img)
    print(np.where(label[0]==max(label[0])))



