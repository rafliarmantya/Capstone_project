import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.models import Model

# Memuat model base MobileNetV2 tanpa lapisan klasifikasi
base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# Membekukan bobot pada model base
for layer in base_model.layers:
    layer.trainable = False

# Menambahkan lapisan baru untuk klasifikasi
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(1024, activation='relu')(x)
output = Dense(num_classes, activation='softmax')(x)

# Membuat model baru dengan lapisan baru
model = Model(inputs=base_model.input, outputs=output)

# Mengompilasi model
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Melatih model
model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_val, y_val))