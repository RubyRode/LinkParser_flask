from flask import Flask, render_template, request, make_response
import csv
import requests
from io import StringIO
from parser import parse

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/parse', methods=['POST'])
def parsing():
    link = request.form['link']
    data = parse(link)

    response = make_response(data)
    response.headers['Content-Disposition'] = 'attachment; filename=data.csv'
    response.headers['Content-type'] = 'text/csv'

    return response


if __name__ == '__main__':
    app.run()
