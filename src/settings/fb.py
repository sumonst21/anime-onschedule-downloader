import os

from .config import DOMAIN, FIREBASE_SECRET


def setDomain():
    os.environ['FIREBASE_APPLICATION_DOMAIN'] = DOMAIN

def setCredential():
    credential = os.path.abspath(FIREBASE_SECRET)

    if os.path.exists(credential):
        os.environ['FIREBASE_APPLICATION_CREDENTIALS'] = credential
    else:
        raise IOError(f'Firebase credentials does not exists\nTried to import from { credential }')