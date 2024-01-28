from flask import Flask, render_template, request
import numpy as np
import pandas as pd
import os
from model import predict


app = Flask(__name__)

UPLOAD_FOLDER= 'static'
ALLOWED_EXTENSIONS=set(['jpg','png'])
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER


@app.route('/')
def start():
    return  render_template('index.html')

@app.route('/', methods=['GET','POST'])
def upload():
    if request.method=='POST':
        file_1=request.form['file_1']
        m= predict(file_1)
        if m:
            result =m
        else:
            result =""
    return render_template('index.html', inp=file_1, result=result)



if __name__ == '__main__':
    app.run(DEBUG=True)