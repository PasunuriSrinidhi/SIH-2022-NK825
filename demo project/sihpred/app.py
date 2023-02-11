import numpy as np
from flask import Flask, request, jsonify, render_template
#from statsmodels.tsa.arima_model import ARIMA
# import model


import pickle
app = Flask(__name__)
import get_future_weather

@app.route('/')
def home():
    return render_template('index.html')
r={}
@app.route('/predict1',methods=['POST'])
def predict1():
    features1 = [x for x in request.form.values()]
    
    return render_template('index.html', prediction1text=str(features1))

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    features = [x for x in request.form.values()]
    


    r=get_future_weather.get_coor(float(features[0]),float(features[1]),features[2])

    # final_features = [np.array(int_features)]
    # prediction = model.predict(final_features)
    #
    # output = round(prediction[0], 2)
    so=''''''
    re=7
    ymir2=str(features[0])
    geo2=ymir2.split('.')
    king2=geo2[1]
    t2=re-len(king2)

    for j in range(t2):
        king2+='0'
    king2=geo2[0]+'.'+king2
    re3=7
    ymir3=str(features[1])

    geo3=ymir3.split('.')
    print(geo3)
    king3=geo3[1]
    t3=re-len(king3)
    for j in range(t3):
        king3+='0'
    king3=geo3[0]+'.'+king3
    so+='''Given Inputs = '''+king2+''' '''+king3+''' '''+features[2]+'''                 '''
    
    so+='''\n'''
    so+='''\n'''
    so+='''\n'''
    
    
    for i in r:
        no=''
        u=r[i]
        ymir=str(round(r[i][0],5))
        mova=str(round(r[i][1],5))
        geo=ymir.split('.')
        geo1=mova.split('.')
        king=geo[1]
        t=5-len(king)
        for j in range(t):
            king+='0'
        king=geo[0]+'.'+king
        queen = geo1[1]
        t = 5 - len(queen)

        for j in range(t):
            queen += '0'
        queen=geo1[0]+'.'+queen

        no+='day:       '+str(i)+' : '+king+','+queen+'\n'
        so+=no
    print(so)


    return render_template('index.html', prediction_text=so)

@app.route('/predict_api',methods=['POST'])
def predict_api():
    '''
    For direct API calls trought request
    '''
    data = request.get_json(force=True)
    prediction = model.predict([np.array(list(data.values()))])

    output = prediction[0]
    return jsonify(output)

if __name__ == "__main__":
    app.run(debug=True)