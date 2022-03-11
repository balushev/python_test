# -*- coding: utf-8 -*-
"""
Created on Tue Dec 14 16:40:56 2021

@author: bbalushev
"""

import certifi
import re
from pymongo import MongoClient
from pymongo import DESCENDING
from common_functions.crypto import Crypto


class MongoDBInteractions:
    """ MongoDBInteractions class interacts with Mongo DB and provides all the necessary information """

    # ================================ Initialization method ================================
    def __init__(self, connection_string: bytes) -> None:
        """ Constructor method

            Method parameters:
               connection_string -> contains connection string for MongoDB

            Return value -> None

        """

        self.crypto = Crypto()
        decrypted_string = self.crypto.decrypt(connection_string)
        tls_certificate = None
        if 'tls' in decrypted_string:
            tls_certificate = certifi.where()
        self.client = MongoClient(self.crypto.decrypt(connection_string), tlsCAFile=tls_certificate)

    # ================================ Find one record method ================================
    def find_one(self, query_condition: dict, db: str, collection: str) -> dict:
        """ find_one method provides the first matching element of our query

            Method parameters:
                query_condition -> contains the condition for our query
                db -> contains the name of MongoDB
                collection -> contains the name of collection in MongoDB

            Return value -> one MongoDB record

        """

        try:
            db = self.client[db]
            collection = db[collection]
            return collection.find_one(query_condition)
        except Exception as e:
            print("An exception occurred: ", e)
            print("============ Sorry, can't find record !!! ============")

    # ================================ Find last record method ================================
    def find_last(self, query_string: dict, db: str, collection: str) -> dict:

        """find_last method provides the last matching element of our query.

             Method parameters:
                query_condition -> contains the condition for our query
                db -> contains the name of MongoDB
                collection -> contains the name of collection in MongoDB

            Return value -> last record which matching with our pattern

        """

        try:
            db = self.client[db]
            collection = db[collection]
            return collection.find_one(query_string, sort=[('_id', DESCENDING)])
        except Exception as e:
            print("An exception occurred: ", e)
            print(f"============ Sorry, can't find record in db: {db}, collection: {collection} ============")

    # ================================ Update many records method ================================
    def update_many(self,
                    query_condition: dict,
                    new_values: dict,
                    db: str, collection: str) -> str:

        """update_many method update fields of found elements

            Method parameters:
                query_condition -> contains the condition for our query
                new_values -> contains the set of values that we want to update in our collection
                db -> contains the name of MongoDB
                collection -> contains the name of collection in MongoDB

            Return value -> message with number of updated records

            """

        try:
            db = self.client[db]
            collection = db[collection]
            result = collection.update_many(query_condition, new_values)
            return f"Number of updated documents: {result.modified_count}"
        except Exception as e:
            print("An exception occurred: ", e)
            print(f"============ Sorry, there was an error updating the records in"
                  f" db: {db}, collection: {collection} ============")

    # ================================ Remove one record method ================================
    def delete_one_query_result(self, query_condition: dict, db: str, collection: str) -> str:

        """delete_one_query_result method makes a query in a collection and then deletes the 1st result from this query

            Method parameters:
                query_condition -> contains the condition for our query
                db -> contains the name of MongoDB
                collection -> contains the name of collection in MongoDB

            Return value -> message with number of deleted records

        """

        try:
            db = self.client[db]
            collection = db[collection]
            result = collection.delete_one(query_condition)
            return f"Number of deleted documents: {result.deleted_count}"
        except Exception as e:
            print("An exception occurred: ", e)
            print(f"============ Sorry, there was an error deleting the record in db: {db}, "
                  f"collection: {collection} ============")

