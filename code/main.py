from playlist import Playlist
from song import Song
from utils import simulate_playback, shuffle_songs


def main():
    playlist = Playlist()

    while True:
        print("\n🎵 Bienvenido a tu Playlist Interactiva 🎵")
        print("1️⃣ Agregar canción")
        print("2️⃣ Avanzar a la siguiente canción")
        print("3️⃣ Retroceder a la canción anterior")
        print("4️⃣ Eliminar una canción")
        print("5️⃣ Mostrar canción en reproducción")
        print("6️⃣ Mostrar toda la playlist")
        print("7️⃣ Activar modo aleatorio")
        print("8️⃣ Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            title = input("Ingrese el título: ")
            artist = input("Ingrese el artista: ")
            duration = int(input("Ingrese la duración (10-15 seg): "))
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
            song = playlist.show_current()
            print(f"🎧 {song}" if song else "🎧 No hay canciones en reproducción.")

        elif opcion == "6":
            print("\n🎶 Playlist Completa:")
            for s in playlist.show_all():
                print("   ", s)

        elif opcion == "7":
            shuffled = shuffle_songs(playlist.get_songs_list())
            print("🔀 Reproducción aleatoria:")
            for song in shuffled:
                simulate_playback(song)

        elif opcion == "8":
            print("👋 ¡Hasta pronto!")
            break

        else:
            print("❌ Opción inválida.")


if __name__ == "__main__":
    main()
