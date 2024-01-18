from lib.request import *
from datetime import datetime, timedelta
from lib.listing import Listing

class RequestRepository:
    def __init__(self, connection):
        self.connection = connection
    
    def get_all_requests(self):
        rows = self.connection.execute('SELECT * FROM requests')
        return [Request(request['id'], request['date_from'], request['date_to'], request['user_id'], request['listing_id'], request['status']) for request in rows]
    
    def get_single_requests(self, id):
        rows = self.connection.execute('SELECT requests.id as request_id, requests.date_from, requests.date_to, requests.user_id as requester_user_id, requests.status, listings.id as listing_id, listings.title, listings.description, listings.price, listings.user_id as host_user_id ' \
                                        ' FROM requests ' \
                                        ' JOIN listings ON requests.listing_id = listings.id ' \
                                        ' WHERE requests.id = %s', [id])
        return Request(rows[0]['request_id'], rows[0]['date_from'], rows[0]['date_to'], rows[0]['requester_user_id'], rows[0]['listing_id'], rows[0]['status'], Listing(rows[0]['listing_id'], rows[0]['title'], rows[0]['description'], rows[0]['price'], rows[0]['host_user_id']))
    
    def create_request(self, request):
        rows = self.connection.execute('INSERT INTO requests (date_from, date_to, user_id, listing_id, status) VALUES (%s, %s, %s, %s, %s) RETURNING id', [request.date_from, request.date_to, request.requester_user_id, request.listing_id, request.status])
        request.id = rows[0]['id']
        return request

    def delete(self, id):
        self.connection.execute('DELETE FROM requests WHERE id = %s', [id])
    
    def update_dates(self, id, date_from, date_to):
        self.connection.execute('UPDATE requests SET date_from = %s, date_to = %s WHERE id = %s', [date_from, date_to, id])

    def update_status(self, id, status):
        self.connection.execute('UPDATE requests SET status = %s WHERE id = %s', [status, id])
        
    def get_requests_I_made(self, loggedin_user_id):
        # Retrieve requests I have made to other books]
        rows = self.connection.execute('SELECT requests.id as request_id, requests.date_from, requests.date_to, requests.user_id as requester_user_id, requests.status, listings.id as listing_id, listings.title, listings.description, listings.price, listings.user_id as host_user_id ' \
                                        ' FROM requests ' \
                                        ' JOIN listings ON requests.listing_id = listings.id ' \
                                        ' WHERE requests.user_id = %s '
                                        ' ORDER BY requests.date_from, listings.title ', [loggedin_user_id])
        requests = []
        for row in rows:
            listing = Listing(row['listing_id'], row['title'], row['description'], row['price'], row['host_user_id'])
            request = Request(row['request_id'], row['date_from'], row['date_to'], row['requester_user_id'], row['listing_id'], row['status'], listing)
            requests.append(request)
        return requests

    def get_recieved_requests(self, loggedin_user_id):
        # Retrieve requests sent to my listings
        rows = self.connection.execute('SELECT requests.id as request_id, requests.date_from, requests.date_to, requests.user_id as requester_user_id, requests.status, listings.id as listing_id, listings.title, listings.description, listings.price, listings.user_id as host_user_id ' \
                                        ' FROM requests ' \
                                        ' JOIN listings ON requests.listing_id = listings.id ' \
                                        ' WHERE listings.user_id = %s ' \
                                        ' ORDER BY requests.date_from, listings.title ', [loggedin_user_id])
        requests = []
        for row in rows:
            listing = Listing(row['listing_id'], row['title'], row['description'], row['price'], row['host_user_id'])
            request = Request(row['request_id'], row['date_from'], row['date_to'], row['requester_user_id'], row['listing_id'], row['status'], listing)
            requests.append(request)
        return requests

    def check_dates(self, date_from, date_to, listing_id):
        rows = self.connection.execute('SELECT * FROM requests WHERE listing_id = %s', [listing_id])
        if rows != []:
            is_available = True
            for row in rows: 
                reserved_start_date = row['date_from']
                reserved_end_date = row['date_to']
                print(date_from)
                current_date_check = datetime.strptime(date_from, '%Y-%m-%d').date()
                print(type(reserved_end_date))
                print(type(current_date_check))
                while is_available == True and current_date_check <= datetime.strptime(date_to, '%Y-%m-%d').date():
                    if reserved_start_date <= current_date_check < reserved_end_date:
                        is_available = False
                    current_date_check += timedelta(days=1)
            return is_available
        else:
            return True
