# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 11:24:26 2021

@author: prabhu
"""

import numpy as np
from flask import Flask,request,jsonify,render_template
import pickle

app=Flask(__name__,template_folder="templates")##creating the flask web app
model=pickle.load(open("model.pkl","rb"))##getting the model
 
@app.route("/")
def home():
     return render_template("index.html")
 ##getting the template
 
@app.route("/predict",methods=["POST"])
def predict():
     
     #For rendering results on html gui
     age=int(request.form["age"])
     embark=request.form["embarkedFrom"]
     parch=int(request.form["numberOf"])
     gender=request.form["gender"]
     pclass=request.form["travelledIn"]
     if(pclass=="First Class"):
         pl=1
     elif(pclass=="Second Class"):
         pl=2
     else:
         pl=3
     if gender=="Male":
         if(embark=="Southampton"):
             list=[pl,age,parch,1,0,1]
         elif(embark=="Cherbourg"):
            list=[pl,age,parch,1,0,0]
         elif(embark=="Queenstown"):
            list=[pl,age,parch,1,1,0]
     else:
         if(embark=="Southampton"):
            list=[pl,age,parch,0,0,1]
         elif(embark=="Cherbourg"):
            list=[pl,age,parch,0,0,0]
         elif(embark=="Queenstown"):
            list=[pl,age,parch,0,1,0]
            
         
     final_features=[np.array(list)]#converting into array
     prediction=model.predict(final_features)##prediction
     
     
     output=prediction[0]
     print(output)
     if output ==1:
         output="Yes you are alive" 
     else:
         output= "Sorry but you dint make it"
     return render_template('index.html', prediction_text=output)
 
if __name__ == "__main__":
    app.run(debug=True)