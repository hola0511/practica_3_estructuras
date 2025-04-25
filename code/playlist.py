class Node:
    def __init__(self, song):
        self.song = song
        self.next = None
        self.prev = None


class Playlist:
    def __init__(self):
        self.current = None
        self.size = 0

    def add_song(self, song):
        if self.contains(song.title):
            return False
        new_node = Node(song)
        if not self.current:
            self.current = new_node
            self.current.next = self.current.prev = self.current
        else:
            tail = self.current.prev
            tail.next = new_node
            new_node.prev = tail
            new_node.next = self.current
            self.current.prev = new_node
        self.size += 1
        return True

    def contains(self, title):
        node = self.current
        if not node:
            return False
        for _ in range(self.size):
            if node.song.title.lower() == title.lower():
                return True
            node = node.next
        return False

    def next_song(self):
        if self.current:
            self.current = self.current.next

    def previous_song(self):
        if self.current:
            self.current = self.current.prev

    def delete_song(self, title):
        if not self.current:
            return False
        node = self.current
        for _ in range(self.size):
            if node.song.title.lower() == title.lower():
                if self.size == 1:
                    self.current = None
                else:
                    node.prev.next = node.next
                    node.next.prev = node.prev
                    if node == self.current:
                        self.current = node.next
                self.size -= 1
                return True
            node = node.next
        return False

    def show_current(self):
        return self.current.song if self.current else None

    def show_all(self):
        songs = []
        node = self.current
        if not node:
            return songs
        for _ in range(self.size):
            songs.append(str(node.song))
            node = node.next
        return songs

    def get_songs_list(self):
        songs = []
        node = self.current
        if node:
            for _ in range(self.size):
                songs.append(node.song)
                node = node.next
        return songs




#agregela a la funcion Playlist
#def top_3_largas(self):
 #   if self.size == 0:
  #      return []
#
 #   # Obtener todas las canciones como lista
  #  canciones = self.get_songs_list()
#
  #  top3 = sorted(canciones, key=lambda song: song.duration, reverse=True)[:3]
#
 #   return top3

#agrege en el menu
#elif opcion == "9":
 #   top = playlist.top_3_largas()
  #  if not top:
   #     print("❌ No hay canciones en la playlist.")
    #else:
     #   print("\n🥇 Top 3 canciones más largas:")
      #  for idx, song in enumerate(top, start=1):
       #     print(f"{idx}. {song}")
