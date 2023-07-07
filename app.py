from lib.database_connection import DatabaseConnection
from lib.artist_repository import ArtistRepository
from lib._album_repository import AlbumRepository




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
