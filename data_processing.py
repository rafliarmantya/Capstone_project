import tensorflow as tf
import numpy as np
import os
import torch
import torchvision
import cv2
import tflite_runtime.interpreter as tflite
from tensorflow import keras
from google.cloud import storage



# Inisialisasi client Cloud Storage
storage_client = storage.Client()

# Fungsi untuk mengunduh gambar dari Cloud Storage
def download_image(bucket_name, source_blob_name, destination_file_name):
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

# Fungsi untuk mengolah data gambar
def preprocess_data(data_dir):
    image_paths = []
    labels = []
    
    # Iterasi melalui direktori data
    for root, dirs, files in os.walk(data_dir):
        for file in files:
            if file.endswith('.jpg') or file.endswith('.png'):
                image_path = os.path.join(root, file)
                label = os.path.basename(root)
                image_paths.append(image_path)
                labels.append(label)
    
    # Konversi gambar menjadi array dan normalisasi
    images = []
    for image_path in image_paths:
        image = cv2.imread(image_path)
        image = cv2.resize(image, (224, 224))
        image = image / 255.0
        images.append(image)
    
    return np.array(images), np.array(labels)

# Mengunduh data dari Cloud Storage
BUCKET_NAME = 'your-bucket-name'
SOURCE_DIR = 'path/to/source/dir'
DESTINATION_DIR = 'path/to/destination/dir'

for root, dirs, files in os.walk(os.path.join(SOURCE_DIR)):
    for file in files:
        source_blob_name = os.path.join(root, file).replace('\\', '/')
        destination_file_name = os.path.join(DESTINATION_DIR, source_blob_name.replace(SOURCE_DIR, ''))
        os.makedirs(os.path.dirname(destination_file_name), exist_ok=True)
        download_image(BUCKET_NAME, source_blob_name, destination_file_name)

# Memproses data gambar
X, y = preprocess_data(DESTINATION_DIR)