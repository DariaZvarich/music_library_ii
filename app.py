from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository




# Connect to the database
connection = DatabaseConnection()
connection.connect()


# Seed with some seed data
connection.seed("seeds/music_library.sql")


# Retrieve all artists
artist_repository = ArtistRepository(connection)
artists = artist_repository.all()


# List them out
for artist in artists:
    print(artist)


print(artist_repository.find(1))
album_repository = AlbumRepository(connection)


for album in album_repository.all():
    print(album)
print(album_repository.find(1))

class Application:
    def __init__(self):
        self.connection = DatabaseConnection()
        self.connection.connect()
        self.connection.seed("seeds/music_library.sql")
    
    def run(self):
        print("Welcome to the music library manager!\n")
        
        while True:
            print("What would you like to do?")
            print(" 1 - List all albums")
            print(" 2 - List all artists")
            print(" 3 - Exit")
            print()
            
            choice = input("Enter your choice: ")
            print()
            
            if choice == "1":
                self.list_all_albums()
            elif choice == "2":
                self.list_all_artists()
            elif choice == "3":
                print("Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.\n")
                
    def list_all_albums(self):
        album_repository = AlbumRepository(self.connection)
        albums = album_repository.all()
        
        if albums:
            print("Here is the list of albums:")
            for album in albums:
                print(f"{album.id}: {album.title} ({album.release_year} - {album.artist_id})")
        else:
            print("No albums found in the library.\n")
    
    def list_all_artists(self):
        artist_repository = ArtistRepository(self.connection)
        artists = artist_repository.all()
        
        if artists:
            print("Here is the list of artists:")
            for artist in artists:
                print(f"{artist.id}: {artist.name} ({artist.genre})")
        else:
            print("No artists found in the library.\n")
            
if __name__ == '__main__':
    app = Application()
    app.run()