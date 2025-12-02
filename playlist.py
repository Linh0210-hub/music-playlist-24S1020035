# Danh sách bài hát (toàn cục)
songs = []
def add_song():
    """
    Nhập tên bài hát, ca sĩ và thời lượng, thêm vào danh sách songs.
    """
    title = input("Nhập tên bài hát: ")
    artist = input("Nhập tên ca sĩ: ")
    while True:
        try:
            duration = int(input("Nhập thời lượng bài hát (giây): "))
            break
        except ValueError:
            print("Vui lòng nhập số nguyên cho thời lượng.")
    
    song = {'title': title, 'artist': artist, 'duration': duration}
    songs.append(song)
    print(f"Đã thêm bài hát: {title} - {artist} ({duration} giây)")

def view_playlist():
    """
    Hiển thị toàn bộ bài hát trong danh sách songs.
    """
    if not songs:
        print("Danh sách phát hiện đang trống.")
        return
    
    print("=== Danh sách phát ===")
    for i, song in enumerate(songs, start=1):
        print(f"{i}. {song['title']} - {song['artist']} ({song['duration']} giây)")

def search_by_artist():
    """
    Tìm bài hát theo ca sĩ.
    """
    artist_name = input("Nhập tên ca sĩ muốn tìm: ")
    found = [song for song in songs if song['artist'].lower() == artist_name.lower()]
    
    if not found:
        print(f"Không tìm thấy bài hát nào của ca sĩ {artist_name}.")
    else:
        print(f"Bài hát của {artist_name}:")
        for i, song in enumerate(found, start=1):
            print(f"{i}. {song['title']} ({song['duration']} giây)")

def main():
    while True:
        print("\n--- MUSIC PLAYLIST MANAGER ---")
        print("1. Thêm bài hát")
        print("2. Xem danh sách phát")
        print("3. Tìm bài hát theo ca sĩ")
        print("4. Thoát")

        choice = input("Chọn chức năng: ")

        if choice == '1':
            add_song()
        elif choice == '2':
            view_playlist()
        elif choice == '3':
            search_by_artist()
        elif choice == '4':
            print("Kết thúc chương trình.")
            break
        else:
            print("Lựa chọn không hợp lệ.")

if __name__ == "__main__":
    main()
def search_by_artist():
    """
    Tìm bài hát theo ca sĩ.
    """
    artist_name = input("Nhập tên ca sĩ muốn tìm: ")
    found = [song for song in songs if song['artist'].lower() == artist_name.lower()]
    
    if not found:
        print(f"Không tìm thấy bài hát nào của ca sĩ {artist_name}.")
    else:
        print(f"Bài hát của {artist_name}:")
        for i, song in enumerate(found, start=1):
            print(f"{i}. {song['title']} ({song['duration']} giây)")
