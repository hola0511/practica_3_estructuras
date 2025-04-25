import time
import random


def simulate_playback(playlist):
    print("\n🎧 Iniciando reproducción automática...\n")

    canciones_reproducidas = 0
    total = playlist.size

    while playlist.size > 0 and canciones_reproducidas < total:
        song = playlist.show_current()
        print(f"▶️ Reproduciendo: {song}")
        for i in range(1, song.duration + 1):
            print(f"⏳ Tiempo: {i}/{song.duration}s")
            time.sleep(1)

        playlist.next_song()
        canciones_reproducidas += 1

    print("\n✅ Fin de la reproducción automática.")

def shuffle_songs(songs):
    shuffled = songs[:]
    random.shuffle(shuffled)
    return shuffled

def simulate_single_song(song):
    print(f"\n▶️ Reproduciendo: {song}")
    for i in range(1, song.duration + 1):
        print(f"⏳ Tiempo: {i}/{song.duration}s")
        time.sleep(1)

