from playlist import Playlist
from song import Song
from utils import simulate_playback, shuffle_songs, simulate_single_song, eliminar_artista_menos_frecuente


def main():
    playlist = Playlist()

    canciones_iniciales = [
        ("Bohemian Rhapsody", "Queen", 10),
        ("Hotel California", "Queen", 5),
        ("Smells Like Teen Spirit", "Nirvana", 7),
        ("Billie Jean", "Michael Jackson", 8),
        ("Come as You Are", "Nirvana", 6),
        ("Sweet Child O' Mine", "Guns N' Roses", 10),
        ("Lose Yourself", "Eminem", 8),
        ("November Rain", "Guns N' Roses", 10),
        ("Whitout me", "Eminem", 8)
    ]

    for titulo, artista, duracion in canciones_iniciales:
        playlist.add_song(Song(titulo, artista, duracion))

    while True:
        print("\n🎵 Bienvenido a tu Playlist Interactiva 🎵")
        print("1️⃣ Agregar canción")
        print("2️⃣ Avanzar a la siguiente canción")
        print("3️⃣ Retroceder a la canción anterior")
        print("4️⃣ Eliminar una canción")
        print("5️⃣ reproducir playlist")
        print("6️⃣ Mostrar toda la playlist")
        print("7️⃣ Activar modo aleatorio")
        print("8️⃣ Salir")
        print("9️⃣ Eliminar canciones del artista con menos cancion")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            title = input("Ingrese el título: ")
            artist = input("Ingrese el artista: ")
            duration = int(input("Ingrese la duración: "))
            if playlist.add_song(Song(title, artist, duration)):
                print("✅ Canción agregada exitosamente.")
            else:
                print("❌ Ya existe una canción con ese título.")

        elif opcion == "2":
            playlist.next_song()
            print("⏩ Avanzado a la siguiente canción.")

        elif opcion == "3":
            playlist.previous_song()
            print("⏪ Retrocedido a la canción anterior.")

        elif opcion == "4":
            print("\n🎶 Playlist Actual:")
            canciones = playlist.show_all()
            if not canciones:
                print("❌ No hay canciones para eliminar.")
                continue
            for s in canciones:
                print("   ", s)
            title = input("Ingrese el título de la canción a eliminar: ")
            if playlist.delete_song(title):
                print("✅ Canción eliminada.")
            else:
                print("❌ Canción no encontrada.")

        elif opcion == "5":
            print("\n🎶 Playlist Completa:")
            for s in playlist.show_all():
                print("   ", s)
            if playlist.size == 0:
                print("❌ No hay canciones para reproducir.")
            else:
                simulate_playback(playlist)

        elif opcion == "6":
            print("\n🎶 Playlist Completa:")
            for s in playlist.show_all():
                print("   ", s)

        elif opcion == "7":
            shuffled = shuffle_songs(playlist.get_songs_list())
            print("\n🎶 Playlist Completa:")
            for s in shuffled:
                print("   ", s)
            print("🔀 Reproducción aleatoria:")
            for song in shuffled:
                simulate_single_song(song)

        elif opcion == "8":
            print("👋 ¡Hasta pronto!")
            break

        elif opcion == "9":
            print("\n Se eliminara el artista con menos canciones")
            eliminar_artista_menos_frecuente(playlist)

        else:
            print("❌ Opción inválida.")


if __name__ == "__main__":
    main()
