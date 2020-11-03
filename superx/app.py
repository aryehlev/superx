"""
importing modules
"""

from datetime import datetime

from flask import Flask, _app_ctx_stack
from sqlalchemy.orm import scoped_session
from flask_bootstrap import Bootstrap
import models
from database import SessionLocal, engine
from os import environ

app = Flask(__name__)



Bootstrap(app)

app.config.from_object('config.BaseConfig')
app.config['SECRET_KEY'] = 'aefguhw49t23465'
app.config['TESTING'] = False
FLASK_APP = environ.get('FLASK_APP')
FLASK_ENV = environ.get('FLASK_ENV')


models.Base.metadata.create_all(bind=engine)
app.session = scoped_session(SessionLocal, scopefunc=_app_ctx_stack.__ident_func__)


# dictionary for information extractors
supermarket_info_dictionary = {'mega': {'store_name': 'mega',
                                        'url': f'http://publishprice.mega.co.il/'
                                               f'{str(datetime.today().strftime("%Y%m%d"))}',
                                        'multiple_pages': False,
                                        'zip_link_prefix':
                                            f'http://publishprice.mega.co.il/'
                                            f'{str(datetime.today().strftime("%Y%m%d"))}/',
                                        'item_attr_name': 'Item',
                                        'price_full': 'PriceFull',
                                        'is_weighted_attr_name': 'bIsWeighted',
                                        'item_date_format': '%Y-%m-%d',
                                        'branch_url': f'http://publishprice.mega.co.il/'
                                                      f'{str(datetime.today().strftime("%Y%m%d"))}'
                                                      f'/Stores7290055700007-'
                                                      f'{str(datetime.today().strftime("%Y%m%d"))}'
                                                      f'0001.xml',
                                        'needs_web_scraping': False,
                                        'need_zip_prefix': False,
                                        'encoding': 'UTF-16',
                                        'link_attrs_name': None,
                                        'attr_path': 'SubChains/SubChain/Stores',
                                        'chain_id': 7290055700007,
                                        'attrs': {'store': 'Store',
                                                  'store_id': 'StoreId',
                                                  'store_name': 'StoreName',
                                                  'address': 'Address',
                                                  'city': 'City',
                                                  'sub_chain_id': 1}
                                        },
                               'shufersal': {'store_name': 'shufersal',
                                             'url': 'http://prices.shufersal.co.il'
                                                    '/FileObject/UpdateCategory?catID=2&storeId=0'
                                                    '&sort=Category&sortdir=ASC&page=1',
                                             'multiple_pages': True,
                                             'zip_link_prefix': None,
                                             'item_attr_name': 'Item',
                                             'price_full': 'PriceFull',
                                             'is_weighted_attr_name': 'bIsWeighted',
                                             'item_date_format': '%Y-%m-%d',
                                             'branch_url': 'http://prices.shufersal.co.il'
                                                           '/FileObject/UpdateCategory?catID=5'
                                                           '&storeId=0&page=1',
                                             'needs_web_scraping': True,
                                             'need_zip_prefix': False,
                                             'encoding': 'UTF-8',
                                             'link_attrs_name': 'Stores7290027600007',
                                             'attr_path': '{http://www.sap.com/abapxml}values'
                                                          '/STORES',
                                             'chain_id': 7290027600007,
                                             'attrs': {'store': 'STORE',
                                                       'store_id': 'STOREID',
                                                       'store_name': 'STORENAME',
                                                       'address': 'ADDRESS',
                                                       'city': 'CITY',
                                                       'sub_chain_id': 'SUBCHAINID'}
                                             },
                               'victory': {'store_name': 'victory',
                                           'url': 'http://matrixcatalog.co.il'
                                                  '/NBCompetitionRegulations.aspx',
                                           'multiple_pages': False,
                                           'zip_link_prefix': 'http://matrixcatalog.co.il/',
                                           'item_attr_name': 'Product',
                                           'price_full': 'PriceFull7290696200003',
                                           'is_weighted_attr_name': 'BisWeighted',
                                           'item_date_format': '%Y/%m/%d',
                                           'branch_url': 'http://matrixcatalog.co.il/',
                                           'needs_web_scraping': True,
                                           'need_zip_prefix': True,
                                           'encoding': 'UTF-8',
                                           'link_attrs_name': 'StoresFull7290696200003',
                                           'attr_path': 'Branches',
                                           'chain_id': 7290696200003,
                                           'attrs': {'store': 'Branch',
                                                     'store_id': 'StoreID',
                                                     'store_name': 'StoreName',
                                                     'address': 'Address',
                                                     'city': 'City',
                                                     'sub_chain_id': 1}
                                           }
                               }

# pylint: disable=wrong-import-position  disable=unused-import disable=wildcard-import disable=unused-wildcard-import
from routing import *


if __name__ == '__main__':
    app.run(debug=True)