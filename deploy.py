from flask import Flask, render_template, request
import pickle
app = Flask(__name__)
# load the model
model = pickle.load(open('savedmodel2.sav', 'rb'))
#hello daddy here
@app.route('/')
def home():
    result = ''
    return render_template('index.html', **locals())

@app.route('/predict', methods=['POST', 'GET'])
def predict():
    Bath = float(request.form['Bath'])
    Balcony = float(request.form['Balcony'])
    New_Total_Sqft = float(request.form['New_Total_Sqft'])
    bhk = float(request.form['bhk'])
    #'Bath','Balcony','New_Total_Sqft','bhk','Price'
    result = model.predict([[Bath,Balcony,New_Total_Sqft,bhk]])[0]
    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.run(debug=True)