#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 07:49:52 2024

@author: erick
"""

from flask_restful import Resource, reqparse
from my_model import db, Application, ParticipantKey
from flask import request
from flask_restful import Resource
from sklearn.preprocessing import LabelEncoder
from model.my_isolation_forest import test_user
from model.my_local_oulier_factor import user_local_outlier_factor_test

class ApplicationResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('name', type=str, required=True)
        self.parser.add_argument('secret_key', type=str, required=True)

    def get(self, application_id=None):
        if application_id:
            application = Application.query.get(application_id)
            if application:
                return application.to_dict()
            else:
                return {'message': 'Application not found'}, 404
        else:
            applications = Application.query.all()
            print(applications)
            return [application.to_dict() for application in applications]

    def post(self):
        args = self.parser.parse_args()
        print("bonjour lr pays")
        application = Application(name=args['name'], secret_key=args['secret_key'])
        db.session.add(application)
        db.session.commit()
        return application.to_dict(), 201

    def put(self, application_id):
        args = self.parser.parse_args()
        application = Application.query.get(application_id)
        if application:
            application.name = args['name']
            application.secret_key = args['secret_key']
            db.session.commit()
            return application.to_dict()
        else:
            return {'message': 'Application not found'}, 404

    def delete(self, application_id):
        application = Application.query.get(application_id)
        if application:
            db.session.delete(application)
            db.session.commit()
            return {'message': 'Application deleted'}, 200
        else:
            return {'message': 'Application not found'}, 404
        
        
    def bonjour():
        return {'salutation': "bonjour"}
    

import numpy as np;
import matplotlib.pyplot as plt
#plt.imshow(np.random.randint(0, 255, 7*10).reshape(7, 10))
#plt.show()

class ParticipantResource(Resource):
    def post(self):
        
        """Crée de nouvelles données de participant"""
        key = request.get_json()
        #print(key)
        data = key['data']
        usrname = key['userName']
        sendedKeys = []
        if len(data)<5:
            return {'succes': data}
        print(data)
        boo = np.array(data)[:, 2:].astype(float).dot(0.001)
        la_en = LabelEncoder()
        la_en.fit_transform([])
        print(boo)
        number = self.countKeyByParticipantName(usrname)
        print(number)
        for participant_data in data:
            participant = ParticipantKey(
                session='1',
                participant = usrname,
                key1=participant_data[0],
                key2=participant_data[1],
                DU_key1_key1=participant_data[2]/1000,
                DD_key1_key2=participant_data[3]/1000,
                DU_key1_key2=participant_data[4]/1000,
                UD_key1_key2=participant_data[5]/1000,
                UU_key1_key2=participant_data[6]/1000
            )
            sendedKeys.append(participant)
        
        if(number <=300):
            db.session.add_all(sendedKeys)
            db.session.commit()
            return [participant.to_dict() for participant in sendedKeys], 201
        else:
            newdata = [element.getTable() for element in sendedKeys]
            oldKeys = self.getAllKeyByParticipantName(usrname)
            dataset = [element.getTable() for element in oldKeys]
            X_train = np.array(dataset).astype(float)
            X_test = np.array(newdata)
            boo = test_user(X_train, X_test)
            print(X_train.shape, X_test.shape)
            y_predict_lof, lof = user_local_outlier_factor_test(X_train, X_test)
            print('je suis la')
            return f'{y_predict_lof}, {y_predict_lof.sum()}', 200
        

    def get(self):
        """Récupère les données de participant pour une session donnée"""
        session = request.args.get('session')
        participants = ParticipantKey.query.all()
        return [participant.to_dict() for participant in participants]
    
    
    def countKeyByParticipantName(self, participant_name):
        """Compte le nombre de participants portant un nom donné"""
        participants = ParticipantKey.query.filter_by(participant=participant_name).all()
        return len(participants)
    
    def getAllKeyByParticipantName(self, participant_name):
        """Compte le nombre de participants portant un nom donné"""
        key = ParticipantKey.query.filter_by(participant=participant_name).all()
        return key