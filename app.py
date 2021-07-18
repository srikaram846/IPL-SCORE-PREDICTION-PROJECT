
import gzip, pickle
import numpy as np
import pandas as pd
from flask import Flask,request,render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('.\model\model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('main.html')

@app.route('/predict',methods=['POST'])
def predict():
    input_features = [float(x) for x in request.form.values()]
    features_value = [np.array(input_features)]
    
    features_name = ['Age', 'Gender', 'Total_Bilirubin', 'Direct_Bilirubin',
       'Alkaline_Phosphotase', 'Alamine_Aminotransferase',
       'Aspartate_Aminotransferase', 'Total_Protiens', 'Albumin',
       'Albumin_and_Globulin_Ratio']
    
    df = pd.DataFrame(features_value, columns=features_name)
    output = model.predict(df)
    print(output)
    
    if input_features[2]>=5.2 and input_features[3]>=5.2:
        res_val = "has liver disease"
    else:
        res_val = "has not liver disease"

    return render_template('main.html', prediction_text='Patient {}'.format(res_val))

if __name__ == "__main__":
    app.run(debug=True)
    
