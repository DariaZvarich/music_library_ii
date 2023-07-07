from lib.album import Album


"""
Constaruct with
id, title, release_year, and album_id
"""


def test_constructs_with_fields():
    album = Album(1, "Dark Side", 1995, 2)
    assert album.id == 1
    assert album.title == "Dark Side"
    assert album.release_year == 1995
    assert album.artist_id == 2
"""
We can format albums to strings nicely
"""
def test_formatting():
    album = Album(1, "Dark Side", 1995, 2)
    assert str(album) == "Album(1, Dark Side, 1995, 2)"
# Try commenting out the `__repr__` method in lib/album.py
# And see what happens when you run this test again.


"""
We i constract two Albums with the same fields
They are equal
"""
def test_equal():
    album_1 = Album(1, "Dark Side", 1995, 2)
    album_2 = Album(1, "Dark Side", 1995, 2)
    assert album_1 == album_2
# Try commenting out the `__eq__` method in lib/album.py
# And see what happens when you run this test again.

