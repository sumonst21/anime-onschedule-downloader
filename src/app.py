import time

from db.db import DB
from downloader.downloader import Downloader
from downloader import config
from downloader.exceptions import RequestBlocked
from downloader.scraper import Scraper
from settings import fb

FILE_FORMAT = '.mp4'
DOWNLOAD_PATH = config.DEFAULT_DOWNLOAD_PATH
TIMEOUT = config.BLOCKED_TIMEOUT


def main():
    # Firebase domain and credential setup
    fb.setDomain()
    fb.setCredential()

    # connect database
    database = DB()

    # get watching anime
    animes = database.watching()

    for anime in animes:
        # if not currently watching anime, skip
        if not anime['watching']:
            continue

        print(f'Downloading episode {anime["episode"]} of {anime["name"]}')

        # NOTE: instantiate scraper
        scraper = Scraper( anime['url'] )

        # get video link
        while True:
            try:
                videos = scraper.get( anime['episode'] )
                break
            except RequestBlocked:
                time.sleep(TIMEOUT)

        # if videos cannot be found, skip 
        if not videos:
            print(f'Cannot find download link for episode {anime["episode"]} of {anime["name"]}')
            continue
        
        filename = f'{anime["name"]} Episode-{anime["episode"]}{FILE_FORMAT}'
        # NOTE: use first download url only
        todownload = videos[0]
        # NOTE: instantiate downloader
        downloader = Downloader( DOWNLOAD_PATH )
        downloader.download(filename, todownload)

        print(f'Downloaded episode {anime["episode"]} of {anime["name"]}')

        # increment episode number in firebase
        database.update(url=anime['url'], episode=anime['episode'] + 1)

if __name__ == '__main__':
    main()