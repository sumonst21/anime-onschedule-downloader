## Anime Auto

#### Umm, What?
- This is my own personal automated script to automatically look for new episode and download to local
- It works with [Firebase](https://firebase.google.com) database to sync episodes (actually do not need it, but I wanted to try Firebase so)

> Check below for how to setup this in your own system

<br/>

#### Left to be added to project later
- I haven't added FTP support and Email updates to user's email as I am cleaning up the code and not very important to use the script

<br/>

#### Anime downloader
Anime Scraper and Downloader is from my another project, ["Anime Heaven Downloader"](https://github.com/the-robot/animeheaven-downloader)
- Go check that out if you want normal simple anime downloader
- **WARN:** never ever touch that source from `downloader` directory, as the code is directly from the project mentioned above and any code changes for downloader should be from there

---

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
