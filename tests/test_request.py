from lib.request import *
from unittest.mock import Mock
from datetime import datetime as dt

def test_request_constructs():
    request = Request(0, '2024-02-01', '2024-02-08', 1, 4, 'pending')
    assert request.id == 0
    assert request.date_from == '2024-02-01'
    assert request.date_to == '2024-02-08'
    assert request.requester_user_id == 1
    assert request.listing_id == 4
    assert request.status == 'pending'
    assert request.listing == None

def test_format():
    request = Request(0, '2024-02-01', '2024-02-08', 1, 4, 'pending')
    assert str(request) == "Request(0, '2024-02-01', '2024-02-08', 1, 4, pending)"

def test_cost_calculator():
    request = Request(0, dt(2024, 2, 1), dt(2024, 2, 3), 1, 4, 'pending')
    assert request.calculate_cost(9.99) == 19.98

def test_request_contains_listing_info():
    listing = Mock()
    listing.title = 'First Listing'
    request = Request(0, '2024-02-01', '2024-02-08', 1, 4, 'pending', listing)
    assert request.listing.title == 'First Listing'
    assert request.status == "pending"

def test_format():
    request = Request(0, '2024-02-01', '2024-02-08', 1, 4, "pending")
    assert str(request) == "Request(0, '2024-02-01', '2024-02-08', 1, 4, pending)"

