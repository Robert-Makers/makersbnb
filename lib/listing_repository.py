from lib.listing import *

class ListingRepository:
    def __init__(self, connection):
        self.connection = connection
    
    def get(self):
        rows = self.connection.execute('SELECT * FROM listings')
        return [Listing(listing['id'], listing['title'], listing['description'], listing['price'], listing['user_id']) for listing in rows]
    
    def select(self, id):
        rows = self.connection.execute('SELECT * FROM listings WHERE id = %s', [id])
        return Listing(rows[0]['id'], rows[0]['title'], rows[0]['description'], rows[0]['price'], rows[0]['user_id'])
    
    #ONCE THIS IS READY REFERENCE THE USER ID
    def insert(self, listing):
        rows = self.connection.execute('INSERT INTO listings (title, description, price, user_id) VALUES (%s, %s, %s, %s) RETURNING id', [listing.title, listing.description, listing.price, listing.host_user_id])
        listing.id = rows[0]['id']
        return listing

    def delete(self, id):
        self.connection.execute('DELETE FROM listings WHERE id = %s', [id])
    
    def update(self, id, title, description, price):
        self.connection.execute('UPDATE listings SET title = %s, description = %s, price = %s WHERE id = %s', [title, description, price, id])
    
    def select_by_user_id(self, id):
        rows = self.connection.execute('SELECT * FROM listings WHERE user_id = %s', [id])
        return [Listing(listing['id'], listing['title'], listing['description'], listing['price'], listing['user_id']) for listing in rows]