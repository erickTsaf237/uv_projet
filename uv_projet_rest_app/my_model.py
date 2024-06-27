#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 07:50:08 2024

@author: erick
"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    secret_key = db.Column(db.String(100), nullable=False, unique=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'secret_key': self.secret_key
        }
    
class KeyPress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False, primary_key=True)

from flask_sqlalchemy import SQLAlchemy

#db = SQLAlchemy()

class ParticipantKey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    participant = db.Column(db.String(100), nullable=False)
    session = db.Column(db.String(100), nullable=False)
    key1 = db.Column(db.String(100), nullable=False)
    key2 = db.Column(db.String(100), nullable=False)
    DU_key1_key1 = db.Column(db.Float, nullable=False)
    DD_key1_key2 = db.Column(db.Float, nullable=False)
    DU_key1_key2 = db.Column(db.Float, nullable=False)
    UD_key1_key2 = db.Column(db.Float, nullable=False)
    UU_key1_key2 = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'session': self.session,
            'key1': self.key1,
            'participant': self.participant,
            'key2': self.key2,
            'DU_key1_key1': self.DU_key1_key1,
            'DD_key1_key2': self.DD_key1_key2,
            'DU_key1_key2': self.DU_key1_key2,
            'UD_key1_key2': self.UD_key1_key2,
            'UU_key1_key2': self.UU_key1_key2
        }
    
    def getTable(self):
        return [self.DU_key1_key1, self.DD_key1_key2, self.DU_key1_key2, self.UD_key1_key2, self.UU_key1_key2]
