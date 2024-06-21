import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Inisialisasi Firebase Admin SDK
cred = credentials.Certificate('path/to/your/serviceAccountKey.json')
firebase_admin.initialize_app(cred)

# Inisialisasi Firestore client
db = firestore.client()

def save_prediction_to_firestore(image_id, predicted_class, confidence):
    doc_ref = db.collection('predictions').document(image_id)
    doc_ref.set({
        'predicted_class': predicted_class,
        'confidence': confidence,
        'timestamp': firestore.SERVER_TIMESTAMP
    })

def get_recipe_from_firestore(predicted_class):
    doc_ref = db.collection('recipes').document(predicted_class)
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict()
    else:
        return None

        def process_and_save_image(image_bytes, image_id):
    # Proses gambar
    processed_image = preprocess_image(image_bytes)
    
    # Buat prediksi
    prediction = model.predict(processed_image)
    predicted_class, confidence = process_prediction(prediction)
    
    # Simpan hasil ke Firestore
    save_prediction_to_firestore(image_id, predicted_class, confidence)
    
    # Dapatkan resep berdasarkan prediksi
    recipe = get_recipe_from_firestore(predicted_class)
    
    return predicted_class, confidence, recipe

# Fungsi ini akan dipanggil dari aplikasi smartphone Anda
def handle_camera_capture(image_bytes, image_id):
    result = process_and_save_image(image_bytes, image_id)
    return result