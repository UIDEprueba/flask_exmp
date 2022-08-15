import requests


def search_in_yahoo_finance(ticker:str):
    user_agent = {'User-agent': 'Mozilla/5.0'}
    url = f'https://query1.finance.yahoo.com/v1/finance/search?q={ticker}&lang=en-US&region=US&quotesCount=6&newsCount=2&listsCount=2&enableFuzzyQuery=false&quotesQueryId=tss_match_phrase_query&multiQuoteQueryId=multi_quote_single_token_query&newsQueryId=news_cie_vespa&enableCb=true&enableNavLinks=true&enableEnhancedTrivialQuery=true&enableResearchReports=true&enableCulturalAssets=true&researchReportsCount=2'
    r = requests.get(url, headers=user_agent) #Lanzar peticion HTTP (GET) Request
    return r.json() #Ver la respuesta JSON (Response)


if __name__ == '__main__':
    print(search_in_yahoo_finance('KO'))