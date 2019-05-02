import json
from datetime import datetime
from .constants import *
import requests

class TraxionHLF:
    """
    TraxionHLF core
    """
    username = ''
    password = ''

    def __init__(self, username, password):
        """
        :param username:
        :param password:
        """
        self.username = username
        self.password = password

    def format_date(self, transaction_date):
        return datetime.strftime(transaction_date, "%B %e. %Y %H:%M:%S")

    def create_transaction(self, customer_ref_id, customer_name,\
                           transaction, transaction_date, product):
        """
        :param customer_ref_id:
        :param customer_name:
        :param transaction:
        :param transaction_date: April 22. 2019 10:22:59 23.34
        :param kwargs: for the fields
        :return transaction_id txid
        """
        datum = {
            "channel": "default",
            "chaincode": "customer_transactions",
            "method": "createTransaction",
            "args": ["""{{\"customer_ref_ID\":\"{}\",\"customer_name\":\"{}\",\"transaction\":\"{}\",\"transactionDate\":\"{}\",\"field1\":\"{}\",\"field2\":\"b1\",\"field3\":\"c1\",\"field4\":\"d1\",\"field5\":\"e1\"}}"""
                         .format(customer_ref_id, customer_name, transaction, self.format_date(transaction_date), product)],
            "chaincodeVer": "v1"
        }
        url = BASE_URL + "invocation"
        return self.transact(url, datum)

    def get_transactions(self, **kwargs):
        """
        :param kwargs:
        :return:
        """
        if len([item for item in kwargs.items()]) > 1:
            return 'Error, please add just 1 kwargs'
        arg = [item for item in kwargs.items()][0]

        datum = {
            "channel": "default",
            "chaincode": "customer_transactions",
            "method": "queryTransactions",
            "args":["""{{\"selector\":{{\"{}\":\"{}\"}}}}""".format(arg[0], arg[1])],
            "chaincodeVer": "v1"
        }
        import pdb
        pdb.set_trace()
        url = BASE_URL + "query"
        return self.transact(url, datum)


    def transact(self, url, datum):
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, auth=(self.username, self.password), data=json.dumps(datum), headers=headers)

        if response.status_code == 200:
            return json.loads(response.content)
        else:
            return response.content




if __name__ == "__main__":
    hlf = TraxionHLF("asset@traxiontech.net", "Bl4ckh0l3@123001")
    # transaction = hlf.create_transaction("ABC1203", "NCCC", "10.00", datetime.now(), "KaPartner")

    query = hlf.get_transactions(customer_ref_ID='ABC1203')
    print(query)
    # print(transaction)