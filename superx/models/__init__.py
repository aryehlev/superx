'''
imports of sql-alchemy and flask login modules
'''
from sqlalchemy import Integer, Column, Text, Boolean, BigInteger, DECIMAL, UniqueConstraint, ForeignKey, String
from sqlalchemy.orm import relationship
from flask_login import LoginManager, UserMixin
from database import Base
#pylint: disable=too-few-public-methods

class User(UserMixin, Base):
    '''
    User model for user table in database
    '''
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(15))
    email = Column(String(50), unique=True)
    password = Column(String(80))
    city = Column(String(80))

class Chain(Base):
    '''
    Chain model for chain table in database
    '''
    __tablename__ = 'chain'

    id = Column(BigInteger, primary_key=True)
    name = Column(Text)
    # branches = relationship("Branch", backref="chain")
    # prices = relationship("BranchPrice", backref="chain")


class Branch(Base):
    '''
    Branch model for branch table in database
    '''
    __tablename__ = 'branch'

    row_number = Column(Integer, primary_key=True, autoincrement=True)
    id = Column(Integer)
    name = Column(Text)
    address = Column(Text)
    city = Column(Text)
    sub_chain_id = Column(Integer)
    chain_id = Column(Integer, ForeignKey("chain.id"))
    UniqueConstraint(id, chain_id)
    # prices = relationship("BranchPrice", backref="branch")


class Product(Base):
    '''
    Product model for product table in database
    '''
    __tablename__ = 'product'

    id = Column(BigInteger, primary_key=True)
    name = Column(Text)
    quantity = Column(DECIMAL)
    is_weighted = Column(Boolean)
    unit_of_measure = Column(Text)
    # prices = relationship("BranchPrice", backref="product")

class BranchPrice(Base):
    '''
    BranchPrice model for branchPrice table in database -table
    with the prices for each product from all the supermarkets
    '''
    __tablename__ = 'branch_price'

    branch_price_id = Column(Integer, primary_key=True, autoincrement=True)
    chain_id = Column(BigInteger, ForeignKey('chain.id'))
    item_code = Column(BigInteger, ForeignKey('product.id'))
    branch_id = Column(Integer, ForeignKey('branch.id'))
    price = Column(DECIMAL)
    update_date = Column(Text)



