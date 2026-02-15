dir
from flask import Flask, request, jsonify, render_template
import pickle
import json
import numpy as np

app = Flask(__name__)

# Load Models
with open("knnmodel.pkl", "rb") as f:
    knn_model = pickle.load(f)

with open("NBmodel.pkl", "rb") as f:
    nb_model = pickle.load(f)

models = {
    "knn": knn_model,
    "naive_bayes": nb_model
}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json
    model_name = data["model"]
    features = np.array(data["features"]).reshape(1, -1)

    model = models[model_name]
    prediction = model.predict(features)

    # Load correct result files
    if model_name == "knn":
        train_file = "train_results_knnmodel.json"
        test_file = "test_results_knn_model.json"
    else:
        train_file = "train_results_NBmodel.json"
        test_file = "test_results_NBmodel.json"

    with open(train_file, "r") as f:
        train_results = json.load(f)

    with open(test_file, "r") as f:
        test_results = json.load(f)

    return jsonify({
        "prediction": prediction.tolist(),
        "train_results": train_results,
        "test_results": test_results
    })

if __name__ == "__main__":
    app.run(debug=True)