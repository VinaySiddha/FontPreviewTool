# firebase_utils.py

import firebase_admin
from firebase_admin import credentials, firestore

def initialize_firebase():
    if not firebase_admin._apps:
        cred = credentials.Certificate('./workspaces/mini-project/trevon/accounts/credentials.json')
        firebase_admin.initialize_app(cred)

def get_firestore_data(collection, document):
    initialize_firebase()
    db = firestore.client()
    doc_ref = db.collection(collection).document(document)
    return doc_ref.get().to_dict()

def set_firestore_data(collection, document, data):
    initialize_firebase()
    db = firestore.client()
    doc_ref = db.collection(collection).document(document)
    doc_ref.set(data)

def update_firestore_data(collection, document, data):
    initialize_firebase()
    db = firestore.client()
    doc_ref = db.collection(collection).document(document)
    doc_ref.update(data)

def delete_firestore_data(collection, document):
    initialize_firebase()
    db = firestore.client()
    doc_ref = db.collection(collection).document(document)
    doc_ref.delete()
