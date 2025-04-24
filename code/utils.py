import time
import random

def simulate_playback(song):
    print(f"▶️ Reproduciendo: {song}")
    for i in range(1, song.duration + 1):
        print(f"⏳ {i}s...", end="\r")
        time.sleep(1)
    print()

def shuffle_songs(songs):
    shuffled = songs[:]
    random.shuffle(shuffled)
    return shuffled
