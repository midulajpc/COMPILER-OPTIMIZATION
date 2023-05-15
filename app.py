import os
from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/upload', methods=['POST'])
def upload():
    uploaded_file = request.files['file']
    if uploaded_file:
        uploaded_file.save(uploaded_file.filename)
        df = pd.read_csv(uploaded_file.filename)
        df.to_csv('output1.csv', index=False)
        os.system('python main.py')
        return render_template('output.html', input_file=uploaded_file.filename, output_file='output1.csv')
    else:
        return render_template('home.html')


def display_output():
    filename = 'output.txt'
    with open(filename, 'r') as file:
        content = file.read()
    return render_template('result.html', content=content)




if __name__ == '__main__':
    app.run(debug=True)
