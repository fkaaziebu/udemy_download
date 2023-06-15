import libtorrent as lt
import time

ses = lt.session()
ses.listen_on(6881, 6891)
downloads = []

params = {
    "save_path": "./Torrent",
    "save_path": "/home/frederick/Documents/GitHub/udemy_download/Torrent",
    "storage_mode": lt.storage_mode_t(2),
    "ti": lt.torrent_info("./8B3D44703C08E0C2EF810AEFCD63151ADD145D51.torrent")
}
downloads.append(ses.add_torrent(params))

state_str = [
    "queued",
    "checking",
    "downloading metadata",
    "downloading",
    "finished",
    "seeding",
    "allocating",
    "checking fastresume",
]


while downloads:
    for index, download in enumerate(downloads[:]):
        if not download.is_seed():
            s = download.status()
            print(f"{download.name()} | {s.progress * 100} | {s.download_rate / 1000} kB/s | {state_str[s.state]}")
        else:
            ses.remove_torrent(download)
            downloads.remove(download)
            print(download.name(), "complete")
    time.sleep(1)