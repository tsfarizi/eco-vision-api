from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import matplotlib.pyplot as plt

model = load_model('best_model.h5')

img_path = 'cardboard_1.jpg'  
img = image.load_img(img_path, target_size=(224, 224))  
img_array = image.img_to_array(img) / 255.0
img_array = np.expand_dims(img_array, axis=0)  

prediksi = model.predict(img_array)
predicted_class = np.argmax(prediksi)

plt.imshow(img)
plt.title(f'Prediksi: Kelas ke-{predicted_class}')
plt.axis('off')
plt.show()
