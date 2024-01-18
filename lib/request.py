from datetime import datetime as dt

class Request:
    def __init__(self, id, date_from, date_to, requester_user_id, listing_id, status='pending', listing=None):
        self.id = id
        self.date_from = date_from
        self.date_to = date_to
        self.requester_user_id = requester_user_id
        self.listing_id = listing_id
        self.status = status
        self.listing = listing

    def __repr__(self):
        return f"Request({self.id}, '{self.date_from}', '{self.date_to}', {self.requester_user_id}, {self.listing_id}, {self.status})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def calculate_cost(self, price):
        number_of_nights = self.date_to - self.date_from
        cost = number_of_nights.days * price
        return cost