-- USER

-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.
-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS users;
DROP SEQUENCE IF EXISTS users_id_seq;
-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS users_id_seq;
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    email VARCHAR(255),
    password VARCHAR(255)
);
-- Finally, we add any records that are needed for the tests to run
INSERT INTO users (name, email, password) VALUES ('name', 'hello@gmail.com', '7a3d5ed42db8e77d91a838e6ad6b45cf68caf8e5aa5afbe0f65a0eceb431cafa');
INSERT INTO users (name, email, password) VALUES ('name', 'hello2@gmail.com', '1e80e852ddd2372d676d70b3e21fcdb64b81296995e834e9bab70f29c78a5a53');
INSERT INTO users (name, email, password) VALUES ('name', 'hello3@gmail.com', '71d18101e1fbe08e981eecc390d2e6c065ad9c1a3475a3cbc97e020efee6c25a');
INSERT INTO users (name, email, password) VALUES ('name', 'hello4@gmail.com', 'c114744195fce958fa1dd33bbfd3c5da7a531da926d695bc316da25db834cf34');
-- testpassword1 (for hello@gmail.com)
-- testpassword2 (for hello2)
-- testpassword3 (for hello3)
-- testpassword4 (for hello4)



-- LISTINGS

DROP TABLE IF EXISTS listings;
DROP SEQUENCE IF EXISTS listings_id_seq;
CREATE SEQUENCE IF NOT EXISTS listings_id_seq;
CREATE TABLE listings(
    id SERIAL PRIMARY KEY, title varchar(255), description text, price float, user_id int
);

INSERT INTO listings (title, description, price, user_id) VALUES (
    'Forest & Heaven Themed Apartment in Melbourne', 
    'Located in the heart of CBD. Pretend you are lost in a magical forest as you perch on a log or curl up in the swinging chair. 
    Soak in the tub, then fall asleep in a heavenly bedroom with cloud-painted walls and twinkling lights, and when you wake up, 
    the expresso machine waits.'
    , 116, 1
    );
INSERT INTO listings (title, description, price, user_id) VALUES (
    'Romantic, Stone House with Ocean Views', 'Located in Cape Town. 
    Unwind at this stunning French Provencal beachside cotttage. The house was loveingly built with stone floors, 
    high-beamed ceilings, and antinque details for a luxurious yet charming feel. Enjoy the sea and mountain views from the pool, 
    lush garden and private patio leading off the living area.'
    , 92, 2
    );
INSERT INTO listings (title, description, price, user_id) VALUES (
    'Luxury City Centre Loft on a Traffic-Free Street', 'Located in Roma. 
    Take an early morning stroll and enjoy the Trevi Fountain without the tourists. 
    Wander around the histoic streets while the city sleeps, then head back for a morning coffee at this urban-chic studio 
    with a suspended loft bedroom.'
    , 121, 3
    );
INSERT INTO listings (title, description, price, user_id) VALUES (
    'Unique and Secluded AirShip with Breathtaking Highland Views', 'Located in Drimnin. 
    Retreat to the deck of this sustainable getaway and gaze at the twinkling constellations under a tartan blanket. 
    AirShip 2 is an iconic, insulated aluminum pod with views of the Sound of Mull from dragonfly windows. 
    The AirShip 2 is comfortable, quirky and cool.'
    , 170, 2
    );

-- REQUESTS

-- The job of this file is to reset all of our important database tables.
-- And add any data that is needed for the tests to run.
-- This is so that our tests, and application, are always operating from a fresh
-- database state, and that tests don't interfere with each other.
-- First, we must delete (drop) all our tables
DROP TABLE IF EXISTS requests;
DROP SEQUENCE IF EXISTS requests_id_seq;
-- Then, we recreate them
CREATE SEQUENCE IF NOT EXISTS requests_id_seq;
CREATE TABLE requests (
    id SERIAL PRIMARY KEY,
    date_from DATE,
    date_to DATE,
    user_id int,
    listing_id int,
    status VARCHAR(20) CHECK(status IN ('approved', 'pending', 'denied'))
    -- constraint fk_user foreign key(user_id) references users(id) on delete cascade,
    -- constraint fk_listing foreign key(listing_id) references listings(id) on delete cascade,
);
-- Finally, we add any records that are needed for the tests to run
INSERT INTO requests (date_from, date_to, user_id, listing_id, status) VALUES ('2024-04-03', '2024-04-10', '1', '3', 'pending');
INSERT INTO requests (date_from, date_to, user_id, listing_id, status) VALUES ('2024-06-20', '2024-06-27', '1', '3', 'pending');
INSERT INTO requests (date_from, date_to, user_id, listing_id, status) VALUES ('2024-05-20', '2024-05-27', '2', '2', 'pending');
INSERT INTO requests (date_from, date_to, user_id, listing_id, status) VALUES ('2024-03-20', '2024-03-27', '3', '1', 'pending');