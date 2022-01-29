import logging
import os
import requests
import json
try:
    from pandas import json_normalize
except:
    from pandas.io.json import json_normalize


class coinmarketcap():
    """
    Class with funcitonality to retrieve data from coinmarketcap
    """
    def __init__(self) -> None:
        self.base_url = 'https://pro-api.coinmarketcap.com'
        self.endpoint = '/v1/cryptocurrency/listings/latest'
        self.access_token = '3d7ae802-0596-459f-a911-7afab3977c1a'
        self.start = '1'
        self.limit = '5000'
        self.convert = 'USD'

    def __get_coinmarket_data(self):
        logging.info(f'Requesting CoinMarketCap data')
        url = os.path.join(self.base_url, self.endpoint)
        parameters = {'start':self.start,'limit':self.limit,'convert':self.convert}
        coinmarketcap_data = self.__execute_request(url,parameters)
        json_result = json_normalize(coinmarketcap_data).to_dict(orient='records')
        return json_result

    def __execute_request(self, url_, params_ = None):
        headers = {'Accepts': 'application/json','X-CMC_PRO_API_KEY': self.access_token}
        try:
            response = requests.get(url_,headers=headers,params=params_)
            response.raise_for_status()
            data_json = json.loads(response.content)
            coinmarket_data = data_json['data']
            return coinmarket_data
        except Exception as e:
            logging.error('error executing CoinMarketCap request. exception: {}.'.format(e))
    
    def get_response_data(self):
        records = self.__get_coinmarket_data
        return records