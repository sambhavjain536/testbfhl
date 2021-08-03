# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 10:24:06 2021

@author: admin
"""

from flask import Flask, render_template, request
import re
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/bfhl", methods=['POST'])
def operate():
    if request.method == "POST":
        #take inputs
        name = request.form["name"]
        dob = request.form["DOB"]
        arr = request.form["array"] 
        
        arr = re.sub(" +", " ", arr)
        arr = arr.split(" ")
        
        dob = dob.replace("-","")
        
        user_id = str(name + "_" + dob)
        result=[]
        even=[]
        odd = []
        
        for i in arr:
            if i.isdigit() and "." not in i:
                result.append(int(i))
                status="sucess"
            else:
                status="Failure"
                break
        if status == "sucess":
            for i in result:
                if i % 2 == 0:
                    even.append(i)
                else:
                    odd.append(i)
                    
            return render_template("home.html", User_id = user_id, Even=even, Odd=odd, Status=status)
        else:
            return render_template("home.html", Status=status)
    return render_template("home.html")
            
if __name__ == "__main__":
    app.run(debug=True)
