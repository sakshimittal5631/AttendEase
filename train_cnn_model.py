from sklearn.preprocessing import LabelEncoder
from keras import layers, models
import numpy as np
import pickle

with open('data/faces_data.pkl', 'rb') as f:
    faces = pickle.load(f)

with open('data/names.pkl', 'rb') as f:
    labels = pickle.load(f)

faces = np.array(faces).reshape(-1, 50, 50, 3) / 255.0
labels = np.array(labels)

le = LabelEncoder()
labels_num = le.fit_transform(labels)

with open('data/label_encoder.pkl', 'wb') as f:
    pickle.dump(le, f)

model = models.Sequential([
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(50, 50, 3)),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dense(len(np.unique(labels_num)), activation='softmax')
])

model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
model.summary()

model.fit(faces, labels_num, epochs=20, batch_size=32, validation_split=0.2)
model.save('face_cnn_model.h5')
