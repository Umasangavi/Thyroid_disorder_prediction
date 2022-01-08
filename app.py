from flask import Flask, render_template, request
import joblib
import numpy as np

model = joblib.load("models/model.pkl")

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
        TSH = request.form["TSH"]
        FTI = request.form["FTI"]
        TT4 = request.form["TT4"]
        T3 = request.form["T3"]
        query_hypothyroid = request.form["query_hypothyroid"]
        on_thyroxine = request.form["on_thyroxine"]
        sex = request.form["sex"]
        pregnant = request.form["pregnant"]
        psych = request.form["psych"]
        arr=np.array([[TSH, FTI ,TT4, T3,query_hypothyroid, on_thyroxine, sex, pregnant, psych]])
        prediction=model.predict(arr)
        return render_template('after.html',data=prediction)

if __name__ == '__main__':
    app.run(debug=True)