from lib.listing import *

def test_listing_constructs():
    listing = Listing(0, "Title", "Desc", 1, 4)
    assert listing.id == 0
    assert listing.title == "Title"
    assert listing.description == "Desc"
    assert listing.price == 1
    assert listing.host_user_id == 4

def test_format():
    listing = Listing(0, "Title", "Desc", 1, 1)
    assert str(listing) == "Listing(0, 'Title', 'Desc', 1, 1)"