from flask import Flask, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)

# Wczytanie modelu (musimy założyć, że model został wcześniej wytrenowany i zapisany jako 'model.pkl')
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Zakładamy, że dane wejściowe są w formacie JSON
        data = request.json
        features = np.array(data["features"]).reshape(1, -1)
        prediction = model.predict(features)
        return jsonify({"prediction": prediction[0]})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
