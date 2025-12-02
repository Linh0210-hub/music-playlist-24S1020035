# Danh sách bài hát (toàn cục)songs = []
songs = []
def add_song():
    print("Chức năng thêm bài hát chưa được triển khai.")

def view_playlist():
    print("Chức năng xem danh sách phát chưa được triển khai.")

def search_by_artist():
    print("Chức năng tìm theo ca sĩ chưa được triển khai.")

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
# Danh sách toàn cục lưu bài hát
songs = []
def add_song(title, artist, duration):
    """
    Thêm một bài hát vào danh sách songs.
    :param title: Tên bài hát (str)
    :param artist: Tên ca sĩ (str)
    :param duration: Thời lượng bài hát (giây) (int)
    """
    song = {
        'title': title,
        'artist': artist,
        'duration': duration
    }
    songs.append(song)
    print(f"Đã thêm bài hát: {title} - {artist}, thời lượng {duration} giây.")
