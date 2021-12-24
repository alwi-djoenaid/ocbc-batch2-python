from config import db, ma
from marshmallow import fields

class Avocado(db.Model):
    __tablename__ = 'avocado'
    avgprice = db.Column(db.Real)
    totalvol = db.Column(db.Integer)
    avo_a = db.Column(db.Integer)
    avo_b = db.Column(db.Real)
    avo_c = db.Column(db.Real)
    type = db.Column(db.ForeignKey('avotype.typeid'))
    regionid = db.Column(db.ForeignKey('avoregion.regionid'))


class Type(db.Model):
    __tablename__ = 'avotype'
    typeid = db.Column(db.Integer, primary_key = True)
    type = db.Column(db.String(32))

class Region(db.Model):
    __tablename__ = 'avoregion'
    regionid = db.Column(db.Integer, primary_key = True)
    region = db.Column(db.String(32))