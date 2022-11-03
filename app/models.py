#  import the SQLAlchemy class from flask_sqlalchemy and create a new instance of it, setting it to a variable conveniently named db.
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
# Passowrd management (this is similar to bcryptjs)
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

# Create Models here
# type = db.relationship("modelname") - used to connect tables
# 
# Defining Join tables 
# "table name" = db.Table(
#   "table name",
    # db.Model.metadata
# )

#                   |       |   --> class inheritence with more than one base class
class Employee(db.Model, UserMixin): # class definition
    # Mapping attributes, here
    __tablename__ = "employees"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    employee_number = db.Column(db.Integer, nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


class Menu(db.Model):
    # items - one to many relationship with MenuItem
    __tablename__ =  "menus"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)

# relationship attributes
    items = db.relationship("MenuItem", back_populates='menu')


class MenuItem(db.Model):
    __tablename__ = "menu_items"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Float, nullable=False)
    menu_id = db.Column(db.Integer, db.ForeignKey('menus.id'),primary_key=True)
    menu_type_id = db.Column(db.Integer, db.ForeignKey('menus.id'),primary_key=True)

# relationship attributes
    # menu - many to one relationship with Menu
    menu = db.relationship("Menu", back_populates='items')
    # type - many to one relationship with MenuItemType
    type = db.relationship("MenuItemType", back_populates="name")

class MenuItemType(db.Model):
    __tablename__ = "menu_item_types"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)

# relationship attributes
    name = db.relationship("MenuItem", back_populates="type")














