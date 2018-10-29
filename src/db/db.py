from os import environ

from firebase_admin import credentials, db
import firebase_admin


class RecordExists(Exception):
    pass

class DB:
    """https://firebase.googleblog.com/2017/07/accessing-database-from-python-admin-sdk.html"""

    def __init__(self):
        # check if environment variables are missing
        if environ.get('FIREBASE_APPLICATION_DOMAIN') == None:
            raise KeyError('FIREBASE_APPLICATION_DOMAIN missing in environment variables')
        if environ.get('FIREBASE_APPLICATION_CREDENTIALS') == None:
            raise KeyError('FIREBASE_APPLICATION_CREDENTIALS missing in environment variables')

        self.__domain = environ.get('FIREBASE_APPLICATION_DOMAIN')
        self.__key = environ.get('FIREBASE_APPLICATION_CREDENTIALS')
        self.__root = None

        self.__connect()
    
    def all(self):
        animes = self.__root.get()
        return list( animes.values() ) if animes else []
    
    def watching(self):
        return [ anime for anime in self.all() if anime['watching'] == True ]

    def get(self, url):
        animes = self.all()
        for anime in animes:
            if anime['url'] == url:
                return anime
        return None

    def delete(self, url):
        animes = self.__root.get()
        for key, anime in animes.items():
            if anime['url'] == url:
                db.reference(f'/{key}').delete()
                break

    def write(self, name, url, episode, watching=True):
        if not self.get(url):
            self.__root.push({
                'name': name,
                'url': url,
                'episode': episode,
                'watching': watching
            })
            return
        raise RecordExists('Record is already exists in database')

    def update(self, url, episode=None, watching=None):
        query = {}
        if episode and type(episode) == int:
            query['episode'] = episode
        if watching in [True, False]:
            query['watching'] = watching

        animes = self.__root.get()
        for key, anime in animes.items():
            if anime['url'] == url:
                db.reference(f'/{key}').update(query)
                break

    def purge(self):
        self.__root.delete()

    def __connect(self):
        cred = credentials.Certificate(self.__key)
        firebase_admin.initialize_app(cred, {
            'databaseURL': self.__domain
        })
        self.__root = db.reference('/')
