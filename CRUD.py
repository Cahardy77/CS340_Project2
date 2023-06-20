#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  7 20:01:59 2023

@author: christopherha4_snhu
"""

from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self,user,passw):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        USER = user
        PASS = passw
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 30614
        DB = 'AAC'
        COL = 'animals'
        #
        # Initialize Connection
        #
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]

#Method that takes dictionary value to create document in database
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)  # data should be dictionary            
            return True
        else:
            raise Exception("Nothing to save, because data parameter is empty")
            return False

#Method that takes a dictionary value to search for a document
    def read(self,data):
        if data is not None:
            results = list(self.database.animals.find(data)) # data should be in dictionary format
            return results
        else:
            raise Exception("Nothing to lookup, because data parameter is empty")
            return False
        
#Method that takes a dictionary value to search and a set operator dictionary to update many documents    
    def updateMany(self,query,updatedValues):
        if query is not None and updatedValues is not None:
            results = self.database.animals.update_many(query, updatedValues) # data should be in dictionary format
            return results.matched_count
        else:
            raise Exception("Nothing to update, because data parameter is empty")
            return False
        
#Method that takes a dictionary value to search and a set operator dictionary to update a single document   
    def updateOne(self,query,updatedValues):
        if query is not None and updatedValues is not None:
            results = self.database.animals.update_one(query, updatedValues) # data should be in dictionary format
            return results.matched_count
        else:
            raise Exception("Nothing to update, because data parameter is empty")
            return False
    
#Method that takes a dictionary value to search and delete one instance
    def delete(self, deleteValue):
        if deleteValue is not None:
            results = self.database.animals.delete_one(deleteValue) # data should be in dictionary format
            return results.deleted_count
        else:
            raise Exception("Nothing to delete, because data parameter is empty")
            return False
        
