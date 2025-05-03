from flask import Flask, request
import pickle

app = Flask(__name__)

# Load model (assuming classifier.pkl exists in the same directory)
with open('classifier.pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/')
def hello_world():
    return "<h1>Hello There!!</h1>"

@app.route('/ping', methods=['GET'])
def ping():
    return {"message": "Why are you pinging me?"}

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return "I will make predictions"

    elif request.method == 'POST':
        try:
            data = request.get_json()
            # You must process `data` into the right format for your model
            # Example: inputs = [data['feature1'], data['feature2'], ...]
            inputs = ...  # Replace with actual preprocessing
            prediction = model.predict([inputs])
            return {"prediction": prediction.tolist()}
        except Exception as e:
            return {"error": str(e)}, 400
