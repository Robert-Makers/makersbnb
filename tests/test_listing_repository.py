from lib.listing_repository import *
from lib.listing import *


def test_getting_the_listings(db_connection):
    db_connection.seed('seeds/DatabaseTables.sql')
    repo = ListingRepository(db_connection)
    listings = repo.get()
    assert listings == [
        Listing(1, "First Listing", "This is a description for the first listing", 0.79, 1),
        Listing(2, "Second Listing", "This is a description for the second listing", 2, 1),
        Listing(3, "Third Listing", "This is a description for the third listing", 0, 3),
        Listing(4, "Fourth Listing", "This is a description for the fourth listing", 0, 1)
    ]

def test_grab_singular_listing(db_connection):
    db_connection.seed('seeds/DatabaseTables.sql')
    repo = ListingRepository(db_connection)
    listings = repo.select(2)
    assert listings == Listing(2, "Second Listing", "This is a description for the second listing", 2, 1)

def test_insert_listing(db_connection):
    db_connection.seed('seeds/DatabaseTables.sql')
    repo = ListingRepository(db_connection)
    repo.insert(Listing(None, 'Title', 'Description', 10, 2))
    listings = repo.get()
    assert len(listings) == 5

def test_delete_listing(db_connection):
    db_connection.seed('seeds/DatabaseTables.sql')
    repo = ListingRepository(db_connection)
    repo.delete(1)
    listings = repo.get()
    assert len(listings) == 3

def test_update_the_listings(db_connection):
    db_connection.seed('seeds/DatabaseTables.sql')
    repo = ListingRepository(db_connection)
    repo.update(4, "Fourth-Hundred Listing", "This is a description for the fourth-hundred listing", 1000)
    listings = repo.get()
    assert listings == [
        Listing(1, "First Listing", "This is a description for the first listing", 0.79, 1),
        Listing(2, "Second Listing", "This is a description for the second listing", 2, 1),
        Listing(3, "Third Listing", "This is a description for the third listing", 0, 3),
        Listing(4, "Fourth-Hundred Listing", "This is a description for the fourth-hundred listing", 1000, 1)
    ]