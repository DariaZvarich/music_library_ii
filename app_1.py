from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib.album_repository import AlbumRepository

connection = DatabaseConnection()
connection.connect()
connection.seed("seeds/music_library.sql")

artist_repository = ArtistRepository(connection)
album_repository = AlbumRepository(connection)

artist = artist_repository.find(1)

albums = album_repository.all()

albums_by_artist = []
for album in albums:
    if album.artist_id == artist.id:
        albums_by_artist.append(album)
        
print(artist)
for album in albums_by_artist:
    print(album)