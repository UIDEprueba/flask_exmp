from flask import Flask, Response, request
import json
from yahoo import search_in_yahoo_finance


app = Flask(__name__)


@app.route('/')
def main():
    return 'Hello raiz'


@app.route('/api/search')
def search():
    ticker = request.args.get('ticker')

    financial_info = search_in_yahoo_finance(ticker=ticker)

    return Response(json.dumps({    #dumps= toma el objeto y lo serializa, luego lo envia como respuesta
        'ticker': ticker,
        'name': financial_info['quotes'][0]['shortname'],
        'sector': financial_info['quotes'][0]['sector']
    }), status=200, mimetype='application/json')    # el estado lo define el desarrollador


@app.route('/api/current-price')
def current_price( ):
    return '<p>Hello current price</p>'


@app.route('/api/chart')
def chart():
    return '<p>Hello chart</p>'


if __name__ == '__main__':
    app.run()