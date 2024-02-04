from flask import Flask, render_template, request
from model import summerized1, summerized2
import sys


app = Flask(__name__)

UPLOAD_FOLDER= 'static'
ALLOWED_EXTENSIONS=set(['jpg','png'])
app.config['UPLOAD_FOLDER']=UPLOAD_FOLDER

@app.route('/')
def home():  # put application's code here
    return render_template('index.html')

@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method=='POST':
       file1=request.form['file1']

      sm1=summerized1(file1)
      sm2=summerized2(file1)
      return render_template('index.html', input=file1, result1=sm1, result2=sm2)










if __name__ == '__main__':
    app.run(DEBUG=True)
