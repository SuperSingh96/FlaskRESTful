from flask_restful import Resource
from models.store import StoreModel

class Store(Resource):
    def get(self,name):
        store=StoreModel.find_by_name(name)
        if store:
            return store.json()
        return {'message': 'not found'},404

    def post(self,name):
        if StoreModel.find_by_name(name):
            return {'message': "a store with name '{}' already exists".format(name)},500
        store=StoreModel(name)
        store.save_to_db()
        return store.json()

    def delete(self,name):
        store=StoreModel.find_by_name(name)
        if store:
            store.delete_from_db()
        return {'message': 'deleted'}

class StoreList(Resource):
    def get(self):
        return {'stores': [i.json() for i in StoreModel.query.all()]}
