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
            barra = generar_barra_progreso(i, song.duration)
            print(f"{barra} {i}/{song.duration}s", end='\n')
            time.sleep(1)
        playlist.next_song()
        canciones_reproducidas += 1
    print("\n✅ Fin de la reproducción automática.")


def generar_barra_progreso(actual, total, largo=20):
    porcentaje = actual / total
    llenos = int(largo * porcentaje)
    vacios = largo - llenos
    return "█" * llenos + "░" * vacios


def shuffle_songs(songs):
    shuffled = songs[:]
    random.shuffle(shuffled)
    return shuffled


def simulate_single_song(song):
    print(f"\n▶️ Reproduciendo: {song}")
    for i in range(1, song.duration + 1):
        barra = generar_barra_progreso(i, song.duration)
        print(f"{barra} {i}/{song.duration}s", end='\n')
        time.sleep(1)


def eliminar_artista_menos_frecuente(playlist, artista_a_eliminar=None, eliminadas=0):
    canciones = playlist.get_songs_list()
    if not canciones:
        print("No hay canciones en la playlist.")
        return
    conteo = {}
    for i in canciones:
        conteo[i.artist] = conteo.get(i.artist, 0) + 1
    menor_cantidad = min(conteo.values())
    for artista, cantidad in conteo.items():
        if cantidad == menor_cantidad:
            artista_a_eliminar = artista
            break
    for song in canciones:
        if song.artist == artista_a_eliminar:
            playlist.delete_song(song.title)
            eliminadas += 1
    print(f"🗑️ Eliminadas {eliminadas} canción(es) de {artista_a_eliminar}.")
