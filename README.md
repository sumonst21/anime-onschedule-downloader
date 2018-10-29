## Anime Auto

#### Umm, What?
- This is my own personal automated script to automatically look for new episode and download to local
- It works with [Firebase](https://firebase.google.com) database to sync episodes (actually do not need it, but I wanted to try Firebase so)

> Check below for how to setup this in your own system

#### Left to be added to project later
- I haven't added FTP support and Email updates to user's email as I am cleaning up the code and not very important to use the script

#### Anime downloader
Anime Scraper and Downloader is from my another project, ["Anime Heaven Downloader"](https://github.com/the-robot/animeheaven-downloader)
- Go check that out if you want normal simple anime downloader
- **WARN:** never ever touch that source from `downloader` directory, as the code is directly from the project mentioned above and any code changes for downloader should be from there

---

#### Dependencies and Python runtime
- Python 3.6+
- `pip install -r requirements.txt`

#### Setting up the automated script
- First of all you need Google account and create Realtime Database in Firebase
- Then copy your Realtime Database Endpoint `https://*.firebaseio.com/` to `src/settings/config.py... DOMAIN`
- After that, create Google Service Account Key. [Read Here](https://cloud.google.com/iam/docs/creating-managing-service-account-keys)
- Copy the key (json format) to `src/SECRET/firebase.json`

> **PS:** You can amend the code if you want to work with other databases. Database connectors should always be from `db` directory.

---

#### Adding new anime to tracker, aka Firebase DB
- create `anime.json` in `src`, then write something like below
- then run `python sync.py --force` to force sync the anime
```json
{
  "animes": [
    {
      "episode": 5,
      "name": "Bording School Juliet",
      "url": "http://animeheaven.eu/i.php?a=Boarding%20School%20Juliet",
      "watching": true
    }
  ]
}
```

- this is how your Firebase database will be like

---

#### Automate downloads
- Upon successfully downloads, the episode number in Firebase will be incremented itself by 1
- I.e., if episode 4 is downloaded successfully, database episode number will be 5 for next download

#### Can you make executable program for `X` platform?
- No, I do not have plan for making executable program at this point as this is more like automated tool to be run on your 24hr machine like on Raspberrry Pi (which I do) or your PC but why tho.. unless you want to turn on PC 24/7
- If you want simple easy to run downloader, go check [Anime Heaven Downloader](https://github.com/the-robot/animeheaven-downloader)
