# Sync script to sync local anime list with records from Firebase
# - if new anime is added to local .json, new record will be created in database
# - episode updates from firebase will be written back to local .json

import json
import os
import sys

from db.db import DB
from settings import fb


class Sync:
    JSON_FILE = 'anime.json'

    # connect Database
    database = None

    def __init__(self):
        # initialize database
        self.database = DB()
        self.__path = self.__get_path()
    
    def start(self):
        # get records from local and database
        local = self.__read_local()
        db_records = self.__read_database()

        # if they are the same, do not sync
        if (local == db_records):
            return

        # get list of existing anime in db
        db_animes = [ anime.get("url") for anime in db_records.get("animes") ]
        # create new records in databse for new data in json
        for anime in local.get("animes"):
            # if anime not exists in db (new created in json), write to db
            if anime.get("url") not in db_animes:
                self.database.write(
                    name=anime.get("name"),
                    url=anime.get("url"),
                    episode=anime.get("episode"),
                    watching=anime.get("watching")
                )

        # get latest records from database, write it to local back
        # episode numbers may be updated on db for existing records
        db_records = self.__read_database()
        # write changes from database to local
        with open(self.JSON_FILE, 'w') as f:
            json.dump(db_records, f, indent=2, separators=(',', ': '))
    
    def __get_path(self):
        return f"{os.path.abspath('.')}/{self.JSON_FILE}"
    
    def __read_local(self):
        empty = { "animes": [] }
        # return json (empty array) if file not exists or empty file
        if not os.path.exists(self.__path) or os.stat(self.__path).st_size == 0:
            return empty
        with open(self.__path, 'r') as f:
            return json.load(f)
    
    def __read_database(self):
        return { "animes": self.database.all() }


if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == '--force':
        print("Syncing local anime.json with firebase")
        # set domain and credential
        fb.setDomain()
        fb.setCredential()
        sync = Sync()
        sync.start()

    else:
        print("python sync.js --force")