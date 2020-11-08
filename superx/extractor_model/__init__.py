'''
imports of sql-alchemy and flask login modules
'''
from sqlalchemy import Integer, Column, Text, Boolean, BigInteger, DECIMAL, UniqueConstraint
from flask_login import LoginManager, UserMixin
from sqlalchemy.sql import func, text
from active_alchemy import ActiveAlchemy

db = ActiveAlchemy("mysql+pymysql://Super_User:SuperX1234@mysql-13101-0.cloudclusters.net:13101/SuperX")
#pylint: disable=too-few-public-methods

class User(UserMixin, db.Model):
    '''
    User model for user table in database
    '''
    __tablename__ = 'user'

    id = Column(db.Integer, primary_key=True)
    name = Column(db.String(15))
    email = Column(db.String(50), unique=True)
    password = Column(db.String(80))
    city = Column(db.String(80))
    created_time   = Column(db.TIMESTAMP, nullable=False, server_default=func.now())
    updated_time   = Column(db.TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))

class Chain(db.Model):
    '''
    Chain model for chain table in database
    '''
    __tablename__ = 'chain'

    id = Column(BigInteger, primary_key=True)
    name = Column(Text)
    created_time   = Column(db.TIMESTAMP, nullable=False, server_default=func.now())
    updated_time   = Column(db.TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))


class Branch(db.Model):
    '''
    Branch model for branch table in database
    '''
    __tablename__ = 'branch'

    row_number = Column(Integer, primary_key=True, autoincrement=True)
    id = Column(Integer)
    name = Column(Text)
    address = Column(Text)
    city = Column(Text)
    created_time   = Column(db.TIMESTAMP, nullable=False, server_default=func.now())
    updated_time   = Column(db.TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    sub_chain_id = Column(Integer)
    chain_id = Column(db.ForeignKey('chain.id'))
    UniqueConstraint(id, chain_id)


class Product(db.Model):
    '''
    Product model for product table in database
    '''
    __tablename__ = 'product'

    id = Column(BigInteger, primary_key=True)
    created_time   = Column(db.TIMESTAMP, nullable=False, server_default=func.now())
    updated_time   = Column(db.TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    name = Column(Text)
    quantity = Column(DECIMAL)
    is_weighted = Column(Boolean)
    unit_of_measure = Column(Text)


class BranchPrice(db.Model):
    '''
    BranchPrice model for branchPrice table in database -table
    with the prices for each product from all the supermarkets
    '''
    __tablename__ = 'branch_price'

    branch_price_id = Column(Integer, primary_key=True, autoincrement=True)
    chain_id = Column(db.ForeignKey('chain.id'))
    created_time   = Column(db.TIMESTAMP, nullable=False, server_default=func.now())
    updated_time   = Column(db.TIMESTAMP, nullable=False, server_default=text('CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'))
    item_code = Column(db.ForeignKey('product.id'))
    branch_id = Column(db.ForeignKey('branch.id'))
    price = Column(DECIMAL)
    update_date = Column(Text)


class Basket(db.Model):
    '''
    Basket model for basket table in database
    '''
    __tablename__ = 'basket'

    id = Column(Integer, primary_key=True)
    cheapest_branch_id = Column(db.ForeignKey('branch.id'))
    user_id = Column(db.ForeignKey('user.id'))

    items = db.relationship('BasketProduct', primaryjoin='Basket.id == BasketProduct.basket_id')


class BasketProduct(db.Model):
    '''
    BasketProduct model for basketproducs table in database
    '''
    __tablename__ = 'basket_product'

    id = Column(Integer, primary_key=True, autoincrement=True)
    basket_id = Column(db.ForeignKey('basket.id'))
    product_id = Column(db.ForeignKey('product.id'))

    product = db.relationship('Product',
                            primaryjoin='BasketProduct.product_id == Product.id',
                            uselist=False)
    basket = db.relationship('Basket',
                    primaryjoin='BasketProduct.basket_id == Basket.id',
                            uselist=False)

db.create_all()