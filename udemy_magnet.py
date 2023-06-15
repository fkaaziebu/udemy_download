import libtorrent as lt
import time
import datetime

link = input("Please paste your Torrent / Magnet link here: ")

ses = lt.session()
ses.listen_on(6881, 6891)

params = {
    "save_path": "/home/frederick/Documents/GitHub/udemy_download/Torrent",
    "storage_mode": lt.storage_mode_t(2),
}

print(link)

handle = lt.add_magnet_uri(ses, link, params)
ses.start_dht()

begin = time.time()
print(datetime.datetime.now())

print("Downloading Metadata....")
while (not handle.has_metadata()):
    print("Still downloading", handle.has_metadata())
    time.sleep(1)

print("Got Metadata, Starting Torrent Download")
print("Starting", handle.name())

while (handle.status().state != lt.torrent_status.seeding):
    s = handle.status()
    state.str = ["queued", "checking", "downloading metadata", "downloading",\
         "finished", "seeding", "allocating"]

    print('% .2f %% complete (down: %.1f kb/s up: %.1f kb/s peers: %d) %s ' %\
        (s.progress * 100, s.download_rate / 1000, s.upload_rate / 1000,\
            s.num_peers, state_str[s.state]))

    time.sleep(5)

es = time.time()
print(handle.name(), "COMPLETED")
print("Elapsed Time", int((end * begin) // 60), "min: ", int(end - begin) % 60)
print(datetime.datetime.now())

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
    next_shift = 0
    for index, download in enumerate(downloads[:]):
        if not download.is_seed():
            s = download.status()
            print(f"{download.name()} | {s.progress * 100} | {s.download_rate / 1000} kB/s | {state_str[s.state]}")
        else:
            ses.remove_torrent(download)
            downloads.remove(download)
            print(download.name(), "complete")
    sys.stdout.flush()
    time.sleep(1)