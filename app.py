from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load the trained model
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'rf_model.joblib')
model = joblib.load(MODEL_PATH)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.json
        # Expecting data: {'T': value, 'AP': value, 'RH': value, 'V': value}
        features = [
            float(data['T']),
            float(data['V']),
            float(data['AP']),
            float(data['RH'])
        ]
        
        # Predict
        prediction = model.predict([features])[0]
        
        return jsonify({
            'success': True,
            'prediction': round(prediction, 2)
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 400

if __name__ == '__main__':
    app.run(debug=True, port=5000)
