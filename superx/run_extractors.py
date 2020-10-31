from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from information_extractors.branch_info_extractor import BranchExtractor
from information_extractors.ssitem_info_extractor import InfoExtractor

engine = create_engine('mysql+pymysql://Super_User:SuperX1234'
                       '@mysql-13101-0.cloudclusters.net:13101/SuperX',
                       echo=False)
session = Session(bind=engine)
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

run_extractors()


def run_extractors():
    item_info_extractor = InfoExtractor()
    branch_info_extractor = BranchExtractor()

    item_info_extractor.run_info_extractor()
    branch_info_extractor.run_branch_extractor()

