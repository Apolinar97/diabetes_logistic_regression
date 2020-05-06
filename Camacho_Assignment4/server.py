#!flask/bin/python
import datetime
import joblib
import pandas as pd
from sklearn.linear_model import LogisticRegression
from flask import Flask, jsonify
from flask import request


app = Flask(__name__)
print("make file for prediction.")
@app.route('/', methods=['GET'])
def home():
    welcome_msg = f'''
    <html>
    <h1>Apolinar Camacho</h1>
    <h2> 2020-05-05 19:06:11.097462 </h2>
    <p1> Diabetes prediction web server </p1>

    </html>
    '''
    return welcome_msg


@app.route('/predict/sample', methods=['POST'])
def predict():
    if not request.json:
        return 'error'
    

    model = joblib.load('finalized_model.pkl')
    sample = {
        'pregnant':request.json['pregnant'],
         'glucose':request.json['glucose'],
         'bp':request.json['bp'],
         'insulin':request.json['insulin'],
         'bmi': request.json['bmi'] , 
         'pedigree': request.json['pedigree'], 
         'age': request.json['age']
    }

    x = [sample['pregnant'], sample['insulin'], sample['bmi'], sample['age'],sample['glucose'], sample['bp'], sample['pedigree']]
    x_input = pd.DataFrame(columns=list(sample.keys()))
    x_input.loc[0] = x

    y = model.predict(x_input)
    return jsonify(f' result: {str(y)}')    

if __name__ == '__main__':
    app.run(debug=True)
