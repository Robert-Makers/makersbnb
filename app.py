import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.sign_up import *
from lib.user import *
from lib.listing import *
from lib.listing_repository import *
from lib.request_repository import RequestRepository
from lib.request import Request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index

@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')

# @app.route('/test', methods=['GET'])
# def get_test():
#     return render_template('test.html')

#AMY AND SEAN'S CODE
# This function gathers all of the details for sign up
@app.route('/login', methods=["POST"])
def submit_signup():
    connection = get_flask_database_connection(app)
    userRepo = UserRepository(connection)
    name = request.form['name']
    email = request.form['email']
    password = request.form['password']
    userRepo.create(name, email, password)
    return render_template('login.html', name=name, email=email, password=password)

@app.route('/login', methods=['GET'])
def login_page():
    return render_template('login.html')

@app.route('/loggedin', methods=["POST"])
def submit_login():
    connection = get_flask_database_connection(app)
    email = request.form['email']
    password = request.form['password']
    userRepo = UserRepository(connection)
    checker = userRepo.check_password(email, password)
    if checker:
        id = userRepo.get_userid(email, password)
        name = userRepo.get_username(email, password)
        return render_template('loggedin.html', id=id, name = name, email=email, password=password)
    else:
        message = "Incorrect details" 
        return render_template('login.html', message = message)

@app.route('/loggedin', methods=['GET'])
def loggedin_page():
    #connection = get_flask_database_connection(app)
    id = request.args['id']
    return render_template('loggedin.html', id = id)

#----------------------------------------------#
#Bookings
@app.route('/book', methods=['GET'])
def booking_page():
    connection = get_flask_database_connection(app)
    repo = ListingRepository(connection)
    #testing authentication
    id = request.args['id']
    listings = repo.get()
    return render_template('booking.html', id=id, listings=listings)

#----------------------------------------------#
# Requests Page
@app.route('/requests', methods=['GET'])
def request_page():
    connection = get_flask_database_connection(app)
    req_repo = RequestRepository(connection)
    #testing authentication
    id = request.args['id']
    sent_requests = req_repo.get_requests_I_made(id)
    recieved_requests = req_repo.get_recieved_requests(id)
    return render_template('requests.html', id=id , sent_requests=sent_requests, recieved_requests=recieved_requests)


@app.route('/request_details/<int:id>', methods=['GET'])
def request_details(id):
    connection = get_flask_database_connection(app)
    req_repo = RequestRepository(connection)
    user_id = request.args['id']
    print('requets booking from repo...')
    booking = req_repo.get_single_requests(id)
    print(id)
    print(user_id)
    return render_template('request_details.html', user_id=user_id, booking=booking)

@app.route('/request_details/<int:id>', methods=['POST'])
def update_request_confirmation(id):
    connection = get_flask_database_connection(app)
    req_repo = RequestRepository(connection)
    status = request.form['status']
    user_id = request.args['id']
    req_repo.update_status(id, status)
    return redirect(f'/requests?id={user_id}')

#----------------------------------------------#
# Listings
@app.route('/listing/<int:id>', methods=['POST'])
def submit_request(id):
    connection = get_flask_database_connection(app)
    date_from = request.form['date_from']
    date_to = request.form['date_to']
    user_id = request.args['id']
    listing_id = request.form['listing_id']
    req_repo = RequestRepository(connection)
    list_repo = ListingRepository(connection)
    booking = Request(None, date_from, date_to, user_id, listing_id, status="pending")
    listing = list_repo.select(id)
    # Run check to see if date available then run if block
    if req_repo.check_dates(booking.date_from, booking.date_to, listing_id):
        booking = req_repo.create_request(booking)
        return redirect(f'/your_booking/{booking.id}?id={user_id}')
    else:
        message = 'Booking failed. Dates not available.'
        return render_template('listing.html', message=message, listing=listing)

@app.route('/your_booking/<int:id>', methods=['GET'])
def your_booking(id):
    connection = get_flask_database_connection(app)
    list_repo = ListingRepository(connection)
    req_repo = RequestRepository(connection)
    booking = req_repo.get_single_requests(id)
    listing = list_repo.select(booking.listing_id)
    # Working out the total price of the booking
    cost = booking.calculate_cost(listing.price)
    return render_template('booking_success.html', listing=listing, booking=booking, cost=cost)

#ROBERT AND HARRY'S CODE
@app.route('/create', methods=['GET'])
def get_data():
    id = request.args['id']
    return render_template('create.html', id=id)

@app.route('/create', methods=['POST'])
def post_data():
    connection = get_flask_database_connection(app)
    repo = ListingRepository(connection)
    title = request.form['title']
    description = request.form['description']
    price = request.form['price']
    user_id = request.args['id']
    listing = Listing(None, title, description, price, user_id)
    listing = repo.insert(listing)
    return redirect(f'/yourspaces?id={user_id}')

@app.route('/listing/<int:id>', methods=['GET'])
def get_listing(id):
    connection = get_flask_database_connection(app)
    repo = ListingRepository(connection)
    listing = repo.select(id)
    return render_template('listing.html', listing = listing)

@app.route('/yourspaces', methods=['GET'])
def your_spaces():
    connection = get_flask_database_connection(app)
    repo = ListingRepository(connection)
    id = request.args['id']
    listing = repo.select_by_user_id(id)
    return render_template('yourspaces.html', listing = listing, id = id)

# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(
        debug=True, 
        port=int(os.environ.get('PORT', 5000)),
        host='0.0.0.0'
        )