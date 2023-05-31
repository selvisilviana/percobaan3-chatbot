from flask import Flask, render_template, request, jsonify
import numpy as np
from tensorflow.keras.models import load_model
from flask_ngrok import run_with_ngrok
import json

def load_dataset():
    with open('dataset.json') as file:
        dataset = json.load(file)
    return dataset

def lstm_predict(input_text):
    # Lakukan transformasi pada input_text jika diperlukan
    
    # Lakukan prediksi menggunakan model LSTM dan dataset JSON
    # Misalnya, mencari tag yang sesuai dengan input_text
    tag = None
    for data in dataset:
        for pattern in data['patterns']:
            if pattern in input_text:
                tag = data['tag']
                break
    
    # Lakukan post-processing pada hasil prediksi jika diperlukan
    # Misalnya, mencari respons berdasarkan tag
    response = None
    if tag:
        for data in dataset:
            if data['tag'] == tag:
                responses = data['responses']
                response = np.random.choice(responses)
                break
    
    return response

app = Flask(__name__)
model = None

# Load model LSTM
def load_lstm_model():
    global model
    model = load_model('chatbot_model.h5')
    # Optional: Lakukan persiapan lain yang diperlukan seperti pengaturan tokenizer, dll.

# [Routing untuk Halaman Utama atau Home]	
@app.route("/")
def beranda():
    return render_template('index.html')

# [Routing untuk API]
@app.route("/api/deteksi", methods=['POST'])
def api_deteksi():
    if request.method == 'POST':
        # Ambil input dari pengguna
        input_text = request.form['input_text']
        
        # Lakukan preprocessing pada input_text jika diperlukan
        
        # Lakukan prediksi menggunakan model LSTM
        prediksi = lstm_predict(input_text)
        
        # Return hasil prediksi dengan format JSON
        return jsonify({"prediksi": prediksi})

# Prediksi menggunakan model LSTM
def lstm_predict(input_text):
    # Lakukan transformasi pada input_text jika diperlukan
    
    # Lakukan prediksi menggunakan model LSTM
    # Contoh:
    # input_data = transform_input_text(input_text)
    # prediksi = model.predict(input_data)
    
    # Lakukan post-processing pada hasil prediksi jika diperlukan
    
    return prediksi

# Main
if __name__ == '__main__':


    # Run Flask di localhost 
      run_with_ngrok(app)
      app.run()