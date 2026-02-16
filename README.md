<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
   
</head>

<body>

<h1>🌸 Iris Flower Prediction System</h1>
<p style="text-align:center;">
    Machine Learning Web Application using Python & Flask
</p>

<hr>

<h2>📌 Project Overview</h2>
<p>
The <strong>Iris Flower Prediction System</strong> is a machine learning–based web application
that predicts the species of an Iris flower using four measurements:
</p>

<ul>
    <li>Sepal Length</li>
    <li>Sepal Width</li>
    <li>Petal Length</li>
    <li>Petal Width</li>
</ul>

<p>
Users can enter values, select a model, and view predictions along with
performance metrics such as accuracy, confusion matrix, and classification report.
</p>

<hr>

<h2>📊 Dataset</h2>
<p>
This project uses the well-known <strong>Iris Dataset</strong>.
</p>

<table>
    <tr>
        <th>Feature</th>
        <th>Description</th>
    </tr>
    <tr>
        <td>SepalLengthCm</td>
        <td>Sepal length in centimeters</td>
    </tr>
    <tr>
        <td>SepalWidthCm</td>
        <td>Sepal width in centimeters</td>
    </tr>
    <tr>
        <td>PetalLengthCm</td>
        <td>Petal length in centimeters</td>
    </tr>
    <tr>
        <td>PetalWidthCm</td>
        <td>Petal width in centimeters</td>
    </tr>
</table>

<p><strong>Target Classes:</strong></p>
<ul>
    <li>Iris Setosa</li>
    <li>Iris Versicolor</li>
    <li>Iris Virginica</li>
</ul>

<div class="note">
    Total Samples: 150 <br>
    Features: 4 <br>
    Classes: 3 (Balanced Dataset)
</div>

<hr>

<h2>📁 Project Structure</h2>
<pre>
├── app.py
├── train.py
├── models/
│   ├── knn.pkl
│   └── NB.pkl
├── performance/
│   ├── performance_k.json
│   └── performance_n.json
├── templates/
│   └── index.html
├── static/
│   └── css / images
├── requirements.txt
└── Procfile
</pre>

<hr>

<h2>🛠 Technology Stack</h2>
<ul>
    <li><strong>Language:</strong> Python 3</li>
    <li><strong>ML Libraries:</strong> Scikit-learn, Pandas, NumPy</li>
    <li><strong>Web Framework:</strong> :contentReference[oaicite:0]{index=0}</li>
    <li><strong>Frontend:</strong> HTML, CSS, Jinja2</li>
    <li><strong>Model Storage:</strong> Pickle (.pkl)</li>
    <li><strong>Deployment:</strong> :contentReference[oaicite:1]{index=1}</li>
    <li><strong>Version Control:</strong> :contentReference[oaicite:2]{index=2}</li>
</ul>

<hr>

<h2>⚙️ How It Works</h2>
<ol>
    <li>Load and preprocess the Iris dataset.</li>
    <li>Split data into training and testing sets.</li>
    <li>Train ML models (KNN and Naive Bayes).</li>
    <li>Evaluate models using accuracy and reports.</li>
    <li>Save models and metrics.</li>
    <li>Use Flask to serve predictions via a web interface.</li>
</ol>

<hr>

<h2>🤖 Models Used</h2>
<ul>
    <li><strong>K-Nearest Neighbors (KNN)</strong></li>
    <li><strong>Gaussian Naive Bayes</strong></li>
</ul>

<p>
Users can switch between models and compare performance directly in the UI.
</p>

<hr>

<h2>🚀 Run Locally</h2>
<pre>
pip install -r requirements.txt
python app.py
</pre>

<p>
Open your browser and visit:
</p>
<pre>
http://127.0.0.1:5000/
</pre>

<hr>

<h2>📈 Results</h2>
<ul>
    <li>Accurate Iris species prediction</li>
    <li>Train and test accuracy displayed</li>
    <li>Confusion matrix and classification report shown</li>
    <li>Easy model comparison</li>
</ul>

<hr>

<h2>🔮 Future Enhancements</h2>
<ul>
    <li>Add more ML models (SVM, Random Forest)</li>
    <li>Include charts and visual analytics</li>
    <li>Probability-based predictions</li>
    <li>User authentication and database support</li>
    <li>Mobile-friendly UI</li>
</ul>

<hr>

<h2>✅ Conclusion</h2>
<p>
This project showcases the full machine learning pipeline,
from data preprocessing to model deployment as a web application.
It is ideal for beginners learning ML with Flask.
</p>

<hr>

<div class="footer">
    <p>
        <strong>Project By:</strong> G. Krishna<br>
        <strong>Last Updated:</strong> 14-02-2026
    </p>
</div>

</body>
</html>
