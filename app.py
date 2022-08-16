from flask import Flask, Response, request
import json
from yahoo import search_in_yahoo_finance

app = Flask(__name__)


@app.route('/')
def main():
    return '**PROYECTO CLASE 1 - FLASK, GITHUB Y AZURE**'


@app.route('/api/search')
def search():
    ticker = request.args.get('ticker')

    financial_info = search_in_yahoo_finance(ticker=ticker)

    return Response(json.dumps({  # dumps= toma el objeto y lo serializa, luego lo envia como respuesta
        'ticker': ticker,
        'name': financial_info['quotes'][0]['shortname'],
        'long name': financial_info['quotes'][0]['longname'],
        'sector': financial_info['quotes'][0]['sector'],
        'industry': financial_info['quotes'][0]['industry']
    }), status=200, mimetype='application/json')  # el estado lo define el desarrollador


@app.route('/api/current-price')
def current_price():
    return '<p>Hello current price</p>'


@app.route('/api/chart')
def chart():
    return '<p>Hello chart</p>'


if __name__ == '__main__':
    app.run()
